---
title: API 監控 - 1
date: 2026-11-19 11:31:00
categories: Metric
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/grafana.png
cover : https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/grafana.png
tags:
    - 
toc:
toc_number:
comments :
---

{% tabs 語法 %}

<!-- tab 定義怎麼切環境 -->

<style>
.grafana-dusk{--gd-bg:#1b1925;--gd-panel:#252030;--gd-code:#111217;--gd-ink:#cbc8d5;--gd-title:#eeeaf4;--gd-muted:#aaa5b8;--gd-line:#554a62;--gd-link:#91b7ff;--gd-orange:#ff8c16;--gd-yellow:#ffc619;background:var(--gd-bg);color:var(--gd-ink);padding:28px;font:16px/1.8 'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif;overflow-wrap:anywhere;color-scheme:dark}
.grafana-dusk *{box-sizing:border-box}
#article-container .grafana-dusk h2,#article-container .grafana-dusk h3,.grafana-dusk h2,.grafana-dusk h3{color:var(--gd-title);line-height:1.4;margin:0 0 16px;font-weight:500}
.grafana-dusk p{margin:12px 0;max-width:68ch}
.grafana-dusk a{color:var(--gd-link)}
#article-container .grafana-dusk code,.grafana-dusk code{background:#342c42;color:#eeeaf4;padding:2px 5px;border-radius:3px;font-family:Consolas,monospace;overflow-wrap:anywhere}
.grafana-dusk .gd-hero{padding:36px 28px;margin:0 0 28px;text-align:center;border-radius:4px;background:linear-gradient(155deg,#713d70 0%,#39234d 48%,#110d23 100%)}
.grafana-dusk .gd-brand-line{display:block;width:64px;height:5px;margin:0 auto 22px;border-radius:2px;background:linear-gradient(90deg,#f45125,#ff8c16,#ffc619)}
.grafana-dusk .gd-hero h2{font-size:clamp(1.7rem,4vw,2.25rem)}
.grafana-dusk .gd-hero p{max-width:42em;margin:12px auto 0;color:var(--gd-title)}
#article-container .grafana-dusk h3.gd-section{font-size:1.3rem;border-left:3px solid var(--gd-orange);padding-left:14px;margin:38px 0 18px}
.grafana-dusk .gd-panel,.grafana-dusk .gd-note,.grafana-dusk .gd-diagram{background:linear-gradient(180deg,var(--gd-panel),var(--gd-bg));border:1px solid var(--gd-line);border-radius:4px;padding:22px;margin:20px 0}
.grafana-dusk .gd-note{border-left:3px solid var(--gd-link)}
.grafana-dusk .gd-caption{font-size:13px;letter-spacing:.08em;color:var(--gd-muted);margin:0 0 16px;text-transform:uppercase}
.grafana-dusk .gd-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(195px,1fr));gap:14px;margin:18px 0}
.grafana-dusk .gd-card{background:#30283e;border:1px solid #675775;border-radius:4px;padding:17px 18px;min-width:0}
.grafana-dusk .gd-card b{display:block;color:var(--gd-title);font-weight:600;margin-bottom:8px}
.grafana-dusk .gd-card p{margin:0;font-size:15px}
.grafana-dusk .gd-card .gd-key{font:700 13px/1.5 Consolas,monospace;color:var(--gd-yellow);display:block;margin-bottom:9px;overflow-wrap:anywhere}
.grafana-dusk .gd-flow{display:flex;align-items:stretch;gap:9px;margin:20px 0;overflow-x:auto;padding:2px 2px 10px}
.grafana-dusk .gd-flow .gd-node{flex:1 0 145px;min-width:145px;background:#30283e;border:1px solid #675775;border-radius:4px;padding:14px 16px}
.grafana-dusk .gd-flow .gd-node b{display:block;color:var(--gd-title);font-size:15px}
.grafana-dusk .gd-flow .gd-node small{display:block;color:var(--gd-ink);font-size:13px;line-height:1.5;margin-top:7px}
.grafana-dusk .gd-flow .gd-arrow{align-self:center;flex:0 0 auto;color:var(--gd-orange);font-size:25px}
.grafana-dusk .gd-flow:has(.gd-node:nth-of-type(4)){flex-direction:column;overflow:visible}
.grafana-dusk .gd-flow:has(.gd-node:nth-of-type(4)) .gd-node{flex:0 0 auto;min-width:0}
.grafana-dusk .gd-flow:has(.gd-node:nth-of-type(4)) .gd-arrow{transform:rotate(90deg);line-height:1}
.grafana-dusk .gd-branch{border-left:3px solid var(--gd-orange);padding-left:18px;margin:20px 0}
.grafana-dusk .gd-branch-row{display:flex;gap:12px;align-items:flex-start;margin:13px 0;flex-wrap:wrap}
.grafana-dusk .gd-branch-row .gd-label{background:#713d70;color:#fff;padding:5px 10px;border-radius:3px;font-size:13px;min-width:110px;text-align:center}
.grafana-dusk .gd-branch-row .gd-value{flex:1;min-width:180px;color:var(--gd-title)}
.grafana-dusk .gd-code{background:var(--gd-code);border:1px solid var(--gd-line);border-radius:3px;overflow:hidden;margin:20px 0}
.grafana-dusk .gd-code-label{padding:8px 16px;color:var(--gd-muted);border-bottom:1px solid var(--gd-line);font-size:13px}
#article-container .grafana-dusk pre.gd-pre,.grafana-dusk pre.gd-pre{background:var(--gd-code)!important;color:var(--gd-ink)!important;margin:0!important;padding:18px!important;border:0!important;border-radius:0!important;box-shadow:none!important;text-shadow:none!important;white-space:pre!important;overflow-x:auto!important;font:14px/1.7 Consolas,monospace!important}
.grafana-dusk .gd-table-scroll{max-width:100%;overflow-x:auto;margin:20px 0}
#article-container .grafana-dusk table.gd-table,.grafana-dusk table.gd-table{width:auto;max-width:100%;border-collapse:collapse;color:var(--gd-ink);background:var(--gd-bg);margin:0}
.grafana-dusk .gd-table th,.grafana-dusk .gd-table td{padding:11px 15px;border:1px solid var(--gd-line);text-align:left;vertical-align:top;color:var(--gd-ink);background:var(--gd-bg)}
.grafana-dusk .gd-table th{background:var(--gd-panel);color:var(--gd-title)}
.grafana-dusk .gd-figure{background:var(--gd-bg);border:1px solid var(--gd-line);border-radius:4px;padding:18px;margin:20px 0;overflow-x:auto}
.grafana-dusk .gd-figure svg{display:block;max-width:none;height:auto;margin:auto}
.grafana-dusk .gd-shot{display:block;width:100%;height:auto;max-width:100%;border:1px solid var(--gd-line);border-radius:4px;margin:18px 0}
.grafana-dusk details.gd-details{background:#252030;border:1px solid var(--gd-line);border-radius:4px;margin:20px 0;padding:12px 16px}
.grafana-dusk details.gd-details summary{cursor:pointer;color:var(--gd-title);font-weight:600}
.grafana-dusk details.gd-details .gd-code{margin-bottom:0}
.grafana-dusk .gd-metric{display:inline-block;color:var(--gd-title);background:#342c42;padding:6px 10px;border:1px solid var(--gd-line);border-radius:3px;font-family:Consolas,monospace;max-width:100%;overflow-wrap:anywhere}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs{background:#252030}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs>.tab{color:#cbc8d5;background:#252030}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs>.tab.active{color:#eeeaf4;background:#30283e;border-top-color:#3d73d9}
@media(max-width:600px){.grafana-dusk{padding:16px}.grafana-dusk .gd-hero{padding:28px 16px}.grafana-dusk .gd-panel,.grafana-dusk .gd-note,.grafana-dusk .gd-diagram{padding:16px}.grafana-dusk .gd-flow{flex-direction:column;overflow:visible}.grafana-dusk .gd-flow .gd-node{flex:0 0 auto;min-width:0;width:100%}.grafana-dusk .gd-flow .gd-arrow{transform:rotate(90deg);line-height:1}.grafana-dusk .gd-table th,.grafana-dusk .gd-table td{min-width:8em;padding:9px}}
</style>
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>一個選單，切換整張 Dashboard 的環境</h2><p>環境變數集中保存資料來源名稱、namespace 與 service 的對照。Panel 引用同一組值，就能跟著環境選單一起切換。</p></div>
<h3 class="gd-section">環境對照如何流向 Panel</h3>
<div class="gd-diagram" role="img" aria-label="選擇 HK Prod 後，環境對照供資料來源變數及 Panel 查詢使用">
<div class="gd-caption">HK Prod 的設定流向</div>
<div class="gd-flow"><div class="gd-node"><b>環境選單</b><small>選擇 HK Prod</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>environment</b><small>取得該環境的對照欄位</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>Panel</b><small>使用對應資料來源與查詢條件</small></div></div>
<div class="gd-branch"><div class="gd-branch-row"><span class="gd-label">prometheusName</span><span class="gd-value"><code>HK-Prod-Prometheus</code>，交給 <code>Cluster</code> 選擇資料來源</span></div><div class="gd-branch-row"><span class="gd-label">namespace</span><span class="gd-value"><code>prod-regular-purchase-service</code>，代入 PromQL 的 namespace 條件</span></div><div class="gd-branch-row"><span class="gd-label">service</span><span class="gd-value"><code>prod-regular-purchase-service</code>，代入 Loki 的 service 條件</span></div></div>
</div>
<p>建立新 Panel 時仍須引用 <code>&#36;{Cluster}</code>、<code>&#36;{environment.namespace}</code> 或 <code>&#36;{environment.service}</code>。各環境的實際值只在 <code>environment</code> 定義一次，不必為 TW、HK、MY 各複製一套 Panel。</p>
<h3 class="gd-section">六個環境共用一份欄位結構</h3>
<div class="gd-grid"><div class="gd-card"><span class="gd-key">TW / HK / MY Prod</span><b>相同 namespace，不同資料來源</b><p>三個正式環境都使用 <code>prod-regular-purchase-service</code>，但各自指向不同市場的 Prometheus 與 Loki。</p></div><div class="gd-card"><span class="gd-key">TW / HK / MY QA</span><b>依環境挑選 namespace</b><p>QA 依市場使用不同 namespace；HK 與 MY 共用同名的 QA 資料來源。</p></div></div>
<details class="gd-details"><summary>查看完整 Custom variable JSON</summary>
<div class="gd-code"><div class="gd-code-label">environment 的 Custom options</div><pre class="gd-pre">[
  {"value":"TW-Prod","text":"TW Prod","prometheusName":"TW-Prod-Prometheus","lokiName":"TW-Prod-Loki","cloudwatchName":"TW-Prod-CloudWatch","namespace":"prod-regular-purchase-service","service":"prod-regular-purchase-service"},
  {"value":"HK-Prod","text":"HK Prod","prometheusName":"HK-Prod-Prometheus","lokiName":"HK-Prod-Loki","cloudwatchName":"HK-Prod-CloudWatch","namespace":"prod-regular-purchase-service","service":"prod-regular-purchase-service"},
  {"value":"MY-Prod","text":"MY Prod","prometheusName":"MY-Prod-Prometheus","lokiName":"MY-Prod-Loki","cloudwatchName":"MY-Prod-CloudWatch","namespace":"prod-regular-purchase-service","service":"prod-regular-purchase-service"},
  {"value":"TW-QA","text":"TW QA","prometheusName":"TW-PX-QA-Prometheus","lokiName":"TW-PX-QA-Loki","cloudwatchName":"TW-PX-QA-CloudWatch","namespace":"qa-regular-purchase-service","service":"qa-regular-purchase-service"},
  {"value":"HK-QA","text":"HK QA","prometheusName":"HK-MY-QA-Prometheus","lokiName":"HK-MY-QA-Loki","cloudwatchName":"HK-MY-QA-CloudWatch","namespace":"hk-qa-regular-purchase-service","service":"hk-qa-regular-purchase-service"},
  {"value":"MY-QA","text":"MY QA","prometheusName":"HK-MY-QA-Prometheus","lokiName":"HK-MY-QA-Loki","cloudwatchName":"HK-MY-QA-CloudWatch","namespace":"my-qa-regular-purchase-service","service":"my-qa-regular-purchase-service"}
]</pre></div>
</details>
</section>

<!-- endtab -->

<!-- tab datasource -->

<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>環境名稱如何選到真正的資料來源</h2><p><code>environment</code> 保存名稱；Datasource variable 依名稱找到 Grafana 中已建立的連線。資料來源的連線設定與 Dashboard 的環境對照各有位置。</p></div>
<h3 class="gd-section">先有連線，再用變數挑選</h3>
<div class="gd-flow"><div class="gd-node"><b>Connections</b><small>預先建立 HK-Prod-Prometheus 與 HK-Prod-Loki</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>environment</b><small>提供 prometheusName 與 lokiName</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>Datasource variable</b><small>依 Type 與 Name filter 選連線</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>Panel</b><small>使用 Cluster 或 Loki</small></div></div>
<p><code>prometheusName</code> 與 <code>lokiName</code> 是資料來源的名稱，不是連線位址。實際資料來源先在 Grafana 的 <strong>Connections → Data sources</strong> 建立。</p>
<h3 class="gd-section">兩道篩選條件</h3>
<div class="gd-grid"><div class="gd-card"><span class="gd-key">Cluster</span><b>Type：Prometheus</b><p>Name filter：<code>^&#36;{environment.prometheusName}&#36;</code></p></div><div class="gd-card"><span class="gd-key">Loki</span><b>Type：Loki</b><p>Name filter：<code>^&#36;{environment.lokiName}&#36;</code></p></div></div>
<div class="gd-note"><p>選擇 HK Prod 時，<code>&#36;{environment.prometheusName}</code> 展開為 <code>HK-Prod-Prometheus</code>。<code>Cluster</code> 先限制 Type 為 Prometheus，再以 Name filter 匹配這個既有資料來源。</p></div>
<h3 class="gd-section">Panel 最後引用哪個變數</h3>
<div class="gd-branch"><div class="gd-branch-row"><span class="gd-label">Prometheus</span><span class="gd-value">Panel 的 Data source 選 <code>&#36;{Cluster}</code></span></div><div class="gd-branch-row"><span class="gd-label">Loki</span><span class="gd-value">Panel 的 Data source 選 <code>&#36;{Loki}</code></span></div></div>
<p>切換環境後，資料來源變數會依新名稱切換。<code>cloudwatchName</code> 也可按相同方式提供 CloudWatch 的名稱對照，但仍需另外建立並引用對應的 Datasource variable。</p>
</section>

<!-- endtab -->

<!-- tab Payment Middleware 畫 StatusCode 趨勢圖 -->

<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>從第三方回應日誌畫出狀態碼趨勢</h2><p>Payment Middleware 在收到第三方 HTTP 回應後寫入結構化日誌。Loki 將符合條件的日誌變成每分鐘筆數，Grafana 再依狀態碼畫線。</p></div>
<img class="gd-shot" src="https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/paymentmiddleware-statuscode-timeseries.png" alt="第三方 API Response Status Code 每分鐘趨勢圖">
<h3 class="gd-section">狀態碼從哪裡來</h3>
<div class="gd-flow"><div class="gd-node"><b>PMW 呼叫第三方</b><small>例如 Stripe API</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>收到 HTTP 回應</b><small>Handler 取得回應 StatusCode</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>寫入 MetricsLog</b><small>記錄 Type、Host、Path、Status</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>Loki 保存日誌</b><small>供 Panel 查詢</small></div></div>
<div class="gd-note"><p>程式的 <code>MetricsLogEntity.Type</code> 固定為 <code>Metrics</code>。回應記錄 Handler 將第三方回應碼寫入 <code>MetricsLog.Status</code>；這是第三方呼叫的回應碼，不等於 PMW 對呼叫方回傳的狀態碼。</p></div>
<h3 class="gd-section">JSON 為什麼要解析</h3>
<div class="gd-code"><div class="gd-code-label">HK Prod 實際日誌的精簡欄位，識別資訊已省略</div><pre class="gd-pre">{
  "_props": {
    "MetricsLog": {
      "Type": "Metrics",
      "Host": "api.stripe.com",
      "Path": "/v1/payment_intents",
      "Status": "402"
    }
  }
}</pre></div>
<div class="gd-branch"><div class="gd-branch-row"><span class="gd-label">service 標籤</span><span class="gd-value"><code>{service="&#36;Namespace"}</code> 先找出 PMW 日誌</span></div><div class="gd-branch-row"><span class="gd-label">JSON 解析</span><span class="gd-value"><code>| json</code> 將巢狀欄位展開為 <code>_props_MetricsLog_Type</code> 與 <code>_props_MetricsLog_Status</code></span></div><div class="gd-branch-row"><span class="gd-label">類型篩選</span><span class="gd-value"><code>Type = Metrics</code> 只留下程式標記的統計紀錄</span></div></div>
<h3 class="gd-section">先計數，再合併相同狀態碼</h3>
<div class="gd-diagram" role="img" aria-label="不同標籤組合先分別計數，再按狀態碼加總">
<div class="gd-caption">模擬：同一分鐘內的三組日誌</div>
<div class="gd-grid"><div class="gd-card"><span class="gd-key">Pod A / 200</span><b>12 筆</b><p>一組標籤的計數</p></div><div class="gd-card"><span class="gd-key">Pod B / 200</span><b>18 筆</b><p>另一組標籤的計數</p></div><div class="gd-card"><span class="gd-key">Pod A / 402</span><b>1 筆</b><p>狀態碼不同，分開保留</p></div></div>
<div class="gd-branch"><div class="gd-branch-row"><span class="gd-label">Status 200</span><span class="gd-value">12 + 18 = <strong>30 筆</strong></span></div><div class="gd-branch-row"><span class="gd-label">Status 402</span><span class="gd-value"><strong>1 筆</strong></span></div></div>
</div>
<p><code>count_over_time</code> 先依原有日誌串流及解析出的標籤組合計數，並非語法指定按 Pod 計數。<code>sum by (_props_MetricsLog_Status)</code> 才忽略其他標籤，依狀態碼加總。</p>
<div class="gd-code"><div class="gd-code-label">Time series Panel 的 LogQL</div><pre class="gd-pre">sum by (_props_MetricsLog_Status) (
  count_over_time(
    {service="&#36;Namespace"}
    | json
    | _props_MetricsLog_Type = `Metrics`
    [1m]
  )
)</pre></div>
<h3 class="gd-section">每個點都往回看一分鐘</h3>
<div class="gd-figure" role="img" aria-label="14 時整與 14 時 1 秒兩個點，各自往回統計一分鐘，視窗重疊約 59 秒"><svg viewBox="0 0 680 154" width="680" height="154" xmlns="http://www.w3.org/2000/svg"><g fill="#cbc8d5" font-size="14" font-family="Segoe UI,Microsoft JhengHei,sans-serif"><text x="14" y="37">14:00:00</text><text x="14" y="88">14:00:01</text><text x="145" y="139">13:59:00</text><text x="570" y="139">14:00:01</text></g><path d="M150 118H610" stroke="#554a62" stroke-width="2"/><rect x="150" y="20" width="450" height="24" rx="3" fill="#713d70"/><rect x="158" y="70" width="450" height="24" rx="3" fill="#3d73d9"/><text x="375" y="37" text-anchor="middle" fill="#fff" font-size="14">前一分鐘</text><text x="383" y="87" text-anchor="middle" fill="#fff" font-size="14">下一秒的前一分鐘</text><circle cx="150" cy="118" r="5" fill="#ffc619"/><circle cx="608" cy="118" r="5" fill="#ffc619"/></svg></div>
<p>Query interval 若為 1 秒，圖表每秒算一個點；<code>[1m]</code> 則決定每個點都往回看一分鐘。相鄰兩個視窗約有 59 秒重疊。Panel 選 Time series、Query Type 選 Range，Legend 使用 <code>{{_props_MetricsLog_Status}}</code>。</p>
</section>

<!-- endtab -->

<!-- tab Payment Middleware 計算 StatusCode 數量 -->

<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>所選時間內的第三方 4xx 有幾筆</h2><p>這張 Stat Panel 只保留 4xx 的 MetricsLog，依 Dashboard 選擇的時間長度計數，最後顯示最新一個統計值。</p></div>
<img class="gd-shot" src="https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/statucode-count.png" alt="第三方 API 4xx 總數 Stat Panel">
<h3 class="gd-section">篩選規則與時間長度</h3>
<div class="gd-grid"><div class="gd-card"><span class="gd-key">=~</span><b>用正規表示式比對</b><p>可一次選出多種狀態碼；<code>=</code> 則只比對單一指定值。</p></div><div class="gd-card"><span class="gd-key">(4)..</span><b>以 4 開頭的三個字元</b><p>例如 <code>402</code>、<code>404</code>、<code>429</code>。更精確可寫 <code>4[0-9]{2}</code>。</p></div><div class="gd-card"><span class="gd-key">[&#36;__range]</span><b>跟隨 Dashboard 時間長度</b><p>選 Last 6 hours 時展開成 <code>[6h]</code>。</p></div></div>
<div class="gd-code"><div class="gd-code-label">第三方 4xx 統計 LogQL</div><pre class="gd-pre">sum by (service) (
  count_over_time(
    {service="&#36;Namespace"}
    | json
    | _props_MetricsLog_Type = `Metrics`
    | _props_MetricsLog_Status =~ `(4)..`
    [&#36;__range]
  )
)</pre></div>
<p><code>sum by (service)</code> 將不同標籤組合的筆數合併，結果保留 service 名稱。這裡的 <code>&#36;Namespace</code> 已選單一 service，因此最後通常只有一個數列。</p>
<h3 class="gd-section">Range 與 Last* 各負責什麼</h3>
<div class="gd-figure" role="img" aria-label="Range 回傳四、六、七等多個時間點，Last 星號取最後一個非空值七"><svg viewBox="0 0 650 210" width="650" height="210" xmlns="http://www.w3.org/2000/svg"><path d="M45 160H620" stroke="#554a62" stroke-width="2"/><path d="M80 122L280 86L480 58" fill="none" stroke="#f4526f" stroke-width="4"/><g fill="#f4526f"><circle cx="80" cy="122" r="7"/><circle cx="280" cy="86" r="7"/><circle cx="480" cy="58" r="8"/></g><g fill="#eeeaf4" font-size="16" font-family="Segoe UI,Microsoft JhengHei,sans-serif" text-anchor="middle"><text x="80" y="108">4</text><text x="280" y="72">6</text><text x="480" y="44">7</text><text x="80" y="188">13:56</text><text x="280" y="188">13:58</text><text x="480" y="188">14:00</text></g><path d="M490 58H565" stroke="#ffc619" stroke-width="2"/><text x="570" y="63" fill="#ffc619" font-size="16" font-family="Segoe UI,Microsoft JhengHei,sans-serif">Last*: 7</text></svg></div>
<p>Range 會在圖表範圍內反覆計算，每個點都往回看 <code>&#36;__range</code>。Stat 的 <code>Calculate → Last*</code> 取最後一個非空值放大顯示，背景保留趨勢線；它不會把重疊視窗的各點再相加。</p>
<div class="gd-note"><p>只需顯示所選時間內的最新總數時，可改用 Instant，直接在結束時間計算一次。保留 Range 是為了顯示背景趨勢；這條趨勢是滑動的區間總數，不是每個查詢間隔內的新事件數。</p></div>
</section>

<!-- endtab -->

<!-- tab Payment Middleware 畫出 request rate 趨勢圖 -->

<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>Ingress 請求數如何變成每秒速率</h2><p>ingress-nginx 累積入口請求數，Prometheus 定期抓取樣本。PromQL 的 <code>irate</code> 再用最新兩筆樣本求出當下的增長速度。</p></div>
<img class="gd-shot" src="https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/paymentmiddleware-irate.png" alt="Payment Middleware Ingress request rate 趨勢圖">
<h3 class="gd-section">監控程式部署在哪裡</h3>
<div class="gd-diagram" role="img" aria-label="EKS Cluster 內監控系統與 Payment Middleware 是各自部署的工作負載"><div class="gd-caption">HK Prod EKS Cluster</div><div class="gd-grid"><div class="gd-card"><span class="gd-key">Monitoring</span><b>Prometheus StatefulSet</b><p>維持 Prometheus Pod。它負責抓取、保存及查詢 metrics。</p></div><div class="gd-card"><span class="gd-key">Payment Middleware</span><b>PMW Deployment</b><p>維持 PMW Web API Pods。處理付款 API 請求。</p></div><div class="gd-card"><span class="gd-key">Ingress</span><b>ingress-nginx Controller</b><p>處理入口流量並提供自身的 metrics endpoint。</p></div></div></div>
<p>Prometheus 是另外部署的應用程式，並非建立 EKS Cluster 時自動出現。StatefulSet 與 Deployment 都會依設定維持 Pods；StatefulSet 額外提供較穩定的 Pod 身分，資料持久性仍取決於儲存設定。</p>
<h3 class="gd-section">指標從產生到繪圖</h3>
<div class="gd-flow"><div class="gd-node"><b>請求進入 Ingress</b><small>Controller 更新累積計數</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>metrics endpoint</b><small>提供 nginx_ingress_controller_requests</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>Prometheus</b><small>定期以 HTTP 抓取並儲存樣本</small></div><span class="gd-arrow" aria-hidden="true">→</span><div class="gd-node"><b>Grafana</b><small>送出 PromQL 並畫圖</small></div></div>
<div class="gd-note"><p><code>nginx_ingress_controller_requests</code> 是 ingress-nginx 定義的累積計數器，不是 PMW API 或 Grafana 自己命名的值。Prometheus 抓取的是 ingress-nginx 的 metrics endpoint，並非 PMW 的業務 API。</p></div>
<h3 class="gd-section">為什麼篩選 exported_namespace</h3>
<div class="gd-branch"><div class="gd-branch-row"><span class="gd-label">namespace</span><span class="gd-value"><code>ingress-nginx</code>，目前樣本中是被抓取的 Controller 所在 namespace</span></div><div class="gd-branch-row"><span class="gd-label">exported_namespace</span><span class="gd-value"><code>prod-payment-middleware</code>，指向這條請求指標所屬的 Ingress namespace</span></div></div>
<p>Prometheus 抓取時若遇到同名的 <code>namespace</code> 標籤，可能把原本指標的欄位改成 <code>exported_namespace</code>。這裡的兩個值已在 HK Prod 指標中觀察到；具體衝突設定仍需以該環境的 scrape 設定核對。</p>
<h3 class="gd-section">五筆樣本，irate 只用最後兩筆</h3>
<div class="gd-figure" role="img" aria-label="五筆累積請求數從 100 到 116，irate 使用最後的 110 和 116 計算"><svg viewBox="0 0 690 250" width="690" height="250" xmlns="http://www.w3.org/2000/svg"><path d="M55 183H650" stroke="#554a62" stroke-width="2"/><path d="M75 143L210 133L345 126L480 109L615 89" fill="none" stroke="#91b7ff" stroke-width="3"/><g fill="#cbc8d5"><circle cx="75" cy="143" r="6"/><circle cx="210" cy="133" r="6"/><circle cx="345" cy="126" r="6"/></g><g fill="#ffc619"><circle cx="480" cy="109" r="8"/><circle cx="615" cy="89" r="8"/></g><g fill="#eeeaf4" font-size="15" font-family="Segoe UI,Microsoft JhengHei,sans-serif" text-anchor="middle"><text x="75" y="128">100</text><text x="210" y="118">103</text><text x="345" y="111">105</text><text x="480" y="94">110</text><text x="615" y="74">116</text><text x="75" y="211">13:58</text><text x="210" y="211">13:58:30</text><text x="345" y="211">13:59</text><text x="480" y="211">13:59:30</text><text x="615" y="211">14:00</text></g><path d="M480 47H615" stroke="#ffc619" stroke-width="2"/><text x="547" y="35" text-anchor="middle" fill="#ffc619" font-size="14">最後兩筆</text></svg></div>
<p>以上是模擬樣本。<code>[2m]</code> 先限定搜尋最近兩分鐘的範圍；即使範圍內有五筆，<code>irate</code> 也只取最後兩筆：<code>(116 − 110) ÷ 30 秒 = 0.2 次／秒</code>。</p>
<div class="gd-code"><div class="gd-code-label">Ingress request rate 的 PromQL</div><pre class="gd-pre">sum(
  irate(
    nginx_ingress_controller_requests{
      exported_namespace="&#36;Namespace"
    }[2m]
  )
) by (ingress)</pre></div>
<p><code>sum ... by (ingress)</code> 將同一 Ingress 的不同 controller Pod、method 與 status 數列速率加總。這條查詢顯示每秒請求速率，沒有篩掉 4xx 或 5xx，也不是 PMW 對第三方的呼叫速率。</p>
</section>

<!-- endtab -->

{% endtabs %}
