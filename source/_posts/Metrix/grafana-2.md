---
title: Alert 設計
date: 2026-11-14 10:09:00
categories: Metric
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/grafana.png
cover : https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/metric/grafana.png
tags:
    - 
toc:
toc_number:
comments :
---

{% tabs Alert %}

<!-- tab 時間模型-->
<style>
.grafana-dusk{--gd-bg:#1b1925;--gd-panel:#252030;--gd-code:#111217;--gd-ink:#cbc8d5;--gd-title:#eeeaf4;--gd-muted:#aaa5b8;--gd-line:#554a62;--gd-link:#91b7ff;background:var(--gd-bg);color:var(--gd-ink);padding:28px;font:16px/1.85 'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif;overflow-wrap:anywhere;color-scheme:dark}
.grafana-dusk *{box-sizing:border-box}
.grafana-dusk p{max-width:72ch;margin:18px 0}
.grafana-dusk a{color:var(--gd-link);text-decoration:underline;text-underline-offset:3px}
.grafana-dusk :focus-visible{outline:3px solid var(--gd-link);outline-offset:3px}
#article-container .grafana-dusk code,.grafana-dusk code{background:#342c42;color:#eeeaf4;padding:2px 5px;border-radius:3px;font-family:Consolas,monospace;overflow-wrap:anywhere}
.grafana-dusk .gd-hero{padding:34px 28px;margin:0 0 26px;text-align:center;border-radius:4px;background:linear-gradient(155deg,#713d70 0%,#39234d 48%,#110d23 100%)}
.grafana-dusk .gd-brand-line{display:block;width:64px;height:5px;margin:0 auto 21px;border-radius:2px;background:linear-gradient(90deg,#f45125,#ff8c16,#ffc619)}
#article-container .grafana-dusk .gd-hero h2{color:var(--gd-title);font-size:clamp(1.55rem,4vw,2.15rem);font-weight:500;line-height:1.4;margin:0}
.grafana-dusk .gd-hero p{color:var(--gd-title);max-width:48em;margin:15px auto 0}
#article-container .grafana-dusk h3.gd-section{color:var(--gd-title);font-size:1.23rem;font-weight:500;line-height:1.4;margin:36px 0 17px;padding-left:14px;border-left:3px solid #ff8c16}
.grafana-dusk .gd-visual{background:var(--gd-bg);border:1px solid var(--gd-line);border-radius:4px;padding:18px 10px;margin:25px 0;overflow-x:auto}
.grafana-dusk .gd-visual svg{display:block;width:100%;min-width:560px;height:auto;margin:auto}
.grafana-dusk .gd-table-scroll{max-width:100%;overflow-x:auto;margin:23px 0}
#article-container .grafana-dusk .gd-table,.grafana-dusk .gd-table{border-collapse:collapse;width:100%;min-width:570px;margin:0;background:var(--gd-bg);color:var(--gd-ink)}
#article-container .grafana-dusk .gd-table th,#article-container .grafana-dusk .gd-table td{padding:11px 14px;border:1px solid var(--gd-line);text-align:left;vertical-align:top;background:var(--gd-bg);color:var(--gd-ink);min-width:7em}
#article-container .grafana-dusk .gd-table th{background:var(--gd-panel);color:var(--gd-title);font-weight:600}
.grafana-dusk .gd-details{border:1px solid var(--gd-line);border-radius:4px;background:var(--gd-panel);margin:22px 0;padding:12px 16px}
.grafana-dusk .gd-details summary{color:var(--gd-title);cursor:pointer;font-weight:600}
#article-container .grafana-dusk pre{background:var(--gd-code)!important;color:var(--gd-ink)!important;border:1px solid var(--gd-line);border-radius:3px;overflow-x:auto;padding:16px!important;margin:20px 0!important;box-shadow:none!important}
#article-container .grafana-dusk pre code{background:transparent;color:inherit;padding:0}
.grafana-dusk .gd-flow-key{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 22px}
.grafana-dusk .gd-flow-key span{border:1px solid var(--gd-line);border-radius:3px;padding:4px 10px;color:var(--gd-muted);font-size:13px}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs{background:#252030}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs>.tab{color:#cbc8d5;background:#252030}
#article-container .tabs:has(.grafana-dusk)>.nav-tabs>.tab.active{color:#eeeaf4;background:#30283e;border-top-color:#3d73d9}
@media(max-width:600px){.grafana-dusk{padding:16px}.grafana-dusk .gd-hero{padding:27px 16px}.grafana-dusk .gd-visual{padding:12px 6px}}
</style>
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>時間模型</h2><p>下午三點，滑鼠停在曲線上中午十二點的那個點，跳出一個數字：12。右上角明明選了 <code>Last 6 hours</code>，這 12 筆是六小時的總數，還是中午前那一小時的紀錄？</p></div>
<figure class="gd-visual" role="img" aria-label="09:00 到 15:00 的時間軸，12:00 的點回看 11:00 到 12:00" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 230" width="700" height="230" aria-hidden="true"><g font-family="Segoe UI, Microsoft JhengHei, sans-serif" font-size="15" fill="#cbc8d5"><text x="350" y="30" text-anchor="middle" fill="#eeeaf4" font-size="18">Dashboard 顯示 09:00～15:00</text><rect x="250" y="76" width="100" height="50" rx="3" fill="#713d70" opacity="0.58"/><line x1="50" y1="126" x2="650" y2="126" stroke="#91829f" stroke-width="2" /><line x1="50" y1="119" x2="50" y2="133" stroke="#554a62" stroke-width="2" /><text x="50" y="154" text-anchor="middle" fill="#cbc8d5" font-size="15">9:00</text><line x1="150" y1="119" x2="150" y2="133" stroke="#554a62" stroke-width="2" /><text x="150" y="154" text-anchor="middle" fill="#cbc8d5" font-size="15">10:00</text><line x1="250" y1="119" x2="250" y2="133" stroke="#554a62" stroke-width="2" /><text x="250" y="154" text-anchor="middle" fill="#cbc8d5" font-size="15">11:00</text><line x1="350" y1="119" x2="350" y2="133" stroke="#554a62" stroke-width="2" /><text x="350" y="154" text-anchor="middle" fill="#cbc8d5" font-size="15">12:00</text><line x1="450" y1="119" x2="450" y2="133" stroke="#554a62" stroke-width="2" /><text x="450" y="154" text-anchor="middle" fill="#cbc8d5" font-size="15">13:00</text><line x1="550" y1="119" x2="550" y2="133" stroke="#554a62" stroke-width="2" /><text x="550" y="154" text-anchor="middle" fill="#cbc8d5" font-size="15">14:00</text><line x1="650" y1="119" x2="650" y2="133" stroke="#554a62" stroke-width="2" /><text x="650" y="154" text-anchor="middle" fill="#cbc8d5" font-size="15">15:00</text><circle cx="350" cy="126" r="8" fill="#ffc619"/><text x="350" y="65" text-anchor="middle" fill="#ffc619" font-size="15">12:00 的點：12 筆</text><text x="300" y="109" text-anchor="middle" fill="#eeeaf4" font-size="13">[1h] 回看 11:00～12:00</text><text x="350" y="198" text-anchor="middle" fill="#aaa5b8" font-size="14">Step 決定點的間距；[1h] 決定每點的窗口</text></g></svg></figure>

<p>故事從右上角開始。<code>Last 6 hours</code> 把畫面拉到約 09:00～15:00，像翻開這六小時的值班紀錄。它讓中午那個點出現在眼前，但還沒有告訴我們，點上的 12 是怎麼算出來的</p>
<p>接著看圖上的點怎麼排。如果 Query options 的 <code>Interval</code>，或查詢的 <code>Step</code>，設為 <code>1h</code>，圖表就大約每小時留下一個點：09:00、10:00、11:00、12:00……。這決定的是<strong>多久算一次</strong></p>
<p>真正替那 12 筆劃出範圍的，是查詢裡的 <code>count_over_time(...[1h])</code>。<code>[1h]</code> 讓十二點的點回頭看約 11:00～12:00，所以 12 代表的是這一小時的筆數。右上角即使展示六小時，也不會把十二點的點變成六小時總數</p>
<p>輪到 Alert 時，又多了兩個時鐘。<code>30m to now</code> 說的是「這次評估要拿哪段查詢結果」，假設現在 15:00，Range Query 約取 14:30～15:00 的一串點，每個點仍照查詢中的 <code>[1h]</code> 各自往前算。<code>Alert evaluation interval = 1m</code> 則表示 Grafana 約每分鐘重新問一次「現在符合條件嗎？」它不會把 <code>[1h]</code> 改成一分鐘。</p>
<p>最後試著把 <code>Step</code> 從一小時改成十五分鐘。十二點的點回看 11:00～12:00，12:15 的點回看 11:15～12:15；兩段紀錄重疊了四十五分鐘。同一筆 log 可能同時被兩個點算進去。曲線可以拿來看變化，卻不能把沿途的點直接相加，當作整段期間的總筆數。</p>
<p>現在把這些時間設定放進同一個現場。假設 11:00～12:00 有 12 筆 log，下午又分別在 14:05、14:20、14:35、14:50 各出現 1 筆。為了看清 Alert 如何選值，以下<strong>示意</strong> Dashboard 和 Alert 的查詢點都剛好每 15 分鐘對齊；Alert 另外使用 Range、<code>Reduce Last</code>、門檻 <code>&gt; 3</code>、Pending 0。這些是教學用的假設，不是某條實際規則的設定。</p>
<div class="gd-table-scroll" role="region" aria-label="時間模型資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>走到哪一步</th>
<th>此時看的時間</th>
<th>算出什麼</th>
<th>接下來發生什麼</th>
</tr>
</thead>
<tbody><tr>
<td>打開 Dashboard</td>
<td>現在 15:00，右上角選 <code>Last 6 hours</code></td>
<td>畫面約展示 09:00～15:00</td>
<td>中午與下午的點都能在圖上看到；尚未決定每點要算幾筆</td>
</tr>
<tr>
<td>設定查詢點間距</td>
<td><code>Step = 15m</code></td>
<td>約每 15 分鐘算一個點</td>
<td>接著查看 12:00、14:30、14:45、15:00 這幾個點</td>
</tr>
<tr>
<td>讀 12:00 的點</td>
<td><code>[1h]</code> 回看 11:00～12:00</td>
<td><strong>12 筆</strong></td>
<td>這是中午前一小時的筆數，不是六小時總數</td>
</tr>
<tr>
<td>讀 14:30 的點</td>
<td><code>[1h]</code> 回看 13:30～14:30</td>
<td><strong>2 筆</strong>：14:05、14:20</td>
<td>等待下一個查詢點</td>
</tr>
<tr>
<td>讀 14:45 的點</td>
<td><code>[1h]</code> 回看 13:45～14:45</td>
<td><strong>3 筆</strong>：再加上 14:35</td>
<td>前兩筆也落在這個窗口裡</td>
</tr>
<tr>
<td>讀 15:00 的點</td>
<td><code>[1h]</code> 回看 14:00～15:00</td>
<td><strong>4 筆</strong>：再加上 14:50</td>
<td>這三個下午的點是 2、3、4，不能相加成 9 筆</td>
</tr>
<tr>
<td>Alert 在 15:00 評估</td>
<td><code>30m to now</code>，取約 14:30～15:00 的查詢點</td>
<td>示意取得 <strong>2、3、4</strong> 這串結果</td>
<td>每個點仍按自己的 <code>[1h]</code> 回看；Range 本身不把它們加總</td>
</tr>
<tr>
<td>Alert 選值並比門檻</td>
<td><code>Reduce Last</code> 取最後一點</td>
<td><strong>Last = 4；4 &gt; 3</strong></td>
<td>Pending 設 0，因此這次評估就符合 Alerting 條件</td>
</tr>
<tr>
<td>下一次評估</td>
<td><code>Evaluation interval = 1m</code>，約 15:01 再執行</td>
<td>重新查詢、重新選最後值</td>
<td>若最後值仍是 4，條件仍成立；這一分鐘不是 <code>Step</code>，也不是 <code>[1h]</code> 的窗口</td>
</tr>
</tbody></table></div>

</section>
<!-- endtab -->

<!-- tab Interval、Min. Interval 與 MD-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>Interval、Min. Interval 與 MD</h2><p>同一張趨勢圖，縮在 Dashboard 的角落時看起來很平順；點開放大，細小的起伏又冒出來了。資料沒有換，Grafana 只是換了「隔多久取一個點」的間距。這個間距，就是 Query options 裡看到的 <code>Interval</code>。</p></div>
<figure class="gd-visual" role="img" aria-label="五分鐘內以十五秒、一分鐘、五分鐘間距取點的密度對照" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 230" width="700" height="230" aria-hidden="true"><g font-family="Segoe UI, Microsoft JhengHei, sans-serif" font-size="15" fill="#cbc8d5"><text x="350" y="28" text-anchor="middle" fill="#eeeaf4" font-size="18">同樣 5 分鐘，點的密度不同</text><text x="120" y="75" text-anchor="end" fill="#cbc8d5" font-size="15">15s 下限</text><line x1="160" y1="70" x2="640" y2="70" stroke="#554a62" stroke-width="2" /><circle cx="160" cy="70" r="4.5" fill="#756583"/><circle cx="184" cy="70" r="4.5" fill="#756583"/><circle cx="208" cy="70" r="4.5" fill="#756583"/><circle cx="232" cy="70" r="4.5" fill="#756583"/><circle cx="256" cy="70" r="4.5" fill="#756583"/><circle cx="280" cy="70" r="4.5" fill="#756583"/><circle cx="304" cy="70" r="4.5" fill="#756583"/><circle cx="328" cy="70" r="4.5" fill="#756583"/><circle cx="352" cy="70" r="4.5" fill="#756583"/><circle cx="376" cy="70" r="4.5" fill="#756583"/><circle cx="400" cy="70" r="4.5" fill="#756583"/><circle cx="424" cy="70" r="4.5" fill="#756583"/><circle cx="448" cy="70" r="4.5" fill="#756583"/><circle cx="472" cy="70" r="4.5" fill="#756583"/><circle cx="496" cy="70" r="4.5" fill="#756583"/><circle cx="520" cy="70" r="4.5" fill="#756583"/><circle cx="544" cy="70" r="4.5" fill="#756583"/><circle cx="568" cy="70" r="4.5" fill="#756583"/><circle cx="592" cy="70" r="4.5" fill="#756583"/><circle cx="616" cy="70" r="4.5" fill="#756583"/><circle cx="640" cy="70" r="4.5" fill="#756583"/><text x="120" y="125" text-anchor="end" fill="#cbc8d5" font-size="15">1m 間距</text><line x1="160" y1="120" x2="640" y2="120" stroke="#554a62" stroke-width="2" /><circle cx="160" cy="120" r="4.5" fill="#91b7ff"/><circle cx="256" cy="120" r="4.5" fill="#91b7ff"/><circle cx="352" cy="120" r="4.5" fill="#91b7ff"/><circle cx="448" cy="120" r="4.5" fill="#91b7ff"/><circle cx="544" cy="120" r="4.5" fill="#91b7ff"/><circle cx="640" cy="120" r="4.5" fill="#91b7ff"/><text x="120" y="175" text-anchor="end" fill="#cbc8d5" font-size="15">5m 間距</text><line x1="160" y1="170" x2="640" y2="170" stroke="#554a62" stroke-width="2" /><circle cx="160" cy="170" r="4.5" fill="#ffc619"/><circle cx="640" cy="170" r="4.5" fill="#ffc619"/><text x="160" y="211" text-anchor="middle" fill="#cbc8d5" font-size="15">15:00</text><text x="640" y="211" text-anchor="middle" fill="#cbc8d5" font-size="15">15:05</text></g></svg></figure>

<p>Grafana 會參考畫面寬度和所選的時間範圍，自動估算適合的 <code>Interval</code>。假設目前算出 <code>1m</code>，意思是圖上約每分鐘取一個點。畫面變窄或把時間拉長，點可能排得更疏，<code>Interval</code> 也會跟著變；畫面上那個數字不一定是事先寫死的設定。</p>
<p>那麼，<code>Min. Interval = 15s</code> 又在做什麼？它替自動計算畫一條底線：點的間距不要比十五秒更密。底線不是指定值，所以 Grafana 仍可能選 <code>1m</code>、<code>5m</code> 或更大的間距。</p>
<p><code>MD = 43200</code> 的全名是 <strong>Max data points</strong>。它談的是每條序列可回傳的點數與查詢解析度。若查詢真的會回傳太多點，資料來源可能再依支援的方式縮減。面板大小也可能影響自動間距，因此改變看到的線條細節</p>
<p>最後還有一個容易混在一起的時間概念，查詢若明確設定 <code>Step = 1m</code>，那是要求每分鐘算一個點；<code>count_over_time(...[1h])</code> 裡的 <code>[1h]</code> 仍讓<strong>每個點</strong>各自回看一小時。點變密了，回看的窗口沒有縮短。</p>
<p>現在 15:00，畫面看最近六小時，假設面板寬度使 Grafana 自動選出 <code>Interval = 1m</code>，查詢的每點窗口固定為 <code>[1h]</code>。實際自動值與點的對齊仍以當時面板和資料來源為準。</p>
<div class="gd-table-scroll" role="region" aria-label="Interval、Min. Interval 與 MD資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>畫面或查詢走到哪一步</th>
<th>設定或時間</th>
<th>會發生什麼</th>
</tr>
</thead>
<tbody><tr>
<td>選定畫面範圍</td>
<td><code>Last 6 hours</code>，約 09:00～15:00</td>
<td>決定圖上可看到哪段歷史</td>
</tr>
<tr>
<td>Grafana 安排查詢點</td>
<td>示意自動算出 <code>Interval = 1m</code></td>
<td>約每分鐘取一點，六小時大約是 360 個間隔，含兩端約 361 個點</td>
</tr>
<tr>
<td>限制最密的間距</td>
<td><code>Min. Interval = 15s</code></td>
<td>一分鐘比十五秒疏，符合這條下限；下限不會強迫間距變成十五秒</td>
</tr>
<tr>
<td>限制回傳點數</td>
<td><code>MD = 43200</code></td>
<td>361 個示意點遠低於設定值，不會因此變成 43,200 個點</td>
</tr>
<tr>
<td>計算 15:00 的點</td>
<td><code>count_over_time(...[1h])</code></td>
<td>約回看 14:00～15:00</td>
</tr>
<tr>
<td>時間往前推進後的下一個查詢點</td>
<td>畫面更新至 15:01，<code>Step = 1m</code></td>
<td>約回看 14:01～15:01；它與 15:00 的一小時窗口重疊約 59 分鐘</td>
</tr>
</tbody></table></div>

</section>
<!-- endtab -->

<!-- tab Range、Instant 與狀態轉換-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>Range、Instant 與狀態轉換</h2><p>下午 13:30 發生一筆錯誤，到了 14:44，Alert 要回答的問題，可以有兩種問法</p></div>
<figure class="gd-visual" role="img" aria-label="14:14 到 14:29 的查詢點為 1，14:34 到 14:44 的查詢點為 0" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 220" width="700" height="220" aria-hidden="true"><g font-family="Segoe UI, Microsoft JhengHei, sans-serif" font-size="15" fill="#cbc8d5"><text x="350" y="27" text-anchor="middle" fill="#eeeaf4" font-size="18">同一筆 13:30 錯誤，在不同查詢點逐漸離開窗口</text><line x1="75" y1="166" x2="630" y2="166" stroke="#554a62" stroke-width="2" /><line x1="75" y1="50" x2="75" y2="166" stroke="#554a62" stroke-width="2" /><polyline points="75,82 167.5,82 260,82 352.5,82 445,166 537.5,166 630,166" fill="none" stroke="#91b7ff" stroke-width="3"/><circle cx="75" cy="82" r="6" fill="#ffc619"/><text x="75" y="69" text-anchor="middle" fill="#eeeaf4" font-size="14">1</text><text x="75" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:14</text><circle cx="167.5" cy="82" r="6" fill="#ffc619"/><text x="167.5" y="69" text-anchor="middle" fill="#eeeaf4" font-size="14">1</text><text x="167.5" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:19</text><circle cx="260" cy="82" r="6" fill="#ffc619"/><text x="260" y="69" text-anchor="middle" fill="#eeeaf4" font-size="14">1</text><text x="260" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:24</text><circle cx="352.5" cy="82" r="6" fill="#ffc619"/><text x="352.5" y="69" text-anchor="middle" fill="#eeeaf4" font-size="14">1</text><text x="352.5" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:29</text><circle cx="445" cy="166" r="6" fill="#ffc619"/><text x="445" y="153" text-anchor="middle" fill="#eeeaf4" font-size="14">0</text><text x="445" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:34</text><circle cx="537.5" cy="166" r="6" fill="#ffc619"/><text x="537.5" y="153" text-anchor="middle" fill="#eeeaf4" font-size="14">0</text><text x="537.5" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:39</text><circle cx="630" cy="166" r="6" fill="#ffc619"/><text x="630" y="153" text-anchor="middle" fill="#eeeaf4" font-size="14">0</text><text x="630" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:44</text></g></svg></figure>

<p>「現在回頭看一小時，還有錯誤嗎？」</p>
<p>或者</p>
<p>「最近半小時算出的那串結果，曾經出現錯誤嗎？」問法一變，即使查的是同一筆 log，答案也可能不同</p>
<p>如果只想知道<strong>評估當下</strong>往前一小時的筆數，<code>Instant</code> 很直接。查詢裡的 <code>count_over_time(...[1h])</code> 在 14:44 看約 13:44～14:44；13:30 的錯誤已經離開窗口，結果是 0。Alert 畫面即使還顯示 <code>30m to now</code>，固定寫在查詢中的 <code>[1h]</code> 也不會被改成半小時，<code>Instant</code> 更不會因此自動產生一整串點</p>
<p>如果問題是「最近半小時的變化如何」，就選 <code>Range</code>。<code>30m to now</code> 讓這次評估拿到約 14:14～14:44 的多個查詢點。每個點依然各自用 <code>[1h]</code> 往前數；早一點的窗口還包著 13:30，晚一點的窗口則已經放開了它。這時不能只說「Range 有資料」，還得看後面怎麼把一串值收成一個答案</p>
<p>選 <code>Reduce Last</code>，看的是最後一點，這個例子得到 0；如果本來只關心最新值，<code>Instant</code> 通常更容易表達。選 <code>Reduce Max</code>，看的則是整串結果裡最高的那一點，這裡得到 1。Max 回答的是「這段結果曾否非零」，並不是把半小時的數字加總。</p>
<p>把時鐘撥回 14:44，完整走一遍，目前只有 13:30 那一筆錯誤，並假設查詢在沒有符合的 log 時用 <code>or vector(0)</code> 回傳數值 0，<code>Range = 30m to now</code>、<code>Step = 5m</code>、每點窗口 <code>[1h]</code>；比較門檻暫設 <code>&gt; 0</code>，Pending 暫設 0</p>
<div class="gd-table-scroll" role="region" aria-label="Range、Instant 與狀態轉換資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>查詢方式與時間點</th>
<th>該點往前回看的區間</th>
<th align="right">算出的筆數</th>
<th>這一步的意思</th>
</tr>
</thead>
<tbody><tr>
<td>Range：14:14</td>
<td>13:14～14:14</td>
<td align="right">1</td>
<td>13:30 的錯誤還在窗口內</td>
</tr>
<tr>
<td>Range：14:19</td>
<td>13:19～14:19</td>
<td align="right">1</td>
<td>同一筆錯誤仍被算到</td>
</tr>
<tr>
<td>Range：14:24</td>
<td>13:24～14:24</td>
<td align="right">1</td>
<td>仍在窗口內</td>
</tr>
<tr>
<td>Range：14:29</td>
<td>13:29～14:29</td>
<td align="right">1</td>
<td>仍在窗口內</td>
</tr>
<tr>
<td>Range：14:34</td>
<td>13:34～14:34</td>
<td align="right">0</td>
<td>13:30 已離開這個窗口</td>
</tr>
<tr>
<td>Range：14:39</td>
<td>13:39～14:39</td>
<td align="right">0</td>
<td>仍是 0</td>
</tr>
<tr>
<td>Range：14:44</td>
<td>13:44～14:44</td>
<td align="right">0</td>
<td>這是這串結果的最後一點</td>
</tr>
<tr>
<td><strong>Range + Reduce Last</strong></td>
<td>從上面一串值取最後一點</td>
<td align="right"><strong>0</strong></td>
<td><code>0 &gt; 0</code> 為假，不符合觸發條件</td>
</tr>
<tr>
<td><strong>Range + Reduce Max</strong></td>
<td>從上面一串值取最大值</td>
<td align="right"><strong>1</strong></td>
<td><code>1 &gt; 0</code> 為真；Pending 為 0 時，當次可進 Alerting</td>
</tr>
<tr>
<td><strong>Instant：14:44</strong></td>
<td>13:44～14:44，只算當下這一點</td>
<td align="right"><strong>0</strong></td>
<td>不會因畫面顯示 <code>30m to now</code> 就回頭挑 14:14 的值</td>
</tr>
</tbody></table></div>

</section>
<!-- endtab -->

<!-- tab Evaluation、Pending、Keep firing for-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>Evaluation、Pending、Keep firing for</h2><p>13:30 的那筆錯誤已經被查到了，Alert 卻不一定立刻響起。它還要看，這個條件是偶爾出現一下，還是持續了一段時間。這時登場的是三個設定：多久檢查一次、要連續異常多久、恢復後又要觀察多久。</p></div>
<figure class="gd-visual" role="img" aria-label="Normal、Pending、Alerting、Recovering、Normal 的狀態轉換時間線" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 230" width="700" height="230" aria-hidden="true"><g font-family="Segoe UI, Microsoft JhengHei, sans-serif" font-size="15" fill="#cbc8d5"><text x="350" y="28" text-anchor="middle" fill="#eeeaf4" font-size="18">每次評估，決定下一個狀態</text><rect x="26" y="82" width="110" height="42" rx="3" fill="#30283e" opacity="1"/><text x="81" y="109" text-anchor="middle" fill="#91b7ff" font-size="14">Normal</text><text x="81" y="154" text-anchor="middle" fill="#aaa5b8" font-size="13">13:29</text><line x1="137" y1="103" x2="160" y2="103" stroke="#91829f" stroke-width="2" /><text x="155" y="98" text-anchor="middle" fill="#ffc619" font-size="20">›</text><rect x="163" y="82" width="110" height="42" rx="3" fill="#30283e" opacity="1"/><text x="218" y="109" text-anchor="middle" fill="#ffc619" font-size="14">Pending</text><text x="218" y="154" text-anchor="middle" fill="#aaa5b8" font-size="13">13:30</text><line x1="274" y1="103" x2="297" y2="103" stroke="#91829f" stroke-width="2" /><text x="292" y="98" text-anchor="middle" fill="#ffc619" font-size="20">›</text><rect x="300" y="82" width="110" height="42" rx="3" fill="#30283e" opacity="1"/><text x="355" y="109" text-anchor="middle" fill="#f45125" font-size="14">Alerting</text><text x="355" y="154" text-anchor="middle" fill="#aaa5b8" font-size="13">13:35</text><line x1="411" y1="103" x2="434" y2="103" stroke="#91829f" stroke-width="2" /><text x="429" y="98" text-anchor="middle" fill="#ffc619" font-size="20">›</text><rect x="437" y="82" width="110" height="42" rx="3" fill="#30283e" opacity="1"/><text x="492" y="109" text-anchor="middle" fill="#ffc619" font-size="14">Recovering</text><text x="492" y="154" text-anchor="middle" fill="#aaa5b8" font-size="13">15:00</text><line x1="548" y1="103" x2="571" y2="103" stroke="#91829f" stroke-width="2" /><text x="566" y="98" text-anchor="middle" fill="#ffc619" font-size="20">›</text><rect x="574" y="82" width="110" height="42" rx="3" fill="#30283e" opacity="1"/><text x="629" y="109" text-anchor="middle" fill="#91b7ff" font-size="14">Normal</text><text x="629" y="154" text-anchor="middle" fill="#aaa5b8" font-size="13">15:10</text><text x="350" y="202" text-anchor="middle" fill="#cbc8d5" font-size="14">Pending 等待異常持續；Recovering 等待恢復持續</text></g></svg></figure>

<p><code>Evaluation interval</code> 是檢查的節奏。設 <code>1m</code>，Grafana 就約每分鐘重跑查詢並重新判斷一次；這和圖表 Query options 的 <code>Interval</code> 各管各的。<code>Pending period</code> 則像一段觀察期。第一次符合門檻先從 Normal 進 Pending，持續符合到設定時間才進 Alerting；中途只要有一次不符合，就回 Normal。若設為 0，第一次符合就能進 Alerting。</p>
<p>已經進入 Alerting 之後，情況好轉了，還有 <code>Keep firing for</code>。它讓狀態先進 Recovering，確認恢復維持到設定時間，才轉 Normal／Resolved；期間若重新超標，就回 Alerting。設為 0 時，評估確認恢復即可解除。狀態仍是<strong>在評估時更新</strong>：每五分鐘才評估一次，即使 Keep firing for 只設一分鐘，也不會在沒有評估的那一分鐘自動確認恢復。</p>
<p>沿用上一分頁的單筆錯誤，看看這三個時間怎麼接力。以下全部是<strong>數值模擬</strong>：錯誤發生在 13:30，規則每分鐘評估；門檻是結果 <code>&gt; 0</code>，Pending 設 <code>5m</code>、Keep firing for 設 <code>10m</code>；Query 在沒有符合 log 時仍回傳數值 0。Range + Max 會讓較早的非零點留在最近半小時的結果裡，直到約 15:00 才不再符合。右欄另外比較改用 Instant + <code>[1h]</code> 時的時間線；實際查詢點對齊與狀態轉換仍以規則設定為準。</p>
<div class="gd-table-scroll" role="region" aria-label="Evaluation、Pending、Keep firing for資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>評估時間（約略）</th>
<th>Range + Max 的判斷</th>
<th>Range + Max 的狀態</th>
<th>若改用 Instant + <code>[1h]</code></th>
</tr>
</thead>
<tbody><tr>
<td>13:30</td>
<td>首次查到錯誤，結果 <code>&gt; 0</code></td>
<td>Normal → Pending</td>
<td>同樣進 Pending</td>
</tr>
<tr>
<td>13:31～13:34</td>
<td>每分鐘重查，條件仍成立</td>
<td>留在 Pending</td>
<td>同樣留在 Pending</td>
</tr>
<tr>
<td>13:35</td>
<td>已持續符合約五分鐘</td>
<td>Pending → Alerting</td>
<td>同樣進 Alerting</td>
</tr>
<tr>
<td>約 14:30</td>
<td>較早的查詢點仍可能含有 13:30 的錯誤</td>
<td>維持 Alerting</td>
<td>當下的一小時窗口已不含錯誤，進 Recovering</td>
</tr>
<tr>
<td>約 14:40</td>
<td>Range + Max 仍可能非零</td>
<td>維持 Alerting</td>
<td>持續恢復約十分鐘，轉 Normal／Resolved</td>
</tr>
<tr>
<td>約 15:00</td>
<td>最近半小時的查詢點不再含這筆錯誤</td>
<td>Alerting → Recovering</td>
<td>已是 Normal</td>
</tr>
<tr>
<td>約 15:10</td>
<td>持續恢復約十分鐘</td>
<td>Recovering → Normal／Resolved</td>
<td>維持 Normal</td>
</tr>
</tbody></table></div>

</section>
<!-- endtab -->

<!-- tab No data-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>No data</h2><p>錯誤消失後，監控畫面安靜了。這個安靜可能有兩種意思：查詢成功，明確算出 <strong>0 筆</strong>；或是查詢根本<strong>沒有回傳任何數值</strong>。對 Grafana Alert 來說，兩者走的是不同的路。</p></div>
<figure class="gd-visual" role="img" aria-label="查詢回傳數值零、整體無資料、單一 Pod 消失、查詢錯誤的分支圖" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 218" width="700" height="218" aria-hidden="true"><g font-family="Segoe UI, Microsoft JhengHei, sans-serif" font-size="15" fill="#cbc8d5"><text x="350" y="28" text-anchor="middle" fill="#eeeaf4" font-size="17">查詢結果先分流，才知道 Normal 代表什麼</text><rect x="270" y="53" width="160" height="38" rx="3" fill="#30283e" opacity="1"/><text x="350" y="78" text-anchor="middle" fill="#eeeaf4" font-size="14">Grafana 執行查詢</text><line x1="350" y1="91" x2="92" y2="126" stroke="#91829f" stroke-width="1.5" /><rect x="20" y="127" width="145" height="38" rx="3" fill="#252030" opacity="1"/><text x="92" y="152" text-anchor="middle" fill="#eeeaf4" font-size="14">數值 0</text><text x="92" y="192" text-anchor="middle" fill="#91b7ff" font-size="13">比較門檻</text><line x1="350" y1="91" x2="264" y2="126" stroke="#91829f" stroke-width="1.5" /><rect x="192" y="127" width="145" height="38" rx="3" fill="#252030" opacity="1"/><text x="264" y="152" text-anchor="middle" fill="#eeeaf4" font-size="14">整體無資料</text><text x="264" y="192" text-anchor="middle" fill="#ffc619" font-size="13">No Data</text><line x1="350" y1="91" x2="436" y2="126" stroke="#91829f" stroke-width="1.5" /><rect x="364" y="127" width="145" height="38" rx="3" fill="#252030" opacity="1"/><text x="436" y="152" text-anchor="middle" fill="#eeeaf4" font-size="14">少一個 Pod</text><text x="436" y="192" text-anchor="middle" fill="#ffc619" font-size="13">Missing Series</text><line x1="350" y1="91" x2="608" y2="126" stroke="#91829f" stroke-width="1.5" /><rect x="536" y="127" width="145" height="38" rx="3" fill="#252030" opacity="1"/><text x="608" y="152" text-anchor="middle" fill="#eeeaf4" font-size="14">查詢失敗</text><text x="608" y="192" text-anchor="middle" fill="#ffc619" font-size="13">Error</text></g></svg></figure>

<p>例如 Loki 的 <code>sum(count_over_time(...[1h]))</code>，完全沒有符合的 log 時，可能回傳空的 series，而不是數值 0。若規則設 <strong>No data → Normal</strong>，Grafana 會依這個設定處理狀態；它不是「先等 Keep firing for，確認持續恢復」的數值路徑。若要讓整個服務的合計在沒有匹配 log 時明確回傳 0，可以寫成：</p>
<pre><code class="language-bash">sum(count_over_time(
  {service=&quot;prod-promotion-service&quot;} |= &quot;錯誤&quot; [1h]
)) or vector(0)
</code></pre>
<p><code>or vector(0)</code> 適合這種合計為<strong>單一數字</strong>的情境。若查詢改成 <code>sum by (pod)</code> 或 <code>sum by (jobname)</code>，它不會替每個消失的 Pod 或 Job 各補一個 0。這時要再分辨：整個查詢都沒有資料，是 <strong>No Data</strong>；查詢仍有其他 Pod，只少了一個 Pod，是 <strong>Missing Series</strong>。查詢 timeout 或失敗則是 <strong>Error</strong>，<code>vector(0)</code> 也無法把失敗變成正常的 0。</p>
<p>再看多維度規則。若 <code>sum by (pod)</code> 回傳 Pod A、Pod B，Grafana 可以替兩個 Pod 分別判斷，A 是 Normal、B 是 Alerting；只用 <code>sum(...)</code>，則把數值合成整體再判斷。當某個 Pod 消失時，<code>Missing series evaluations to resolve = 2</code> 表示它連續缺席兩次評估後，舊的 alert instance 才被視為 stale、解除並移除。Pod 被替換也可能造成這種缺席。</p>
<p>因此畫面顯示 Normal，仍要回頭查原因：數值確實恢復、No Data 被設成 Normal、查詢錯誤被設成 Normal、某個 series 消失，或規則剛被修改，都可能讓狀態改變。State history 與 <code>grafana_state_reason</code> 可以協助辨認；No Data／Error 設為 Normal 時，走的是設定的狀態處理，不是一般門檻恢復的 Keep firing for 流程。</p>
<p>把「0、整體無資料、只少一個 Pod、查詢失敗」排在一起看。下表是<strong>模擬</strong>：每分鐘評估，門檻暫設 <code>&gt; 3</code>、Pending 設 0、No Data／Error 都設 Normal，Missing series 次數設 2。前兩列使用單一合計值，後面改用依 Pod 分組的查詢；兩種 Query 是用來比較行為，並非同一條線上規則同時切換。</p>
<div class="gd-table-scroll" role="region" aria-label="No data資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>查詢與時間</th>
<th>回傳情況</th>
<th>Grafana 走哪條路</th>
<th>畫面該怎麼讀</th>
</tr>
</thead>
<tbody><tr>
<td>整體合計，15:00</td>
<td>明確回傳數值 <code>0</code></td>
<td>正常比較門檻，<code>0 &gt; 3</code> 為假</td>
<td>Normal 是一次<strong>有數值</strong>的判斷</td>
</tr>
<tr>
<td>整體合計，15:01</td>
<td>查詢成功，卻沒有任何 series</td>
<td>走 <strong>No Data → Normal</strong> 的設定</td>
<td>同樣顯示 Normal，但沒有證明錯誤數是 0</td>
</tr>
<tr>
<td>依 Pod 分組，15:02</td>
<td>Pod A = 2、Pod B = 5</td>
<td>A 正常，B 因 <code>5 &gt; 3</code> 進 Alerting</td>
<td>一條規則有兩個 alert instances</td>
</tr>
<tr>
<td>依 Pod 分組，15:03</td>
<td>只回傳 Pod A = 2，Pod B 首次缺席</td>
<td>B 進入 Missing Series 的缺席計數</td>
<td>不能把 B 的消失直接當成 B = 0</td>
</tr>
<tr>
<td>依 Pod 分組，15:04</td>
<td>仍只回傳 Pod A，Pod B 第二次缺席</td>
<td>B 被視為 stale，舊 instance 解除並移除</td>
<td>可能是 Pod 替換，須查 State history</td>
</tr>
<tr>
<td>任一查詢，15:05</td>
<td>查詢 timeout</td>
<td>走 <strong>Error → Normal</strong> 的設定</td>
<td>Normal 不代表服務健康，只表示規則選擇這樣處理錯誤</td>
</tr>
</tbody></table></div>

</section>
<!-- endtab -->

<!-- tab 實際案例 1：MY Prod Cart-Service 的 Ingress 成功率 Alert-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>實際案例 1：MY Prod Cart-Service 的 Ingress 成功率 Alert</h2><p>MY Prod 的購物車入口還在回應請求，成功率卻慢慢往下掉。Alert 要抓的不是「曾經失敗過一次」，而是成功率是否持續低於 80%。先看它如何把每一筆請求換算成一個比例：</p></div>
<figure class="gd-visual" role="img" aria-label="15:00 到 15:04 成功率 75%，15:05 上升至 85%；觸發門檻為 80%" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 220" width="700" height="220" aria-hidden="true"><g font-family="Segoe UI, Microsoft JhengHei, sans-serif" font-size="15" fill="#cbc8d5"><text x="350" y="27" text-anchor="middle" fill="#eeeaf4" font-size="18">成功率持續低於 80%，三分鐘後進 Alerting</text><line x1="75" y1="166" x2="630" y2="166" stroke="#554a62" stroke-width="2" /><line x1="75" y1="50" x2="75" y2="166" stroke="#554a62" stroke-width="2" /><line x1="75" y1="106" x2="630" y2="106" stroke="#ff8c16" stroke-width="2" stroke-dasharray="6 5"/><text x="633" y="98" text-anchor="end" fill="#ffc619" font-size="13">門檻 80%</text><polyline points="75,121 186,121 297,121 408,121 519,121 630,91" fill="none" stroke="#91b7ff" stroke-width="3"/><circle cx="75" cy="121" r="6" fill="#ffc619"/><text x="75" y="108" text-anchor="middle" fill="#eeeaf4" font-size="14">75</text><text x="75" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:00</text><circle cx="186" cy="121" r="6" fill="#ffc619"/><text x="186" y="108" text-anchor="middle" fill="#eeeaf4" font-size="14">75</text><text x="186" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:01</text><circle cx="297" cy="121" r="6" fill="#ffc619"/><text x="297" y="108" text-anchor="middle" fill="#eeeaf4" font-size="14">75</text><text x="297" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:02</text><circle cx="408" cy="121" r="6" fill="#f45125"/><text x="408" y="108" text-anchor="middle" fill="#eeeaf4" font-size="14">75</text><text x="408" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:03</text><circle cx="519" cy="121" r="6" fill="#f45125"/><text x="519" y="108" text-anchor="middle" fill="#eeeaf4" font-size="14">75</text><text x="519" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:04</text><circle cx="630" cy="91" r="6" fill="#91b7ff"/><text x="630" y="78" text-anchor="middle" fill="#eeeaf4" font-size="14">85</text><text x="630" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:05</text></g></svg></figure>

<pre><code class="language-promql">sum by (ingress) (
  rate(nginx_ingress_controller_requests{
    status!~&quot;[4-5].*&quot;, exported_namespace=&quot;prod-cart-service&quot;
  }[2m])
)
/
sum by (ingress) (
  rate(nginx_ingress_controller_requests{
    exported_namespace=&quot;prod-cart-service&quot;
  }[2m])
)
</code></pre>
<p>分母是全部請求速率；分子排除狀態碼以 4、5 開頭的請求，所以這裡的「成功」依查詢定義也包含 3xx 等狀態碼。兩邊各自按 <code>ingress</code> 分組，再相除。結果 <code>0.75</code> 就是 75%，每個 ingress 都有自己的數值與 Alert instance。</p>
<p>有了比例，還要問「拿哪個時間的比例來判斷」。查詢 A 取最近 15 分鐘的一串點，串中每一點用 <code>[2m]</code> 回看前兩分鐘；B 只取最後的有效值，C 再比較是否 <code>&lt; 0.8</code>。規則每分鐘重跑一次，低於門檻要持續三分鐘，才真的進 Alerting。</p>
<details class="gd-details"><summary>查看完整規則設定</summary><div class="gd-table-scroll" role="region" aria-label="實際案例 1：MY Prod Cart-Service 的 Ingress 成功率 Alert資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>設定</th>
<th>本例的值</th>
<th>意義</th>
</tr>
</thead>
<tbody><tr>
<td>A 的 Query type</td>
<td>Range</td>
<td>每次評估取最近 15 分鐘的一串成功率點</td>
</tr>
<tr>
<td>A 的 Relative time range</td>
<td><code>15m to now</code></td>
<td>決定這串點的時間範圍，不是「成功率統計 15 分鐘」</td>
</tr>
<tr>
<td>PromQL 的 <code>[2m]</code></td>
<td>2 分鐘</td>
<td><strong>每個點</strong>各自往前 2 分鐘計算 <code>rate</code></td>
</tr>
<tr>
<td>A 的 <code>intervalMs</code>／<code>maxDataPoints</code></td>
<td><code>15000</code>／<code>43200</code></td>
<td>查詢採樣相關參數；不是 Alert 每 15 秒評估，也不是一定產生 43,200 點</td>
</tr>
<tr>
<td>Evaluation group interval</td>
<td>1 分鐘</td>
<td>Grafana 約每分鐘重新執行 A → B → C</td>
</tr>
<tr>
<td>B：Reduce</td>
<td><code>Last</code>，忽略非數值</td>
<td>每個 ingress 只拿這串點最後一個可用數值</td>
</tr>
<tr>
<td>C：Threshold</td>
<td><code>&lt; 0.8</code></td>
<td>B 的值<strong>低於</strong> 80% 才符合門檻；恰好 80% 不符合 <code>&lt;</code></td>
</tr>
<tr>
<td>Pending period</td>
<td>3 分鐘</td>
<td>持續符合門檻約 3 分鐘後才由 Pending 進 Alerting</td>
</tr>
<tr>
<td>Keep firing for</td>
<td>0 秒</td>
<td>條件恢復時，不另等 Recovering 時間</td>
</tr>
</tbody></table></div></details>
<p>規則資料中的 B、C 也帶有 <code>relativeTimeRange: 1h to now</code>，但它們只是處理 A 的結果，<strong>A 實際查詢範圍仍是 15 分鐘</strong>。<code>intervalMs = 15000</code> 和 <code>maxDataPoints = 43200</code> 是查詢採樣參數，也不代表 Alert 每十五秒評估一次。</p>
<h3 class="gd-section">狀態確認後，通知才開始計時</h3>
<p>這條規則另外設定了通知節奏：<code>Group wait = 5s</code>、<code>Group interval = 30s</code>、<code>Repeat interval = 1m</code>。它們在 Alert 進入 Alerting 後才接手，不會縮短三分鐘的 Pending。新群組先等五秒再送第一則通知；後續群組若有新增或解除的 Alert，以三十秒的週期處理變化；如果群組沒有變化、仍在 firing，約一分鐘後才考慮重送提醒。實際通知還受路由與群組排程影響。</p>
<div class="gd-table-scroll" role="region" aria-label="實際案例 1：MY Prod Cart-Service 的 Ingress 成功率 Alert資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>設定</th>
<th>控制的事</th>
<th>本例</th>
</tr>
</thead>
<tbody><tr>
<td>Evaluation interval</td>
<td>多久重新執行查詢與條件判斷</td>
<td>每 1 分鐘</td>
</tr>
<tr>
<td>Pending period</td>
<td>條件持續符合多久，才從 Pending 進入 Alerting</td>
<td>3 分鐘</td>
</tr>
<tr>
<td>Keep firing for</td>
<td>條件恢復後，Alert 還要維持 firing 多久</td>
<td>0 秒；下一次確認恢復時可轉 Normal／Resolved</td>
</tr>
<tr>
<td>Group wait</td>
<td><strong>新通知群組</strong>成立後，首次發送前等待多久</td>
<td>5 秒；期間可合併其他 Alert</td>
</tr>
<tr>
<td>Group interval</td>
<td>首次通知後，檢查群組是否有<strong>新增或解除的 Alert</strong>，並通知變化的週期</td>
<td>30 秒</td>
</tr>
<tr>
<td>Repeat interval</td>
<td>群組<strong>沒有變化且仍有 firing Alert</strong> 時，隔多久重送提醒</td>
<td>1 分鐘；依 Group interval 的週期檢查</td>
</tr>
</tbody></table></div>
<p>這裡最要分開的是 <code>Repeat interval</code> 與 <code>Keep firing for</code>。前者問「還在 firing 時，多久再提醒一次？」後者問「條件恢復後，多久才解除？」這條規則 Keep firing for 設 0，所以評估確認跨過恢復門檻 <code>&gt; 0.8</code> 時，就可轉 Normal／Resolved；解除通知屬於群組變化，不是 Repeat 提醒。</p>
<h3 class="gd-section">從成功率下降走到通知</h3>
<p>下面是<strong>模擬</strong>，假設剛好在每分鐘整點評估，通知群組原本只有 <code>cart-web-api</code>，15:00 首次得到 75%，之後持續低於 80%。每次 A 都重新查最近十五分鐘的一串點，B 再取最後有效點；表中的兩分鐘窗口，指的是該最後點約略回看的資料。通知時間只是便於理解的估計，並非這條規則的歷史紀錄。</p>
<div class="gd-table-scroll" role="region" aria-label="實際案例 1：MY Prod Cart-Service 的 Ingress 成功率 Alert資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>時間</th>
<th>最後一點約回看</th>
<th>查詢值與狀態</th>
<th>通知群組會做什麼</th>
</tr>
</thead>
<tbody><tr>
<td>15:00</td>
<td>14:58～15:00</td>
<td>75%，首次低於 80%；Normal → Pending</td>
<td>尚未通知</td>
</tr>
<tr>
<td>15:01</td>
<td>14:59～15:01</td>
<td>再次低於 80%；維持 Pending</td>
<td>尚未通知</td>
</tr>
<tr>
<td>15:02</td>
<td>15:00～15:02</td>
<td>再次低於 80%；維持 Pending</td>
<td>尚未通知</td>
</tr>
<tr>
<td>15:03</td>
<td>15:01～15:03</td>
<td>仍低於 80%，Pending 約滿三分鐘；進 Alerting</td>
<td>新通知群組開始等五秒</td>
</tr>
<tr>
<td>約 15:03:05</td>
<td>沒有新增查詢；沿用 15:03 的狀態</td>
<td>仍在 Alerting</td>
<td>可發出第一次 firing 通知</td>
</tr>
<tr>
<td>約 15:03:35</td>
<td>尚未到下一次假設中的狀態變化</td>
<td>若群組沒有變化</td>
<td>Group interval 到點，但不必為不變內容送變更通知</td>
</tr>
<tr>
<td>約 15:04:05 起</td>
<td>15:04 已重新評估，假設仍低於 80%</td>
<td>仍在 Alerting</td>
<td>若群組沒有變化，達 Repeat interval 後可在通知週期重送提醒</td>
</tr>
<tr>
<td>15:05</td>
<td>15:03～15:05</td>
<td>假設最新值升至 85%，跨過恢復門檻；轉 Normal／Resolved</td>
<td>後續依通知週期處理解除通知，不再為這個已解除的 instance 重送 firing 提醒</td>
</tr>
</tbody></table></div>

</section>
<!-- endtab -->

<!-- tab 實際案例 2 ：Shopping Service Exception Alert-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>實際案例 2 ：Shopping Service Exception Alert</h2><p>購物服務偶爾出現一筆例外，不一定值得立刻驚動值班人員；同一種錯誤密集出現，情況就不同了。這條規則想抓的，正是「最近十分鐘內，某一種例外訊息是否超過三十筆」。</p></div>
<figure class="gd-visual" role="img" aria-label="15:00 為 29 筆，15:05 為 31 筆超過 30，15:10 降至 20 筆的門檻圖" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 220" width="700" height="220" aria-hidden="true"><g font-family="Segoe UI, Microsoft JhengHei, sans-serif" font-size="15" fill="#cbc8d5"><text x="350" y="25" text-anchor="middle" fill="#eeeaf4" font-size="18">同一組例外訊息，每 5 分鐘重新計數</text><line x1="85" y1="166" x2="635" y2="166" stroke="#554a62" stroke-width="2" /><line x1="85" y1="70" x2="635" y2="70" stroke="#ff8c16" stroke-width="2" stroke-dasharray="6 5"/><text x="630" y="62" text-anchor="end" fill="#ffc619" font-size="13">門檻：大於 30</text><rect x="148" y="73.19999999999999" width="64" height="92.80000000000001" rx="3" fill="#91b7ff" opacity="0.86"/><text x="180" y="62.19999999999999" text-anchor="middle" fill="#eeeaf4" font-size="17">29</text><text x="180" y="193" text-anchor="middle" fill="#cbc8d5" font-size="15">15:00</text><rect x="318" y="66.8" width="64" height="99.2" rx="3" fill="#f45125" opacity="0.86"/><text x="350" y="55.8" text-anchor="middle" fill="#eeeaf4" font-size="17">31</text><text x="350" y="193" text-anchor="middle" fill="#cbc8d5" font-size="15">15:05</text><rect x="488" y="102" width="64" height="64" rx="3" fill="#91b7ff" opacity="0.86"/><text x="520" y="91" text-anchor="middle" fill="#eeeaf4" font-size="17">20</text><text x="520" y="193" text-anchor="middle" fill="#cbc8d5" font-size="15">15:10</text></g></svg></figure>

<p>它先從 <code>prod-shopping-service</code> 的 <code>shopping-web-api</code>、<code>exception_logs</code> 撈 log，排除「購物車資料過期」與兩種點數錯誤，再用 JSON 解析 <code>_ext</code> 與 <code>_msg</code>。<code>sum by (_ext, _msg)</code> 把<strong>例外類型與完整訊息都相同</strong>的 log 放在一起。因此同一類型若帶著不同訊息，會分開計數。尾端的 <code>or on() vector(0)</code> 只在整個查詢沒有匹配序列時補 0，並不會替每個消失的訊息組合各補一個 0。</p>
<p>時間接著分成三層。Evaluation group <code>Shopping5mQuery10m</code> 每<strong>五分鐘</strong>重新評估；Query A 的 Range 是 <code>10m to now</code>，會取一串點；串中的每一點又用 <code>count_over_time(...[10m])</code> 各自回看十分鐘。條件 B 是 Classic condition，對每組結果取 <strong>Last</strong>，只要有一組 <strong><code>&gt; 30</code></strong> 就觸發。Classic condition 最後只形成<strong>一個</strong> Alert instance，不會每種例外訊息各送一個 Alert。</p>
<p>Pending 與 Keep firing for 都設為 0。也就是說，評估時首次發現某組超過三十筆，就可進 Alerting；下一次評估確認條件不成立，就可解除。No Data 與查詢 Error 都設為 Normal，看到 Normal 時仍要區分是數值真的下降，還是走了無資料或錯誤的設定。</p>
<p>這條規則沒有自行覆寫通知時間。匹配的通知路由送往 <code>#shopping-rd-sg-maintain</code>，Group wait 是五秒、Group interval 是三十秒；該路由沒有顯示 Repeat interval 的覆寫值。這些是通知的節奏，並不會讓規則改成每三十秒評估一次。</p>
<p>沿著同一組 <code>_ext</code>、<code>_msg</code> 看三次評估。下表的筆數是<strong>模擬</strong>，時間假設剛好落在整五分鐘；每列都重新查詢，而相鄰的十分鐘窗口會重疊五分鐘，不能把 29、31、20 加起來當作總數。最後兩列另外假設把 Keep firing for 改成一分鐘，只用來看評估頻率的影響，<strong>不是這條規則目前的設定</strong>。</p>
<div class="gd-table-scroll" role="region" aria-label="實際案例 2 ：Shopping Service Exception Alert資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>時間與設定</th>
<th>最後一點約回看</th>
<th align="right">該組筆數</th>
<th>狀態如何走</th>
</tr>
</thead>
<tbody><tr>
<td>15:00，目前設定</td>
<td>14:50～15:00</td>
<td align="right">29</td>
<td><code>29 &gt; 30</code> 為假，維持 Normal</td>
</tr>
<tr>
<td>15:05，目前設定</td>
<td>14:55～15:05</td>
<td align="right">31</td>
<td><code>31 &gt; 30</code> 為真，Pending 為 0，當次進 Alerting</td>
</tr>
<tr>
<td>15:10，目前設定</td>
<td>15:00～15:10</td>
<td align="right">20</td>
<td>首次評估發現恢復，Keep firing for 為 0，轉 Normal／Resolved</td>
</tr>
<tr>
<td>15:10，<strong>假設</strong> Keep firing for 改為 <code>1m</code></td>
<td>15:00～15:10</td>
<td align="right">20</td>
<td>先進 Recovering，開始計算恢復時間</td>
</tr>
<tr>
<td>15:11，延續上述假設</td>
<td>沒有重新評估</td>
<td align="right">無新數值</td>
<td>即使滿一分鐘，也不能在此刻確認恢復或更新狀態</td>
</tr>
<tr>
<td>15:15，延續上述假設</td>
<td>15:05～15:15</td>
<td align="right">假設仍未超標</td>
<td>再次評估確認恢復，才轉 Normal／Resolved</td>
</tr>
</tbody></table></div>

</section>
<!-- endtab -->

<!-- tab 實際案例 3 ：Promotion Service Exception Alert 的 Range 與 Last-->
<section class="grafana-dusk">
<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>實際案例 3 ：Promotion Service Exception Alert 的 Range 與 Last</h2><p>這條 Promotion Alert 的名字寫著「30 秒間隔」，查詢畫面裡卻同時出現 <code>1h to now</code> 和 <code>[30s]</code>。三個時間放在一起，看似互相拉扯，其實各有工作：<strong>每三十秒重新評估</strong>，<strong>每次取最近一小時的一串結果</strong>，而<strong>串中的每個點只回看三十秒 log</strong>。</p></div>
<figure class="gd-visual" role="img" aria-label="14:59:30 為 12 筆，14:59:45 為 15 筆，15:00 最後值 8 筆，15:00:30 最後值 11 筆，15:01 為 6 筆" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 220" width="700" height="220" aria-hidden="true"><g font-family="Segoe UI, Microsoft JhengHei, sans-serif" font-size="15" fill="#cbc8d5"><text x="350" y="27" text-anchor="middle" fill="#eeeaf4" font-size="18">Last 取最後一點，不會挑前面的最高值</text><line x1="75" y1="166" x2="630" y2="166" stroke="#554a62" stroke-width="2" /><line x1="75" y1="50" x2="75" y2="166" stroke="#554a62" stroke-width="2" /><line x1="75" y1="107.66666666666666" x2="630" y2="107.66666666666666" stroke="#ff8c16" stroke-width="2" stroke-dasharray="6 5"/><text x="633" y="99.66666666666666" text-anchor="end" fill="#ffc619" font-size="13">門檻 10</text><polyline points="75,96 213.75,78.5 352.5,119.33333333333334 491.25,101.83333333333333 630,131" fill="none" stroke="#91b7ff" stroke-width="3"/><circle cx="75" cy="96" r="6" fill="#91b7ff"/><text x="75" y="83" text-anchor="middle" fill="#eeeaf4" font-size="14">12</text><text x="75" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:59:30</text><circle cx="213.75" cy="78.5" r="6" fill="#91b7ff"/><text x="213.75" y="65.5" text-anchor="middle" fill="#eeeaf4" font-size="14">15</text><text x="213.75" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">14:59:45</text><circle cx="352.5" cy="119.33333333333334" r="6" fill="#ffc619"/><text x="352.5" y="106.33333333333334" text-anchor="middle" fill="#eeeaf4" font-size="14">8</text><text x="352.5" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:00</text><circle cx="491.25" cy="101.83333333333333" r="6" fill="#f45125"/><text x="491.25" y="88.83333333333333" text-anchor="middle" fill="#eeeaf4" font-size="14">11</text><text x="491.25" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:00:30</text><circle cx="630" cy="131" r="6" fill="#91b7ff"/><text x="630" y="118" text-anchor="middle" fill="#eeeaf4" font-size="14">6</text><text x="630" y="193" text-anchor="middle" fill="#cbc8d5" font-size="13">15:01</text></g></svg></figure>

<p>查詢 A 從 Promotion Service 的 exception log 計數，條件 B 使用 Classic condition：每條結果序列取 <code>Last</code>，只要有一條 <strong><code>&gt; 10</code></strong>，就符合門檻。Pending 和 Keep firing for 都設 0；No Data、查詢 Error 都設為 Normal。這條規則沒有自行設定通知時間；匹配的路由送往 <code>#promotion-service-rd-sg-maintain</code>，Group wait 為五秒、Group interval 為三十秒，沒有顯示 Repeat interval 覆寫值。通知的三十秒與評估的三十秒是兩個不同計時器。</p>
<p>現在沿著一次評估往回走。假設 15:00:00 開始，A 取約 14:00～15:00 的查詢點。最早的點若也要往前數三十秒，Loki 可能得讀到約 13:59:30 的 log；但這<strong>不是</strong>把一小時的 log 全加成一個數字。B 只看各條序列的最後可用值，不會把沿途的 12、15、8 相加，也不是挑最大的 15。</p>
<p>這裡還有一個值得先看清的欄位問題。原查詢寫 <code>| json _ext=&quot;_ext&quot;</code>，只抽出了例外類型 <code>_ext</code>，後面卻寫 <code>sum by (_ext, _msg)</code>。以同一批實際 log 對照，指定欄位的解析只回傳 <code>_ext</code> label；改用 <code>| json</code> 才同時得到 <code>_ext</code>、<code>_msg</code>。因此現行查詢實際按<strong>例外類型</strong>計數，沒有再依訊息內容拆分。這是查詢結果的驗證，不代表線上規則已被修改。</p>
<p><code>Last</code> 也有資料缺口要留意。某種 <code>_ext</code> 在一小時內曾有值，卻在最後幾個查詢點消失時，最後可用值未必代表評估當下的三十秒。<code>or on() vector(0)</code> 只在整體沒有匹配序列時補 0，不會替每個消失的 <code>_ext</code> 各補一個 0。遇到這種情況，應看 A 回傳的實際序列與 B 取出的值，再判讀觸發原因。</p>
<p>最後用一條<strong>每個列出的查詢點都有值</strong>的示意序列走完判斷。表中僅摘出 A 的幾個點，實際 A 在一小時內還會有其他點；評估假設剛好落在表中的時間，筆數不是線上歷史紀錄。</p>
<div class="gd-table-scroll" role="region" aria-label="實際案例 3 ：Promotion Service Exception Alert 的 Range 與 Last資料表" tabindex="0"><table class="gd-table">
<thead>
<tr>
<th>評估與查詢點</th>
<th>該點約回看的 log</th>
<th align="right">同一 <code>_ext</code> 的筆數</th>
<th>B 與 Alert 如何判斷</th>
</tr>
</thead>
<tbody><tr>
<td>15:00 評估時，A 的 14:59:30 點</td>
<td>14:59:00～14:59:30</td>
<td align="right">12</td>
<td>先留在 A 的序列中，還不是 B 選出的最後值</td>
</tr>
<tr>
<td>同次評估，A 的 14:59:45 點</td>
<td>14:59:15～14:59:45</td>
<td align="right">15</td>
<td>比前一點高，但 B 設的是 Last，並非 Max</td>
</tr>
<tr>
<td>同次評估，A 的 <strong>15:00:00 點</strong></td>
<td>14:59:30～15:00:00</td>
<td align="right"><strong>8</strong></td>
<td>B 取 <strong>Last = 8</strong>；<code>8 &gt; 10</code> 為假，維持 Normal</td>
</tr>
<tr>
<td><strong>15:00:30 再評估</strong>，取新的一串 A</td>
<td>最後點約看 15:00:00～15:00:30</td>
<td align="right"><strong>11</strong></td>
<td>B 取 <strong>Last = 11</strong>；<code>11 &gt; 10</code> 為真，Pending 為 0，進 Alerting</td>
</tr>
<tr>
<td><strong>15:01:00 再評估</strong></td>
<td>最後點約看 15:00:30～15:01:00</td>
<td align="right">假設降為 <strong>6</strong></td>
<td><code>6 &gt; 10</code> 為假，Keep firing for 為 0，可轉 Normal／Resolved</td>
</tr>
</tbody></table></div>

</section>


<!-- endtab -->

{% endtabs %}
