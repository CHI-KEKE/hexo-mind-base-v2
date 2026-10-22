---
title: 監控基礎架構
date: 2026-09-22 08:29:00
categories: Metric
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/grafana.png
cover : https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/grafana.png
tags:
    - 
toc:
toc_number:
comments :
---

{% tabs grafana-1 %}

<!-- tab 架構-->


<style>
.grafana-dusk{--gd-bg:#1b1925;--gd-panel:#252030;--gd-code:#111217;--gd-ink:#cbc8d5;--gd-title:#eeeaf4;--gd-muted:#aaa5b8;--gd-line:#554a62;--gd-link:#91b7ff;background:var(--gd-bg);color:var(--gd-ink);padding:28px;font:16px/1.8 'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif;overflow-wrap:anywhere;color-scheme:dark;}
.grafana-dusk *{box-sizing:border-box;}
#article-container .grafana-dusk h2,#article-container .grafana-dusk h3,.grafana-dusk h2,.grafana-dusk h3{color:var(--gd-title);font-weight:500;line-height:1.4;margin:0 0 16px;}
.grafana-dusk p{margin:12px 0;}
.grafana-dusk a{color:var(--gd-link);text-decoration:underline;text-underline-offset:3px;}
.grafana-dusk :focus-visible{outline:3px solid var(--gd-link);outline-offset:4px;}
#article-container .grafana-dusk code,.grafana-dusk code{background:#342c42;color:#eeeaf4;padding:2px 5px;border-radius:3px;font-family:Consolas,monospace;}
.grafana-dusk .gd-hero{padding:40px 28px;margin-bottom:30px;text-align:center;border-radius:4px;background:linear-gradient(155deg,#713d70 0%,#39234d 48%,#110d23 100%);}
.grafana-dusk .gd-brand-line{display:block;width:64px;height:5px;margin:0 auto 24px;border-radius:2px;background:linear-gradient(90deg,#f45125,#ff8c16,#ffc619);}
.grafana-dusk .gd-hero h2{font-size:clamp(1.8rem,4vw,2.25rem);}
.grafana-dusk .gd-hero p{max-width:38em;margin:16px auto 0;color:var(--gd-title);}
.grafana-dusk .gd-section{padding-left:14px;border-left:3px solid #ff8c16;margin-top:30px;}
.grafana-dusk .gd-panel{background:linear-gradient(180deg,var(--gd-panel),var(--gd-bg));border:1px solid var(--gd-line);border-radius:4px;padding:22px;margin:22px 0;}
.grafana-dusk .gd-note{background:var(--gd-panel);border-left:3px solid var(--gd-link);padding:16px 20px;margin:22px 0;border-radius:3px;}
.grafana-dusk .gd-table-scroll{max-width:100%;overflow-x:auto;margin:22px 0;}
#article-container .grafana-dusk table.gd-table,.grafana-dusk table.gd-table{width:100%;margin:0;border-collapse:collapse;table-layout:auto;background:var(--gd-bg);color:var(--gd-ink);}
.grafana-dusk .gd-table th,.grafana-dusk .gd-table td{padding:12px 16px;border:1px solid var(--gd-line);text-align:left;vertical-align:top;background:var(--gd-bg);color:var(--gd-ink);}
.grafana-dusk .gd-table th{background:var(--gd-panel);color:var(--gd-title);font-weight:600;}
.grafana-dusk .gd-code{background:var(--gd-code);color:var(--gd-ink);border:1px solid var(--gd-line);border-radius:3px;overflow:hidden;margin:22px 0;}
.grafana-dusk .gd-code-label{padding:8px 16px;color:var(--gd-muted);border-bottom:1px solid var(--gd-line);font-size:13px;}
#article-container .grafana-dusk pre.gd-pre,.grafana-dusk pre.gd-pre{background:var(--gd-code)!important;color:var(--gd-ink)!important;margin:0!important;padding:18px!important;border:0!important;border-radius:0!important;box-shadow:none!important;text-shadow:none!important;white-space:pre!important;overflow-x:auto!important;font:14px/1.8 Consolas,monospace!important;}
@media(max-width:600px){.grafana-dusk{padding:16px;}.grafana-dusk .gd-hero{padding:28px 16px;}.grafana-dusk .gd-panel,.grafana-dusk .gd-note{padding:16px;}.grafana-dusk .gd-table th,.grafana-dusk .gd-table td{padding:10px;min-width:8em;}}

#article-container .grafana-dusk h3.gd-section{margin:36px 0 20px;font-size:1.3rem;}
#article-container .grafana-dusk .gd-table th,#article-container .grafana-dusk .gd-table td{background:var(--gd-bg);color:var(--gd-ink);}
#article-container .grafana-dusk .gd-table th{background:var(--gd-panel);color:var(--gd-title);}
.grafana-dusk .gd-diagram,.grafana-dusk .gd-plot{background:var(--gd-bg);border:1px solid var(--gd-line);border-radius:4px;padding:22px 12px;margin:24px 0;overflow:auto;}
#article-container .grafana-dusk .mermaid-wrap{background:var(--gd-bg);padding:0;margin:0;border:0;}
#article-container .grafana-dusk .mermaid-wrap svg{display:block;height:auto;max-height:none;margin:auto;}
#article-container .grafana-dusk img.gd-sequence{display:block;width:100%;height:auto;margin:0;max-width:100%;}
.grafana-dusk .gd-plot svg{display:block;max-width:none;margin:auto;}
.grafana-dusk .gd-table{min-width:470px;}
#article-container .grafana-dusk .gd-table td:first-child,#article-container .grafana-dusk .gd-table th:first-child{min-width:7em;overflow-wrap:normal;word-break:normal;}
#article-container .grafana-dusk ul{padding-left:24px;}
#article-container .grafana-dusk li{margin:8px 0;}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs{background:#252030;}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs>.tab{color:#cbc8d5;background:#252030;}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs>.tab.active{color:#eeeaf4;background:#30283e;border-top-color:#3d73d9;}
@media(max-width:600px){.grafana-dusk .gd-diagram,.grafana-dusk .gd-plot{padding:16px 6px;}}
</style>
<section class="grafana-dusk">

<h3 class="gd-section">收到 API Error Rate > 5% 通知之後</h3>
<div class="gd-table-scroll" role="region" aria-label="調查方向資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">調查方向</th><th scope="col">具體問題</th><th scope="col">資料來源</th></tr></thead><tbody><tr><td>觀察趨勢</td><td>目前錯誤多不多？從什麼時候開始？哪一台 Pod 特別嚴重？</td><td>Prometheus 的 Metrics</td></tr><tr><td>追查細節</td><td>到底報什麼錯？哪個 endpoint？Exception 是什麼？Request ID 是多少？</td><td>Loki 的 Logs</td></tr></tbody></table></div>
<p>Grafana 將這兩條調查路線接在同一個介面。能否依服務、Pod 或 Request ID 對照，仍取決於實際收集的指標 Labels、Log 欄位及資料來源設定。</p>
<h3 class="gd-section">監控系統分工：兩條資料路徑</h3>
<div class="gd-diagram" role="region" aria-label="監控系統分工：兩條資料路徑" tabindex="0"><div class="gd-diagram-inner" style="min-width:530px"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;background&quot;: &quot;#1b1925&quot;, &quot;primaryColor&quot;: &quot;#30283e&quot;, &quot;primaryTextColor&quot;: &quot;#eeeaf4&quot;, &quot;primaryBorderColor&quot;: &quot;#91829f&quot;, &quot;lineColor&quot;: &quot;#b8aec8&quot;, &quot;secondaryColor&quot;: &quot;#252030&quot;, &quot;tertiaryColor&quot;: &quot;#252030&quot;, &quot;clusterBkg&quot;: &quot;#211c2b&quot;, &quot;clusterBorder&quot;: &quot;#756583&quot;, &quot;edgeLabelBackground&quot;: &quot;#1b1925&quot;, &quot;textColor&quot;: &quot;#eeeaf4&quot;, &quot;fontSize&quot;: &quot;16px&quot;, &quot;fontFamily&quot;: &quot;Segoe UI, Microsoft JhengHei, sans-serif&quot;, &quot;actorBkg&quot;: &quot;#30283e&quot;, &quot;actorBorder&quot;: &quot;#91829f&quot;, &quot;actorTextColor&quot;: &quot;#eeeaf4&quot;, &quot;actorLineColor&quot;: &quot;#91829f&quot;, &quot;signalColor&quot;: &quot;#cbc8d5&quot;, &quot;signalTextColor&quot;: &quot;#eeeaf4&quot;, &quot;labelBoxBkgColor&quot;: &quot;#252030&quot;, &quot;labelBoxBorderColor&quot;: &quot;#91829f&quot;, &quot;labelTextColor&quot;: &quot;#eeeaf4&quot;, &quot;loopTextColor&quot;: &quot;#eeeaf4&quot;, &quot;noteBkgColor&quot;: &quot;#30283e&quot;, &quot;noteBorderColor&quot;: &quot;#91829f&quot;, &quot;noteTextColor&quot;: &quot;#eeeaf4&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true, &quot;curve&quot;: &quot;linear&quot;, &quot;nodeSpacing&quot;: 28, &quot;rankSpacing&quot;: 45}, &quot;sequence&quot;: {&quot;useMaxWidth&quot;: true, &quot;mirrorActors&quot;: false, &quot;actorMargin&quot;: 45, &quot;messageMargin&quot;: 35}}" hidden>flowchart TB
subgraph Source[&quot;應用與基礎設施&quot;]
System[&quot;Pod / API / Worker / DB&quot;]
end
subgraph Storage[&quot;收集與儲存&quot;]
Endpoint[&quot;Metrics endpoint / Exporter&quot;]
Collector[&quot;Log Collector&quot;]
Prom[&quot;Prometheus：指標&quot;]
Loki[&quot;Loki：Log&quot;]
Endpoint --&gt;|指標樣本| Prom
Collector --&gt;|Push Logs| Loki
end
subgraph View[&quot;查詢與呈現&quot;]
Grafana[&quot;Grafana&quot;]
Uses[&quot;Dashboard、Explore、Alerting&quot;]
Grafana --&gt;|呈現與評估| Uses
end
System --&gt;|CPU、Memory、Request 數| Endpoint
System --&gt;|Error、Exception、訊息| Collector
Prom --&gt;|查詢結果| Grafana
Loki --&gt;|查詢結果| Grafana</pre></div></div></div>

<div class="gd-table-scroll" role="region" aria-label="資料種類資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">資料種類</th><th scope="col">示例</th><th scope="col">主要用途</th></tr></thead><tbody><tr><td>Metrics</td><td>CPU = 80%；Memory = 1.8 GB；Error count = 12</td><td>比較用量、數量與變化趨勢</td></tr><tr><td>Logs</td><td><code>Start processing job</code>、<code>DynamoDB timeout</code>、<code>OutOfMemoryException</code></td><td>保存事件訊息與錯誤細節</td></tr></tbody></table></div>
</section>
<!-- endtab -->
<!-- tab metric-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>讓數字帶上觀測上下文</h2><p>同樣是 100，單獨看只能知道數量。加上指標名稱、分類與觀測時間後，才知道哪個服務發生了什麼變化。</p></div>
<h3 class="gd-section">Metric 與一般數值</h3>
<p><code>metric</code> 是單數，例如「CPU 使用率這個 metric」；<code>metrics</code> 是複數，也常泛指監控指標資料。Metric 是量化系統狀態或行為的指標，觀測時會連同對象、時間與分類資訊一起解讀。</p>
<p>核心仍是數字，例如 <code>80</code>、<code>512</code>、<code>1000</code>、<code>0.52</code>。有了上下文，才可以回答「誰、什麼時候、屬於哪一類，以及如何變化」。一般變數也能保存數值，但是否成為可持續查詢的監控資料，取決於後續的量測、暴露與收集流程。</p>
<div class="gd-code"><div class="gd-code-label">程式內的一般變數</div><pre class="gd-pre">request_count = 100</pre></div>
<p>程式結束後，這個變數可能跟著消失。若要監控 <code>order-api</code> 收到多少 Request，可以透過指標暴露累計數量。</p>
<div class="gd-code"><div class="gd-code-label">帶有名稱的指標樣本</div><pre class="gd-pre">http_requests_total 100</pre></div>
<h3 class="gd-section">Labels 是可組合的分類維度</h3>
<p>系統可能同時提供 <code>GET /users</code>、<code>POST /orders</code>、<code>GET /products</code>。加入 Labels 後，同一個指標名稱可以描述不同請求類別。</p>
<div class="gd-code"><div class="gd-code-label">指標名稱、Labels 與樣本值</div><pre class="gd-pre">http_requests_total{method=&quot;POST&quot;, path=&quot;/orders&quot;, status=&quot;200&quot;} 100</pre></div>
<div class="gd-table-scroll" role="region" aria-label="組成資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">組成</th><th scope="col">範例</th><th scope="col">意義</th></tr></thead><tbody><tr><td>指標名稱</td><td><code>http_requests_total</code></td><td>記錄 HTTP 請求累計數</td></tr><tr><td>Labels</td><td><code>method="POST"</code>、<code>path="/orders"</code>、<code>status="200"</code></td><td>共同識別同一組分類</td></tr><tr><td>樣本值</td><td><code>100</code></td><td>該組分類在觀測時的累計值</td></tr></tbody></table></div>
<p>指標名稱與完整 Label 集合共同識別一條時間序列。Prometheus 保存該序列的時間戳記與樣本值。參考 <a href="https://prometheus.io/docs/concepts/">Prometheus 資料模型</a>。</p>
<div class="gd-code"><div class="gd-code-label">另一組分類的樣本</div><pre class="gd-pre">http_requests_total{method=&quot;GET&quot;, status=&quot;200&quot;, pod=&quot;api-01&quot;} 5000</pre></div>
<div class="gd-table-scroll" role="region" aria-label="分類維度資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">分類維度</th><th scope="col">可觀察的值</th><th scope="col">關係</th></tr></thead><tbody><tr><td>Method</td><td><code>GET</code>、<code>POST</code></td><td>依請求方法篩選</td></tr><tr><td>Status</td><td><code>200</code>、<code>404</code>、<code>500</code></td><td>依回應狀態篩選</td></tr><tr><td>Pod</td><td><code>api-01</code>、<code>api-02</code></td><td>依執行實例篩選</td></tr></tbody></table></div>
<div class="gd-note"><p>Method、Status 與 Pod 是不同維度，可以同時套用條件。例如查詢 <code>api-01</code> 中狀態為 <code>200</code> 的 <code>GET</code> 請求。它們不是互斥的樹狀分支。</p></div>
<h3 class="gd-section">同一條時間序列，持續累積樣本</h3>
<p>以 <code>method="POST", path="/orders", status="200"</code> 這組 Labels 為例，Prometheus 定期取得下列樣本。</p>
<div class="gd-table-scroll" role="region" aria-label="時間資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">時間</th><th scope="col">http_requests_total</th></tr></thead><tbody><tr><td>08:00</td><td>100</td></tr><tr><td>08:01</td><td>150</td></tr><tr><td>08:02</td><td>230</td></tr><tr><td>08:03</td><td>310</td></tr></tbody></table></div>
<div class="gd-plot" role="img" aria-label="時間序列：08:00 為 100，08:01 為 150，08:02 為 230，08:03 為 310"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 320" width="640" height="320"><g fill="none" stroke="#554a62"><path d="M70 45V265H595"/><path d="M70 202H595M70 139H595M70 76H595"/></g><g fill="#cbc8d5" font-size="16" font-family="Segoe UI, sans-serif"><text x="20" y="270">0</text><text x="20" y="207">100</text><text x="20" y="144">200</text><text x="20" y="81">300</text><text x="70" y="25">http_requests_total</text><text x="73" y="300">08:00</text><text x="223" y="300">08:01</text><text x="373" y="300">08:02</text><text x="523" y="300">08:03</text></g><path d="M95 202L245 170.5L395 120.2L545 69.9" fill="none" stroke="#91b7ff" stroke-width="3"/><g fill="#ffc619"><circle cx="95" cy="202" r="5"/><circle cx="245" cy="170.5" r="5"/><circle cx="395" cy="120.2" r="5"/><circle cx="545" cy="69.9" r="5"/></g><g fill="#eeeaf4" font-size="16" text-anchor="middle"><text x="95" y="185">100</text><text x="245" y="153">150</text><text x="395" y="103">230</text><text x="545" y="53">310</text></g></svg></div>
<p>橫軸是時間，縱軸是請求累計數；折線只連接示例樣本，不代表已知兩次抓取之間的每一筆請求。</p>
<ul><li>最近增加多快？</li><li>最近 5 分鐘有多少 Request？</li><li>今天與昨天差多少？</li><li>哪個 Pod 的 Request 最多？</li><li><code>500</code> Error 的比例是多少？</li></ul>
<h3 class="gd-section">原始量測與衍生指標</h3>
<p>Pod 記憶體可以直接以 <code>container_memory_working_set_bytes</code> 表示。這接近原始量測（raw measurement）的用途，但 working set 本身仍是監控元件依底層資訊定義的量測值。</p>
<div class="gd-code"><div class="gd-code-label">記憶體樣本：1,572,864,000 bytes</div><pre class="gd-pre">container_memory_working_set_bytes 1572864000</pre></div>
<div class="gd-table-scroll" role="region" aria-label="時間資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">時間</th><th scope="col">Memory 顯示示例</th></tr></thead><tbody><tr><td>08:00</td><td>1.2 GB</td></tr><tr><td>08:01</td><td>1.3 GB</td></tr><tr><td>08:02</td><td>1.5 GB</td></tr></tbody></table></div>
<p>上述時間表是一組獨立的顯示示例，不是把同一筆 <code>1,572,864,000 bytes</code> 重複換算。資料從真實系統的量測產生 Metric，再經計算或聚合形成衍生指標或查詢結果，最後由 Grafana 顯示。</p>
<h3 class="gd-section">記憶體換算：bytes、GiB 與使用率</h3>
<div class="gd-diagram" role="region" aria-label="記憶體換算：bytes、GiB 與使用率" tabindex="0"><div class="gd-diagram-inner" style="min-width:510px"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;background&quot;: &quot;#1b1925&quot;, &quot;primaryColor&quot;: &quot;#30283e&quot;, &quot;primaryTextColor&quot;: &quot;#eeeaf4&quot;, &quot;primaryBorderColor&quot;: &quot;#91829f&quot;, &quot;lineColor&quot;: &quot;#b8aec8&quot;, &quot;secondaryColor&quot;: &quot;#252030&quot;, &quot;tertiaryColor&quot;: &quot;#252030&quot;, &quot;clusterBkg&quot;: &quot;#211c2b&quot;, &quot;clusterBorder&quot;: &quot;#756583&quot;, &quot;edgeLabelBackground&quot;: &quot;#1b1925&quot;, &quot;textColor&quot;: &quot;#eeeaf4&quot;, &quot;fontSize&quot;: &quot;16px&quot;, &quot;fontFamily&quot;: &quot;Segoe UI, Microsoft JhengHei, sans-serif&quot;, &quot;actorBkg&quot;: &quot;#30283e&quot;, &quot;actorBorder&quot;: &quot;#91829f&quot;, &quot;actorTextColor&quot;: &quot;#eeeaf4&quot;, &quot;actorLineColor&quot;: &quot;#91829f&quot;, &quot;signalColor&quot;: &quot;#cbc8d5&quot;, &quot;signalTextColor&quot;: &quot;#eeeaf4&quot;, &quot;labelBoxBkgColor&quot;: &quot;#252030&quot;, &quot;labelBoxBorderColor&quot;: &quot;#91829f&quot;, &quot;labelTextColor&quot;: &quot;#eeeaf4&quot;, &quot;loopTextColor&quot;: &quot;#eeeaf4&quot;, &quot;noteBkgColor&quot;: &quot;#30283e&quot;, &quot;noteBorderColor&quot;: &quot;#91829f&quot;, &quot;noteTextColor&quot;: &quot;#eeeaf4&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true, &quot;curve&quot;: &quot;linear&quot;, &quot;nodeSpacing&quot;: 28, &quot;rankSpacing&quot;: 45}, &quot;sequence&quot;: {&quot;useMaxWidth&quot;: true, &quot;mirrorActors&quot;: false, &quot;actorMargin&quot;: 45, &quot;messageMargin&quot;: 35}}" hidden>flowchart TB
Raw[&quot;Container 量測：1,800,000,000 bytes&quot;] --&gt;|原始 bytes| Convert[&quot;除以 1024 的三次方&quot;]
Convert --&gt;|約 1.6764 GiB| Display[&quot;顯示值：1.68 GiB&quot;]
Display --&gt;|除以 Limit，再乘以 100| Ratio[&quot;顯示值算例：84%&quot;]
Limit[&quot;Memory Limit：2 GiB&quot;] --&gt;|提供分母| Ratio</pre></div></div></div>
<p>由上往下讀，箭頭表示數值轉換與計算輸入。以顯示值計算，1.68 ÷ 2 × 100 = 84%；使用未四捨五入的原始 bytes 計算則約為 83.82%。1.68 GiB 與 84% 都能作為觀察指標。</p>
<div class="gd-note"><p><code>GB</code> 與 <code>GiB</code> 不同：1 GB = 10⁹ bytes，1 GiB = 1024³ bytes。原稿的 GB 顯示例與這裡的 GiB 換算例分開使用。Memory Used 以此處的 working set 為例，實務上仍須確認儀表板採用的記憶體定義。</p></div>
<h3 class="gd-section">Counter 經 rate() 轉成每秒速率</h3>
<div class="gd-table-scroll" role="region" aria-label="時間資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">時間</th><th scope="col">http_requests_total 累計值</th><th scope="col">rate() 結果示意</th></tr></thead><tbody><tr><td>08:00</td><td>10000</td><td>8 req/s</td></tr><tr><td>08:01</td><td>10600</td><td>10 req/s</td></tr><tr><td>08:02</td><td>11500</td><td>13 req/s</td></tr></tbody></table></div>
<div class="gd-code"><div class="gd-code-label">查詢最近 5 分鐘的平均每秒增長率</div><pre class="gd-pre">rate(http_requests_total[5m])</pre></div>
<p><code>http_requests_total</code> 是累加型 Counter，<code>rate()</code> 將時間窗內的樣本轉成平均每秒速率，並處理 Counter reset。右欄的 <code>8</code>、<code>10</code>、<code>13 req/s</code> 保留作為輸出形式示意；單靠左欄三筆資料，無法計算完整 5 分鐘視窗的這些結果。參考 <a href="https://prometheus.io/docs/prometheus/latest/querying/functions/#rate">Prometheus rate() 定義</a>。</p>
</section>
<!-- endtab -->
<!-- tab Prometheus-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>分清楚量測與抓取的責任</h2><p>底層元件先取得系統資訊並暴露指標，Prometheus 再定期抓取、保存與查詢。知道數字從哪裡來，才能判斷儀表板正在觀察什麼。</p></div>
<h3 class="gd-section">Prometheus 的起源與角色</h3>
<p>Prometheus 是用於收集、保存與查詢系統 Metrics 的開源監控系統。Matt T. Proud 與 Julius Volz 在 2012 年於 SoundCloud 啟動專案；2016 年加入 CNCF，成為 Kubernetes 之後第二個託管專案，2018 年畢業。參考 <a href="https://prometheus.io/community/">Prometheus 專案發起者</a>與 <a href="https://www.cncf.io/announcements/2018/08/09/prometheus-graduates/">CNCF 畢業公告</a>。</p>
<h3 class="gd-section">記憶體指標：量測、暴露與抓取</h3>
<div class="gd-diagram" role="region" aria-label="記憶體指標：量測、暴露與抓取" tabindex="0"><div class="gd-diagram-inner" style="min-width:340px"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;background&quot;: &quot;#1b1925&quot;, &quot;primaryColor&quot;: &quot;#30283e&quot;, &quot;primaryTextColor&quot;: &quot;#eeeaf4&quot;, &quot;primaryBorderColor&quot;: &quot;#91829f&quot;, &quot;lineColor&quot;: &quot;#b8aec8&quot;, &quot;secondaryColor&quot;: &quot;#252030&quot;, &quot;tertiaryColor&quot;: &quot;#252030&quot;, &quot;clusterBkg&quot;: &quot;#211c2b&quot;, &quot;clusterBorder&quot;: &quot;#756583&quot;, &quot;edgeLabelBackground&quot;: &quot;#1b1925&quot;, &quot;textColor&quot;: &quot;#eeeaf4&quot;, &quot;fontSize&quot;: &quot;16px&quot;, &quot;fontFamily&quot;: &quot;Segoe UI, Microsoft JhengHei, sans-serif&quot;, &quot;actorBkg&quot;: &quot;#30283e&quot;, &quot;actorBorder&quot;: &quot;#91829f&quot;, &quot;actorTextColor&quot;: &quot;#eeeaf4&quot;, &quot;actorLineColor&quot;: &quot;#91829f&quot;, &quot;signalColor&quot;: &quot;#cbc8d5&quot;, &quot;signalTextColor&quot;: &quot;#eeeaf4&quot;, &quot;labelBoxBkgColor&quot;: &quot;#252030&quot;, &quot;labelBoxBorderColor&quot;: &quot;#91829f&quot;, &quot;labelTextColor&quot;: &quot;#eeeaf4&quot;, &quot;loopTextColor&quot;: &quot;#eeeaf4&quot;, &quot;noteBkgColor&quot;: &quot;#30283e&quot;, &quot;noteBorderColor&quot;: &quot;#91829f&quot;, &quot;noteTextColor&quot;: &quot;#eeeaf4&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true, &quot;curve&quot;: &quot;linear&quot;, &quot;nodeSpacing&quot;: 28, &quot;rankSpacing&quot;: 45}, &quot;sequence&quot;: {&quot;useMaxWidth&quot;: true, &quot;mirrorActors&quot;: false, &quot;actorMargin&quot;: 45, &quot;messageMargin&quot;: 35}}" hidden>flowchart TB
subgraph Measured[&quot;量測與暴露端&quot;]
Container[&quot;Pod / Container&quot;] --&gt;|使用資源| Kernel[&quot;Linux Kernel / cgroup&quot;]
Kernel --&gt;|提供原始資訊| Monitor[&quot;監控元件&quot;]
Monitor --&gt;|暴露 Metric| Endpoint[&quot;Metrics endpoint&quot;]
end
subgraph Prom[&quot;Prometheus&quot;]
Scraper[&quot;Scrape：定期抓取&quot;] --&gt;|保存樣本| Store[&quot;儲存 / PromQL 查詢&quot;]
end
Scraper --&gt;|HTTP scrape 請求| Endpoint
Endpoint -.-&gt;|指標樣本回應| Scraper
Grafana[&quot;Grafana&quot;] --&gt;|PromQL 查詢| Store
Store -.-&gt;|查詢結果| Grafana</pre></div></div></div>
<p>上方是量測與暴露流程；跨邊界的實線表示請求，虛線表示回應。Prometheus 通常不會進入應用程式 Pod 自行檢查 RAM，實際量測由 OS、Kubernetes 相關元件、應用程式或 Exporter 提供。此圖以 Container 記憶體為例，省略監控元件的具體部署方式。</p>
<p>例如監控元件提供 <code>container_memory_working_set_bytes</code>，樣本值為 <code>1800000000</code>，也就是十進位的 <code>1.8 GB</code>。暴露格式應使用 bytes 數值，不直接在樣本後面寫 <code>1.8GB</code>。</p>
<h3 class="gd-section">Scrape 是定期取得最新樣本</h3>
<p>假設抓取週期設為每 15 秒，Prometheus 取得的數字可能如下。這是範例設定，不代表所有部署都使用相同週期。</p>
<div class="gd-table-scroll" role="region" aria-label="時間資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">時間</th><th scope="col">Memory</th></tr></thead><tbody><tr><td>08:00:00</td><td>1.20 GiB</td></tr><tr><td>08:00:15</td><td>1.25 GiB</td></tr><tr><td>08:00:30</td><td>1.31 GiB</td></tr><tr><td>08:00:45</td><td>1.42 GiB</td></tr></tbody></table></div>
<div class="gd-table-scroll" role="region" aria-label="元件資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">元件</th><th scope="col">以 10 個 API Pod 為例</th></tr></thead><tbody><tr><td>Kubernetes</td><td>讓期望的 10 個 API Pod 執行，處理排程與生命週期。</td></tr><tr><td>Prometheus</td><td>收集 CPU、Memory、Request Rate、Error Rate、Latency 等指標，觀察這 10 個 Pod 的狀態。</td></tr></tbody></table></div>
<h3 class="gd-section">四種主要 Metric 型別</h3>
<div class="gd-table-scroll" role="region" aria-label="型別資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">型別</th><th scope="col">觀察方式</th><th scope="col">範例與限制</th></tr></thead><tbody><tr><td>Counter</td><td>持續累加，重啟等情況可能重設</td><td>Request 總數、Error 總數；通常搭配 <code>rate()</code> 或 <code>increase()</code>。</td></tr><tr><td>Gauge</td><td>可以增加，也可以減少</td><td>Memory、在線人數、已計算的 CPU 使用率；CPU 累計使用秒數則通常是 Counter。</td></tr><tr><td>Histogram</td><td>觀察大量事件的分布</td><td>例如 Request 耗時。Classic Histogram 使用累積 bucket，查詢端可計算 quantile。</td></tr><tr><td>Summary</td><td>記錄觀測總數、總和，並可輸出用戶端計算的 quantile</td><td>例如 Request 耗時；不同實例的 quantile 不能直接相加或平均成整體 quantile。</td></tr></tbody></table></div>
<div class="gd-note"><p>「0–100 ms 有幾次、100–500 ms 有幾次」是在問區間分布。Classic Histogram 的 <code>le="0.1"</code> 表示不超過 100 ms 的累計次數，<code>le="0.5"</code> 表示不超過 500 ms；兩者相減才能得到大於 100 ms、且不超過 500 ms 的次數。</p></div>
<p>Histogram 與 Summary 都能描述分布，選擇時還要考慮跨實例聚合、精度與用戶端支援。這裡以 Classic Histogram 說明 bucket；Prometheus 另支援 Native Histogram。參考 <a href="https://prometheus.io/docs/concepts/metric_types/">Metric 型別</a>與 <a href="https://prometheus.io/docs/practices/histograms/">Histograms and summaries</a>。</p>
</section>
<!-- endtab -->
<!-- tab Loki-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>把分散的事件紀錄集中保存</h2><p>結帳在 10:32 失敗，處理請求的 Pod 卻不一定還在原處。集中保存 Log，才能跨實例查找當時留下的線索。</p></div>
<h3 class="gd-section">Loki 的起源與用途</h3>
<p>Loki 是集中儲存、搜尋與分析 Logs 的系統。Grafana Labs 在 2018 年啟動專案，Tom Wilkie 與 David Kaltschmidt 的早期設計文件推動了它的誕生，同年底在 KubeCon Seattle 公開。官方以「Like Prometheus, but for logs.」描述其方向。參考 <a href="https://grafana.com/events/grafanacon/2020/loki-future/">Loki 早期設計回顧</a>與 <a href="https://grafana.com/blog/open-source-log-monitoring-the-concise-guide-to-grafana-loki/">Loki 五週年介紹</a>。</p>
<p>假設 Order API 分散在 Pod A、Pod B、Pod C、Pod D、Pod E。得知「剛剛 10:32 結帳失敗」時，首先要找出是哪個 Pod 處理，以及該實例的錯誤紀錄。</p>
<div class="gd-note"><p>Crash 後可能發生 Container Restart，也可能因 Pod 被刪除或替換而讓舊 Pod 消失；Container 重啟不等於 Pod 一定被替換。只依賴本機 Log 會受到輪替、節點與 Pod 生命週期影響，因此需要將紀錄送到集中儲存。</p></div>
<h3 class="gd-section">Log 寫入路徑：從程式到 Loki</h3>
<div class="gd-diagram" role="region" aria-label="Log 寫入路徑：從程式到 Loki" tabindex="0"><div class="gd-diagram-inner" style="min-width:350px"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;background&quot;: &quot;#1b1925&quot;, &quot;primaryColor&quot;: &quot;#30283e&quot;, &quot;primaryTextColor&quot;: &quot;#eeeaf4&quot;, &quot;primaryBorderColor&quot;: &quot;#91829f&quot;, &quot;lineColor&quot;: &quot;#b8aec8&quot;, &quot;secondaryColor&quot;: &quot;#252030&quot;, &quot;tertiaryColor&quot;: &quot;#252030&quot;, &quot;clusterBkg&quot;: &quot;#211c2b&quot;, &quot;clusterBorder&quot;: &quot;#756583&quot;, &quot;edgeLabelBackground&quot;: &quot;#1b1925&quot;, &quot;textColor&quot;: &quot;#eeeaf4&quot;, &quot;fontSize&quot;: &quot;16px&quot;, &quot;fontFamily&quot;: &quot;Segoe UI, Microsoft JhengHei, sans-serif&quot;, &quot;actorBkg&quot;: &quot;#30283e&quot;, &quot;actorBorder&quot;: &quot;#91829f&quot;, &quot;actorTextColor&quot;: &quot;#eeeaf4&quot;, &quot;actorLineColor&quot;: &quot;#91829f&quot;, &quot;signalColor&quot;: &quot;#cbc8d5&quot;, &quot;signalTextColor&quot;: &quot;#eeeaf4&quot;, &quot;labelBoxBkgColor&quot;: &quot;#252030&quot;, &quot;labelBoxBorderColor&quot;: &quot;#91829f&quot;, &quot;labelTextColor&quot;: &quot;#eeeaf4&quot;, &quot;loopTextColor&quot;: &quot;#eeeaf4&quot;, &quot;noteBkgColor&quot;: &quot;#30283e&quot;, &quot;noteBorderColor&quot;: &quot;#91829f&quot;, &quot;noteTextColor&quot;: &quot;#eeeaf4&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true, &quot;curve&quot;: &quot;linear&quot;, &quot;nodeSpacing&quot;: 28, &quot;rankSpacing&quot;: 45}, &quot;sequence&quot;: {&quot;useMaxWidth&quot;: true, &quot;mirrorActors&quot;: false, &quot;actorMargin&quot;: 45, &quot;messageMargin&quot;: 35}}" hidden>flowchart TB
subgraph Node[&quot;Kubernetes Node&quot;]
subgraph Pod[&quot;Pod / Container&quot;]
App[&quot;C# Application&quot;] --&gt;|ILogger| Provider[&quot;Logging Provider&quot;]
Provider --&gt;|Console 輸出| Std[&quot;stdout / stderr&quot;]
end
Std --&gt;|交由 Runtime 處理| Runtime[&quot;Container Runtime&quot;]
Runtime --&gt;|寫入紀錄| Files[&quot;Node 上的 Container Logs&quot;]
Files --&gt;|讀取| Collector[&quot;Log Collector&quot;]
Collector --&gt;|附加 metadata / labels| Enriched[&quot;Log 與時間戳記、Labels&quot;]
end
subgraph Central[&quot;集中服務&quot;]
Loki[&quot;Loki API：接收並保存&quot;]
end
Enriched --&gt;|HTTP Push Logs| Loki</pre></div></div></div>
<p>由上往下讀，箭頭表示紀錄的傳遞與處理。圖中以 Node 層級 Collector 讀取 Container Log 為例；Collector 也可能採其他部署或讀取方式。Pod A 至 Pod E 的紀錄都可經相應收集路徑集中送往 Loki，並非每個 Pod 必須各部署一個 Collector。</p>
<h3 class="gd-section">1. C# 程式產生 Log</h3>
<div class="gd-code"><div class="gd-code-label">Worker 的紀錄呼叫</div><pre class="gd-pre">_logger.LogInformation(&quot;Start processing ShopId {ShopId}&quot;, shopId);
_logger.LogError(
    exception,
    &quot;Failed to process promotion {PromotionId}&quot;,
    promotionId);</pre></div>
<p>假設 <code>shopId = 2</code>、<code>promotionId = 574730</code>，設定好的 Logging Provider 可能輸出以下文字。日期、等級與格式由 Provider／Formatter 設定決定。</p>
<div class="gd-code"><div class="gd-code-label">Log 輸出示例</div><pre class="gd-pre">08:30:01 INFO  Start processing ShopId 2
08:30:02 INFO  Loading promotions
08:30:05 ERROR Failed to process promotion 574730
08:30:05 ERROR System.TimeoutException...</pre></div>
<p>在 ASP.NET Core 中，同一個 <code>_logger.LogInformation()</code> 呼叫若搭配帶日期的 Console 格式，可能產生 <code>2026-09-22 08:30:01 INFO Start processing ShopId 2</code>。<code>ILogger</code> 只把紀錄交給設定好的 Provider；執行到這裡不代表 Loki 已收到資料。</p>
<h3 class="gd-section">2. Container Runtime 將標準輸出保存為 Node Log</h3>
<p>Container／Kubernetes 的常見配置讓程式寫入 <code>stdout</code> 或 <code>stderr</code>。Container Runtime 處理這些輸出，在 Node 上留下對應 Log，Kubernetes 可透過下列指令讀取。</p>
<div class="gd-code"><div class="gd-code-label">讀取 Pod 的 Container Log</div><pre class="gd-pre">kubectl logs promotion-worker-abc</pre></div>
<div class="gd-code"><div class="gd-code-label">kubectl logs 輸出示例</div><pre class="gd-pre">INFO Start processing ShopId 2
INFO Loading promotions
ERROR DynamoDB timeout</pre></div>
<p>資料此時仍可能只在 Node 的 Log 路徑中，尚未送入 Loki。參考 <a href="https://kubernetes.io/docs/concepts/cluster-administration/logging/">Kubernetes Logging Architecture</a>。</p>
<h3 class="gd-section">3. Collector 讀取紀錄並附加分類</h3>
<p>Collector 負責搬運 Log。例如 Grafana Alloy，或其他環境中的 Fluent Bit。舊版 Loki 教學也常見 Promtail；官方已標示 Promtail 於 2026-03-02 結束生命週期。參考 <a href="https://grafana.com/docs/loki/latest/send-data/promtail/">Promtail 官方狀態</a>。</p>
<div class="gd-code"><div class="gd-code-label">Collector 讀取的新紀錄</div><pre class="gd-pre">2026-09-22 08:30 INFO Start Job
2026-09-22 08:31 ERROR Timeout</pre></div>
<div class="gd-table-scroll" role="region" aria-label="Metadata／Label資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">Metadata／Label</th><th scope="col">示例值</th></tr></thead><tbody><tr><td><code>namespace</code></td><td><code>production</code></td></tr><tr><td><code>pod</code></td><td><code>promotion-worker-abc</code></td></tr><tr><td><code>container</code></td><td><code>worker</code></td></tr><tr><td><code>service</code></td><td><code>promotion-worker</code></td></tr></tbody></table></div>
<p>上述 Labels 是示例配置，不代表 Collector 自動產生所有欄位。尤其 <code>service</code> 的命名與映射需要在收集設定中一致。</p>
<h3 class="gd-section">4. Collector 透過 HTTP Push 給 Loki</h3>
<div class="gd-table-scroll" role="region" aria-label="傳送內容資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">傳送內容</th><th scope="col">概念示例</th></tr></thead><tbody><tr><td>Timestamp</td><td><code>2026-09-22 08:30:01</code></td></tr><tr><td>Labels</td><td><code>service="promotion-worker"</code>、<code>pod="promotion-worker-abc"</code>、<code>namespace="production"</code></td></tr><tr><td>Log</td><td><code>INFO Start processing ShopId 2</code></td></tr></tbody></table></div>
<p>這是內容概念表，不是可直接提交的 Loki API payload。Collector 依 API 格式將資料送入 Loki，Loki 才能保存並供後續查詢。</p>
<h3 class="gd-section">5. 透過 Grafana 查詢 Loki</h3>
<div class="gd-code"><div class="gd-code-label">篩選指定服務的錯誤文字</div><pre class="gd-pre">{service=&quot;promotion-worker&quot;} |= &quot;ERROR&quot;</pre></div>
<p>這段 <code>LogQL</code> 先選取 <code>service="promotion-worker"</code> 的 Log stream，再篩選包含大寫 <code>ERROR</code> 的紀錄。它是區分大小寫的文字篩選，不會自動判斷所有語意上的錯誤。參考 <a href="https://grafana.com/docs/loki/latest/query/log_queries/">Loki Log queries</a>。</p>
<h3 class="gd-section">Log 查詢時序：請求與回傳</h3>
<div class="gd-diagram" role="region" aria-label="Log 查詢時序：請求與回傳" tabindex="0"><div class="gd-diagram-inner" style="min-width:620px"><img class="gd-sequence" src="/Mind/images/grafana-1/loki-query.svg" alt="Log 查詢時序：請求與回傳" width="779" height="293"></div></div>
<p>參與者由左至右排列，時間向下。實線是查詢或操作，虛線是結果返回。這張圖只描述成功查詢的概念路徑；Grafana 是查詢介面，本文架構中的 Log 儲存在 Loki。</p>
</section>
<!-- endtab -->
<!-- tab Grafana-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>把查詢結果變成畫面與告警</h2><p>Grafana 接上資料來源，將查詢結果呈現為儀表板與探索畫面，也能定期評估告警條件。資料儲存、查詢運算與畫面呈現各有負責的元件。</p></div>
<h3 class="gd-section">三種主要使用方式</h3>
<div class="gd-table-scroll" role="region" aria-label="功能資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">功能</th><th scope="col">操作方式</th><th scope="col">用途</th></tr></thead><tbody><tr><td>Dashboard</td><td>由 Panel 對資料來源執行查詢</td><td>持續查看 CPU、Memory 與服務指標</td></tr><tr><td>Explore</td><td>選擇資料來源，互動式執行 PromQL 或 LogQL</td><td>逐步調查數值變化與錯誤紀錄</td></tr><tr><td>Alerting</td><td>定期查詢並評估規則</td><td>依告警與通知設定送出訊息</td></tr></tbody></table></div>
<p>整體架構仍是應用系統提供 Metrics 與 Logs：Prometheus 負責指標收集與儲存，Alloy／Fluent Bit 等 Collector 將 Log 送入 Loki，Grafana 再查詢這些資料來源。</p>
<h3 class="gd-section">Panel 如何顯示 Pod Memory</h3>
<div class="gd-table-scroll" role="region" aria-label="時間資料表" tabindex="0"><table class="gd-table"><thead><tr><th scope="col">時間</th><th scope="col">Prometheus 中的 Memory 顯示示例</th></tr></thead><tbody><tr><td>08:00</td><td>1.2 GB</td></tr><tr><td>08:01</td><td>1.4 GB</td></tr><tr><td>08:02</td><td>1.7 GB</td></tr><tr><td>08:03</td><td>1.9 GB</td></tr></tbody></table></div>
<div class="gd-code"><div class="gd-code-label">Memory Panel 查詢</div><pre class="gd-pre">container_memory_working_set_bytes{
    pod=&quot;promotion-worker&quot;
}</pre></div>
<p>範例假設 Pod Label 恰好是 <code>promotion-worker</code>；實際部署需使用真正的 Pod 名稱與必要的 namespace／container 篩選。查詢原始單位是 bytes，Panel 可設定顯示為 GB 或 GiB。</p>
<h3 class="gd-section">Memory Panel 查詢時序</h3>
<div class="gd-diagram" role="region" aria-label="Memory Panel 查詢時序" tabindex="0"><div class="gd-diagram-inner" style="min-width:480px"><img class="gd-sequence" src="/Mind/images/grafana-1/memory-panel.svg" alt="Memory Panel 查詢時序" width="457" height="301"></div></div>
<p>時間由上往下。上表的 1.2、1.4、1.7、1.9 GB 形成上升趨勢；圖表由 Grafana 畫出，底下的時間序列資料由 Prometheus 提供。Panel 不會只靠查詢名稱推定所有 Container 的聚合方式。</p>
<h3 class="gd-section">Explore 如何顯示 Error Log</h3>
<p>將 Data Source 選為 Loki，在 Explore 輸入下列查詢。Grafana 將 LogQL 送給 Loki，再顯示 Loki 回傳的紀錄。</p>
<div class="gd-code"><div class="gd-code-label">Explore 查詢</div><pre class="gd-pre">{service=&quot;promotion-worker&quot;} |= &quot;ERROR&quot;</pre></div>
<div class="gd-code"><div class="gd-code-label">Explore 結果示例</div><pre class="gd-pre">08:31 ERROR DynamoDB timeout
08:35 ERROR OutOfMemoryException</pre></div>
<p>在 Grafana 撰寫 LogQL，表示透過 Grafana 介面對 Loki 下查詢。寫入管線、Log 儲存與查詢呈現的責任仍然分開。</p>
<h3 class="gd-section">Alert：過去 5 分鐘 Dify Error > 5</h3>
<p>假設規則要觀察過去 5 分鐘的 Dify Error 數量，門檻為大於 <code>5</code>。Grafana 定期查詢 Loki，某次取得 <code>8</code>，因此滿足門檻。實際查詢需要依 Dify 的 Labels 與 Log 格式建立計數條件；純 Log 清單查詢還不是告警所需的數值結果。</p>
<h3 class="gd-section">告警評估：超過門檻後才進入狀態判定</h3>
<div class="gd-diagram" role="region" aria-label="告警評估：超過門檻後才進入狀態判定" tabindex="0"><div class="gd-diagram-inner" style="min-width:600px"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;background&quot;: &quot;#1b1925&quot;, &quot;primaryColor&quot;: &quot;#30283e&quot;, &quot;primaryTextColor&quot;: &quot;#eeeaf4&quot;, &quot;primaryBorderColor&quot;: &quot;#91829f&quot;, &quot;lineColor&quot;: &quot;#b8aec8&quot;, &quot;secondaryColor&quot;: &quot;#252030&quot;, &quot;tertiaryColor&quot;: &quot;#252030&quot;, &quot;clusterBkg&quot;: &quot;#211c2b&quot;, &quot;clusterBorder&quot;: &quot;#756583&quot;, &quot;edgeLabelBackground&quot;: &quot;#1b1925&quot;, &quot;textColor&quot;: &quot;#eeeaf4&quot;, &quot;fontSize&quot;: &quot;16px&quot;, &quot;fontFamily&quot;: &quot;Segoe UI, Microsoft JhengHei, sans-serif&quot;, &quot;actorBkg&quot;: &quot;#30283e&quot;, &quot;actorBorder&quot;: &quot;#91829f&quot;, &quot;actorTextColor&quot;: &quot;#eeeaf4&quot;, &quot;actorLineColor&quot;: &quot;#91829f&quot;, &quot;signalColor&quot;: &quot;#cbc8d5&quot;, &quot;signalTextColor&quot;: &quot;#eeeaf4&quot;, &quot;labelBoxBkgColor&quot;: &quot;#252030&quot;, &quot;labelBoxBorderColor&quot;: &quot;#91829f&quot;, &quot;labelTextColor&quot;: &quot;#eeeaf4&quot;, &quot;loopTextColor&quot;: &quot;#eeeaf4&quot;, &quot;noteBkgColor&quot;: &quot;#30283e&quot;, &quot;noteBorderColor&quot;: &quot;#91829f&quot;, &quot;noteTextColor&quot;: &quot;#eeeaf4&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true, &quot;curve&quot;: &quot;linear&quot;, &quot;nodeSpacing&quot;: 28, &quot;rankSpacing&quot;: 45}, &quot;sequence&quot;: {&quot;useMaxWidth&quot;: true, &quot;mirrorActors&quot;: false, &quot;actorMargin&quot;: 45, &quot;messageMargin&quot;: 35}}" hidden>flowchart TB
Evaluate[&quot;Grafana 定期評估&quot;] --&gt;|查詢最近 5 分鐘| Query[&quot;Loki 回傳 Dify Error 數量&quot;]
Query --&gt; Threshold{&quot;錯誤數量大於 5？&quot;}
Threshold --&gt;|否| Next[&quot;本次未達門檻，等待下次評估&quot;]
Threshold --&gt;|是，範例值為 8| State[&quot;依 Pending 等設定判定告警狀態&quot;]
State --&gt; Ready{&quot;已達 Alerting？&quot;}
Ready --&gt;|否| Wait[&quot;繼續評估條件是否持續成立&quot;]
Ready --&gt;|是| Policy[&quot;依通知策略與時機處理&quot;]
Policy --&gt;|符合通知條件| Notify[&quot;Slack / Email / 其他管道&quot;]</pre></div></div></div>
<p>由上往下讀，菱形表示判斷，箭頭直接標示條件。圖中以原先非告警、查詢成功且有資料的規則為例，沒有展開既有告警恢復、No Data 或查詢錯誤的處理。</p>
<div class="gd-note"><p>超過門檻不等於立即通知。評估週期決定多久檢查一次；Pending period 決定條件需持續多久才進入 Alerting；通知策略還可能涉及分組、等待與靜音等設定。Pending 設為 0 時可略過等待。</p></div>
<p>以上為 Grafana-managed alert rule 的概念流程。參考 <a href="https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rule-evaluation/">Grafana 告警評估說明</a>。Grafana 的核心用途，是將不同監控資料來源接到同一個平台，提供查詢、視覺化、Dashboard 與 Alert。</p>
</section>
<!-- endtab -->

{% endtabs %}
