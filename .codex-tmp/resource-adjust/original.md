---
title: Resource-adjust
date: 2026-10-01 08:30:00
categories: kubernetes
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
tags:
    - 
toc:
toc_number:
comments :
---

{% tabs Resource-adjust%}


<!-- tab 狀況發生!-->



```bash
pods "promotion-web-api-76d9db5667-8wxfr" is forbidden: exceeded quota: default-4w42q, requested: limits.cpu=2250m, used: limits.cpu=7250m, limited: limits.cpu=8:Deployment does not have minimum availability.
```

這段訊息包含了三個層面的資訊

- 1️⃣ 資源配額（ResourceQuota）超限
- 2️⃣ Pod 建立被拒絕（forbidden）
- 3️⃣ Deployment 無法達到最低可用數量（minimum availability）


| 部分                                                         | 意義                                                                             |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **pods "promotion-web-api-76d9db5667-8wxfr" is forbidden** | 這個 Pod 嘗試被建立時，被 Kubernetes API Server 拒絕。                                      |
| **exceeded quota: default-4w42q**                          | 你所在的 Namespace 有設定一個 ResourceQuota（名字是 `default-4w42q`），Pod 的請求超過了這個 quota 限制。 |
| **requested: limits.cpu=2250m**                            | 新 Pod 嘗試要求 2250m（即 2.25 核心）的 CPU limit。                                        |
| **used: limits.cpu=7250m**                                 | 目前該 Namespace 裡已經使用了 7250m（即 7.25 核心）。                                         |
| **limited: limits.cpu=8**                                  | 這個 Namespace 被限制的上限是 8 核心。                                                     |
| **Deployment does not have minimum availability**          | 因為 Pod 沒建起來，Deployment 無法達到期望的 replica 數（例如希望 3 副本，實際只跑 2）。                    |



<!-- endtab -->


<!-- tab 資源調整的觀察-->


- resource request 下降 / 上升
- Node 數量減少 / 增加
- 是否 Throttled
- 有遇到 Limits 沒有正常套用的情形，目前在 rancher 手動調整 limits
- chart 檔 limits 需使用 pipeline v1.3.3-stable 以上版本



https://91app.slack.com/archives/CJHPX1DGF/p1746165782611889




<!-- endtab -->




<!-- tab request 寫 500m 的意義-->


## request 寫 500m  = 起一個 500m 的 pod 嗎?  


**`request: 500m` 是建立一個「排程時計入 0.5 CPU 需求」的 Pod，不是建立一台只有 0.5 CPU 的小主機。**


假設 Pod 只有一個容器

```yaml
resources:
  requests:
    cpu: 500m
  limits:
    cpu: 2000m
```


它實際跑在 Node 上，共用 Node 的 CPU


| 當下情況 | 可能的 CPU 使用量 |
|---|---|
| 沒什麼請求 | 可能只用 `20m`，不會固定消耗 `500m` |
| 工作變多，Node 有空閒 CPU | 可以用到 `800m`、`1500m` |
| 想使用超過 `2000m` | 受到 CPU limit 限速 |


1. **能不能排進 Node**：Scheduler 會確認這台 Node 還有至少 `500m` 尚未被其他 requests 占用
2. **CPU 忙碌時如何分配**：CPU request 會影響容器在競爭 CPU 時的相對分配權重


**「這個容器申請 0.5 CPU 的排程容量，最高允許使用 2 CPU；實際用多少取決於工作量與可用資源。」** 一般情況下，這不代表綁定半顆專屬 CPU


可以把 request 想成「訂位」，實際 CPU 使用量則是「當下有多少人在用」


例如一台 Node 有 `4000m` 可排程 CPU：

- 每個 Pod 的 request 是 `500m`，只考慮 CPU 時可以排入 8 個。
- 即使這 8 個 Pod 當下各只用 `10m`，排程容量仍已被訂滿。
- 新增第 9 個同樣的 Pod 時，Scheduler 會找其他有空間的 Node，而不是因為當下使用量很低就繼續塞。


**這樣做是避免大家平常很閒，被全部塞在同一台 Node，忙起來卻沒有足夠資源。** 所以排程依據是申報的 request，而非瞬間使用量


另外，CPU request 還有兩個作用：

| 用途 | 影響 |
|---|---|
| Node 的 CPU 發生競爭 | request 影響容器取得 CPU 時間的相對權重，不是綁定專屬核心 |
| HPA 使用 CPU 百分比擴縮 | request 是使用率的分母，例如實際 `400m` ÷ request `500m` \= 80% |


因此，**request 是容量規劃與分配的依據，limit 是執行時的使用上限。** Request 設太大容易讓 Node 容量閒置；設太小則可能讓太多 Pod 擠在一起，忙碌時互相競爭。[CPU 分配](<https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/>)、[HPA 計算方式](<https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/>)



設定 `requests.cpu: 500m` 後，一個標準流程是這樣

- Scheduler 會找一台還有至少 `500m` 可分配容量、且符合其他排程條件的 Node。
- 成功排入後，這份需求會被計入，避免同一份容量又被其他 Pod 的 request 占用。
- 沒有合適的 Node 時，Pod 可能維持 `Pending`，不保證建立後就能立刻執行。




但 CPU request 若設得過大，會占用過多排程容量，壓縮共用這批 Node 的其他服務新增 Pod 或擴容的空間。即使 Node 實際 CPU 使用率只有 10%，也可能因為已配置的 requests 接近可排程容量，無法再放入新 Pod。Scheduler 判斷資源是否足夠時，依據的是 requests，而不是當下的 CPU 使用率，若有啟用 Node 自動擴縮，也可能因此**提早新增 Node、增加成本**，而不是一直無法擴容



<!-- endtab -->



<!-- tab limits-->



那 limit 呢? 以剛才的例子,假如一個 pod request 500m 排進來了 然後他有 1000m limit, node 不是只剩 1m 了嗎


這裡的 **「只剩 `1m`」是指剩餘的排程容量，不是 CPU 當下只剩 `1m` 能運算。**

`request` 是訂位，`limit` 是使用上限。其他 Pod 訂了位置，但當下可能沒用完。

假設 Node 可排程 CPU 共 `2000m`：

| 項目 | CPU request | 當下實際使用 |
|---|---:|---:|
| 其他 Pods 合計 | `1499m` | `600m` |
| 新 Pod | `500m` | 可以嘗試使用到 `1000m` |
| 合計 | `1999m` | `1600m` |


如果其他pods也忙起來 就會變成 throttling嗎  

**可能變慢，但要區分「CPU 競爭」與「碰到 limit 的 throttling」。**

沿用 request `500m`、limit `1000m` 的 Pod：

| 情況 | 發生什麼事 |
|---|---|
| 其他 Pods 忙起來，Node 的 CPU 不夠大家同時使用 | 發生 **CPU 競爭**。容器要等待 CPU 執行時間，request 會影響分配權重；即使沒達到 limit，也可能變慢 |
| 這個容器用完自身 CPU limit 對應的配額 | 發生 **CPU throttling**，暫停取得 CPU，等下一個配額週期；即使 Node 還有空閒 CPU，也可能發生 |

所以，**其他 Pods 忙起來，不代表這個 Pod 一定觸發 limit throttling**。它可能只是分到的 CPU 時間減少；兩種情況也可能同時存在。

另外，request `500m` 不是「一忙起來就強制限制在 `500m`」，實際能取得多少 CPU 仍取決於當下競爭情況。




<!-- endtab -->




<!-- tab Node-->




**Node 屬於整個 Cluster，不屬於某個 namespace，因此 namespace 本身沒有固定分配幾台 Node。** 同一台 Node 可以同時執行不同 namespace 的 Pod。[官方：Namespaces](<https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>)



例如，這是一種可能的分布


| Node | 上面執行的 Pods |
|---|---|
| Node 1 | namespace A 的 Pod、namespace B 的 Pod |
| Node 2 | namespace A 的 Pod、namespace C 的 Pod |
| Node 3 | namespace B 的 Pod |



而 namespace CPU／Memory request 上限，通常是管理員設定的 **`ResourceQuota`**&#65292;不是每個 namespace 自動就有

假設 namespace A 設定


```yaml
hard:
  requests.cpu: "4"
  requests.memory: 8Gi
```


表示這個 namespace 內，受配額計算的 Pods

- CPU requests 加總不能超過 `4 CPU`
- Memory requests 加總不能超過 `8Gi`



**這是申請資源的總額上限，不表示預留了 4 CPU，也不表示分配了幾台 Node。** Pods 可能集中在一台，也可能分散在多台。[官方：ResourceQuota](<https://kubernetes.io/docs/concepts/policy/resource-quotas/>)



因此會有兩種不同的「放不進去」

| 情況 | 結果 |
|---|---|
| namespace 配額已滿，即使 Node 還有空間 | 新 Pod 的建立請求會被配額檢查拒絕 |
| namespace 配額還夠，但沒有符合需求的 Node | Pod 可以建立，但可能維持 `Pending` |





而在**有啟用 Node 自動擴縮**之下，例如 Cluster Autoscaler 或 Karpenter 就可能依據需求新增或減少 Node


流程是

1. Pod 宣告 CPU／Memory `request`。
2. Scheduler 找不到容量足夠、且符合排程條件的 Node，Pod 維持 `Pending`。
3. Node Autoscaler 判斷新增 Node 能否解決問題。
4. 若符合擴容設定且未達上限，就新增合適的 Node，再由 Scheduler 排入 Pod。



**不是所有 `Pending` 都會觸發加 Node**。例如排程條件無法滿足、已達擴容上限，或雲端容量不足，就可能無法擴容。[Kubernetes：Node 自動擴縮](<https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/>)



<!-- endtab -->






<!-- tab HPA-->


## 使用率 - 擴展的標準

若設定  CPU Utilization 百分比，它的 CPU 使用率是相對於 request

```bash
HPA CPU 使用率 = 實際 CPU 使用量 ÷ CPU request
```

同樣使用 `400m` CPU


| CPU request | HPA 看到的使用率 |
|---|---:|
| `500m` | 80% |
| `1000m` | 40% |



## 假設提高 request 對 HPA 的影響


假設提高 request，每個 Pod 更占排程容量，另一方面可能降低 HPA 算出的使用率，要判斷目前環境調整後的結果，需要一起看 **Pod 的 request／limit、replicas／HPA，以及 Node 規格與自動擴縮設定。**




**假設每個 Pod 的 CPU request 合計是 `500m`，HPA 的 `minReplicas: 2` 代表至少維持 2 個副本，合計需要 `1000m` 的 CPU 排程容量。**



## POD 都會放在同一個 NODE 嗎?


- **HPA 決定副本數**：在 2～4 個之間調整
- **Scheduler 決定放哪裡**：兩個 Pod 可以在同一台 Node，也可以分別放在不同 Node
- **成功排入才占用排程容量**：如果容量不足，部分 Pod 可能維持 `Pending`


## Node 不夠擴展


**假設服務需要 2 個 Pod、每個 request 是 `500m`，而所有符合條件的 Node 合計只剩 `500m` 排程容量**


| Pod | 結果 |
|---|---|
| 第一個 | 成功排入，容器正常啟動後成為 `Running` |
| 第二個 | 無法排入，維持 `Pending`，通常會顯示 `Insufficient cpu` |


**HPA 的 `minReplicas: 2` 是要求至少 2 個副本，不保證當下有足夠資源讓兩個都跑起來。**

若已啟用 Node 自動擴縮，且允許擴容，新增 Node 後，第二個 Pod 才有機會排入；否則會繼續等待容量釋放



<!-- endtab -->






<!-- tab Running and Ready-->


**`Running` 與 `Ready` 是兩個不同維度，不是互相取代的狀態。**

- **`Running`**&#65306;Pod 的執行階段，表示容器已啟動。
- **`Ready`**&#65306;Pod 的就緒條件，表示是否準備好接流量。

典型變化是：

```
Pending
   ↓
Running + Ready=False   啟動中，尚未就緒
   ↓
Running + Ready=True    已就緒，可以接流量
   ↓ readiness 檢查失敗
Running + Ready=False   程式仍在跑，暫停接收一般 Service 的新流量
```

所以 **Pod Ready 之後，仍然是 Running；也可能在持續 Running 的期間，反覆變成 Ready 或未 Ready。**


例如

1. **程式剛啟動，還在初始化**

   容器裡的 API 程式已經執行，所以是 `Running`，但還在載入設定、預熱資料，尚未準備好處理請求。此時 readiness 可能連不上，或端點回傳 `503`。初始化完成、檢查通過後，才變成 `Ready`。
2. **服務原本正常，必要的依賴暫時故障**

   例如 API 程式仍活著，也能接受 HTTP 連線，但必要的資料庫連線失敗。**如果 readiness 的檢查邏輯有檢查這項依賴**，就可能回傳 `503`，讓 Pod 變成未 Ready。Kubernetes 不會自動知道資料庫故障，必須由檢查邏輯反映。
3. **服務太忙，健康檢查逾時**

   例如 CPU 競爭、throttling 或執行緒池耗盡，讓 `/health/ready` 無法在設定的時間內回應。程式沒有退出，所以仍是 `Running`；但檢查失敗達到設定門檻後，就會變成未 Ready。

這三種情況的共同點是：**程式仍在執行，但就緒檢查尚未成功，或已經失敗。** 一般 Service 會在就緒狀態更新後，停止將新流量導向該 Pod；readiness 失敗本身不會重啟容器，恢復通過檢查後可以再次接流量。[Kubernetes 官方：探針行為](<https://kubernetes.io/docs/concepts/workloads/pods/probes/>)




<!-- endtab -->





{% endtabs %}
