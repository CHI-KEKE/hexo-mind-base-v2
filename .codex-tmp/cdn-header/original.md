---
title: CDN-Header-Lost
date: 2026-09-28 10:03:00
categories: kubernetes
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
tags:
    - 
toc:
toc_number:
comments :
---


{% tabs CDN-Header-Lost%}




<!-- tab 狀況發生!-->



CDN → ALB → EKS Header 遺失排查

透過 CDN 打 API 後，Header 在抵達 Pod 前消失的排查流程。


<!-- endtab -->




<!-- tab 架構-->


CDN → ALB → EKS 是現代 Web / API 系統很常見的 AWS 架構之一，尤其是服務跑在 Kubernetes / EKS 時


```bash
使用者 Browser / App
        │
        ▼
┌─────────────────┐
│ CDN / CloudFront│  ← 對外入口、快取、WAF、防護
└────────┬────────┘
         │ HTTP Request + Headers
         ▼
┌─────────────────┐
│      ALB        │  ← Load Balancer、路由、TLS
└────────┬────────┘
         │ HTTP Request + Headers
         ▼
┌─────────────────┐
│      EKS        │
│                 │
│ Pod   Pod   Pod │  ← 真正執行 API
└─────────────────┘

```



Header 在這條路徑的任一節點都可能被丟棄。



<!-- endtab -->




<!-- tab CloudFront Origin Request Policy-->


CloudFront 可以直接把 S3、ALB 等 AWS 資源當作 Origin，IAM、憑證、WAF、Route 53、監控等也都在 AWS 生態系裡，所以維運上比較方便。


CloudFront 收到瀏覽器的 request 後，不會預設把所有 viewer request 的 Header 全部原樣送到 Origin。哪些 Header 要送到 Origin，主要由 Cache Policy + Origin Request Policy 決定。AWS 官方文件也明確說，除了 CloudFront 自動包含的資訊外，其他 viewer headers、query strings、cookies 預設不會包含在 origin request


```
CloudFront → Distributions → 選 Distribution
→ Behaviors → 選 Path Pattern → Edit
→ Cache key and origin requests
  → Origin request policy
```



> ⚠️ **Cache policy** 與 **Origin request policy** 是不同的，要看的是 **Origin request policy**


例如 `GET /products/123`

User A: Accept-Language: zh-TW

User B: Accept-Language: en-US

假設 API 會根據 Accept-Language 回傳不同內容，那 CloudFront 就必須知道 `/products/123 + zh-TW` 跟 `/products/123 + en-US` 是否應該被視為不同 Cache。

所以 CloudFront 把兩件事情拆開


```bash
                 CloudFront
                     │
        ┌────────────┴────────────┐
        │                         │
   Cache Policy          Origin Request Policy
        │                         │
        ▼                         ▼
哪些值影響 Cache Key       哪些值送給 Origin
```


例如 X-Request-Id 後端可能需要它來 trace request，但你完全不希望


- X-Request-Id: aaa
- X-Request-Id: bbb
- X-Request-Id: ccc



產生三份不同 cache。因此可以設定成 Cache Policy 不要包含 X-Request-Id

```bash
Origin Request Policy
    ↓
Forward X-Request-Id

```

結果就是


```bash
Browser
   │
   │ X-Request-Id: abc123
   ▼
CloudFront
   │
   ├── Cache Key：不考慮它
   │
   └── Origin Request：帶著它
                ↓
               ALB
                ↓
               EKS
```

這就是要把 Cache Policy 和 Origin Request Policy 分開的核心原因





自訂 Header 例如 Webhook / API Header


| Header | 用途 |
|--------|------|
| `X-GitHub-Event` | GitHub Webhook 事件類型 |
| `X-Hub-Signature-256` | GitHub Webhook HMAC 驗證 |
| `X-Gitlab-Event` | GitLab Webhook 事件類型 |
| `X-Gitlab-Token` | GitLab Webhook Token 驗證 |
| `Authorization` | API 授權（CloudFront 預設不轉發） |


建立自訂 Origin request policy，把所需 Header 全部加進去或改用內建 `Managed-AllViewer` policy（轉發所有 Header，但會影響快取效率）



另外 CloudFront 是透過 Origin（來源站）設定 指向 ALB 的，在 AWS 建立 ALB 後，會得到一個 DNS Name，例如 `my-alb-123456.ap-northeast-1.elb.amazonaws.com`，接著 CloudFront Distribution 裡設定一個 `Origin domain -> my-alb-123456.ap-northeast-1.elb.amazonaws.com`，而 `Behavior` 這個設定就是 「什麼 Request 要去哪個 Origin？」，例如一個 Distribution 可以有

```bash
CloudFront
│
├─ Origin A
│    └─ S3
│
└─ Origin B
     └─ ALB
```

Behavior 再決定 `/images/*` 去 `S3 Origin`，而 `/api/*` 去 `ALB Origin`





<!-- endtab -->




<!-- tab ALB Listener Rules-->


```bash
Browser
   ↓
CloudFront
   │ Origin = xxx.elb.amazonaws.com
   ↓
ALB

```

ALB 收到 request 之後，第一個要處理的就是 `Listener`，而 `Listener` 就是「ALB 要在哪個 Port 接 Request」

```bash
ALB
│
├── Listener :80  HTTP
│
└── Listener :443 HTTPS
```


而 `Listener Rule` 是「這個 Request 應該送去哪裡」，例如 EKS 裡有很多服務


```bash
ALB :443
   │
   ├─ /api/orders/*
   │       ↓
   │   Order Target Group
   │
   ├─ /api/members/*
   │       ↓
   │   Member Target Group
   │
   └─ /api/products/*
           ↓
       Product Target Group
```



一般情況下，ALB 會把收到的 request headers 繼續送給 Target，不需要像 CloudFront 那樣建立 Origin Request Policy，而 ALB 自己也會動一些 Header，ALB 雖然通常保留收到的 Header，但它作為 HTTP reverse proxy / load balancer，會新增或處理部分 Header。最經典的是 X-Forwarded-For、X-Forwarded-Proto、X-Forwarded-Port

```bash
X-Forwarded-For: 203.0.113.10
X-Forwarded-Proto: https
X-Forwarded-Port: 443
```

X-Forwarded-For 的本質意義是讓後端知道這個 HTTP Request 原本是從哪個 Client IP 來的，以及中途可能經過哪些 Proxy。但 X-Forwarded-For 的實際內容要特別注意，因為前面已經有 CloudFront 等 proxy 時，它可能形成一串 IP，而 ALB 對 X-Forwarded-For 也有 append / preserve / remove 的設定。AWS 預設是 append，因此後端不能簡單假設「看到的唯一 IP 就一定是 Client IP」。




**Console 路徑：**
```
EC2 → Load Balancers → 選 ALB → Listeners → 查 Rules
```

確認 Rules 中沒有 `remove header` action，ALB 本身通常不會主動刪除 Header



<!-- endtab -->




<!-- tab Step 3 — EKS Ingress Controller Annotations-->



EKS = AWS 提供的 Managed Kubernetes（受管 Kubernetes）服務，假設完全自己架 Kubernetes，需要自己處理 Control Plane 的建置、高可用、版本升級、故障處理等




```bash
你自己管理 Kubernetes
│
├── Control Plane
│   ├── kube-apiserver
│   ├── etcd
│   ├── scheduler
│   └── controller manager
│
└── Worker Nodes
    ├── Node A
    ├── Node B
    └── Node C
```


換成 Amazon EKS，AWS 幫你管理 Kubernetes Control Plane，但使用者仍然需要考慮

- Deployment
- Service
- Ingress
- Pod
- CPU / Memory requests & limits
- HPA
- Node Group
- IAM
- Security Group
- Kubernetes 版本升級
- Container Image
- Monitoring
...



```bash
             EKS
              │
     ┌────────┴────────┐
     │                 │
Control Plane       Worker
     │               Nodes
     │                 │
 AWS 管理         你仍需要管理*
                       │
                 ┌─────┼─────┐
                 ▼     ▼     ▼
               Node  Node  Node
                 │
                Pods
```


到這裡，我們再叵悉一下架構



AWS Load Balancer Controller 負責把 Kubernetes 世界裡動態變化的 Pod 和 AWS 世界裡的 Target Group 串起來。這也是為什麼在 AWS Console 看 Target Group 時，可能會發現裡面的 10.x.x.x targets 過一陣子有所變化，Pod 被重新建立後，Target Group 也會跟著更新



以我目前查詢的 Target Group 為例，他的 Target Type 是 Instance，表示 ALB 正在把流量送到兩台 EC2 Instance 並且是 32080 port，32080 落在 Kubernetes 預設 NodePort 範圍 30000–32767 內，所以這兩個 Instance 是 EKS Worker Nodes，而 32080 是某個 Kubernetes Service 暴露的 NodePort


```bash
CloudFront
     ↓
ALB :443
     ↓
Listener Rule
     ↓
Target Group
     ↓
┌─────────────────────────┐
│                         │
▼                         ▼
EC2 Worker Node A       EC2 Worker Node B
:32080                  :32080
│                         │
└────────────┬────────────┘
             ↓
     Kubernetes Service
        (NodePort)
             ↓
     Ingress Controller
             ↓
      Ingress Rules
             │
      ┌──────┼───────┐
      ↓      ↓       ↓
  Shopping Payment  Member
   Service Service  Service
      ↓      ↓       ↓
     Pods   Pods    Pods
```


這個 ALB 很可能是在把不同 domain 的流量統一送進 Kubernetes 的 Ingress Controller。真正的 Shopping、Payment 等服務分流，可以在 Kubernetes Ingress Controller 那一層進行


Kubernetes 的每個 Resource 都可以有 metadata，其中就包含 annotations，他是附加在 Kubernetes Resource 上的 Key-Value 設定資訊，讓特定 Controller 或工具讀取並採取相應行為


EKS Ingress Controller Annotations 指的就是在 Kubernetes 的 Ingress 資源上，透過 metadata.annotations 加入額外設定，讓對應的 Ingress Controller 知道該如何處理流量、建立路由，或設定 AWS 資源。


到這一步，為了查看有沒有影響 Header 的 annotation 在 K8S Resouorce 上，我們需要連線到 AWS EKS 查看，最標準的方式是 AWS CLI 取得 EKS 連線資訊 → 寫進 kubeconfig → kubectl 連線



```bash
你的 Windows
    │
    │ AWS CLI 驗證身分
    ▼
AWS / IAM
    │
    │ aws eks update-kubeconfig
    ▼
~/.kube/config
    │
    ▼
kubectl
    │
    ▼
EKS Kubernetes API Server

```



```bash
## 先確認 AWS CLI
aws --version

## 確認「你現在是用哪個 AWS 身分」 成功，會看到 Account、Arn 等資訊
aws sts get-caller-identity

## 如果公司使用 AWS SSO / IAM Identity Center，通常會先有這個
aws sso login --profile <公司-profile>

aws sts get-caller-identity --profile <公司-profile>


## 找到 EKS Cluster 名稱
aws eks list-clusters --region <region>


## 如果使用 profile
aws eks list-clusters --region <region> --profile <profile>


## 安裝 kubectl (https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html?utm_source=chatgpt.com)
kubectl version --client


## 建立 kubeconfig
Cluster = public-eks-hk
Region  = ap-east-1

aws eks update-kubeconfig --region ap-east-1 --name public-eks-hk


####　如果公司使用特定 profile，它會更新：C:\Users\<你的帳號>\.kube\config
#### https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html?utm_source=chatgpt.com

aws eks update-kubeconfig --region ap-east-1 --name public-eks-hk --profile <profile>


## 確認現在指向哪個 Cluster
## 如果 EKS API Endpoint 是 private-only，電腦還必須能進入公司 VPC 網路，例如透過 VPN
kubectl config current-context


kubectl get nodes

kubectl get svc -A | Select-String 32080


## 檢查 Ingress yaml
kubectl get ingress -n <namespace> -o yaml

## 確認沒有影響 Header 的 annotation
# 這類 annotation 可能操作 Header
alb.ingress.kubernetes.io/actions.*


## 第一種：AWS ALB 的設定 : alb.ingress.kubernetes.io/target-type: instance

## 第二種：NGINX Ingress 的設定 : nginx.ingress.kubernetes.io/proxy-read-timeout: "60"

```



<!-- endtab -->




<!-- tab Step 4 — 快速診斷：直接看 Pod 收到的 Header-->


## 方法 1：.NET API 加暫時性 Log

```csharp
// Middleware 或 Controller 裡加這段 debug log
var headers = Request.Headers.Select(h => $"{h.Key}={h.Value}");
_logger.LogInformation("Received headers: {Headers}", string.Join(", ", headers));
```

**方法 2：kubectl exec 進 Pod curl 打自己**

```bash
kubectl exec -it <pod-name> -n <namespace> -- curl -v http://localhost:<port>/api/ping
```



## 方法 2：部署 httpbin 測試 Pod

```bash
# 部署 httpbin
kubectl run httpbin --image=kennethreitz/httpbin --port=80 -n <namespace>

# 打 /headers endpoint，可以直接看 Pod 實際收到的所有 Header
curl https://<your-domain>/headers
```



<!-- endtab -->




{% endtabs %}