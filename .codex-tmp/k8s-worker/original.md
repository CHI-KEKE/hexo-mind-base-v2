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


{% tabs worker-pod-cpu-memory%}



<!-- tab requests-->



- `worker.resources`：通常對應 **requests**（排程保留的最小資源），request 是「這個 Container 向 Kubernetes 申請／要求多少資源」
- `limits`：對應 **上限**（CPU 超過會 throttling、Memory 超過會 OOMKill）。

目前設定（以單一 worker Pod/主要 container 來看）：

- request：`cpu=500m`、`memory=2000Mi`
- limit：`cpu=1000m`、`memory=2000Mi`


> 這些數值是「每個 Pod（更精確是每個 container）」的設定，不是整個服務總量



```yaml
resources:
  requests:
    cpu: 500m
    memory: 2000Mi
  limits:
    cpu: 1000m
    memory: 2000Mi
```


request = 我要求你至少幫我準備這麼多資源，所以 Worker 跟 Kubernetes 說我要執行而我要

- CPU：我需要 500m
- RAM：我需要 2000Mi

Kubernetes 的 Scheduler 再決定「這個 Pod 要放到哪一台 Node？」，這就會看 Node 能不能容納這個 request


假設

```bash
Node A
CPU capacity = 4000m
Memory capacity = 8Gi
```


現在已經有其他 Pod request

```bash
CPU    3000m / 4000m
Memory 7Gi   / 8Gi
```


我的 Pod 要

```bash
request:
  cpu: 500m
  memory: 2000Mi
```

CPU：3000 + 500 = 3500m  ✓

Memory：7Gi + ~2Gi = ~9Gi > 8Gi  ✗

因此 Scheduler 不會把這個 Pod 排到 Node A。

這就是為什麼叫 request，Pod 在被排程時，向 Kubernetes 宣告「我需要這麼多資源，請幫我找一台容得下我的 Node」


<!-- endtab -->






<!-- tab limit-->




limit 則是在講 Pod 被放上 Node 之後

- request CPU    = 500m
- limit CPU      = 1000m
- request Memory = 2000Mi
- limit Memory   = 2000Mi



```bash
             request                 limit
                ↓                      ↓
CPU       ─────500m──────────────────1000m──→
             排程依據                  上限


Memory    ───────────────2000Mi────────────→
                          ↑
                   request = limit
```

CPU 的意思大致是「排程時幫我按照 500m 的需求找位置；執行時最多讓我使用到 1000m。」CPU 1000m 大約就是 1 CPU core 的運算額度。超過 CPU limit 時通常會被 throttle，程式變慢，通常不會因此直接被殺掉。

但 Memory 則不同：

request = 2000Mi
limit   = 2000Mi

代表「排程時請按照約 2Gi RAM 幫我找位置，而且我的 Container 最多也只能用約 2Gi。」


```bash
Memory usage
   │
   │
2Gi├──────────────── LIMIT
   │             ↗ 💥
   │           ↗
   │         ↗
1Gi│       ↗
   │     ↗
   │
0  └──────────────────────→ time
```


Container 觸及／超過 memory limit 並出現記憶體壓力時，可能被 Linux cgroup OOM 機制終止，Kubernetes 最後就可能看到 Reason: OOMKilled



<!-- endtab -->







<!-- tab HPA 設定-->


- `enabled: true`
- `minReplicas: 2`
- `maxReplicas: 4`
- `targetCPUUtilizationPercentage: 90`
- `targetMemoryUtilizationPercentage: 70`


代表 Pod 數會在 **2 ~ 4** 之間自動調整



HPA 預設看的是 **整體平均利用率**（對應 workload 內所有 Pod），不是單一 Pod 一過線就一定擴。

概念公式（簡化）：

`desiredReplicas = ceil(currentReplicas × currentMetricValue / desiredMetricValue)`

其中 `currentMetricValue` 為目前平均利用率，`desiredMetricValue` 為目標利用率（例如 Memory 70%）


- CPU 平均 70%，target 90%：`ceil(2 × 70 / 90) = 2`
- Memory 平均 65%，target 70%：`ceil(2 × 65 / 70) = 2`

=> 維持 2 Pods。

若 CPU 平均 95%、Memory 平均 80%：

- CPU: `ceil(2 × 95 / 90) = 3`
- Memory: `ceil(2 × 80 / 70) = 3`

=> 擴到 3 Pods（仍受 min/max 夾制）



因為 HPA 是比例控制：目標是把「每 Pod 平均負載」拉回 target。

- 平均負載是 target 的 2 倍 -> 副本理論上也要約 2 倍。
- 平均負載是 target 的 1/2 -> 副本可縮成約 1/2。

這比固定每次 +1 更快貼近目標。


那「目前副本數 × 平均利用率」是否等於「利用率總和」？

在每個 Pod request 相同時，可以這樣理解，但更本質上，HPA 是看「總使用量 / 總 request」的加權利用率



若單一 job 需要的記憶體已超過單 Pod 可承受上限，**只靠 HPA 通常無效**。  
HPA 解的是「總量/吞吐」，不是「單一工作過大」。

建議方向：

1. 調大單 Pod 記憶體 request/limit（先讓單 job 跑得動）。
2. 將 job 切批/分段，降低單次峰值記憶體。
3. 降低同 Pod 併發，避免重 job 疊加。
4. 將重型 job 分離到獨立 worker group 與資源規格。


最常觸發擴容的情況是工作量多且工作內容很重（每個 job 本身耗 CPU/Memory 高），只要反映到平均 CPU/Memory 利用率超過 target，就會觸發 scale out




<!-- endtab -->






<!-- tab worker-->


- 1 個 Pod：可視為 1 個常駐 worker 實例。
- 2 個 Pod：可視為 2 個常駐 worker 實例，同時從同一批 job（queue/group）取件處理。

工作分配由 queue/consumer 調度決定，不保證平均分配到每個 Pod。



一般情況下，不是「1 個 job 對應 1 個 container」

在此 worker 型架構中可這樣理解

- Pod：K8S 執行單位。
- Container（worker 程式）：常駐行程，持續從 queue 拉工作。
- Job：worker 程式內被處理的任務，不是 K8S container 實體。

因此「一個 Pod 同時處理多個 job」通常是因為同一個 worker container 內有並行處理能力，  
不是因為 Pod 內新增了多個對應 job 的 container。



單一 worker 實例可同時處理幾個 job，不能只看 Thread Count。

實際同時處理數由多層限制共同決定：

1. Group 層：`Thread Count`（整個 group 的總併發上限）
2. Job 層：`Max Processes`（該 job 的併發上限）
3. Worker 程式層：consumer concurrency / prefetch / thread pool 等設定
4. 執行拓撲層：當下可用 Pod 數量與調度分配結果

因此單 Pod 併發通常不是單一欄位可直接判定，而是上述條件的交集結果。


單一 Pod 確實可能同時處理多個 job。  
當多個 job 在同一 Pod 內並行執行時，會共享同一組 CPU/Memory 配額，因此會互相影響：

1. 某個 job 吃掉較多 CPU，其他 job 可能延遲上升或吞吐下降。
2. CPU 接近/超過 limit 時，可能出現 throttling。
3. 多個記憶體重型 job 疊加時，容易造成 memory 壓力，嚴重時可能 OOMKill。




<!-- endtab -->





{% endtabs %}