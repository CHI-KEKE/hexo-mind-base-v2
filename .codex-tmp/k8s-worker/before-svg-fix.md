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

{% tabs worker-pod-cpu-memory %}

<!-- tab requests-->

<style>
.kubernetes-helm{--kh-blue:#326de6;--kh-link:#2455b5;--kh-bg:#fff;--kh-ink:#303b4b;--kh-soft:#eef4ff;--kh-line:#d5deed;--kh-muted:#566b88;background:var(--kh-bg);color:var(--kh-ink);padding:24px;font-family:'Segoe UI','Microsoft JhengHei',sans-serif;line-height:1.9;overflow-wrap:anywhere;}
.kubernetes-helm *{box-sizing:border-box;}
#article-container .kubernetes-helm h2,#article-container .kubernetes-helm h3{color:var(--kh-ink);font-weight:800;line-height:1.45;}
.kubernetes-helm .kh-hero{border-bottom:3px solid var(--kh-blue);padding:8px 0 24px;margin-bottom:28px;}
#article-container .kubernetes-helm .kh-logo{width:52px;height:52px;margin:0 0 18px;display:block;object-fit:contain;}
.kubernetes-helm .kh-hero h2{font-size:clamp(1.5rem,3vw,2.1rem);margin:0 0 14px!important;}
.kubernetes-helm .kh-hero p{max-width:46em;}
.kubernetes-helm .kh-section{border-left:4px solid var(--kh-blue);padding-left:12px;margin:34px 0 18px!important;font-size:1.22rem;}
.kubernetes-helm p{margin:14px 0;}
.kubernetes-helm a{color:var(--kh-link);text-decoration:underline;text-underline-offset:3px;}
.kubernetes-helm code{color:var(--kh-link);background:var(--kh-soft);padding:2px 5px;border-radius:3px;overflow-wrap:anywhere;}
.kubernetes-helm .kh-note{background:var(--kh-soft);border-left:4px solid var(--kh-blue);padding:12px 18px;margin:22px 0;border-radius:4px;}
.kubernetes-helm .kh-note.warn{border-left-color:#b97c18;}
.kubernetes-helm .kh-table-scroll{overflow-x:auto;margin:22px 0;}
#article-container .kubernetes-helm table.kh-table{width:100%;table-layout:fixed;margin:0;border-collapse:collapse;color:var(--kh-ink);}
#article-container .kubernetes-helm .kh-table th,#article-container .kubernetes-helm .kh-table td{padding:12px;border:1px solid var(--kh-line);text-align:left;vertical-align:top;background:var(--kh-bg);color:var(--kh-ink);}
#article-container .kubernetes-helm .kh-table th{background:var(--kh-soft);}
.kubernetes-helm .kh-code{background:#182235;color:#f3f6fc;border-radius:5px;overflow:hidden;margin:22px 0;}
.kubernetes-helm .kh-code-label{border-bottom:1px solid #43516a;padding:6px 16px;font-size:.8rem;letter-spacing:.08em;}
#article-container .kubernetes-helm pre.kh-pre{background:#182235!important;color:#f3f6fc!important;padding:18px!important;margin:0!important;border:0!important;box-shadow:none!important;text-shadow:none!important;font:14px/1.8 Consolas,monospace!important;white-space:pre!important;overflow-x:auto!important;border-radius:0!important;}
.kubernetes-helm .kh-diagram{background:#fff;color:#233650;border:1px solid var(--kh-line);border-radius:6px;padding:20px 10px;margin:22px 0;overflow:auto;}
.kubernetes-helm .kh-diagram .mermaid-wrap{background:#fff!important;min-width:510px;}
.kubernetes-helm .kh-capacity,.kubernetes-helm .kh-scale{background:var(--kh-soft);padding:18px 24px;margin:24px 0;border-radius:5px;}
.kubernetes-helm .kh-track{height:22px;display:flex;position:relative;background:var(--kh-line);border-radius:3px;}
.kubernetes-helm .kh-used{background:#8397b7;}.kubernetes-helm .kh-new{background:var(--kh-blue);}
.kubernetes-helm .kh-boundary{position:absolute;top:-5px;height:32px;width:3px;background:#ac5422;}
.kubernetes-helm .kh-ruler{display:flex;justify-content:space-between;border-top:8px solid var(--kh-blue);padding-top:8px;margin:18px 0 24px;font-size:.9rem;}
.kubernetes-helm .kh-ruler span{width:33.33%;}.kubernetes-helm .kh-ruler span:nth-child(2){text-align:center;}.kubernetes-helm .kh-ruler span:last-child{text-align:right;}
.kubernetes-helm :focus-visible{outline:3px solid var(--kh-blue);outline-offset:3px;}
[data-theme=dark] .kubernetes-helm{--kh-blue:#7fa9ff;--kh-link:#a4c2ff;--kh-bg:#17202e;--kh-ink:#eef2f8;--kh-soft:#23334e;--kh-line:#52647f;--kh-muted:#bdcce0;}
@media(max-width:600px){.kubernetes-helm{padding:12px;}.kubernetes-helm .kh-table{min-width:530px;}.kubernetes-helm .kh-capacity,.kubernetes-helm .kh-scale{padding:14px;}.kubernetes-helm .kh-diagram{padding:12px 4px;}}
</style>
<div class="kubernetes-helm">
<div class="kh-hero"><img class="kh-logo" src="https://raw.githubusercontent.com/kubernetes/kubernetes/master/logo/logo.svg" alt="" aria-hidden="true" width="52" height="52"><h2>先找得到位置，才能開始工作</h2><p>同一份工作設定有三種不同用途：requests 決定排程時需要多少資源，limits 限制執行時的用量，HPA 則調整 Worker 副本數。先從一個 Worker Container 的需求開始。</p></div>

<h3 class="kh-section">一個 Container 的資源設定</h3>

<p>本文案例為每個 Pod 配置一個主要 Worker Container。以下數值屬於該 Container，不是整個服務的總量；若還有 sidecar、init container 或 Pod overhead，排程需求還要依實際配置計算。</p>

<div class="kh-table-scroll" role="region" aria-label="資源比較" tabindex="0"><table class="kh-table"><thead><tr><th scope="col">資源</th><th scope="col">requests</th><th scope="col">limits</th></tr></thead><tbody><tr><td>CPU</td><td><code>500m</code></td><td><code>1000m</code></td></tr><tr><td>Memory</td><td><code>2000Mi</code></td><td><code>2000Mi</code></td></tr></tbody></table></div>

<div class="kh-code"><div class="kh-code-label">yaml</div><pre class="kh-pre">resources:
  requests:
    cpu: 500m
    memory: 2000Mi
  limits:
    cpu: 1000m
    memory: 2000Mi</pre></div>

<div class="kh-note info"><p><code>worker.resources</code> 看起來是專案或 Helm Chart 的設定名稱，不能只憑名稱認定它等同 <code>requests</code>。本文以實際產出的 <code>resources.requests</code> 與 <code>resources.limits</code> 為準；Chart 對應仍待核對。</p></div>

<p><code>requests</code> 是 Container 宣告的資源需求。Scheduler 依此尋找容得下 Pod 的 Node；它不表示 Container 每一刻都會使用這麼多資源，也不表示預先占用一整塊專屬 CPU 或實體記憶體。</p>

<h3 class="kh-section">Node A：CPU 放得下，Memory 放不下</h3>

<p>假設 Node A 的 CPU capacity 為 <code>4000m</code>，Memory capacity 為 <code>8Gi</code>。實際排程比較的是 <code>allocatable</code>，通常會扣掉系統保留量；以下為簡化算例，暫以相同數字作為可分配上限。</p>

<div class="kh-table-scroll" role="region" aria-label="資源比較" tabindex="0"><table class="kh-table"><thead><tr><th scope="col">資源</th><th scope="col">既有 requests</th><th scope="col">新增需求</th><th scope="col">合計與結果</th></tr></thead><tbody><tr><td>CPU</td><td><code>3000m</code></td><td><code>500m</code></td><td><code>3500m ≤ 4000m</code>，足夠</td></tr><tr><td>Memory</td><td><code>7Gi = 7168Mi</code></td><td><code>2000Mi</code></td><td><code>9168Mi &gt; 8192Mi</code>，不足</td></tr></tbody></table></div>

<p><code>2000Mi = 1.953125Gi</code>，所以記憶體合計是 <code>8.953125Gi</code>。若將新增需求近似為 2Gi，合計便約為 9Gi。兩種算法的結論相同：Node A 無法容納這個 Pod。</p>

<div class="kh-capacity"><p><strong>CPU：3500 / 4000m</strong></p><div class="kh-track"><span style="width:75%" class="kh-used"></span><span style="width:12.5%" class="kh-new"></span></div><p>灰藍為既有 3000m，藍色為新增 500m，右側剩餘 500m。</p><p><strong>Memory：9168 / 8192Mi</strong></p><div class="kh-track"><span style="width:78.18%" class="kh-used"></span><span style="width:21.82%" class="kh-new"></span><span class="kh-boundary" style="left:89.35%"></span></div><p>灰藍為既有 7168Mi，藍色為新增 2000Mi；上限線右側超出 976Mi。兩條容量帶各自使用不同單位與尺度。</p></div>

<h3 class="kh-section">排程判斷：每一種資源都要足夠</h3>

<div class="kh-diagram"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;primaryColor&quot;: &quot;#eef4ff&quot;, &quot;primaryTextColor&quot;: &quot;#233650&quot;, &quot;primaryBorderColor&quot;: &quot;#326de6&quot;, &quot;lineColor&quot;: &quot;#526886&quot;, &quot;secondaryColor&quot;: &quot;#ffffff&quot;, &quot;tertiaryColor&quot;: &quot;#f5f8ff&quot;, &quot;clusterBkg&quot;: &quot;#f4f7ff&quot;, &quot;clusterBorder&quot;: &quot;#8eaade&quot;, &quot;fontSize&quot;: &quot;16px&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true}}" hidden>flowchart TD
R[&quot;Pod 宣告 CPU 500m / Memory 2000Mi&quot;] --&gt; C{&quot;Node A 的 CPU 足夠？&quot;}
C --&gt;|是| M{&quot;Node A 的 Memory 足夠？&quot;}
C --&gt;|否| N[&quot;排除此 Node，評估其他候選&quot;]
M --&gt;|否，本例| N
M --&gt;|是| O[&quot;資源條件通過，再檢查其他排程條件&quot;]</pre></div></div>

<p>本例依序確認 CPU 與 Memory。CPU 足夠、Memory 不足，故排除 Node A；若兩者都足夠，仍須通過其他排程條件。若沒有任何可用候選，Pod 可能維持 Pending。</p>

<p>資源申請與限制的依據見 <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">Kubernetes 資源管理文件</a>。</p>

</div>
<!-- endtab -->

<!-- tab limit-->
<div class="kubernetes-helm">
<div class="kh-hero"><img class="kh-logo" src="https://raw.githubusercontent.com/kubernetes/kubernetes/master/logo/logo.svg" alt="" aria-hidden="true" width="52" height="52"><h2>上限相同，CPU 與 Memory 的反應不同</h2><p>Pod 排進 Node 之後，仍需控制執行時的資源用量。CPU 額度不足通常造成等待，記憶體不足則可能使 Container 中的程序遭到終止。</p></div>

<div class="kh-table-scroll" role="region" aria-label="比較項目比較" tabindex="0"><table class="kh-table"><thead><tr><th scope="col">比較項目</th><th scope="col">CPU</th><th scope="col">Memory</th></tr></thead><tbody><tr><td>request</td><td><code>500m</code>，排程需求</td><td><code>2000Mi</code>，排程需求</td></tr><tr><td>limit</td><td><code>1000m</code>，即 1 CPU 的運算額度</td><td><code>2000Mi</code>，約 <code>1.953Gi</code></td></tr><tr><td>接近或超過限制</td><td>CPU 配額耗盡時 throttling，通常不直接因此殺掉程序</td><td>達到限制且無法滿足記憶體需求時，可能觸發 cgroup OOM</td></tr><tr><td>可見影響</td><td>執行變慢、延遲增加、吞吐下降</td><td>Container 狀態可能顯示 <code>Reason: OOMKilled</code></td></tr></tbody></table></div>

<h3 class="kh-section">CPU 配額刻度與 Memory 上限</h3>

<div class="kh-scale">
<p><strong>CPU：request 500m → limit 1000m</strong></p>
<div class="kh-ruler"><span>0</span><span>500m<br>request</span><span>1000m<br>limit</span></div>
<p>500m 是排程需求；Node 有餘裕時可使用更多 CPU，但仍受 1000m 的執行配額限制。</p>
<p><strong>Memory：request = limit = 2000Mi</strong></p>
<div class="kh-ruler memory"><span>0</span><span>1000Mi</span><span>2000Mi<br>request / limit</span></div>
<p>2000Mi 約等於 1.953Gi。兩個欄位數值相同，但排程需求與執行上限仍是不同角色。</p>
</div>

<h3 class="kh-section">Memory 使用量逐漸增加時</h3>

<div class="kh-diagram"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;primaryColor&quot;: &quot;#eef4ff&quot;, &quot;primaryTextColor&quot;: &quot;#233650&quot;, &quot;primaryBorderColor&quot;: &quot;#326de6&quot;, &quot;lineColor&quot;: &quot;#526886&quot;, &quot;secondaryColor&quot;: &quot;#ffffff&quot;, &quot;tertiaryColor&quot;: &quot;#f5f8ff&quot;, &quot;clusterBkg&quot;: &quot;#f4f7ff&quot;, &quot;clusterBorder&quot;: &quot;#8eaade&quot;, &quot;fontSize&quot;: &quot;16px&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true}}" hidden>flowchart TD
A[&quot;任務執行，Memory 用量增加&quot;] --&gt; B[&quot;逐漸接近 2000Mi 上限&quot;]
B --&gt; C{&quot;記憶體需求能否滿足？&quot;}
C --&gt;|可以，例如回收後足夠| D[&quot;繼續執行&quot;]
C --&gt;|無法滿足，觸發 cgroup OOM| E[&quot;程序可能被終止&quot;]
E --&gt; F[&quot;Container 可能顯示 OOMKilled&quot;]</pre></div></div>

<p>這是概念示意，沒有實測時間軸。使用量可從 0、約 1Gi 逐漸接近約 2Gi；精確上限為 2000Mi，不是一碰到線就必定立刻 OOMKilled。</p>

<div class="kh-note warn"><p>Memory limit 的執行帶有反應式特性；是否觸發 OOM 與當下記憶體需求、回收及核心處理有關。Container 後續是否重啟，還要看工作負載與重啟政策。</p></div>

<p>CPU 的 <code>1000m</code> 表示 1 CPU 單位，依環境可對應實體核心或虛擬 CPU，不代表專屬綁定一顆實體核心。本文的限制行為以一般 Linux Container 環境說明。</p>

</div>
<!-- endtab -->

<!-- tab HPA 設定-->
<div class="kubernetes-helm">
<div class="kh-hero"><img class="kh-logo" src="https://raw.githubusercontent.com/kubernetes/kubernetes/master/logo/logo.svg" alt="" aria-hidden="true" width="52" height="52"><h2>增加副本，分擔可平行處理的工作</h2><p>HPA 調整的是 Worker 副本數。它可以增加整體處理能力，但新增 Pod 不會自動提高既有 Container 的記憶體上限。</p></div>

<h3 class="kh-section">案例設定與利用率基準</h3>

<div class="kh-table-scroll" role="region" aria-label="設定比較" tabindex="0"><table class="kh-table"><thead><tr><th scope="col">設定</th><th scope="col">案例值</th><th scope="col">用途</th></tr></thead><tbody><tr><td><code>enabled</code></td><td><code>true</code></td><td>專案設定啟用 HPA</td></tr><tr><td><code>minReplicas</code></td><td><code>2</code></td><td>副本下限</td></tr><tr><td><code>maxReplicas</code></td><td><code>4</code></td><td>副本上限</td></tr><tr><td><code>targetCPUUtilizationPercentage</code></td><td><code>90</code></td><td>CPU 目標利用率 90%</td></tr><tr><td><code>targetMemoryUtilizationPercentage</code></td><td><code>70</code></td><td>Memory 目標利用率 70%</td></tr></tbody></table></div>

<div class="kh-note info"><p>以上是案例中的專案設定名稱，不是可直接套用的 HPA manifest。CPU 與 Memory 多指標通常使用 <code>autoscaling/v2</code> 的 <code>spec.metrics</code>；實際啟用與欄位映射應核對 Chart 產物。</p></div>

<p>本例假設 HPA 使用資源利用率指標。百分比以 <code>requests</code> 為基準：CPU 的 <code>90% × 500m = 450m</code>，Memory 的 <code>70% × 2000Mi = 1400Mi</code>。這些是目標平均值，不是 limits，也不是單一 Pod 的強制擴容線。</p>

<p>HPA 綜合目標工作負載中符合計算條件的 Pod 資料，不是任一 Pod 一超線就必定擴容。就資源利用率而言，可用資料中的「總使用量 ÷ 總 request」反映加權利用率；requests 相同時，才可直接理解為各 Pod 百分比的算術平均。缺失指標、未就緒 Pod 等還會影響實際計算。</p>

<h3 class="kh-section">先用簡化公式理解副本數</h3>

<div class="kh-code"><div class="kh-code-label">text</div><pre class="kh-pre">desiredReplicas = ceil(currentReplicas × currentMetricValue / desiredMetricValue)</pre></div>

<p><code>currentMetricValue</code> 是目前利用率，<code>desiredMetricValue</code> 是目標利用率；<code>ceil</code> 表示向上取整。下面兩組都從 2 個 Pod 開始，先展示理想公式，再補上實際控制條件。</p>

<div class="kh-table-scroll" role="region" aria-label="情境比較" tabindex="0"><table class="kh-table"><thead><tr><th scope="col">情境</th><th scope="col">CPU 計算</th><th scope="col">Memory 計算</th><th scope="col">判讀</th></tr></thead><tbody><tr><td>平均 CPU 70%、Memory 65%</td><td><code>ceil(2 × 70 / 90) = 2</code></td><td><code>ceil(2 × 65 / 70) = 2</code></td><td>維持 2 個 Pod</td></tr><tr><td>平均 CPU 95%、Memory 80%</td><td><code>ceil(2 × 95 / 90) = 3</code></td><td><code>ceil(2 × 80 / 70) = 3</code></td><td>簡化公式均為 3；實際擴容依下方條件判斷</td></tr></tbody></table></div>

<div class="kh-note warn"><p>預設 10% 容忍範圍下，CPU 比值 <code>95 / 90 ≈ 1.056</code> 仍在容忍範圍內，因此不會只因這個 CPU 值就擴容。Memory 比值 <code>80 / 70 ≈ 1.143</code> 超出範圍，在指標有效、其他條件允許時可建議 3 個副本。最終仍受擴縮政策、穩定視窗與副本上下限影響。</p></div>

<h3 class="kh-section">從多個指標得到一個副本建議</h3>

<div class="kh-diagram"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;primaryColor&quot;: &quot;#eef4ff&quot;, &quot;primaryTextColor&quot;: &quot;#233650&quot;, &quot;primaryBorderColor&quot;: &quot;#326de6&quot;, &quot;lineColor&quot;: &quot;#526886&quot;, &quot;secondaryColor&quot;: &quot;#ffffff&quot;, &quot;tertiaryColor&quot;: &quot;#f5f8ff&quot;, &quot;clusterBkg&quot;: &quot;#f4f7ff&quot;, &quot;clusterBorder&quot;: &quot;#8eaade&quot;, &quot;fontSize&quot;: &quot;16px&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true}}" hidden>flowchart TD
S[&quot;取得工作負載的資源指標&quot;] --&gt; C[&quot;CPU 利用率，以 request 為基準&quot;]
S --&gt; M[&quot;Memory 利用率，以 request 為基準&quot;]
C --&gt; CA[&quot;套用容忍範圍與有效資料調整&quot;]
M --&gt; MA[&quot;套用容忍範圍與有效資料調整&quot;]
CA --&gt; X[&quot;比較各指標的建議副本數，取最大值&quot;]
MA --&gt; X
X --&gt; P[&quot;套用穩定視窗、擴縮政策與 2～4 副本限制&quot;]
P --&gt; D{&quot;最終建議是否改變？&quot;}
D --&gt;|否| K[&quot;維持目前副本數&quot;]
D --&gt;|增加或減少| U[&quot;更新目標工作負載的副本數&quot;]</pre></div></div>

<p>圖示表達多指標匯合與控制條件，不代表控制器逐行實作順序。CPU 與 Memory 分別評估後，取最大的副本建議；再綜合政策及 2～4 的上下限。副本目標改變也不保證新 Pod 立即 Ready。</p>

<p>若部分指標取得失敗，而其他指標建議縮容，HPA 可能跳過縮容；有效指標若建議擴容，仍可能擴容。實際行為應查看 HPA 的條件與事件。</p>

<h3 class="kh-section">為何按比例調整，而不是每次只加一個？</h3>

<ul><li>在總負載可分攤且近似不變的假設下，平均負載若是目標的 2 倍，副本理論上也需要約 2 倍。</li><li>平均負載若是目標的 1/2，副本理論上可縮成約 1/2，但仍受下限與縮容控制限制。</li><li>每個 Pod request 相同時，「目前副本數 × 平均利用率」可理解為各 Pod 利用率的總和；request 不同時不能直接套用這個直觀解釋。</li><li>工作量多、每個任務耗用資源高，且負載反映在平均 CPU／Memory 指標上時，可能推動擴容；僅有 Queue 積壓不保證這兩種指標會升高。</li></ul>

<h3 class="kh-section">單一任務太大時，增加 Pod 仍可能無效</h3>

<p>若單一 job 的記憶體需求已超過一個 Container 的上限，只增加副本通常無法讓這個 job 執行成功。HPA 改善的是可分攤的總量與吞吐；單一工作的峰值仍需另外處理。</p>

<div class="kh-table-scroll" role="region" aria-label="改善方向比較" tabindex="0"><table class="kh-table"><thead><tr><th scope="col">改善方向</th><th scope="col">處理的問題</th></tr></thead><tbody><tr><td>調大單 Pod 主要 Container 的記憶體 request／limit</td><td>先讓單一 job 有足夠空間；同步確認 Node 能否容納</td></tr><tr><td>將 job 切批或分段</td><td>降低單次峰值記憶體</td></tr><tr><td>降低同 Pod 併發</td><td>避免多個重型 job 的峰值疊加</td></tr><tr><td>分離獨立 Worker group 與資源規格</td><td>讓重型 job 使用適合的資源配置</td></tr></tbody></table></div>

<p>公式、容忍範圍、多指標及擴縮政策依據見 <a href="https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/">Kubernetes HPA 文件</a>。本文未取得實際叢集版本與 HPA manifest，因此案例保留明確假設。</p>

</div>
<!-- endtab -->

<!-- tab worker-->
<div class="kubernetes-helm">
<div class="kh-hero"><img class="kh-logo" src="https://raw.githubusercontent.com/kubernetes/kubernetes/master/logo/logo.svg" alt="" aria-hidden="true" width="52" height="52"><h2>多個任務，共享同一個 Worker 的資源</h2><p>這裡討論的是常駐 Worker 從 Queue 取件的架構。一個 Pod 可承載一個主要 Worker 實例，而一個 Worker Container 內又可能同時處理多個任務。</p></div>

<div class="kh-table-scroll" role="region" aria-label="名詞比較" tabindex="0"><table class="kh-table"><thead><tr><th scope="col">名詞</th><th scope="col">本文情境</th></tr></thead><tbody><tr><td>Pod</td><td>Kubernetes 的執行與排程單位；本例每個 Pod 有一個主要 Worker Container</td></tr><tr><td>Container</td><td>執行常駐 Worker 程式，持續從 Queue 拉取工作</td></tr><tr><td>job</td><td>Worker 處理的應用層任務；不是為每個任務新增一個 Container，也不等同 Kubernetes 的 Job 物件</td></tr></tbody></table></div>

<h3 class="kh-section">兩個 Pod，共用一個工作來源</h3>

<div class="kh-diagram"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;primaryColor&quot;: &quot;#eef4ff&quot;, &quot;primaryTextColor&quot;: &quot;#233650&quot;, &quot;primaryBorderColor&quot;: &quot;#326de6&quot;, &quot;lineColor&quot;: &quot;#526886&quot;, &quot;secondaryColor&quot;: &quot;#ffffff&quot;, &quot;tertiaryColor&quot;: &quot;#f5f8ff&quot;, &quot;clusterBkg&quot;: &quot;#f4f7ff&quot;, &quot;clusterBorder&quot;: &quot;#8eaade&quot;, &quot;fontSize&quot;: &quot;16px&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true}}" hidden>flowchart TD
Q[&quot;共用 Queue / 工作來源&quot;]
subgraph P1[&quot;Pod 1&quot;]
W1[&quot;Worker Container 1&quot;]
end
subgraph P2[&quot;Pod 2&quot;]
W2[&quot;Worker Container 2&quot;]
end
W1 --&gt;|拉取工作| Q
W2 --&gt;|拉取工作| Q</pre></div></div>

<p>一個 Pod 可視為一個常駐 Worker 實例，兩個 Pod 就有兩個實例。箭頭代表 Worker 主動取件的關係，不表示 Queue 主動推送，也不表示任務平均分配。實際分配依 Queue／consumer 機制決定；group 是否對應同一佇列仍須看實作。</p>

<h3 class="kh-section">放大一個 Pod：任務共享資源配額</h3>

<div class="kh-diagram"><div class="mermaid-wrap"><pre class="mermaid-src" data-config="{&quot;theme&quot;: &quot;base&quot;, &quot;themeVariables&quot;: {&quot;primaryColor&quot;: &quot;#eef4ff&quot;, &quot;primaryTextColor&quot;: &quot;#233650&quot;, &quot;primaryBorderColor&quot;: &quot;#326de6&quot;, &quot;lineColor&quot;: &quot;#526886&quot;, &quot;secondaryColor&quot;: &quot;#ffffff&quot;, &quot;tertiaryColor&quot;: &quot;#f5f8ff&quot;, &quot;clusterBkg&quot;: &quot;#f4f7ff&quot;, &quot;clusterBorder&quot;: &quot;#8eaade&quot;, &quot;fontSize&quot;: &quot;16px&quot;}, &quot;flowchart&quot;: {&quot;htmlLabels&quot;: false, &quot;useMaxWidth&quot;: true}}" hidden>flowchart TD
subgraph P[&quot;單一 Pod&quot;]
subgraph C[&quot;主要 Worker Container&quot;]
J1[&quot;任務甲&quot;] --&gt;|共同耗用| R[&quot;CPU limit 1000m / Memory limit 2000Mi&quot;]
J2[&quot;任務乙&quot;] --&gt;|共同耗用| R
J3[&quot;其他並行任務&quot;] --&gt;|共同耗用| R
end
end</pre></div></div>

<p>任務甲、任務乙與其他任務位於同一個 Container 內，箭頭表示共同耗用資源，沒有先後順序。圖中的任務數僅供示意，不代表實際併發設定，也不是 Pod 內有三個 Container。</p>

<h3 class="kh-section">併發量由多層限制共同決定</h3>

<p>單一 Worker 能同時處理多少 job，不能只看 <code>Thread Count</code>。以下列出案例中的四層限制；專案欄位的作用範圍仍需以 Worker 平台文件或程式碼確認。</p>

<div class="kh-table-scroll" role="region" aria-label="限制層比較" tabindex="0"><table class="kh-table"><thead><tr><th scope="col">限制層</th><th scope="col">設定或條件</th><th scope="col">需要核對的範圍</th></tr></thead><tbody><tr><td>Group</td><td><code>Thread Count</code></td><td>案例假設為整個 group 的總併發上限；確認是否跨 Pod 共用</td></tr><tr><td>Job</td><td><code>Max Processes</code></td><td>案例假設為該 job 的併發上限；確認是否跨 Worker 統計</td></tr><tr><td>Worker 程式</td><td>consumer concurrency／prefetch／thread pool</td><td>處理併發、預取與執行緒是不同限制；prefetch 不直接等於同時執行數</td></tr><tr><td>執行拓撲</td><td>當下可用 Pod 數量與調度分配</td><td>確認任務分配、可用實例與資源限制</td></tr></tbody></table></div>

<p>單 Pod 的實際併發是這些條件共同作用的結果，不能直接由單一欄位推算，也不能把 group 上限直接乘上 Pod 數量。</p>

<h3 class="kh-section">多個任務並行時，會互相影響</h3>

<ul><li>某個 job 消耗較多 CPU，其他 job 的延遲可能增加、吞吐可能下降。</li><li>合計 CPU 用量耗盡 limit 配額時，可能發生 throttling。</li><li>多個記憶體重型 job 疊加會增加記憶體壓力，嚴重時可能造成 OOMKilled，影響同一 Container 內的工作。</li></ul>

<div class="kh-note info"><p>判斷瓶頸時，同時觀察單一任務的資源峰值、單 Pod 併發與可用副本數。調大 Container、降低併發與增加 Pod 各自處理不同問題，應依實際瓶頸選擇。</p></div>

<p>圖示來源：<a href="https://github.com/kubernetes/kubernetes/tree/master/logo">Kubernetes 專案 Logo</a>。本文圖表為案例說明，不代表已驗證的正式環境拓撲。</p>

</div>
<!-- endtab -->

{% endtabs %}
