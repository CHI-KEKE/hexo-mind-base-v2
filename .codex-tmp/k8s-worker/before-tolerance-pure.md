---
title: worker-pod-cpu-memory
date: 2026-09-19 15:40:00
categories: kubernetes
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
tags:
    - 
toc:
toc_number:
comments :
---

## requests

### 先找得到位置，才能開始工作

同一份工作設定有三種不同用途：requests 決定排程時需要多少資源，limits 限制執行時的用量，HPA 則調整 Worker 副本數。先從一個 Worker Container 的需求開始。

### 一個 Container 的資源設定

本文案例為每個 Pod 配置一個主要 Worker Container。以下數值屬於該 Container，不是整個服務的總量；若還有 sidecar、init container 或 Pod overhead，排程需求還要依實際配置計算。

| 資源 | requests | limits |
| --- | --- | --- |
| CPU | `500m` | `1000m` |
| Memory | `2000Mi` | `2000Mi` |

yaml

```yaml
resources:
  requests:
    cpu: 500m
    memory: 2000Mi
  limits:
    cpu: 1000m
    memory: 2000Mi
```

> `worker.resources` 看起來是專案或 Helm Chart 的設定名稱，不能只憑名稱認定它等同 `requests`。本文以實際產出的 `resources.requests` 與 `resources.limits` 為準；Chart 對應仍待核對。

`requests` 是 Container 宣告的資源需求。Scheduler 依此尋找容得下 Pod 的 Node；它不表示 Container 每一刻都會使用這麼多資源，也不表示預先占用一整塊專屬 CPU 或實體記憶體。

### Node A：CPU 放得下，Memory 放不下

假設 Node A 的 CPU capacity 為 `4000m`，Memory capacity 為 `8Gi`。實際排程比較的是 `allocatable`，通常會扣掉系統保留量；以下為簡化算例，暫以相同數字作為可分配上限。

| 資源 | 既有 requests | 新增需求 | 合計與結果 |
| --- | --- | --- | --- |
| CPU | `3000m` | `500m` | `3500m ≤ 4000m`，足夠 |
| Memory | `7Gi = 7168Mi` | `2000Mi` | `9168Mi > 8192Mi`，不足 |

`2000Mi = 1.953125Gi`，所以記憶體合計是 `8.953125Gi`。若將新增需求近似為 2Gi，合計便約為 9Gi。兩種算法的結論相同：Node A 無法容納這個 Pod。

CPU：3500 / 4000m

灰藍為既有 3000m，藍色為新增 500m，右側剩餘 500m。

Memory：9168 / 8192Mi

灰藍為既有 7168Mi，藍色為新增 2000Mi；上限線右側超出 976Mi。兩條容量帶各自使用不同單位與尺度。

### 排程判斷：每一種資源都要足夠

本例依序確認 CPU 與 Memory。CPU 足夠、Memory 不足，故排除 Node A；若兩者都足夠，仍須通過其他排程條件。若沒有任何可用候選，Pod 可能維持 Pending。

資源申請與限制的依據見 [Kubernetes 資源管理文件](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)。

## limit

### 上限相同，CPU 與 Memory 的反應不同

Pod 排進 Node 之後，仍需控制執行時的資源用量。CPU 額度不足通常造成等待，記憶體不足則可能使 Container 中的程序遭到終止。

| 比較項目 | CPU | Memory |
| --- | --- | --- |
| request | `500m`，排程需求 | `2000Mi`，排程需求 |
| limit | `1000m`，即 1 CPU 的運算額度 | `2000Mi`，約 `1.953Gi` |
| 接近或超過限制 | CPU 配額耗盡時 throttling，通常不直接因此殺掉程序 | 達到限制且無法滿足記憶體需求時，可能觸發 cgroup OOM |
| 可見影響 | 執行變慢、延遲增加、吞吐下降 | Container 狀態可能顯示 `Reason: OOMKilled` |

### CPU 配額刻度與 Memory 上限

CPU：request 500m → limit 1000m

0 → 500m request → 1000m limit

500m 是排程需求；Node 有餘裕時可使用更多 CPU，但仍受 1000m 的執行配額限制。

Memory：request = limit = 2000Mi

0 → 1000Mi → 2000Mi request / limit

2000Mi 約等於 1.953Gi。兩個欄位數值相同，但排程需求與執行上限仍是不同角色。

### Memory 使用量逐漸增加時

這是概念示意，沒有實測時間軸。使用量可從 0、約 1Gi 逐漸接近約 2Gi；精確上限為 2000Mi，不是一碰到線就必定立刻 OOMKilled。

> Memory limit 的執行帶有反應式特性；是否觸發 OOM 與當下記憶體需求、回收及核心處理有關。Container 後續是否重啟，還要看工作負載與重啟政策。

CPU 的 `1000m` 表示 1 CPU 單位，依環境可對應實體核心或虛擬 CPU，不代表專屬綁定一顆實體核心。本文的限制行為以一般 Linux Container 環境說明。

## HPA 設定

### 增加副本，分擔可平行處理的工作

HPA 調整的是 Worker 副本數。它可以增加整體處理能力，但新增 Pod 不會自動提高既有 Container 的記憶體上限。

### 案例設定與利用率基準

| 設定 | 案例值 | 用途 |
| --- | --- | --- |
| `enabled` | `true` | 專案設定啟用 HPA |
| `minReplicas` | `2` | 副本下限 |
| `maxReplicas` | `4` | 副本上限 |
| `targetCPUUtilizationPercentage` | `90` | CPU 目標利用率 90% |
| `targetMemoryUtilizationPercentage` | `70` | Memory 目標利用率 70% |

> 以上是案例中的專案設定名稱，不是可直接套用的 HPA manifest。CPU 與 Memory 多指標通常使用 `autoscaling/v2` 的 `spec.metrics`；實際啟用與欄位映射應核對 Chart 產物。

本例假設 HPA 使用資源利用率指標。百分比以 `requests` 為基準：CPU 的 `90% × 500m = 450m`，Memory 的 `70% × 2000Mi = 1400Mi`。這些是目標平均值，不是 limits，也不是單一 Pod 的強制擴容線。

HPA 綜合目標工作負載中符合計算條件的 Pod 資料，不是任一 Pod 一超線就必定擴容。就資源利用率而言，可用資料中的「總使用量 ÷ 總 request」反映加權利用率；requests 相同時，才可直接理解為各 Pod 百分比的算術平均。缺失指標、未就緒 Pod 等還會影響實際計算。

### 先用簡化公式理解副本數

text

```text
desiredReplicas = ceil(currentReplicas × currentMetricValue / desiredMetricValue)
```

`currentMetricValue` 是目前利用率，`desiredMetricValue` 是目標利用率；`ceil` 表示向上取整。下面兩組都從 2 個 Pod 開始，先展示理想公式，再補上實際控制條件。

| 情境 | CPU 計算 | Memory 計算 | 判讀 |
| --- | --- | --- | --- |
| 平均 CPU 70%、Memory 65% | `ceil(2 × 70 / 90) = 2` | `ceil(2 × 65 / 70) = 2` | 維持 2 個 Pod |
| 平均 CPU 95%、Memory 80% | `ceil(2 × 95 / 90) = 3` | `ceil(2 × 80 / 70) = 3` | 簡化公式均為 3；實際擴容依下方條件判斷 |

> 預設 10% 容忍範圍下，CPU 比值 `95 / 90 ≈ 1.056` 仍在容忍範圍內，因此不會只因這個 CPU 值就擴容。Memory 比值 `80 / 70 ≈ 1.143` 超出範圍，在指標有效、其他條件允許時可建議 3 個副本。最終仍受擴縮政策、穩定視窗與副本上下限影響。

### 從多個指標得到一個副本建議

圖示表達多指標匯合與控制條件，不代表控制器逐行實作順序。CPU 與 Memory 分別評估後，取最大的副本建議；再綜合政策及 2～4 的上下限。副本目標改變也不保證新 Pod 立即 Ready。

若部分指標取得失敗，而其他指標建議縮容，HPA 可能跳過縮容；有效指標若建議擴容，仍可能擴容。實際行為應查看 HPA 的條件與事件。

### 為何按比例調整，而不是每次只加一個？

- 在總負載可分攤且近似不變的假設下，平均負載若是目標的 2 倍，副本理論上也需要約 2 倍。
- 平均負載若是目標的 1/2，副本理論上可縮成約 1/2，但仍受下限與縮容控制限制。
- 每個 Pod request 相同時，「目前副本數 × 平均利用率」可理解為各 Pod 利用率的總和；request 不同時不能直接套用這個直觀解釋。
- 工作量多、每個任務耗用資源高，且負載反映在平均 CPU／Memory 指標上時，可能推動擴容；僅有 Queue 積壓不保證這兩種指標會升高。

### 單一任務太大時，增加 Pod 仍可能無效

若單一 job 的記憶體需求已超過一個 Container 的上限，只增加副本通常無法讓這個 job 執行成功。HPA 改善的是可分攤的總量與吞吐；單一工作的峰值仍需另外處理。

| 改善方向 | 處理的問題 |
| --- | --- |
| 調大單 Pod 主要 Container 的記憶體 request／limit | 先讓單一 job 有足夠空間；同步確認 Node 能否容納 |
| 將 job 切批或分段 | 降低單次峰值記憶體 |
| 降低同 Pod 併發 | 避免多個重型 job 的峰值疊加 |
| 分離獨立 Worker group 與資源規格 | 讓重型 job 使用適合的資源配置 |

公式、容忍範圍、多指標及擴縮政策依據見 [Kubernetes HPA 文件](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)。本文未取得實際叢集版本與 HPA manifest，因此案例保留明確假設。

## worker

### 多個任務，共享同一個 Worker 的資源

這裡討論的是常駐 Worker 從 Queue 取件的架構。一個 Pod 可承載一個主要 Worker 實例，而一個 Worker Container 內又可能同時處理多個任務。

| 名詞 | 本文情境 |
| --- | --- |
| Pod | Kubernetes 的執行與排程單位；本例每個 Pod 有一個主要 Worker Container |
| Container | 執行常駐 Worker 程式，持續從 Queue 拉取工作 |
| job | Worker 處理的應用層任務；不是為每個任務新增一個 Container，也不等同 Kubernetes 的 Job 物件 |

### 兩個 Pod，共用一個工作來源

一個 Pod 可視為一個常駐 Worker 實例，兩個 Pod 就有兩個實例。箭頭代表 Worker 主動取件的關係，不表示 Queue 主動推送，也不表示任務平均分配。實際分配依 Queue／consumer 機制決定；group 是否對應同一佇列仍須看實作。

### 放大一個 Pod：任務共享資源配額

任務甲、任務乙與其他任務位於同一個 Container 內，箭頭表示共同耗用資源，沒有先後順序。圖中的任務數僅供示意，不代表實際併發設定，也不是 Pod 內有三個 Container。

### 併發量由多層限制共同決定

單一 Worker 能同時處理多少 job，不能只看 `Thread Count`。以下列出案例中的四層限制；專案欄位的作用範圍仍需以 Worker 平台文件或程式碼確認。

| 限制層 | 設定或條件 | 需要核對的範圍 |
| --- | --- | --- |
| Group | `Thread Count` | 案例假設為整個 group 的總併發上限；確認是否跨 Pod 共用 |
| Job | `Max Processes` | 案例假設為該 job 的併發上限；確認是否跨 Worker 統計 |
| Worker 程式 | consumer concurrency／prefetch／thread pool | 處理併發、預取與執行緒是不同限制；prefetch 不直接等於同時執行數 |
| 執行拓撲 | 當下可用 Pod 數量與調度分配 | 確認任務分配、可用實例與資源限制 |

單 Pod 的實際併發是這些條件共同作用的結果，不能直接由單一欄位推算，也不能把 group 上限直接乘上 Pod 數量。

### 多個任務並行時，會互相影響

- 某個 job 消耗較多 CPU，其他 job 的延遲可能增加、吞吐可能下降。
- 合計 CPU 用量耗盡 limit 配額時，可能發生 throttling。
- 多個記憶體重型 job 疊加會增加記憶體壓力，嚴重時可能造成 OOMKilled，影響同一 Container 內的工作。

> 判斷瓶頸時，同時觀察單一任務的資源峰值、單 Pod 併發與可用副本數。調大 Container、降低併發與增加 Pod 各自處理不同問題，應依實際瓶頸選擇。

圖示來源：[Kubernetes 專案 Logo](https://github.com/kubernetes/kubernetes/tree/master/logo)。本文圖表為案例說明，不代表已驗證的正式環境拓撲。
