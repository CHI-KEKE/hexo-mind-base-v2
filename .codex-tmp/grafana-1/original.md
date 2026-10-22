---
title: 監控基礎架構
date: 2026-09-22 08:29:00
categories: Metric
top_img: 
cover : 
tags:
    - 
toc:
toc_number:
comments :
---

{% tabs grafana-1%}



<!-- tab 架構-->




```bash
你的系統
Pod / API / Worker / DB
       │
       ├── 數值型資料 ──→ Prometheus ──┐
       │   CPU、Memory、Request 數     │
       │                              ├──→ Grafana
       └── 文字型 Log ──→ Loki ───────┘
           Error、Exception、訊息
```

例如凌晨收到通知：

API Error Rate > 5%

你第一個問題通常是：

現在錯誤很多嗎？
從什麼時候開始？
哪一台 Pod 特別嚴重？

這些很適合 Prometheus。

接著你會想知道：

到底報什麼錯？
哪個 endpoint？
exception 是什麼？
request id 是多少？

這時候就進 Loki。

最後 Grafana 把這兩條調查路線串起來



<!-- endtab -->


<!-- tab metric-->


metric：單數，一個指標，例如「CPU 使用率這個 metric」
metrics：複數，多個指標，也常泛指「監控指標資料」


Metric（指標）跟一般數值最大的差異，在於 Metric 是「帶著觀測對象、時間與分類資訊的數值」，所以它可以持續拿來比較系統狀態

一般數值只告訴你「現在是多少」，Metric 則讓這個數字可以回答「誰、什麼時候、屬於哪一類，以及它怎麼變化」
所以 Metric 的核心依然是數字，例如：

80
512
1000
0.52

關鍵在於這個數字被賦予了可持續觀測的上下文。



它是用來量化某個系統狀態或行為的數值指標

例如 Pod 的 Memory：

container_memory_working_set_bytes = 1,572,864,000

已經可以直接當 Metric。你可以把它理解成比較接近 raw measurement


時間       memory
08:00      1.2 GB
08:01      1.3 GB
08:02      1.5 GB


但也可以進一步加工。例如原始 Metric 是：

http_requests_total

08:00 → 10000
08:01 → 10600
08:02 → 11500

這是一個持續累加的 Counter。

你真正關心的可能是：

「現在每秒有多少 Request？」

Prometheus 就可以計算：

rate(http_requests_total[5m])

得到：

08:00 → 8 req/s
08:01 → 10 req/s
08:02 → 13 req/s

這就是由 Metric 計算出的衍生指標。

所以可以把資料流想成：

真實世界 / 系統
        ↓
原始 measurement
        ↓
Metric
        ↓
計算 / 聚合
        ↓
衍生 Metric / 查詢結果
        ↓
Grafana

例如：

Container 實際用了多少記憶體
        ↓
container_memory_working_set_bytes
        ↓
1,800,000,000 bytes
        ↓
÷ 1024³
        ↓
1.68 GiB

甚至：

Memory Used = 1.68 GiB
Memory Limit = 2 GiB

        ↓ 計算

Memory Usage = 84%

1.68 GiB 本身可以是 Metric，84% 這種加工後的結果也可以作為指標來看。




假設程式裡有一個普通變數：

request_count = 100

這就是一般數值：

100

如果程式結束，這個數字可能也跟著消失。

現在我們希望監控：

order-api 到底收到多少 Request？

於是建立一個 Metric：

http_requests_total 100

這時候 100 有名字了：

http_requests_total
        ↓
      100

但還是不夠。

因為系統可能有很多 API：

GET  /users
POST /orders
GET  /products

所以加入 Label：

http_requests_total{
    method="POST",
    path="/orders",
    status="200"
} 100

現在這個數字就可以被分類：

                    ┌─ method = POST
                    │
http_requests_total ├─ path   = /orders
                    │
                    └─ status = 200
                              │
                              ▼
                             100

接著 Prometheus 每隔一段時間來取得它：

08:00 → 100
08:01 → 150
08:02 → 230
08:03 → 310

於是我們得到非常重要的東西：

時間序列（Time Series）。

數值
 ↑
350 |                ●
300 |             ●
250 |
200 |          ●
150 |       ●
100 |    ●
    +--------------------→ 時間
      08:00 01 02 03

這時候你已經可以開始問：

最近增加多快？
最近 5 分鐘有多少 Request？
今天跟昨天差多少？
哪個 Pod Request 最多？
500 Error 比例多少？

Metric 的威力才真正出現。

Metric 通常會有 Label，Label 讓同一個 Metric 可以切成不同角度觀察，像是在數字上貼分類標籤
http_requests_total{
    method="GET",
    status="200",
    pod="api-01"
} 5000

你就可以切：

全部 Request
    │
    ├── GET
    │
    ├── POST
    │
    ├── 200
    │
    ├── 404
    │
    ├── 500
    │
    ├── api-01
    │
    └── api-02

<!-- endtab -->


<!-- tab Prometheus-->


Prometheus 是一套專門「持續收集、保存、查詢系統 Metric」的開源監控系統。


它最初在 SoundCloud 內部誕生，由 Matt T. Proud 與 Julius Volz 在 2012 年開始建立；Prometheus 官方也明確列出兩人為專案發起者。

它後來在 2016 年加入 CNCF，成為 Kubernetes 之後第二個 CNCF hosted project，並在 2018 年畢業成為 CNCF graduated project。




Prometheus 主要負責「定期取得 Metric → 儲存 → 查詢/計算」。實際量測通常由應用程式、OS、Kubernetes 元件或 Exporter 完成。



Pod / Container
     │
     │ 實際使用記憶體
     ▼
Linux Kernel / cgroup
     │
     │ 提供原始資訊
     ▼
監控元件
     │
     │ 暴露成 Metric
     │
     │ container_memory_working_set_bytes 1.8GB
     ▼
Prometheus
     │
     ├── 定期抓取（scrape）
     ├── 儲存歷史資料
     └── 查詢 / 計算
             │
             ▼
           Grafana


Prometheus 本身通常沒有跑進你的 Pod 裡面說：

「我來檢查你現在用了多少 RAM。」

底層的 container/cgroup/Kubernetes 相關元件掌握這些資訊，再把它整理成 Prometheus 能讀的 Metric。

Prometheus 做的事情比較像：

Prometheus：
「每 15 秒我要來拿一次最新數字。」

08:00:00 → 1.20 GiB
08:00:15 → 1.25 GiB
08:00:30 → 1.31 GiB
08:00:45 → 1.42 GiB

這個定期取得資料的動作叫做：

Scrape（抓取）



Kubernetes
「我要讓 10 個 API Pod 跑起來」

        ↓

┌─────┬─────┬─────┬─────┐
│Pod 1│Pod 2│Pod 3│ ... │
└─────┴─────┴─────┴─────┘

Prometheus
「我要知道這 10 個 Pod 現在過得好不好」

        ↓

CPU
Memory
Request Rate
Error Rate
Latency



Counter、Gauge、Histogram、Summary 是 Prometheus Metric 的四種主要型別。

它們都在記錄「數字」，差別在於：

你想用這個數字回答什麼問題？


```bash
我想記錄一個數字
      │
      ├── 只會累加？
      │      ↓
      │   Counter
      │   Request 總數、Error 總數
      │
      ├── 會增加也會減少？
      │      ↓
      │    Gauge
      │    CPU、Memory、在線人數
      │
      └── 想知道大量事件的「分布」？
             │
             ├── Histogram
             │   Request 花多久
             │   0~100ms 有幾次？
             │   100~500ms 有幾次？
             │
             └── Summary
                 Request 花多久
                 Client 端直接計算 quantile
```



<!-- endtab -->



<!-- tab Loki-->



Loki 是專門用來集中儲存、搜尋、分析 Logs 的系統

它由 Grafana Labs 在 2018 年啟動，核心發起者之一是 Tom Wilkie；官方資料也提到 Tom Wilkie 與 David Kaltschmidt 的早期設計文件啟動了 Loki 專案。Loki 在 2018 年底的 KubeCon Seattle 正式公開。Grafana Labs 自己常用一句概念來介紹 Loki：

Like Prometheus, but for logs.


想像你有 Kubernetes：

Order API

├── Pod A
│    └── logs...
│
├── Pod B
│    └── logs...
│
├── Pod C
│    └── logs...
│
├── Pod D
│    └── logs...
│
└── Pod E
     └── logs...

突然有人跟你說：

「剛剛 10:32 結帳失敗。」

問題來了。

到底是哪個 Pod？

Pod A？
Pod B？
Pod C？
Pod D？
Pod E？

更麻煩的是 Kubernetes 的 Pod 還可能：

Crash
 ↓
Restart
 ↓
舊 Pod 消失

所以需要一個中央地方保存 Log：

Pod A ──┐
Pod B ──┤
Pod C ──┼──→ Loki
Pod D ──┤       │
Pod E ──┘       │
                ▼
           集中保存 Log

這就是 Loki 最基本的存在理由。




```bash

Pod / API / Worker
        │
        ├── Metrics ──→ Prometheus
        │
        │   CPU = 80%
        │   Memory = 1.8 GB
        │   Error count = 12
        │
        └── Logs ─────→ Loki
            "Start processing job"
            "DynamoDB timeout"
            "OutOfMemoryException"
```


Loki 收的是什麼？

假設你的 C# Worker 有：

_logger.LogInformation("Start processing ShopId {ShopId}", shopId);

_logger.LogError(
    exception,
    "Failed to process promotion {PromotionId}",
    promotionId);

程式實際產生：

08:30:01 INFO  Start processing ShopId 2
08:30:02 INFO  Loading promotions
08:30:05 ERROR Failed to process promotion 574730
08:30:05 ERROR System.TimeoutException...

這些 Log 最後可以被送進 Loki 保存。

然後你可以用 Loki 的查詢語言 LogQL 搜尋：

{service="promotion-worker"} |= "ERROR"

意思大概就是：

幫我找 promotion-worker 裡包含 ERROR 的 Log。


1. C# 程式先產生 Log

例如 ASP.NET Core：

_logger.LogInformation(
    "Start processing ShopId {ShopId}",
    shopId);

假設：

shopId = 2

執行之後會產生類似：

2026-09-22 08:30:01 INFO Start processing ShopId 2

這時候 Loki 還沒有收到任何東西。

ILogger 只是把 Log 交給設定好的 Logging Provider。

例如在 Container / Kubernetes 的常見情況，程式把 Log 寫到：

stdout

也就是標準輸出。

所以你執行：

kubectl logs promotion-worker-abc

可以看到：

INFO Start processing ShopId 2
INFO Loading promotions
ERROR DynamoDB timeout

這代表 Kubernetes / Container runtime 已經能取得這些 stdout/stderr Log。

2. Kubernetes Node 上會有這些 Container Logs

概念上可以想成：

Pod
│
└── Container
      │
      │ stdout
      ▼
Container Runtime
      │
      ▼
Node 上的 container log

例如 Node 上可能存在對應的 container log 檔案。

所以到這一步：

Application
    ↓
stdout
    ↓
Container Runtime
    ↓
Node 上的 Log

依然還沒進 Loki。

3. Log Collector 負責「搬運」

這時候會有另一個程式專門收集這些 Logs。

例如現在 Grafana 生態常見的 Grafana Alloy，其他環境也可能使用 Fluent Bit；較舊的 Loki 架構教學則常看到 Promtail。

它做的事情可以簡化成：

「Node 有新的 Log！」

        ↓

讀取

2026-09-22 08:30 INFO Start Job
2026-09-22 08:31 ERROR Timeout

        ↓

加上一些 metadata / labels

namespace="production"
pod="promotion-worker-abc"
container="worker"
service="promotion-worker"

        ↓

送給 Loki

所以 Log Collector 很像一個搬運工。

4. Collector 透過網路把 Log Push 給 Loki

這一步才真的「進 Loki」。

概念上：

Log Collector
      │
      │ HTTP
      │ Push Logs
      ▼
   Loki API

送過去的內容概念上可能包含：

timestamp:
2026-09-22 08:30:01

labels:
service="promotion-worker"
pod="promotion-worker-abc"
namespace="production"

log:
"INFO Start processing ShopId 2"

Loki 收到後才負責保存與後續查詢。

5. Grafana 再去查 Loki

當你在 Grafana 寫：

{service="promotion-worker"} |= "ERROR"

資料方向是：

你
 │
 ▼
Grafana
 │
 │ LogQL Query
 ▼
Loki
 │
 │ Query Result
 ▼
Grafana
 │
 ▼
你看到 Logs

所以 Grafana 通常也不是 Log 的儲存位置。



<!-- endtab -->



<!-- tab Grafana-->

它會去查詢像 Prometheus、Loki 這些資料來源，再把結果呈現出來


```bash
                    你的系統
                       │
             ┌─────────┴─────────┐
             │                   │
          Metrics               Logs
             │                   │
             ▼                   ▼
       Prometheus           Log Collector
       收集 + 儲存          Alloy / Fluent Bit
             │                   │
             │                   ▼
             │                 Loki
             │              儲存 + 查詢
             │                   │
             └────────┬──────────┘
                      │
                      ▼
                   Grafana
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Dashboard     Explore      Alert
```

例如你想看 Pod Memory

Prometheus 裡已經有：

08:00 → 1.2 GB
08:01 → 1.4 GB
08:02 → 1.7 GB
08:03 → 1.9 GB

你可以在 Grafana 建立一個 Panel，讓 Grafana 對 Prometheus 執行 PromQL：

container_memory_working_set_bytes{
    pod="promotion-worker"
}

Grafana 拿到結果之後畫成：

Memory
2.0GB │                   ╭─
      │                ╭──╯
1.5GB │         ╭──────╯
      │    ╭────╯
1.0GB │────╯
      └─────────────────────
       08:00  08:01  08:02

所以這張漂亮的圖是 Grafana 畫的，底下的資料是 Prometheus 提供的。


同樣地，你想看 Error Log。

你在 Grafana Explore 寫：

{service="promotion-worker"} |= "ERROR"

這次 Grafana 知道你選的 Data Source 是 Loki，因此：

Grafana
   │
   │ LogQL
   ▼
 Loki
   │
   │ 查詢結果
   ▼
Grafana

08:31 ERROR DynamoDB timeout
08:35 ERROR OutOfMemoryException

所以你之前在 Grafana 裡面寫的 LogQL，本質上可以理解成：

你透過 Grafana 這個 UI，對 Loki 下查詢。


Grafana 還有一個重要功能：Alert

例如你設定：

過去 5 分鐘
Dify Error > 5

Grafana 定期執行查詢：

Grafana
   │
   ▼
Loki
   │
   ▼
過去 5 分鐘 Dify Error = 8
   │
   ▼
超過門檻 5
   │
   ▼
Alerting
   │
   ▼
Slack / Email / ...

這就是你之前研究的 Grafana Alert。

所以可以把 Grafana 的核心功能濃縮成：

Grafana = 把不同監控資料來源接進來，讓人查詢、視覺化、做 Dashboard 與 Alert 的平台。



<!-- endtab -->



{% endtabs %}
