from pathlib import Path
import re, html, json

root=Path('C:/Dev/Hexo-mind')
work=root/'.codex-tmp/grafana-1'
original=(work/'original.md').read_text(encoding='utf-8')
front=original[:original.index('---',3)+3]
out=[]; pure=[]; diagrams=[]
def txt(s):
    s=re.sub(r'<a href="([^"]+)">(.*?)</a>',r'[\2](\1)',s)
    return html.unescape(re.sub(r'<[^>]+>','',s.replace('<code>','`').replace('</code>','`').replace('<strong>','**').replace('</strong>','**')))
def p(s): out.append('<p>'+s+'</p>');pure.append(txt(s))
def h(s): out.append('<h3 class="gd-section">'+s+'</h3>');pure.append('### '+txt(s))
def note(s): out.append('<div class="gd-note"><p>'+s+'</p></div>');pure.append('> '+txt(s))
def code(s,lang='text',label=None):
    label=label or lang
    out.append('<div class="gd-code"><div class="gd-code-label">'+label+'</div><pre class="gd-pre">'+html.escape(s)+'</pre></div>')
    pure.append(label+'\n\n```'+lang+'\n'+s+'\n```')
def table(headers,rows):
    out.append('<div class="gd-table-scroll" role="region" aria-label="'+html.escape(txt(headers[0]).replace('`',''),quote=True)+'資料表" tabindex="0"><table class="gd-table"><thead><tr>'+''.join('<th scope="col">'+s+'</th>' for s in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+s+'</td>' for s in row)+'</tr>' for row in rows)+'</tbody></table></div>')
    pure.append('\n'.join(['| '+' | '.join(map(txt,headers))+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(txt,row))+' |' for row in rows]))
def ul(items): out.append('<ul>'+''.join('<li>'+s+'</li>' for s in items)+'</ul>');pure.append('\n'.join('- '+txt(s) for s in items))
def graph(title,src,caption,width=620):
    if title.startswith('記憶體指標'): width=340
    if title.startswith('Log 寫入'): width=350
    if title.startswith('Memory Panel'): width=480
    if title.startswith('監控系統'): width=530
    h(title)
    cfg={'theme':'base','themeVariables':{'background':'#1b1925','primaryColor':'#30283e','primaryTextColor':'#eeeaf4','primaryBorderColor':'#91829f','lineColor':'#b8aec8','secondaryColor':'#252030','tertiaryColor':'#252030','clusterBkg':'#211c2b','clusterBorder':'#756583','edgeLabelBackground':'#1b1925','textColor':'#eeeaf4','fontSize':'16px','fontFamily':'Segoe UI, Microsoft JhengHei, sans-serif','actorBkg':'#30283e','actorBorder':'#91829f','actorTextColor':'#eeeaf4','actorLineColor':'#91829f','signalColor':'#cbc8d5','signalTextColor':'#eeeaf4','labelBoxBkgColor':'#252030','labelBoxBorderColor':'#91829f','labelTextColor':'#eeeaf4','loopTextColor':'#eeeaf4','noteBkgColor':'#30283e','noteBorderColor':'#91829f','noteTextColor':'#eeeaf4'},'flowchart':{'htmlLabels':False,'useMaxWidth':True,'curve':'linear','nodeSpacing':28,'rankSpacing':45},'sequence':{'useMaxWidth':True,'mirrorActors':False,'actorMargin':45,'messageMargin':35}}
    if src.startswith('sequenceDiagram'):
        name='loki-query' if 'Log 查詢' in title else 'memory-panel'
        assets=root/'source/images/grafana-1'
        assert (assets/(name+'.svg')).exists()
        (assets/(name+'.mmd')).write_text(src+'\n',encoding='utf-8')
        dims='779 293' if name=='loki-query' else '457 301'
        w,hh=dims.split()
        out.append('<div class="gd-diagram" role="region" aria-label="'+title+'" tabindex="0"><div class="gd-diagram-inner" style="min-width:'+str(min(width,620))+'px"><img class="gd-sequence" src="/Mind/images/grafana-1/'+name+'.svg" alt="'+title+'" width="'+w+'" height="'+hh+'"></div></div>')
    else:
        out.append('<div class="gd-diagram" role="region" aria-label="'+title+'" tabindex="0"><div class="gd-diagram-inner" style="min-width:'+str(min(width,620))+'px"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="'+html.escape(json.dumps(cfg),quote=True)+'" hidden>'+html.escape(src)+'</pre></div></div></div>')
    pure.append('```mermaid\n'+src+'\n```')
    diagrams.append({'title':title,'source':src})
    p(caption)
def tab(name,title,lead):
    out.append('<!-- tab '+name+'-->\n<section class="grafana-dusk">\n<div class="gd-hero"><span class="gd-brand-line" aria-hidden="true"></span><h2>'+title+'</h2><p>'+lead+'</p></div>')
    pure.extend(['## '+name,'### '+title,txt(lead)])
def end():out.append('</section>\n<!-- endtab -->')

tab('架構','從數字找到異常，從紀錄追查原因','凌晨收到服務錯誤通知時，先確認影響範圍與開始時間，再查看當時留下的事件紀錄。監控架構把這兩種資料接到同一個觀察介面。')
h('收到 API Error Rate > 5% 通知之後')
table(['調查方向','具體問題','資料來源'],[
['觀察趨勢','目前錯誤多不多？從什麼時候開始？哪一台 Pod 特別嚴重？','Prometheus 的 Metrics'],
['追查細節','到底報什麼錯？哪個 endpoint？Exception 是什麼？Request ID 是多少？','Loki 的 Logs']])
p('Grafana 將這兩條調查路線接在同一個介面。能否依服務、Pod 或 Request ID 對照，仍取決於實際收集的指標 Labels、Log 欄位及資料來源設定。')
graph('監控系統分工：兩條資料路徑', '''flowchart TB
subgraph Source["應用與基礎設施"]
System["Pod / API / Worker / DB"]
end
subgraph Storage["收集與儲存"]
Endpoint["Metrics endpoint / Exporter"]
Collector["Log Collector"]
Prom["Prometheus：指標"]
Loki["Loki：Log"]
Endpoint -->|指標樣本| Prom
Collector -->|Push Logs| Loki
end
subgraph View["查詢與呈現"]
Grafana["Grafana"]
Uses["Dashboard、Explore、Alerting"]
Grafana -->|呈現與評估| Uses
end
System -->|CPU、Memory、Request 數| Endpoint
System -->|Error、Exception、訊息| Collector
Prom -->|查詢結果| Grafana
Loki -->|查詢結果| Grafana''', '由上往下讀。實線箭頭表示資料流向，不表示請求由哪一端發起。Prometheus 主動抓取指標，Grafana 主動查詢資料來源；請求與回應方向會在後續章節展開。這是概念分工圖，不代表特定環境的部署實例。',700)
table(['資料種類','示例','主要用途'],[
['Metrics','CPU = 80%；Memory = 1.8 GB；Error count = 12','比較用量、數量與變化趨勢'],
['Logs','<code>Start processing job</code>、<code>DynamoDB timeout</code>、<code>OutOfMemoryException</code>','保存事件訊息與錯誤細節']])
end()

tab('metric','讓數字帶上觀測上下文','同樣是 100，單獨看只能知道數量。加上指標名稱、分類與觀測時間後，才知道哪個服務發生了什麼變化。')
h('Metric 與一般數值')
p('<code>metric</code> 是單數，例如「CPU 使用率這個 metric」；<code>metrics</code> 是複數，也常泛指監控指標資料。Metric 是量化系統狀態或行為的指標，觀測時會連同對象、時間與分類資訊一起解讀。')
p('核心仍是數字，例如 <code>80</code>、<code>512</code>、<code>1000</code>、<code>0.52</code>。有了上下文，才可以回答「誰、什麼時候、屬於哪一類，以及如何變化」。一般變數也能保存數值，但是否成為可持續查詢的監控資料，取決於後續的量測、暴露與收集流程。')
code('request_count = 100','text','程式內的一般變數')
p('程式結束後，這個變數可能跟著消失。若要監控 <code>order-api</code> 收到多少 Request，可以透過指標暴露累計數量。')
code('http_requests_total 100','text','帶有名稱的指標樣本')
h('Labels 是可組合的分類維度')
p('系統可能同時提供 <code>GET /users</code>、<code>POST /orders</code>、<code>GET /products</code>。加入 Labels 後，同一個指標名稱可以描述不同請求類別。')
code('http_requests_total{method="POST", path="/orders", status="200"} 100','text','指標名稱、Labels 與樣本值')
table(['組成','範例','意義'],[['指標名稱','<code>http_requests_total</code>','記錄 HTTP 請求累計數'],['Labels','<code>method="POST"</code>、<code>path="/orders"</code>、<code>status="200"</code>','共同識別同一組分類'],['樣本值','<code>100</code>','該組分類在觀測時的累計值']])
p('指標名稱與完整 Label 集合共同識別一條時間序列。Prometheus 保存該序列的時間戳記與樣本值。參考 <a href="https://prometheus.io/docs/concepts/">Prometheus 資料模型</a>。')
code('http_requests_total{method="GET", status="200", pod="api-01"} 5000','text','另一組分類的樣本')
table(['分類維度','可觀察的值','關係'],[['Method','<code>GET</code>、<code>POST</code>','依請求方法篩選'],['Status','<code>200</code>、<code>404</code>、<code>500</code>','依回應狀態篩選'],['Pod','<code>api-01</code>、<code>api-02</code>','依執行實例篩選']])
note('Method、Status 與 Pod 是不同維度，可以同時套用條件。例如查詢 <code>api-01</code> 中狀態為 <code>200</code> 的 <code>GET</code> 請求。它們不是互斥的樹狀分支。')
h('同一條時間序列，持續累積樣本')
p('以 <code>method="POST", path="/orders", status="200"</code> 這組 Labels 為例，Prometheus 定期取得下列樣本。')
table(['時間','http_requests_total'],[['08:00','100'],['08:01','150'],['08:02','230'],['08:03','310']])
out.append('<div class="gd-plot" role="img" aria-label="時間序列：08:00 為 100，08:01 為 150，08:02 為 230，08:03 為 310"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 320" width="640" height="320"><g fill="none" stroke="#554a62"><path d="M70 45V265H595"/><path d="M70 202H595M70 139H595M70 76H595"/></g><g fill="#cbc8d5" font-size="16" font-family="Segoe UI, sans-serif"><text x="20" y="270">0</text><text x="20" y="207">100</text><text x="20" y="144">200</text><text x="20" y="81">300</text><text x="70" y="25">http_requests_total</text><text x="73" y="300">08:00</text><text x="223" y="300">08:01</text><text x="373" y="300">08:02</text><text x="523" y="300">08:03</text></g><path d="M95 202L245 170.5L395 120.2L545 69.9" fill="none" stroke="#91b7ff" stroke-width="3"/><g fill="#ffc619"><circle cx="95" cy="202" r="5"/><circle cx="245" cy="170.5" r="5"/><circle cx="395" cy="120.2" r="5"/><circle cx="545" cy="69.9" r="5"/></g><g fill="#eeeaf4" font-size="16" text-anchor="middle"><text x="95" y="185">100</text><text x="245" y="153">150</text><text x="395" y="103">230</text><text x="545" y="53">310</text></g></svg></div>')
p('橫軸是時間，縱軸是請求累計數；折線只連接示例樣本，不代表已知兩次抓取之間的每一筆請求。')
ul(['最近增加多快？','最近 5 分鐘有多少 Request？','今天與昨天差多少？','哪個 Pod 的 Request 最多？','<code>500</code> Error 的比例是多少？'])
h('原始量測與衍生指標')
p('Pod 記憶體可以直接以 <code>container_memory_working_set_bytes</code> 表示。這接近原始量測（raw measurement）的用途，但 working set 本身仍是監控元件依底層資訊定義的量測值。')
code('container_memory_working_set_bytes 1572864000','text','記憶體樣本：1,572,864,000 bytes')
table(['時間','Memory 顯示示例'],[['08:00','1.2 GB'],['08:01','1.3 GB'],['08:02','1.5 GB']])
p('上述時間表是一組独立的顯示示例，不是把同一筆 <code>1,572,864,000 bytes</code> 重複換算。資料從真實系統的量測產生 Metric，再經計算或聚合形成衍生指標或查詢結果，最後由 Grafana 顯示。')
graph('記憶體換算：bytes、GiB 與使用率', '''flowchart TB
Raw["Container 量測：1,800,000,000 bytes"] -->|原始 bytes| Convert["除以 1024 的三次方"]
Convert -->|約 1.6764 GiB| Display["顯示值：1.68 GiB"]
Display -->|除以 Limit，再乘以 100| Ratio["顯示值算例：84%"]
Limit["Memory Limit：2 GiB"] -->|提供分母| Ratio''', '由上往下讀，箭頭表示數值轉換與計算輸入。以顯示值計算，1.68 ÷ 2 × 100 = 84%；使用未四捨五入的原始 bytes 計算則約為 83.82%。1.68 GiB 與 84% 都能作為觀察指標。',510)
note('<code>GB</code> 與 <code>GiB</code> 不同：1 GB = 10⁹ bytes，1 GiB = 1024³ bytes。原稿的 GB 顯示例與這裡的 GiB 換算例分開使用。Memory Used 以此處的 working set 為例，實務上仍須確認儀表板採用的記憶體定義。')
h('Counter 經 rate() 轉成每秒速率')
table(['時間','http_requests_total 累計值','rate() 結果示意'],[['08:00','10000','8 req/s'],['08:01','10600','10 req/s'],['08:02','11500','13 req/s']])
code('rate(http_requests_total[5m])','promql','查詢最近 5 分鐘的平均每秒增長率')
p('<code>http_requests_total</code> 是累加型 Counter，<code>rate()</code> 將時間窗內的樣本轉成平均每秒速率，並處理 Counter reset。右欄的 <code>8</code>、<code>10</code>、<code>13 req/s</code> 保留作為輸出形式示意；單靠左欄三筆資料，無法計算完整 5 分鐘視窗的這些結果。參考 <a href="https://prometheus.io/docs/prometheus/latest/querying/functions/#rate">Prometheus rate() 定義</a>。')
end()

tab('Prometheus','分清楚量測與抓取的責任','底層元件先取得系統資訊並暴露指標，Prometheus 再定期抓取、保存與查詢。知道數字從哪裡來，才能判斷儀表板正在觀察什麼。')
h('Prometheus 的起源與角色')
p('Prometheus 是用於收集、保存與查詢系統 Metrics 的開源監控系統。Matt T. Proud 與 Julius Volz 在 2012 年於 SoundCloud 啟動專案；2016 年加入 CNCF，成為 Kubernetes 之後第二個託管專案，2018 年畢業。參考 <a href="https://prometheus.io/community/">Prometheus 專案發起者</a>與 <a href="https://www.cncf.io/announcements/2018/08/09/prometheus-graduates/">CNCF 畢業公告</a>。')
graph('記憶體指標：量測、暴露與抓取', '''flowchart TB
subgraph Measured["量測與暴露端"]
Container["Pod / Container"] -->|使用資源| Kernel["Linux Kernel / cgroup"]
Kernel -->|提供原始資訊| Monitor["監控元件"]
Monitor -->|暴露 Metric| Endpoint["Metrics endpoint"]
end
subgraph Prom["Prometheus"]
Scraper["Scrape：定期抓取"] -->|保存樣本| Store["儲存 / PromQL 查詢"]
end
Scraper -->|HTTP scrape 請求| Endpoint
Endpoint -.->|指標樣本回應| Scraper
Grafana["Grafana"] -->|PromQL 查詢| Store
Store -.->|查詢結果| Grafana''', '上方是量測與暴露流程；跨邊界的實線表示請求，虛線表示回應。Prometheus 通常不會進入應用程式 Pod 自行檢查 RAM，實際量測由 OS、Kubernetes 相關元件、應用程式或 Exporter 提供。此圖以 Container 記憶體為例，省略監控元件的具體部署方式。',660)
p('例如監控元件提供 <code>container_memory_working_set_bytes</code>，樣本值為 <code>1800000000</code>，也就是十進位的 <code>1.8 GB</code>。暴露格式應使用 bytes 數值，不直接在樣本後面寫 <code>1.8GB</code>。')
h('Scrape 是定期取得最新樣本')
p('假設抓取週期設為每 15 秒，Prometheus 取得的數字可能如下。這是範例設定，不代表所有部署都使用相同週期。')
table(['時間','Memory'],[['08:00:00','1.20 GiB'],['08:00:15','1.25 GiB'],['08:00:30','1.31 GiB'],['08:00:45','1.42 GiB']])
table(['元件','以 10 個 API Pod 為例'],[['Kubernetes','讓期望的 10 個 API Pod 執行，處理排程與生命週期。'],['Prometheus','收集 CPU、Memory、Request Rate、Error Rate、Latency 等指標，觀察這 10 個 Pod 的狀態。']])
h('四種主要 Metric 型別')
table(['型別','觀察方式','範例與限制'],[
['Counter','持續累加，重啟等情況可能重設','Request 總數、Error 總數；通常搭配 <code>rate()</code> 或 <code>increase()</code>。'],
['Gauge','可以增加，也可以減少','Memory、在線人數、已計算的 CPU 使用率；CPU 累計使用秒數則通常是 Counter。'],
['Histogram','觀察大量事件的分布','例如 Request 耗時。Classic Histogram 使用累積 bucket，查詢端可計算 quantile。'],
['Summary','記錄觀測總數、總和，並可輸出用戶端計算的 quantile','例如 Request 耗時；不同實例的 quantile 不能直接相加或平均成整體 quantile。']])
note('「0–100 ms 有幾次、100–500 ms 有幾次」是在問區間分布。Classic Histogram 的 <code>le="0.1"</code> 表示不超過 100 ms 的累計次數，<code>le="0.5"</code> 表示不超過 500 ms；兩者相減才能得到大於 100 ms、且不超過 500 ms 的次數。')
p('Histogram 與 Summary 都能描述分布，選擇時還要考慮跨實例聚合、精度與用戶端支援。這裡以 Classic Histogram 說明 bucket；Prometheus 另支援 Native Histogram。參考 <a href="https://prometheus.io/docs/concepts/metric_types/">Metric 型別</a>與 <a href="https://prometheus.io/docs/practices/histograms/">Histograms and summaries</a>。')
end()

tab('Loki','把分散的事件紀錄集中保存','結帳在 10:32 失敗，處理請求的 Pod 卻不一定還在原處。集中保存 Log，才能跨實例查找當時留下的線索。')
h('Loki 的起源與用途')
p('Loki 是集中儲存、搜尋與分析 Logs 的系統。Grafana Labs 在 2018 年啟動專案，Tom Wilkie 與 David Kaltschmidt 的早期設計文件推動了它的誕生，同年底在 KubeCon Seattle 公開。官方以「Like Prometheus, but for logs.」描述其方向。參考 <a href="https://grafana.com/events/grafanacon/2020/loki-future/">Loki 早期設計回顧</a>與 <a href="https://grafana.com/blog/open-source-log-monitoring-the-concise-guide-to-grafana-loki/">Loki 五週年介紹</a>。')
p('假設 Order API 分散在 Pod A、Pod B、Pod C、Pod D、Pod E。得知「剛剛 10:32 結帳失敗」時，首先要找出是哪個 Pod 處理，以及該實例的錯誤紀錄。')
note('Crash 後可能發生 Container Restart，也可能因 Pod 被刪除或替換而讓舊 Pod 消失；Container 重啟不等於 Pod 一定被替換。只依賴本機 Log 會受到輪替、節點與 Pod 生命週期影響，因此需要將紀錄送到集中儲存。')
graph('Log 寫入路徑：從程式到 Loki', '''flowchart TB
subgraph Node["Kubernetes Node"]
subgraph Pod["Pod / Container"]
App["C# Application"] -->|ILogger| Provider["Logging Provider"]
Provider -->|Console 輸出| Std["stdout / stderr"]
end
Std -->|交由 Runtime 處理| Runtime["Container Runtime"]
Runtime -->|寫入紀錄| Files["Node 上的 Container Logs"]
Files -->|讀取| Collector["Log Collector"]
Collector -->|附加 metadata / labels| Enriched["Log 與時間戳記、Labels"]
end
subgraph Central["集中服務"]
Loki["Loki API：接收並保存"]
end
Enriched -->|HTTP Push Logs| Loki''', '由上往下讀，箭頭表示紀錄的傳遞與處理。圖中以 Node 層級 Collector 讀取 Container Log 為例；Collector 也可能採其他部署或讀取方式。Pod A 至 Pod E 的紀錄都可經相應收集路徑集中送往 Loki，並非每個 Pod 必須各部署一個 Collector。',600)
h('1. C# 程式產生 Log')
code('_logger.LogInformation("Start processing ShopId {ShopId}", shopId);\n_logger.LogError(\n    exception,\n    "Failed to process promotion {PromotionId}",\n    promotionId);','csharp','Worker 的紀錄呼叫')
p('假設 <code>shopId = 2</code>、<code>promotionId = 574730</code>，設定好的 Logging Provider 可能輸出以下文字。日期、等級與格式由 Provider／Formatter 設定決定。')
code('08:30:01 INFO  Start processing ShopId 2\n08:30:02 INFO  Loading promotions\n08:30:05 ERROR Failed to process promotion 574730\n08:30:05 ERROR System.TimeoutException...','text','Log 輸出示例')
p('在 ASP.NET Core 中，同一個 <code>_logger.LogInformation()</code> 呼叫若搭配帶日期的 Console 格式，可能產生 <code>2026-09-22 08:30:01 INFO Start processing ShopId 2</code>。<code>ILogger</code> 只把紀錄交給設定好的 Provider；執行到這裡不代表 Loki 已收到資料。')
h('2. Container Runtime 將標準輸出保存為 Node Log')
p('Container／Kubernetes 的常見配置讓程式寫入 <code>stdout</code> 或 <code>stderr</code>。Container Runtime 處理這些輸出，在 Node 上留下對應 Log，Kubernetes 可透過下列指令讀取。')
code('kubectl logs promotion-worker-abc','bash','讀取 Pod 的 Container Log')
code('INFO Start processing ShopId 2\nINFO Loading promotions\nERROR DynamoDB timeout','text','kubectl logs 輸出示例')
p('資料此時仍可能只在 Node 的 Log 路徑中，尚未送入 Loki。參考 <a href="https://kubernetes.io/docs/concepts/cluster-administration/logging/">Kubernetes Logging Architecture</a>。')
h('3. Collector 讀取紀錄並附加分類')
p('Collector 負責搬運 Log。例如 Grafana Alloy，或其他環境中的 Fluent Bit。舊版 Loki 教學也常見 Promtail；官方已標示 Promtail 於 2026-03-02 結束生命週期。參考 <a href="https://grafana.com/docs/loki/latest/send-data/promtail/">Promtail 官方狀態</a>。')
code('2026-09-22 08:30 INFO Start Job\n2026-09-22 08:31 ERROR Timeout','text','Collector 讀取的新紀錄')
table(['Metadata／Label','示例值'],[['<code>namespace</code>','<code>production</code>'],['<code>pod</code>','<code>promotion-worker-abc</code>'],['<code>container</code>','<code>worker</code>'],['<code>service</code>','<code>promotion-worker</code>']])
p('上述 Labels 是示例配置，不代表 Collector 自動產生所有欄位。尤其 <code>service</code> 的命名與映射需要在收集設定中一致。')
h('4. Collector 透過 HTTP Push 給 Loki')
table(['傳送內容','概念示例'],[['Timestamp','<code>2026-09-22 08:30:01</code>'],['Labels','<code>service="promotion-worker"</code>、<code>pod="promotion-worker-abc"</code>、<code>namespace="production"</code>'],['Log','<code>INFO Start processing ShopId 2</code>']])
p('這是內容概念表，不是可直接提交的 Loki API payload。Collector 依 API 格式將資料送入 Loki，Loki 才能保存並供後續查詢。')
h('5. 透過 Grafana 查詢 Loki')
code('{service="promotion-worker"} |= "ERROR"','logql','篩選指定服務的錯誤文字')
p('這段 <code>LogQL</code> 先選取 <code>service="promotion-worker"</code> 的 Log stream，再篩選包含大寫 <code>ERROR</code> 的紀錄。它是區分大小寫的文字篩選，不會自動判斷所有語意上的錯誤。參考 <a href="https://grafana.com/docs/loki/latest/query/log_queries/">Loki Log queries</a>。')
graph('Log 查詢時序：請求與回傳', '''sequenceDiagram
participant User as 使用者
participant Grafana as Grafana Explore
participant Loki as Loki
User->>Grafana: 選擇資料來源與時間範圍
Grafana->>Loki: LogQL Query
Loki-->>Grafana: Query Result：符合條件的 Logs
Grafana-->>User: 顯示 Log 清單''', '參與者由左至右排列，時間向下。實線是查詢或操作，虛線是結果返回。這張圖只描述成功查詢的概念路徑；Grafana 是查詢介面，本文架構中的 Log 儲存在 Loki。',710)
end()

tab('Grafana','把查詢結果變成畫面與告警','Grafana 接上資料來源，將查詢結果呈現為儀表板與探索畫面，也能定期評估告警條件。資料儲存、查詢運算與畫面呈現各有負責的元件。')
h('三種主要使用方式')
table(['功能','操作方式','用途'],[['Dashboard','由 Panel 對資料來源執行查詢','持續查看 CPU、Memory 與服務指標'],['Explore','選擇資料來源，互動式執行 PromQL 或 LogQL','逐步調查數值變化與錯誤紀錄'],['Alerting','定期查詢並評估規則','依告警與通知設定送出訊息']])
p('整體架構仍是應用系統提供 Metrics 與 Logs：Prometheus 負責指標收集與儲存，Alloy／Fluent Bit 等 Collector 將 Log 送入 Loki，Grafana 再查詢這些資料來源。')
h('Panel 如何顯示 Pod Memory')
table(['時間','Prometheus 中的 Memory 顯示示例'],[['08:00','1.2 GB'],['08:01','1.4 GB'],['08:02','1.7 GB'],['08:03','1.9 GB']])
code('container_memory_working_set_bytes{\n    pod="promotion-worker"\n}','promql','Memory Panel 查詢')
p('範例假設 Pod Label 恰好是 <code>promotion-worker</code>；實際部署需使用真正的 Pod 名稱與必要的 namespace／container 篩選。查詢原始單位是 bytes，Panel 可設定顯示為 GB 或 GiB。')
graph('Memory Panel 查詢時序', '''sequenceDiagram
participant Panel as Grafana Panel
participant Prom as Prometheus
Panel->>Prom: PromQL 與時間範圍
Prom-->>Panel: 時間序列樣本
Panel->>Panel: 換算顯示單位並繪圖''', '時間由上往下。上表的 1.2、1.4、1.7、1.9 GB 形成上升趨勢；圖表由 Grafana 畫出，底下的時間序列資料由 Prometheus 提供。Panel 不會只靠查詢名稱推定所有 Container 的聚合方式。',600)
h('Explore 如何顯示 Error Log')
p('將 Data Source 選為 Loki，在 Explore 輸入下列查詢。Grafana 將 LogQL 送給 Loki，再顯示 Loki 回傳的紀錄。')
code('{service="promotion-worker"} |= "ERROR"','logql','Explore 查詢')
code('08:31 ERROR DynamoDB timeout\n08:35 ERROR OutOfMemoryException','text','Explore 結果示例')
p('在 Grafana 撰寫 LogQL，表示透過 Grafana 介面對 Loki 下查詢。寫入管線、Log 儲存與查詢呈現的責任仍然分開。')
h('Alert：過去 5 分鐘 Dify Error > 5')
p('假設規則要觀察過去 5 分鐘的 Dify Error 數量，門檻為大於 <code>5</code>。Grafana 定期查詢 Loki，某次取得 <code>8</code>，因此滿足門檻。實際查詢需要依 Dify 的 Labels 與 Log 格式建立計數條件；純 Log 清單查詢還不是告警所需的數值結果。')
graph('告警評估：超過門檻後才進入狀態判定', '''flowchart TB
Evaluate["Grafana 定期評估"] -->|查詢最近 5 分鐘| Query["Loki 回傳 Dify Error 數量"]
Query --> Threshold{"錯誤數量大於 5？"}
Threshold -->|否| Next["本次未達門檻，等待下次評估"]
Threshold -->|是，範例值為 8| State["依 Pending 等設定判定告警狀態"]
State --> Ready{"已達 Alerting？"}
Ready -->|否| Wait["繼續評估條件是否持續成立"]
Ready -->|是| Policy["依通知策略與時機處理"]
Policy -->|符合通知條件| Notify["Slack / Email / 其他管道"]''', '由上往下讀，菱形表示判斷，箭頭直接標示條件。圖中以原先非告警、查詢成功且有資料的規則為例，沒有展開既有告警恢復、No Data 或查詢錯誤的處理。',600)
note('超過門檻不等於立即通知。評估週期決定多久檢查一次；Pending period 決定條件需持續多久才進入 Alerting；通知策略還可能涉及分組、等待與靜音等設定。Pending 設為 0 時可略過等待。')
p('以上為 Grafana-managed alert rule 的概念流程。參考 <a href="https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rule-evaluation/">Grafana 告警評估說明</a>。Grafana 的核心用途，是將不同監控資料來源接到同一個平台，提供查詢、視覺化、Dashboard 與 Alert。')
end()

template=Path('C:/Users/Allen/.codex/skills/hexo-article-creator/assets/components/grafana-dusk-style.html').read_text(encoding='utf-8')
css=re.search(r'<style>.*?</style>',template,re.S).group()
extra='''
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
'''
css=css.replace('</style>',extra+'</style>')
body='\n'.join(out).replace('独立','獨立')
body=body.replace('<!-- tab 架構-->','<!-- tab 架構-->\n\n'+css,1)
(root/'source/_posts/Metrix/grafana-1.md').write_text(front+'\n\n{% tabs grafana-1 %}\n\n'+body+'\n\n{% endtabs %}\n',encoding='utf-8')
(root/'source/_posts/Metrix/grafana-1-pure.md').write_text(front+'\n\n'+'\n\n'.join(pure).replace('独立','獨立')+'\n',encoding='utf-8')
(work/'diagrams.json').write_text(json.dumps(diagrams,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Wrote article, pure version and {len(diagrams)} Mermaid sources.')
