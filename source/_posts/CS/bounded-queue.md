---
title: Bounded Queue
date: 2026-09-13 10:40:00
categories: CS
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/cs/queue.png
cover: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/cs/queue.png
tags:
toc:
toc_number:
comments:
---

{% tabs Bounded Queue %}

<!-- tab 應用時機 -->

<style>
.wp{display:block;font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,'PingFang TC','Microsoft JhengHei',sans-serif;background:radial-gradient(700px 400px at 90% -5%,rgba(255,182,72,.18),transparent 60%),radial-gradient(900px 500px at -5% 10%,rgba(124,108,247,.1),transparent 55%),#fbf9f4;color:#1f2430!important;line-height:1.75;border-radius:20px;padding:1px 0 28px;margin:0 0 20px;overflow:hidden;--ink:#1f2430;--sub:#5b6472;--line:#ece7dc;--brand:#ff6b4a;--brand2:#ffb648;--teal:#12a594;--shadow:0 10px 30px -12px rgba(31,36,48,.15)}
.wp *{box-sizing:border-box}.wp .wp-hero{padding:48px 6vw 34px;text-align:center}.wp .wp-eyebrow{display:inline-block;font-size:.78rem;letter-spacing:.14em;color:var(--brand)!important;font-weight:700;background:rgba(255,107,74,.1);padding:6px 14px;border-radius:999px}.wp h1{font-size:1.8rem;margin:12px 0;color:var(--ink)!important}.wp .wp-hero p{color:var(--sub)!important;max-width:720px;margin:auto}.wp .wp-badges{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:20px}.wp .wp-badge{background:#fff;border:1px solid var(--line);padding:6px 14px;border-radius:999px;font-size:.8rem;color:var(--sub)!important;box-shadow:var(--shadow)}.wp .wp-container{padding:0 5vw}.wp section{margin-bottom:42px}.wp .wp-section-head{display:flex;align-items:center;gap:12px;margin-bottom:16px}.wp .wp-chip{flex:none;width:38px;height:38px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-weight:800;background:linear-gradient(135deg,#1f2430,#485068);color:#fff!important}.wp .wp-section-head.ok .wp-chip{background:linear-gradient(135deg,#12a594,#5ee6bf)}.wp .wp-section-head.warn .wp-chip{background:linear-gradient(135deg,#ff6b4a,#ffb648)}.wp .wp-section-head.purple .wp-chip{background:linear-gradient(135deg,#7c6cf7,#a78bfa)}.wp h2{margin:0;font-size:1.3rem;color:var(--ink)!important}.wp h3{font-size:1.08rem;margin:26px 0 10px;color:var(--ink)!important;border-left:4px solid var(--brand);padding-left:10px}.wp p{color:var(--sub)!important}.wp .wp-card,.wp .wp-evidence{background:#fff;border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);padding:18px 22px;margin:14px 0}.wp .wp-callout{border-radius:16px;padding:18px 22px;margin:18px 0;border:1px solid transparent;display:flex;gap:14px}.wp .wp-callout .wp-icon{flex:none;font-size:1.3rem}.wp .info{background:#eff6ff;border-color:#bfdbfe}.wp .warn{background:#fffbeb;border-color:#fde68a}.wp .danger{background:#fef2f2;border-color:#fecaca}.wp .ok{background:#ecfdf5;border-color:#a7f3d0}.wp .wp-callout p{margin:0;color:#3b4150!important}.wp code{font-family:Consolas,'SFMono-Regular',monospace;background:#f1eee6!important;color:#c2410c!important;padding:2px 7px;border-radius:6px;font-size:.88em;border:1px solid #e9e3d5}.wp .wp-summary-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:18px 0}.wp .wp-box{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px;box-shadow:var(--shadow);border-top:4px solid var(--brand)}.wp .wp-box:nth-child(2){border-top-color:var(--brand2)}.wp .wp-box:nth-child(3){border-top-color:var(--teal)}.wp .wp-box h4{margin:0 0 8px;color:var(--ink)!important}.wp .wp-box p{margin:0;font-size:.9rem}.wp .wp-steps{display:flex;flex-direction:column;gap:14px;margin:16px 0 22px}.wp .wp-stepcard{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 20px 16px 60px;position:relative;box-shadow:var(--shadow)}.wp .wp-stepnum{position:absolute;left:16px;top:16px;width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff!important;font-weight:800;display:flex;align-items:center;justify-content:center}.wp .wp-step-title{font-weight:700;color:var(--ink)!important}.wp .wp-stepcard p{margin:6px 0;font-size:.9rem}.wp .wp-checklist{list-style:none;padding:0;margin:16px 0}.wp .wp-checklist li{position:relative;padding:10px 0 10px 34px;border-bottom:1px dashed var(--line);color:var(--sub)!important}.wp .wp-checklist li:before{content:'✓';position:absolute;left:0;top:11px;width:22px;height:22px;border-radius:7px;background:#dcfce7;color:#15803d;display:flex;align-items:center;justify-content:center;font-weight:900}.wp table{width:100%;border-collapse:separate;border-spacing:0;background:#fff!important;border:1px solid var(--line);border-radius:16px;overflow:hidden;margin:14px 0 22px;font-size:.9rem;box-shadow:var(--shadow)}.wp th{background:#f3f0e8!important;color:var(--ink)!important;text-align:left;padding:13px 16px;border-bottom:1px solid var(--line)}.wp td{padding:13px 16px;border-bottom:1px solid var(--line);color:#3b4150!important;vertical-align:top}.wp tr:last-child td{border-bottom:none}.wp pre.wp-pre{background:#1c1f2b!important;border-radius:16px;padding:20px 22px;overflow-x:auto;color:#e9ecf7!important;font:.85rem/1.7 Consolas,monospace;white-space:pre!important;box-shadow:var(--shadow)}.wp footer{text-align:center;padding:24px 5vw 6px;color:var(--sub)!important;font-size:.82rem;border-top:1px solid var(--line)}
@media(max-width:780px){.wp .wp-summary-grid{grid-template-columns:1fr}.wp .wp-container{padding:0 6vw}.wp .wp-hero{padding-left:6vw;padding-right:6vw}}
.wp .wp-section-head.warn,.wp .wp-section-head.ok{background:transparent}
.wp .wp-library-table{table-layout:fixed}.wp .wp-library-table th:nth-child(1),.wp .wp-library-table td:nth-child(1){width:12%}.wp .wp-library-table th:nth-child(2),.wp .wp-library-table td:nth-child(2){width:43%}.wp .wp-library-table th:nth-child(3),.wp .wp-library-table td:nth-child(3){width:45%}.wp .wp-library-table td{overflow-wrap:anywhere}
.wp .wp-detail{background:#fff;border:1px solid var(--line);border-radius:14px;margin:12px 0;box-shadow:var(--shadow);overflow:hidden}.wp .wp-detail summary{cursor:pointer;list-style:none;padding:15px 20px;font-weight:800;color:var(--ink)}.wp .wp-detail summary::-webkit-details-marker{display:none}.wp .wp-detail summary:before{content:'＋';display:inline-block;color:var(--brand);margin-right:10px;font-weight:900}.wp .wp-detail[open] summary:before{content:'−'}.wp .wp-detail-body{padding:0 20px 16px;border-top:1px solid var(--line)}.wp .wp-detail-body p{margin:12px 0}
.wp .wp-causal-timeline{position:relative;margin:22px 0 26px;padding-left:38px}.wp .wp-causal-timeline:before{content:'';position:absolute;left:10px;top:6px;bottom:6px;width:3px;background:repeating-linear-gradient(180deg,#c8c0b3 0 9px,transparent 9px 17px)}.wp .wp-causal-event{position:relative;margin-bottom:18px}.wp .wp-causal-event:last-child{margin-bottom:0}.wp .wp-causal-event:before{content:'';position:absolute;left:-34px;top:17px;width:14px;height:14px;border-radius:50%;background:#485068;border:3px solid #fbf9f4;box-shadow:0 0 0 2px #485068}.wp .wp-causal-event.warn:before{background:#ffb648;box-shadow:0 0 0 2px #d99a2b}.wp .wp-causal-event.danger:before{background:#e5484d;box-shadow:0 0 0 2px #c9343b}.wp .wp-causal-event .wp-causal-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 18px;box-shadow:var(--shadow)}.wp .wp-causal-event.warn .wp-causal-card{border-left:4px solid #ffb648}.wp .wp-causal-event.danger .wp-causal-card{border-left:4px solid #e5484d}.wp .wp-causal-title{font-weight:800;color:var(--ink)!important}.wp .wp-causal-card p{margin:5px 0 0;font-size:.9rem}.wp .wp-causal-label{display:inline-block;margin-right:8px;color:var(--sub)!important;font:700 .72rem Consolas,monospace;letter-spacing:.05em}
.wp .wp-usecase-table{table-layout:fixed}.wp .wp-usecase-table th:nth-child(1),.wp .wp-usecase-table td:nth-child(1){width:18%}.wp .wp-usecase-table th:nth-child(2),.wp .wp-usecase-table td:nth-child(2){width:27%}.wp .wp-usecase-table th:nth-child(3),.wp .wp-usecase-table td:nth-child(3){width:30%}.wp .wp-usecase-table th:nth-child(4),.wp .wp-usecase-table td:nth-child(4){width:25%}.wp .wp-usecase-table td{overflow-wrap:anywhere}.wp .wp-usecase-table tbody tr td:first-child{font-weight:800;color:var(--ink)!important;border-left:4px solid var(--brand)}.wp .wp-usecase-table tbody tr:nth-child(2) td:first-child{border-left-color:var(--brand2)}.wp .wp-usecase-table tbody tr:nth-child(3) td:first-child{border-left-color:var(--teal)}
.wp .wp-decision{margin:20px 0}.wp .wp-decision-root{width:max-content;max-width:100%;margin:0 auto 26px;background:#fff;border:2px solid var(--brand);border-radius:16px;padding:12px 24px;text-align:center;font-weight:800;color:var(--ink);box-shadow:var(--shadow);position:relative}.wp .wp-decision-root:after{content:'↓';position:absolute;left:50%;bottom:-28px;color:var(--violet);font-size:1.3rem}.wp .wp-decision-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}.wp .wp-decision-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px;box-shadow:var(--shadow)}.wp .wp-decision-question{display:inline-block;background:#f3f0e8;border-radius:999px;padding:4px 12px;font-weight:800;color:var(--ink);margin-bottom:12px}.wp .wp-decision-option{border-left:4px solid var(--teal);padding:9px 0 9px 14px;margin:8px 0;color:var(--sub)}.wp .wp-decision-option strong{color:var(--ink)}.wp .wp-decision-option em{display:block;font-style:normal;font-size:.86rem;color:var(--sub)}
@media(max-width:780px){.wp .wp-decision-grid{grid-template-columns:1fr}}
</style>

<div class="wp">
<div class="wp-hero">
<span class="wp-eyebrow">Concurrency · Backpressure</span>
<h1>當資料來得比處理速度快</h1>
<p>有界佇列把等待中的資料量限制在可預測範圍內。系統必須在排隊、拒絕、丟棄或阻塞之間做出明確選擇，才能避免短暫流量把整台服務拖垮。</p>
<div class="wp-badges"><span class="wp-badge">容量有限</span><span class="wp-badge">背壓可見</span><span class="wp-badge">失敗策略明確</span></div>
</div>
<div class="wp-container">
<section>
<div class="wp-section-head"><div class="wp-chip">01</div><h2>什麼時候需要 Bounded Queue</h2></div>
<table class="wp-usecase-table"><thead><tr><th>觸發情境</th><th>沒有容量邊界時</th><th>Bounded Queue 的作用</th><th>必須接受的代價</th></tr></thead><tbody>
<tr><td>供需速率嚴重不對稱</td><td>前端 API 閘道器每秒湧入 <code>50,000</code> 筆請求，但後端資料庫每秒最多只能寫入 <code>3,000</code> 筆，等待資料持續增加。</td><td>搭配 Kafka 的非同步削峰填谷，也就是 Asynchronous Write 或 Queue based Load Leveling，暫時吸收上游與下游的速率落差。</td><td>使用者點完按鈕後無法立刻在資料庫看到結果，必須等待系統非同步消化完畢。佇列只能吸收短期尖峰，不是永久產能。</td></tr>
<tr><td>預防 OOM</td><td>雙 11、跨年、股市開盤、搶票，或下游第三方 API 變慢時，無界佇列持續成長，可能造成 <code>OutOfMemoryError</code>。</td><td>固定容量限制等待中的資料，讓記憶體上限、滿載行為與失敗範圍可以事先定義。</td><td>容量到頂後仍必須拒絕、丟棄、阻塞或持久化，無法同時保留所有資料並維持無限流量。</td></tr>
<tr><td>外部服務有頻率限制</td><td>黑貓物流 API、金流刷卡閘道、Twilio 簡訊與 OpenAI API 可能限制每秒呼叫 <code>100</code> 次，超過就鎖 IP、罰款或直接報錯。</td><td>建立固定大小的佇列，由固定數量的執行緒，例如 <code>10</code> 個 Worker，依序取出任務呼叫外部 API。</td><td>超過處理能力的請求需要等待或被拒絕，不能讓所有請求立即通過。</td></tr>
</tbody></table>
<div class="wp-callout info"><span class="wp-icon">💡</span><p><strong>核心界線：</strong>入列成功只代表資料進入等待區，不代表資料已經寫入資料庫。若需要讓使用者立即知道永久寫入結果，就不應只用非同步佇列取代同步確認。</p></div>
</section>

<section>
<div class="wp-section-head warn"><div class="wp-chip">02</div><h2>容量用盡時的處理策略</h2></div>
<p>以下是彼此獨立的滿載處理策略，不是依序執行的步驟。實際系統會依資料是否可丟失，以及業務是否能接受等待來選擇。</p>
<div class="mermaid">
flowchart TB
    Root([佇列已滿]) --> Q1{資料不能丟失？}
    Q1 -->|是| Q2{業務可以等待？}
    Q2 -->|是| A[阻塞上游，形成背壓]
    Q2 -->|否| B[轉交持久化訊息系統]
    Q1 -->|否| Q3{只需要最新資料？}
    Q3 -->|是| C[丟棄舊資料或低價值資料]
    Q3 -->|否| Q4{上游可以重試？}
    Q4 -->|是| D[拒絕新資料並快速回報]
    Q4 -->|否| E[重新檢視業務承諾與資料優先級]
</div>
</section>

<section>
<div class="wp-section-head purple"><div class="wp-chip">03</div><h2>不一定要排隊的替代方案</h2></div>
<table><thead><tr><th>方案</th><th>適用條件</th><th>主要代價</th></tr></thead><tbody>
<tr><td><code>Write Back</code> 快取</td><td>可接受資料先存在 Redis 或其他快取，稍後批次寫入資料庫。</td><td>快取故障、批次尚未落盤或重複寫入時，需要額外的可靠性設計。</td></tr>
<tr><td>資料庫分片</td><td>資料可以依使用者 ID、設備編號等穩定 Key 分散到多個資料庫。</td><td>跨分片查詢、交易與資料重新分布都會增加複雜度。</td></tr>
<tr><td><code>Load Shedding</code></td><td>請求有清楚的優先級，低價值資料可以被捨棄。</td><td>被捨棄的資料無法靠佇列補回，業務必須接受降級結果。</td></tr>
<tr><td>同步處理與擴充</td><td>結果必須立即確認，且流量可透過更多處理節點或更快的儲存系統承接。</td><td>硬體、資料庫授權與維運成本上升，擴充也可能有上限。</td></tr>
</tbody></table>
<div class="wp-callout info"><span class="wp-icon">💡</span><p><strong>選擇方式：</strong>先比較資料能不能延後、資料能不能丟、下游能不能水平擴充。若三個答案都是否定，系統需要重新檢視業務承諾，單靠佇列無法消除容量矛盾。</p></div>
<details class="wp-detail"><summary>Write Back 的批次寫入</summary><div class="wp-detail-body"><p>資料庫寫入慢，可能是因為硬碟 I/O 成本高。前端的 <code>50,000</code> 筆請求可以先直接寫入 Redis 或記憶體資料庫，寫入成功後立刻回傳使用者。後台再每隔 1 秒把累積的幾萬筆資料打包成巨大的 <code>INSERT</code>，使用 Batch Insert 一次寫入資料庫。</p><p>對資料庫來說，逐筆寫入與一次批次寫入 <code>10,000</code> 筆資料的磁碟尋道成本可能接近。這種方式能大幅降低資料庫負擔，但必須處理快取故障與資料尚未落盤的風險。</p></div></details>
<details class="wp-detail"><summary>Sharding 的數量級推導</summary><div class="wp-detail-body"><p>假設單一資料庫每秒只能承受 <code>3,000</code> 筆寫入，可以依使用者 ID 或 IoT 設備編號進行分片。ID 尾數為 0 到 9 的資料送往 A 資料庫，10 到 19 的資料送往 B 資料庫，以此類推，共使用 20 台資料庫獨立運作。</p><p>原本單台每秒 <code>3,000</code> 筆，20 台並行後，整個叢集的寫入能力約為 <code>3,000 × 20 = 60,000</code> 筆／秒，理論上可以承接每秒 <code>50,000</code> 筆流量。這條路徑不需要讓使用者排隊，但會增加跨分片查詢、交易與資料重新分布的複雜度。</p></div></details>
<details class="wp-detail"><summary>遊戲系統的主動捨棄</summary><div class="wp-detail-body"><p>即時系統的 <code>50,000</code> 筆請求可能包含玩家移動座標、玩家聊天與玩家買裝備。當資料庫處理速度跌破警戒線，閘道器可以啟動 Load Shedding，捨棄 <code>80%</code> 的玩家移動座標，只保留買裝備與聊天。</p><p>若前端過濾後只剩 <code>2,500</code> 筆送往資料庫，核心業務可以繼續運作，但被捨棄的座標資料無法靠佇列補回。</p></div></details>
</section>

<section>
<div class="wp-section-head"><div class="wp-chip">04</div><h2>無界佇列為什麼可能造成更大損失</h2></div>
<p>無界佇列把等待資料放在程序記憶體中。當輸入速度長時間高於處理速度，佇列會持續成長，最後可能觸發 <code>OutOfMemoryError</code>。程序被終止後，尚未持久化的資料也會跟著消失。</p>
<div class="wp-causal-timeline">
<div class="wp-causal-event"><div class="wp-causal-card"><span class="wp-causal-label">起點</span><span class="wp-causal-title">輸入速度持續高於處理速度</span><p>等待中的任務逐漸增加，記憶體使用量跟著上升。</p></div></div>
<div class="wp-causal-event warn"><div class="wp-causal-card"><span class="wp-causal-label">壓力升高</span><span class="wp-causal-title">記憶體壓力擴大</span><p>垃圾回收更頻繁，處理速度可能進一步下降，形成惡性循環。</p></div></div>
<div class="wp-causal-event danger"><div class="wp-causal-card"><span class="wp-causal-label">故障點</span><span class="wp-causal-title">程序被迫終止</span><p>程序崩潰或被作業系統終止後，記憶體中的等待資料沒有持久化副本。</p></div></div>
</div>
<div class="wp-card"><h3>程序終止後的流量分支</h3><p>程序被終止後，結果取決於負載平衡器是否把流量轉移到其他節點。</p></div>
<div class="mermaid">
flowchart TB
    Stop[程序被終止] --> Lost[尚未持久化的等待資料遺失]
    Stop --> Route{負載平衡器轉移流量？}
    Route -->|否| Isolated[單一節點受影響]
    Route -->|是| Overflow[其他節點承受額外流量]
    Overflow --> Repeat[無界佇列持續成長]
    Repeat --> Cascade[連鎖 OOM，形成雪崩]
</div>
<div class="wp-card"><p>無界佇列的風險不只是一批資料遺失。當一台伺服器因 OOM 當機，負載平衡器可能把原本分配給它的流量轉移到其他健康節點。其他節點若也使用無界佇列，就可能一台接一台被撐爆，形成雪崩。</p><p>在斷電或程序暴斃的幾個小時內，核心服務可能完全無法提供，丟失的資料量與商業損失可能遠高於採用明確 Drop Policy 的有界佇列。</p></div>
</section>

<section>
<div class="wp-section-head ok"><div class="wp-chip">05</div><h2>標準庫裡的有界佇列</h2></div>
<table class="wp-library-table"><thead><tr><th>語言</th><th>常見工具</th><th>容量設定</th></tr></thead><tbody>
<tr><td>Java</td><td><code>ArrayBlockingQueue</code>、<code>LinkedBlockingQueue</code></td><td>建立佇列時指定容量</td></tr>
<tr><td>Go</td><td><code>make(chan Type, capacity)</code></td><td>建立帶容量的 Channel</td></tr>
<tr><td>C#</td><td><code>System.Threading.Channels</code>、<code>BlockingCollection</code></td><td>依 API 設定 bounded capacity</td></tr>
<tr><td>Python</td><td><code>queue.Queue(maxsize)</code></td><td>以 <code>maxsize</code> 設定上限</td></tr>
<tr><td>C++</td><td>標準容器通常不直接提供執行緒安全的 bounded queue</td><td>需由應用程式或第三方函式庫補上同步與容量策略</td></tr>
</tbody></table>
<div class="wp-card"><p>C++ 的 STL 預設容器通常是無界的，但 Boost 等高效能函式庫，以及 Meta、Google 等科技公司的開源函式庫，都能找到專用的 BoundedQueue 實作。</p></div>
</section>

<section>
<div class="wp-section-head"><div class="wp-chip">06</div><h2>作業系統與網路中的有界緩衝區</h2></div>
<p>有界佇列不只存在於應用程式。網卡接收區、核心 Socket Buffer、資料庫連線池，都會用固定或可設定的容量限制資源使用量。</p>
<div class="wp-card"><h3>封包穿過多層有界緩衝區</h3><p>閱讀方向由上往下。每一層都是容量有限的等待區，處理速度跟不上時，封包會在該層被捨棄或讓上游降低速度。</p></div>
<div class="mermaid">
flowchart TB
    NIC[網卡硬體] --> RX[RX Ring Buffer]
    RX -->|DMA 寫入| IRQ[Hard IRQ / SoftIRQ]
    IRQ --> NAPI[NAPI 驅動處理]
    NAPI --> SKB[sk_buff]
    SKB --> Stack[IP / TCP / UDP 協議棧]
    Stack --> Socket[Socket Receive Buffer]
    Socket --> App["應用程式 read() / recv()"]
</div>
<details class="wp-detail"><summary>硬體接收區與核心搬運</summary><div class="wp-detail-body"><p>網卡可透過 DMA 把封包寫入固定大小的 <code>RX Ring Buffer</code>。Ring Buffer 的長度通常在系統啟動或驅動程式載入時固定，例如常見的 <code>512</code> 或 <code>1024</code> 個插槽。網卡填入封包後會向 CPU 發出 Hard IRQ。</p><p>若 CPU 忙於昂貴運算或頻繁上下文切換，SoftIRQ 可能無法及時執行驅動程式的 <code>poll()</code>，搬運工作就會延遲。當 RX Ring Buffer 沒有可寫入的 Descriptor，網卡硬體會直接拒絕新封包。在 Linux 中，這類情況可能反映在 <code>rx_fifo_errors</code> 或 <code>overruns</code> 計數器。</p><p>核心再透過 NAPI 與 SoftIRQ 將封包交給協議棧，封裝成 <code>sk_buff</code>，最後放進應用程式的 Socket Receive Buffer。</p></div></details>
<details class="wp-detail"><summary>Socket 滿載時的 UDP／TCP 分支</summary><div class="wp-detail-body"><p>若應用程式沒有及時執行 <code>read()</code> 或 <code>recv()</code>，Socket 接收緩衝區也會到達上限。可透過 Linux 的 <code>net.core.rmem_max</code> 設定接收緩衝區上限。</p></div></details>
<div class="mermaid">
flowchart TB
    Full[Socket Receive Buffer 已滿] --> Protocol{傳輸協議？}
    Protocol -->|UDP| UDPDrop["kfree_skb()，新封包被捨棄"]
    Protocol -->|TCP| TCPWindow["縮小接收 Window 或送出 Zero Window"]
    TCPWindow --> Sender["發送端降速或重傳"]
</div>
<div class="wp-card"><h3>UDP 與 TCP 的差異</h3><p>UDP 沒有連線層的重傳與流量控制，接收緩衝區滿載時，新封包可能直接被捨棄。TCP 則透過接收視窗通知發送端降低傳送量，並在偵測到遺失時依協議進行重傳。若發送端遇到遺失，通常會等待數百毫秒後重傳，並依擁塞控制降低傳送速度，因此使用者可能感受到 Lag 與吞吐量下降。</p></div>
</section>

<section>
<div class="wp-section-head purple"><div class="wp-chip">07</div><h2>資料庫連線池也是容量邊界</h2></div>
<p>資料庫的容量限制通常同時出現在資料庫端與應用程式端。兩者都有限，錯誤訊息可能相似，但處理責任不同。</p>
<table><thead><tr><th>位置</th><th>容量邊界</th><th>滿載結果</th></tr></thead><tbody>
<tr><td>MySQL</td><td><code>max_connections</code> 與每條連線需要的執行緒、記憶體資源</td><td>新連線可能收到 <code>Too many connections</code></td></tr>
<tr><td>應用程式連線池</td><td>例如 <code>HikariCP</code> 的最大連線數與等待逾時</td><td>等待超過 <code>Connection Timeout</code> 後拋出連線取得失敗</td></tr>
</tbody></table>
<pre class="wp-pre" data-lang="flow">[應用程式執行緒]
        │ 取得連線
        ▼
[有限容量的等待區]
        │ 等待可用連線
        ▼
[連線池，最大 10 條]
        │ SQL
        ▼
[MySQL，max_connections 有上限]</pre>
<div class="wp-callout info"><span class="wp-icon">🔎</span><p><strong>閱讀方式：</strong>連線池的等待上限保護資料庫，也保護應用程式執行緒。等待逾時不是資料庫成功處理的證明，而是應用程式在期限內拿不到資源的結果。</p></div>
<div class="wp-card"><p>假設微服務有 <code>100</code> 個執行緒，連線池大小固定為 <code>10</code>。突發流量進來時，前 10 個執行緒取得連線，剩下的 90 個執行緒進入等待區。若等待區的 Connection Timeout 設為 <code>30</code> 秒，超過期限仍拿不到連線的執行緒就會被移出，程式可能拋出 <code>SQLTransientConnectionException: Connection is not available, request timed out after 30000ms</code>。</p><p>寧可讓前端網頁逾時，也不要讓 100 個甚至 1,000 個連線同時湧入 MySQL。資料庫若因 CPU 使用率達到 100% 或資源競爭陷入 Deadlock，整個系統可能徹底癱瘓。</p></div>
</section>

<section>
<div class="wp-section-head warn"><div class="wp-chip">08</div><h2>Token Bucket 與 Bounded Queue 的關係</h2></div>
<p><code>Token Bucket</code> 以固定速率 <code>r</code> 產生令牌，桶子的容量為 <code>B</code>。請求進來時先取得令牌，有令牌就能通過，沒有令牌則拒絕或回傳 <code>HTTP 429</code>。</p>
<pre class="wp-pre" data-lang="flow">[令牌產生器，每秒產生 r 個]
              │
              ▼
[Token Bucket，容量 B]
       │ 有令牌       │ 無令牌
       ▼              ▼
[放行請求]       [拒絕或回傳 429]</pre>
<div class="wp-callout ok"><span class="wp-icon">✅</span><p><strong>關鍵差異：</strong>一般 Bounded Queue 儲存等待中的工作，Token Bucket 儲存可用額度。前者控制待處理資料量，後者控制一段時間內允許通過的流量。</p></div>
<div class="wp-card"><p>當系統平時流量很低，桶子會累積令牌，最多累積到 <code>B</code> 個。突然有 <code>5,000</code> 筆請求湧入時，桶中的令牌可以讓一批請求在極短時間內通過，直到令牌耗盡才開始嚴格限流。桶子已滿時，新產生的令牌會自動作廢，而不是無限累積。</p><p>因此 Token Bucket 的重點是讓系統在安全上限內保有 Burstiness 彈性，不是把所有請求排進等待佇列。</p></div>
</section>

<section>
<div class="wp-section-head"><div class="wp-chip">09</div><h2>設計時的檢查清單</h2></div>
<ul class="wp-checklist">
<li>容量是依記憶體、延遲、下游處理速度，還是業務可接受等待時間推導出來的？</li>
<li>佇列滿載時要拒絕、丟棄、阻塞，還是轉存到持久化訊息系統？</li>
<li>上游是否能辨識入列成功與業務完成的差異？</li>
<li>重試是否有上限、退避策略、冪等處理與死信位置？</li>
<li>是否監控佇列深度、等待時間、拒絕數、丟棄數與 Consumer 速度？</li>
<li>尖峰持續超過下游產能時，系統是否仍有可預期的降級結果？</li>
</ul>
</section>
<footer>Bounded Queue 的重點不是讓所有資料永遠等待，而是讓系統在資源不足時仍保持可預期。</footer>
</div>
</div>

<!-- endtab -->


{% endtabs %}
