from pathlib import Path
import re, html, json
root=Path('C:/Dev/Hexo-mind')
target=root/'source/_posts/K8S/CDN-Header-Lost.md'
out=root/'.codex-tmp/cdn-header'
out.mkdir(exist_ok=True)
backup=out/'original.md'
if not backup.exists(): backup.write_bytes(target.read_bytes())
front=backup.read_text(encoding='utf-8').split('---',2)[1]
template=Path('C:/Users/Allen/.codex/skills/hexo-article-creator/assets/components/kubernetes-helm-style.html').read_text(encoding='utf-8')
css=re.search(r'<style>(.*?)</style>',template,re.S)[1]
css+='''
#article-container .kubernetes-helm table.kh-table{width:auto;max-width:100%;}
.kubernetes-helm .kh-diagram{overflow-x:auto;border:1px solid var(--kh-line);border-radius:4px;margin:22px 0;padding:16px;background:var(--kh-bg);}
.kubernetes-helm .kh-diagram .mermaid{min-width:540px;}
.kubernetes-helm .kh-diagram svg{min-width:540px;max-width:none!important;}
.kubernetes-helm .kh-diagram p{font-size:.9em;color:var(--kh-ink);}
#article-container .kubernetes-helm .kh-diagram svg{background:var(--kh-bg)!important;}
#article-container .kubernetes-helm .kh-diagram svg .node rect{fill:var(--kh-soft)!important;stroke:var(--kh-blue)!important;}
#article-container .kubernetes-helm .kh-diagram svg .nodeLabel,#article-container .kubernetes-helm .kh-diagram svg .nodeLabel p,#article-container .kubernetes-helm .kh-diagram svg .nodeLabel span{color:var(--kh-ink)!important;fill:var(--kh-ink)!important;}
#article-container .kubernetes-helm .kh-diagram svg .cluster rect{fill:var(--kh-bg)!important;stroke:var(--kh-line)!important;}
#article-container .kubernetes-helm pre.kh-pre{tab-size:4;}
.kubernetes-helm .kh-section{margin-top:32px!important;}
@media(max-width:600px){.kubernetes-helm{padding:12px;}.kubernetes-helm .kh-diagram{padding:8px;}.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{min-width:7em;}}
'''
tabs=[]
def tab(title):
    tabs.append({'title':title,'blocks':[]})
def add(kind, **kw): tabs[-1]['blocks'].append({'kind':kind,**kw})
def p(s): add('p',text=s)
def h(s): add('h',text=s)
def note(s): add('note',text=s)
def table(headers,rows): add('table',headers=headers,rows=rows)
def code(title,lang,s): add('code',title=title,lang=lang,text=s.strip())
def diagram(title,s,caption): add('diagram',title=title,text=s.strip(),caption=caption)
def link(label,url): return f'[{label}]({url})'
tab('狀況發生!')
add('hero',title='CDN → ALB → EKS Header 遺失排查',text='呼叫 API 時明明帶了 Header，後端卻讀不到。請求在抵達程式前會經過多層代理，先找出哪一段沒有傳到，再檢查那一層的設定。')
p('本文沿著 CDN、ALB 與 EKS 的請求路徑，整理 Header 轉發規則、路由關係與檢查指令。')
note('目前是排查筆記，尚未確認根因。文中的兩台 EC2 Instance 與 32080 port 來自原始觀察紀錄；實際 Service、Ingress Controller 與遺失的 Header 仍需以現場設定及同一筆請求的紀錄確認。')
tab('架構')
h('先辨認請求經過哪些層')
p('CDN → ALB → EKS 可用於部署在 AWS 的 Web／API 服務。CloudFront 是對外入口，可提供快取並整合 WAF；ALB 負責負載平衡、路由與 TLS；EKS 內的 Pod 執行 API。')
diagram('請求路徑與系統邊界','''flowchart TB
Client["使用者 Browser / App"] -->|HTTP Request + Headers| CDN["CDN / CloudFront：入口與快取"]
CDN -->|需要回源時| ALB["ALB：路由、負載平衡與 TLS"]
subgraph Cluster["EKS：應用程式執行環境"]
Pod["API Pods"]
end
ALB -->|經已設定的叢集入口| Pod''','由上往下閱讀。箭頭代表請求方向；叢集內的實際路由留到 EKS 分頁展開，這張圖不假設一定存在 NGINX。')
p('沿途代理可能依各自規則篩選或改寫 Header。EKS 是執行環境，真正需要檢查的是入口代理與應用程式的處理行為。')
note('CloudFront 命中快取時，該次讀取可能直接由邊緣回應，沒有新的請求抵達 Pod。排查時先確認請求確實回源，避免把「未回源」判成「Header 被刪除」。')
tab('CloudFront Origin Request Policy')
h('回源資料與快取識別分開檢查')
p('CloudFront 可以把 S3、ALB 等資源設為 Origin，並與 IAM、憑證、WAF、Route 53 及監控服務整合。收到 viewer request 後，CloudFront 不會無條件把所有 Header、query string 與 cookie 原樣送往 Origin。')
table(['設定','回答的問題','與回源的關係'],[
['Cache Policy','哪些值讓回應視為不同快取？','納入 Cache Key 的 Header、query string 與 cookie 也會送往 Origin。'],
['Origin Request Policy','還有哪些資料需要送到 Origin？','可額外轉發資料，而不把這些欄位加入 Cache Key。']])
p('兩種 Policy 必須一起看。不能只看 Origin Request Policy 的白名單，就斷定某個 Header 不會被轉發。'+link('AWS：兩種 Policy 如何配合','https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-how-origin-request-policies-and-cache-policies-work-together.html'))
code('AWS Console 檢查位置','text','''CloudFront → Distributions → 選 Distribution
→ Behaviors → 選 Path Pattern → Edit
→ Cache key and origin requests
  → Cache policy
  → Origin request policy''')
h('案例：相同商品，不同語系')
p('假設 API 根據 `Accept-Language` 回傳不同內容，兩筆 `GET /products/123` 就可能需要不同的快取識別。')
table(['請求','Header','快取識別示意'],[['User A','`Accept-Language: zh-TW`','`/products/123 + zh-TW`'],['User B','`Accept-Language: en-US`','`/products/123 + en-US`']])
p('這個案例將語系納入 Cache Policy，才能區分兩份內容。只把語系送往 Origin，而沒有區分快取，不能保證每次取得正確語系。')
h('案例：Request ID 只用來追蹤')
p('`X-Request-Id: aaa`、`X-Request-Id: bbb`、`X-Request-Id: ccc` 代表三筆請求，但不一定代表三份不同內容。後端需要追蹤識別值時，可由 Origin Request Policy 轉發 `X-Request-Id`，Cache Policy 則不包含它。')
code('回源時的 Request ID','text','''Browser: X-Request-Id: abc123
CloudFront Cache Key: 不包含 X-Request-Id
CloudFront Origin Request: X-Request-Id: abc123
ALB → EKS: 繼續檢查同一個識別值''')
p('此例描述需要回源時的行為；命中快取時，後端不一定會收到這筆 Request ID。')
h('Webhook 與授權 Header')
table(['Header','用途'],[['`X-GitHub-Event`','GitHub Webhook 事件類型'],['`X-Hub-Signature-256`','GitHub Webhook HMAC 驗證'],['`X-Gitlab-Event`','GitLab Webhook 事件類型'],['`X-Gitlab-Token`','GitLab Webhook Token 驗證'],['`Authorization`','API 授權，需另行檢查 CloudFront 的特殊轉發規則']])
p('一般自訂 Header 可加入自訂 Origin Request Policy，或視需求採用 `Managed-AllViewer`。轉發全部 viewer headers 不等於把全部 Header 加入 Cache Key，不能直接推論會產生更多快取項目。')
note('Authorization 不能加入 Origin Request Policy 的個別 Header 白名單。可把它納入 Cache Policy；若停用快取，可使用 AllViewer 或 AllViewerExceptHostHeader 轉發。後者會改用 Origin 的 Host，必須確認 ALB／Ingress 的 Host 路由相容。需要依身分授權的內容，也必須避免不同使用者共用不適當的快取。')
p(link('AWS：Authorization 轉發方式','https://repost.aws/knowledge-center/cloudfront-authorization-header')+'；'+link('AWS：Managed Origin Request Policies','https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html'))
h('Origin 與 Behavior 決定送往哪裡')
p('建立 ALB 後會取得 DNS Name，例如 `my-alb-123456.ap-northeast-1.elb.amazonaws.com`。在 CloudFront Origin 的 `Origin domain` 填入此名稱，即可將該 ALB 設為來源站；HTTPS 回源時仍需確認憑證與使用的主機名稱相符。')
diagram('依 Path Pattern 選擇 Origin','''flowchart TB
CF["CloudFront Distribution"] -->|/images/*| S3["Origin A：S3"]
CF -->|/api/*| ALB["Origin B：ALB"]''','箭頭標示 Behavior 的 Path Pattern。這是兩條指定規則的示例，未畫出其他規則與 Default Behavior；實際排查需確認請求命中哪條規則及其 Policy。')
tab('ALB Listener Rules')
h('Listener 接收連線，Rule 決定去向')
p('CloudFront 的 Origin 指向 `xxx.elb.amazonaws.com` 時，請求會送到該 ALB。Listener 定義接收連線的 port 與協定，例如 `:80 HTTP` 或 `:443 HTTPS`；Listener Rule 再依條件決定路由。')
diagram('ALB 的 Path 路由示例','''flowchart TB
L["ALB Listener :443"] -->|/api/orders/*| O["Order Target Group"]
L -->|/api/members/*| M["Member Target Group"]
L -->|/api/products/*| P["Product Target Group"]''','三條箭頭代表不同 Path 條件，不是依序呼叫三個服務。未列出的請求由其他規則或 Default Rule 處理。')
p('一般情況下，ALB 會繼續轉發收到的 request headers，不需要 CloudFront 的 Origin Request Policy。不過它仍會新增或處理部分 Header，不能把 ALB 視為完全不改動 HTTP 的通道。')
table(['Header','示例','解讀方式'],[['`X-Forwarded-For`','`203.0.113.10`','記錄來源／代理鏈；ALB 預設 append，可設 preserve 或 remove。'],['`X-Forwarded-Proto`','`https`','連到 ALB 時使用的協定；前面有 CloudFront 時，不能直接當成 viewer 端協定。'],['`X-Forwarded-Port`','`443`','連到 ALB 的目的 port；不一定等於最外層呼叫使用的 port。']])
p('前面有 CloudFront 等代理時，`X-Forwarded-For` 可能是一串 IP。ALB 預設追加上一跳來源，後端應依受信任代理鏈解讀，不可把唯一 IP 或最左側值無條件當成真實 Client IP。'+link('AWS：X-Forwarded Headers','https://docs.aws.amazon.com/elasticloadbalancing/latest/application/x-forwarded-headers.html'))
h('檢查 Rule 與 Header 相關屬性')
code('AWS Console 檢查位置','text','EC2 → Load Balancers → 選 ALB → Listeners → 查 Rules')
p('先確認命中的 Rule 是否導向預期 Target Group。ALB 沒有通用的 `remove header` Listener Rule action，因此不應把尋找此 action 當成排查步驟。'+link('AWS：Listener Rule actions','https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-action-types.html'))
table(['檢查項目','與 Header 的關係'],[['`routing.http.drop_invalid_header_fields.enabled`','啟用時會丟棄不符合 ALB Header 名稱規則的欄位。'],['`routing.http.xff_header_processing.mode`','控制 X-Forwarded-For 的 append／preserve／remove。'],['`routing.http.preserve_host_header.enabled`','控制是否保留原始 Host，影響後續 Host 路由判讀。']])
p(link('AWS：ALB 屬性與 Header 名稱規則','https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html')+'；'+link('AWS：Host Header preservation','https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-load-balancer-attributes.html'))
tab('Step 3：EKS Ingress Controller Annotations')
h('先分清 EKS 與應用程式的管理責任')
p('Amazon EKS 是 AWS 提供的受管 Kubernetes 服務。自行架設 Kubernetes 時，Control Plane 的建置、高可用、版本升級與故障處理都需自行負責；使用 EKS 後，由 AWS 維運受管 Control Plane，應用程式與叢集使用方式仍需規劃。')
table(['範圍','自行架設 Kubernetes','使用 Amazon EKS'],[['Control Plane','管理 kube-apiserver、etcd、scheduler、controller manager。','AWS 維運受管 Control Plane；仍需規劃版本升級時機與相容性。'],['Worker Nodes','管理 Node A、Node B、Node C 等工作節點。','EC2 Node Group 仍有節點維護責任；實際責任依運算模式不同。'],['應用與容量','管理 Deployment、Service、Ingress、Pod。','仍需管理上述資源、CPU／Memory requests & limits、HPA 與 Container Image。'],['權限與觀測','規劃網路、授權及監控。','仍需規劃 IAM、Security Group、Monitoring 與 Node Group。']])
h('Controller 與 Target Type 的差異')
p('AWS Load Balancer Controller 會依 Kubernetes 資源設定協調 AWS 的負載平衡資源與 targets。它屬於控制層，不是每筆 API 請求都會穿過的 HTTP proxy。')
table(['Target Type','ALB 的直接目標','Pod 重建時的解讀'],[['`ip`','Pod IP 等 IP targets。','若由 Controller 管理 Pod targets，Pod 重建後，10.x.x.x 等註冊目標可能跟著更新。'],['`instance`','EC2 Instance 的 Service NodePort。','不能把 Target Group 的 Instance targets 當成 Pod IP；Pod 變化由叢集內 Service 對應處理。']])
p(link('AWS Load Balancer Controller：流量模式','https://github.com/kubernetes-sigs/aws-load-balancer-controller/blob/main/docs/how-it-works.md'))
h('觀察紀錄：兩台 Instance 與 32080')
p('原始紀錄中的 Target Group 使用 `Instance`，流量送往兩台 EC2 Instance 的 `32080` port。這個 port 落在 Kubernetes 預設 NodePort 範圍 `30000–32767`，符合 Worker Node／NodePort 的可能架構，但仍需比對 EC2 身分與 Service 設定。')
diagram('待確認的 NodePort 與 Ingress 拓撲','''flowchart TB
CF["CloudFront"] --> ALB["ALB :443 / Listener Rule"]
ALB --> TG["Target Group：Instance"]
TG --> A["EC2 Instance A :32080"]
TG --> B["EC2 Instance B :32080"]
A -.-> S["Service NodePort：待確認"]
B -.-> S
S -.-> IC["Ingress Controller：待確認"]
IC -.-> R["Ingress Rules：待確認"]
R -.-> Shop["Shopping Service → Pods"]
R -.-> Pay["Payment Service → Pods"]
R -.-> Member["Member Service → Pods"]''','實線表示原稿記錄的入口關係，虛線表示尚待查證的叢集內路徑。若 NodePort 指向應用 Pod，後面就不會有這層 Ingress Controller；Service 是邏輯路由關係，不是額外 HTTP proxy。')
p('一種可能是 ALB 將不同 domain 的流量統一交給叢集內 Ingress Controller，再分流到 Shopping、Payment、Member 等服務。需先找到 `32080` 所屬 Service，再查看 selector、EndpointSlice 與 IngressClass，才能確定是否符合這個假設。')
h('Annotations 由對應 Controller 解讀')
p('Kubernetes Resource 的 `metadata.annotations` 是附加的 Key-Value 資訊。Ingress 上的 annotations 可供對應 Controller 調整路由或 AWS 資源，但不同 Controller 的設定不能混為一談。')
table(['設定示例','用途與限制'],[['`alb.ingress.kubernetes.io/target-type: instance`','AWS Load Balancer Controller 的目標模式，instance 模式需要適用的 NodePort／LoadBalancer Service。'],['`alb.ingress.kubernetes.io/actions.*`','定義 ALB 自訂 action，需讀取實際 JSON；不是任意刪除 Header 的設定。'],['`nginx.ingress.kubernetes.io/proxy-read-timeout: "60"`','NGINX Ingress 的讀取逾時示例，不表示會刪除 Header，也不適用於 ALB Controller。']])
p(link('AWS Load Balancer Controller：Annotations','https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/ingress/annotations/'))
h('從 Windows 連線到 EKS')
p('連線順序是 Windows 上以 AWS CLI 驗證 IAM 身分，再透過 `aws eks update-kubeconfig` 寫入 `~/.kube/config`，最後由 `kubectl` 連線至 EKS Kubernetes API Server。以下是操作範例，佔位符需替換為實際值。')
code('1. 確認工具與 AWS 身分','powershell','''aws --version
aws sts get-caller-identity
# 使用 AWS SSO / IAM Identity Center 時
aws sso login --profile <公司-profile>
aws sts get-caller-identity --profile <公司-profile>''')
p('身分查詢成功會回傳 `Account`、`Arn` 等資訊。後續指令應持續使用同一個已確認的 profile。')
code('2. 查詢叢集與確認 kubectl','powershell','''aws eks list-clusters --region <region>
# 使用具名 profile 時
aws eks list-clusters --region <region> --profile <profile>
kubectl version --client''')
p('若尚未安裝 kubectl，可依 '+link('AWS：安裝 kubectl','https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html')+' 處理。')
code('3. 建立 kubeconfig','powershell','''# 原稿範例：Cluster = public-eks-hk，Region = ap-east-1
aws eks update-kubeconfig --region ap-east-1 --name public-eks-hk
# 使用具名 profile 時，改用此指令
aws eks update-kubeconfig --region ap-east-1 --name public-eks-hk --profile <profile>
kubectl config current-context
kubectl get nodes''')
p('預設會更新 `C:/Users/使用者帳號/.kube/config`。如果 EKS API Endpoint 是 private-only，電腦必須能連入 VPC，例如透過公司 VPN；IAM 身分驗證成功也不代表已具備 Kubernetes 資源讀取權限。'+link('AWS：建立 kubeconfig','https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html'))
code('4. 找出 NodePort 對應服務','powershell','''kubectl get svc -A | Select-String 32080
kubectl get svc <service-name> -n <namespace> -o yaml
kubectl get endpointslices -n <namespace> -l kubernetes.io/service-name=<service-name> -o yaml
kubectl get ingressclass
kubectl get ingress -n <namespace> -o yaml''')
p('檢查 Service 的 `nodePort`、`targetPort`、`selector`，再比對 EndpointSlice 與實際 Pods。Ingress 則查看 `spec.ingressClassName`、Host、Path、backend 與 annotations；如果確認有 NGINX，再檢查該 Controller 的 ConfigMap 及適用的 Header 設定。')
tab('Step 4：快速診斷：直接看 Pod 收到的 Header')
h('每種方法驗證的範圍不同')
table(['方法','能確認什麼','限制'],[['.NET API 暫時性 Log','實際請求到達應用程式後，指定 Header 是否存在。','只代表紀錄位置收到的內容，需與上游同一筆請求對照。'],['kubectl exec + localhost curl','Pod 內應用是否接收測試 Header。','繞過 CloudFront、ALB 與外部 Ingress，不能證明完整路徑正常。'],['httpbin /headers','經測試入口送往回顯服務的 Header。','需先建立 Service 及適用路由，且測試路徑必須符合要驗證的入口設定。']])
h('方法 1：.NET API 加暫時性 Log')
p('在 Controller 的入口，或可存取 Request 的診斷位置，記錄待查 Header。以 Request ID 對照同一筆請求；授權與 Webhook token 只記錄是否存在，避免把憑證值寫入 Log。')
code('Controller 診斷示例','csharp','''var names = new[] { "X-Request-Id", "X-GitHub-Event", "X-Gitlab-Event" };
var headers = Request.Headers
    .Where(h => names.Contains(h.Key, StringComparer.OrdinalIgnoreCase))
    .Select(h => $"{h.Key}={h.Value}");
_logger.LogInformation("Received headers: {Headers}", string.Join(", ", headers));
_logger.LogInformation("Authorization present: {Present}",
    Request.Headers.ContainsKey("Authorization"));
_logger.LogInformation("GitLab token present: {Present}",
    Request.Headers.ContainsKey("X-Gitlab-Token"));
_logger.LogInformation("GitHub signature present: {Present}",
    Request.Headers.ContainsKey("X-Hub-Signature-256"));''')
p('範例需引用 `System` 與 `System.Linq`。在 Middleware 中改用 `context.Request.Headers`；若要定位應用內的改寫，需比較相關 Middleware 前後的紀錄。')
h('方法 2：kubectl exec 進 Pod 打 localhost')
code('Pod 內的局部測試','powershell','''kubectl exec -it <pod-name> -n <namespace> -- curl -v http://localhost:<port>/api/ping
# 加上可辨識的測試值
kubectl exec -it <pod-name> -n <namespace> -- curl -v -H "X-Request-Id: local-check-001" http://localhost:<port>/api/ping''')
p('容器需要已安裝 curl。`curl -v` 顯示送出的 Header，仍需搭配應用 Log 或回顯回應，才能確認接收端看到的值；這個方法不經過 CDN／ALB。')
h('方法 3：部署 httpbin 測試 Pod')
p('以下保留原稿的 httpbin image 範例，實際使用前需確認環境允許的來源與版本。此處僅提供操作範例，未對叢集執行部署。')
code('建立 Pod 與叢集內 Service','powershell','''kubectl run httpbin --image=kennethreitz/httpbin --port=80 -n <namespace>
kubectl expose pod httpbin --name=httpbin --port=80 --target-port=80 -n <namespace>''')
note('建立 Pod 與 Service 不會自動讓外部 /headers 可用。需依實際 IngressClass、Host 與既有入口，將測試路徑導向 httpbin Service，並確認 CloudFront Behavior、ALB Rule 與快取設定涵蓋該路徑。這些現場資訊尚未提供，因此不預填可能導向錯誤入口的 Ingress YAML。')
code('入口路由完成後，再從外部測試','powershell','''curl.exe -v -H "X-Request-Id: edge-check-001" https://<your-domain>/headers''')
p('Windows 使用 `curl.exe`，避免 Windows PowerShell 的 curl alias 改變指令行為；其他 shell 可使用 `curl`。在回傳 JSON 檢查 `X-Request-Id`，並確認本次請求回源。診斷端點應限制測試存取，不攜帶真實憑證，使用完畢後移除測試路由與資源。')
p('能在 httpbin 看見 Header，代表該測試路徑有送達，不代表所有 API 路徑都採用同一組 Policy。仍需對照原本失敗請求的 Host、Path、method 與 Header，才能縮小遺失位置。')

def inline(s):
    s=html.escape(s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    return re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<a href="\2">\1</a>',s)
formal=['---'+front+'---\n\n{% tabs CDN-Header-Lost %}\n']
pure=['---'+front+'---\n']
for ti,t in enumerate(tabs):
    formal.append('<!-- tab '+t['title']+'-->\n')
    if ti==0: formal.append('<style>'+css+'</style>\n')
    formal.append('<div class="kubernetes-helm">\n')
    pure.append('## '+t['title']+'\n')
    for b in t['blocks']:
        k=b['kind']
        if k in ['p','note','h']:
            s=inline(b['text'])
            formal.append((f'<h3 class="kh-section">{s}</h3>' if k=='h' else f'<div class="kh-note"><p>{s}</p></div>' if k=='note' else f'<p>{s}</p>')+'\n')
            pure.append(('### ' if k=='h' else '')+b['text']+'\n')
        elif k=='hero':
            formal.append(f'<div class="kh-hero"><span class="kh-emblem" aria-hidden="true"></span><h2>{inline(b["title"])}</h2><p>{inline(b["text"])}</p></div>\n')
            pure.extend(['### '+b['title']+'\n',b['text']+'\n'])
        elif k=='table':
            formal.append('<div class="kh-table-scroll" role="region" aria-label="'+html.escape(b['headers'][0])+'比較" tabindex="0">\n<table class="kh-table">\n<thead><tr>'+''.join('<th scope="col">'+inline(x)+'</th>' for x in b['headers'])+'</tr></thead>\n<tbody>\n')
            for r in b['rows']: formal.append('<tr>'+''.join('<td>'+inline(x)+'</td>' for x in r)+'</tr>\n')
            formal.append('</tbody>\n</table>\n</div>\n')
            pure.append('| '+' | '.join(b['headers'])+' |\n| '+' | '.join(['---']*len(b['headers']))+' |\n'+'\n'.join('| '+' | '.join(r)+' |' for r in b['rows'])+'\n')
        elif k=='code':
            # Raw pre avoids theme highlighter tables and inline code overrides.
            formal.append('<div class="kh-code">\n<div class="kh-code-label">'+'<span>'+inline(b['title'])+'</span></div>\n<pre class="kh-pre">'+html.escape(b['text'])+'</pre>\n</div>\n')
            pure.extend(['#### '+b['title']+'\n','```'+b['lang']+'\n'+b['text']+'\n```\n'])
        elif k=='diagram':
            formal.append('<h4>'+inline(b['title'])+'</h4>\n<div class="kh-diagram">\n\n{% mermaid %}\n'+b['text']+'\n{% endmermaid %}\n\n</div>\n<p>'+inline(b['caption'])+'</p>\n')
            pure.extend(['#### '+b['title']+'\n','```mermaid\n'+b['text']+'\n```\n',b['caption']+'\n'])
    formal.append('</div>\n<!-- endtab -->\n')
formal.append('{% endtabs %}\n')
target.write_text('\n'.join(formal),encoding='utf-8')
(target.parent/'CDN-Header-Lost-pure.md').write_text('\n'.join(pure),encoding='utf-8')
(out/'content.json').write_text(json.dumps(tabs,ensure_ascii=False,indent=2),encoding='utf-8')
print('Wrote article and pure version,',len(tabs),'tabs')
