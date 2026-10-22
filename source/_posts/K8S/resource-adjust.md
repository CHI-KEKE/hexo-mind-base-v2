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

{% tabs resource-adjust %}

<!-- tab 狀況發生!-->

<style>
.kubernetes-helm{--kh-blue:#326de6;--kh-link:#2455b5;--kh-bg:#fff;--kh-ink:#333;--kh-soft:#eef4ff;--kh-line:#d5deed;--kh-code:#182235;--kh-code-ink:#f3f6fc;background:var(--kh-bg);color:var(--kh-ink);padding:24px;font-family:'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif;line-height:1.85;overflow-wrap:anywhere;}
.kubernetes-helm *{box-sizing:border-box;}
#article-container .kubernetes-helm h2,#article-container .kubernetes-helm h3,.kubernetes-helm h2,.kubernetes-helm h3{color:var(--kh-ink);line-height:1.4;font-weight:800;margin:0 0 16px;}
.kubernetes-helm p{margin:12px 0;}
.kubernetes-helm a{color:var(--kh-link);text-decoration:underline;text-underline-offset:3px;}
.kubernetes-helm :focus-visible{outline:3px solid var(--kh-link);outline-offset:4px;}
.kubernetes-helm code{font-family:Consolas,monospace;background:var(--kh-soft);color:inherit;padding:2px 5px;border-radius:3px;}
.kubernetes-helm .kh-hero{padding:28px 0 32px;margin-bottom:28px;border-bottom:3px solid var(--kh-blue);}
.kubernetes-helm .kh-emblem{display:block;width:58px;height:58px;margin-bottom:20px;background:var(--kh-blue);clip-path:polygon(50% 0,89% 19%,99% 61%,72% 96%,28% 96%,1% 61%,11% 19%);}
.kubernetes-helm .kh-hero h2{font-size:clamp(1.6rem,4vw,2.6rem);letter-spacing:-.02em;}
.kubernetes-helm .kh-hero p{max-width:42em;}
.kubernetes-helm .kh-section{padding-left:14px;border-left:5px solid var(--kh-blue);margin-top:30px;}
.kubernetes-helm .kh-note{padding:16px 20px;margin:22px 0;background:var(--kh-soft);border-left:4px solid var(--kh-blue);border-radius:4px;}
.kubernetes-helm .kh-table-scroll{max-width:100%;overflow-x:auto;margin:22px 0;}
#article-container .kubernetes-helm table.kh-table,.kubernetes-helm table.kh-table{width:100%;margin:0;border-collapse:collapse;table-layout:auto;background:var(--kh-bg);color:var(--kh-ink);}
.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{padding:12px 16px;border:1px solid var(--kh-line);text-align:left;vertical-align:top;background:var(--kh-bg);color:var(--kh-ink);}
.kubernetes-helm .kh-table th{background:var(--kh-soft);font-weight:700;}
.kubernetes-helm .kh-code{margin:24px 0;background:var(--kh-code);color:var(--kh-code-ink);border-radius:4px;overflow:hidden;}
.kubernetes-helm .kh-code-label{padding:8px 16px;border-bottom:1px solid #43516a;font-size:.85rem;}
#article-container .kubernetes-helm pre.kh-pre,.kubernetes-helm pre.kh-pre{margin:0!important;padding:18px!important;background:var(--kh-code)!important;color:var(--kh-code-ink)!important;border:0!important;border-radius:0!important;box-shadow:none!important;text-shadow:none!important;white-space:pre!important;overflow-x:auto!important;font:14px/1.8 Consolas,monospace!important;}
.kubernetes-helm pre.kh-pre code{background:transparent;color:inherit;padding:0;}
[data-theme='dark'] .kubernetes-helm{--kh-blue:#7fa9ff;--kh-link:#a4c2ff;--kh-bg:#17202e;--kh-ink:#eef2f8;--kh-soft:#23334e;--kh-line:#52647f;}
@media(max-width:600px){.kubernetes-helm{padding:16px;}.kubernetes-helm .kh-hero{padding:16px 0 24px;}.kubernetes-helm .kh-note{padding:14px;}.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{padding:10px;min-width:8em;}}

#article-container .kubernetes-helm table.kh-table{width:auto;max-width:100%;}
.kubernetes-helm .kh-diagram{overflow-x:auto;border:1px solid var(--kh-line);border-radius:4px;margin:22px 0;padding:16px;background:var(--kh-bg);}
.kubernetes-helm .kh-diagram .mermaid{min-width:540px;}
.kubernetes-helm .kh-diagram svg{min-width:540px;max-width:none!important;}
.kubernetes-helm .kh-diagram p{font-size:.9em;color:var(--kh-ink);}
#article-container .kubernetes-helm .kh-diagram svg{background:var(--kh-bg)!important;}
#article-container .kubernetes-helm .kh-diagram svg .node rect{fill:var(--kh-soft)!important;stroke:var(--kh-blue)!important;}
#article-container .kubernetes-helm .kh-diagram svg .nodeLabel,#article-container .kubernetes-helm .kh-diagram svg .nodeLabel p,#article-container .kubernetes-helm .kh-diagram svg .nodeLabel span{color:var(--kh-ink)!important;fill:var(--kh-ink)!important;}
#article-container .kubernetes-helm .kh-diagram svg .cluster rect{fill:var(--kh-bg)!important;stroke:var(--kh-line)!important;}
#article-container .kubernetes-helm pre.kh-pre{tab-size:4;}
.kubernetes-helm .kh-section{margin-top:32px!important;}
@media(max-width:600px){.kubernetes-helm{padding:12px;}.kubernetes-helm .kh-diagram{padding:8px;}.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{min-width:7em;}}

#article-container .kubernetes-helm .kh-diagram svg .node polygon{fill:var(--kh-soft)!important;stroke:var(--kh-blue)!important;}
.kubernetes-helm .kh-diagram svg{min-width:620px;}
</style>

<div class="kubernetes-helm">

<div class="kh-hero"><span class="kh-emblem" aria-hidden="true"></span><h2>Kubernetes 資源調整：從配額到可用副本</h2><p>服務想增加一個副本，卻被資源配額擋下。調整 CPU 時，需要分清楚允許申請多少、Node 還能排入多少，以及程式當下實際用了多少。</p></div>

<h3 class="kh-section">原始錯誤訊息</h3>

<div class="kh-code">
<div class="kh-code-label"><span>Pod 建立失敗紀錄</span></div>
<pre class="kh-pre">pods &quot;promotion-web-api-76d9db5667-8wxfr&quot; is forbidden: exceeded quota: default-4w42q, requested: limits.cpu=2250m, used: limits.cpu=7250m, limited: limits.cpu=8:Deployment does not have minimum availability.</pre>
</div>

<p>這段紀錄同時呈現三個層面：ResourceQuota 超限、Pod 建立遭到拒絕，以及 Deployment 未達最低可用性。先解讀配額欄位，再檢查 Deployment 的實際狀態。</p>

<div class="kh-table-scroll" role="region" aria-label="訊息欄位比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">訊息欄位</th><th scope="col">意義</th></tr></thead>
<tbody>

<tr><td><code>pods &quot;promotion-web-api-76d9db5667-8wxfr&quot; is forbidden</code></td><td>Kubernetes API Server 拒絕這次 Pod 建立請求，這個新 Pod 尚未成功建立。</td></tr>

<tr><td><code>exceeded quota: default-4w42q</code></td><td>Namespace 中名為 default-4w42q 的 ResourceQuota 不允許這次新增。</td></tr>

<tr><td><code>requested: limits.cpu=2250m</code></td><td>這次新增會計入 2250m，即 2.25 CPU 的 limits.cpu 配額。此處 requested 是配額增量，不是 resources.requests.cpu。</td></tr>

<tr><td><code>used: limits.cpu=7250m</code></td><td>已有 7250m，即 7.25 CPU 的 limits.cpu 被計入配額；不是當下實際消耗 7.25 CPU。</td></tr>

<tr><td><code>limited: limits.cpu=8</code></td><td>Namespace 的 limits.cpu 配額上限是 8 CPU，即 8000m。</td></tr>

<tr><td><code>Deployment does not have minimum availability</code></td><td>Deployment 的可用副本未達最低要求，需再查看 replicas、Available condition 與更新策略。</td></tr>

</tbody>
</table>
</div>

<div class="kh-note"><p>配額計算：7250m + 2250m = 9500m &gt; 8000m。原本只剩 750m 的 limits.cpu 配額，這次新增需要 2250m，因此超出 1500m。即使 Node 還有空閒 CPU，也無法繞過這項配額檢查。</p></div>



<p><a href="https://kubernetes.io/docs/concepts/policy/resource-quotas/">Kubernetes：ResourceQuota</a>；<a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/">Kubernetes：Deployment 可用性</a></p>

</div>
<!-- endtab -->

<!-- tab 資源調整的觀察-->

<div class="kubernetes-helm">

<h3 class="kh-section">調整設定後，要一起觀察哪些變化</h3>

<div class="kh-table-scroll" role="region" aria-label="觀察項目比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">觀察項目</th><th scope="col">應核對的內容</th></tr></thead>
<tbody>

<tr><td>resource request 下降／上升</td><td>調整前後的 Pod requests、排程容量，以及 HPA 的 CPU Utilization 分母是否改變。</td></tr>

<tr><td>Node 數量減少／增加</td><td>是否啟用 Node 自動擴縮、是否有排不進去的 Pods，以及是否符合擴容或整併條件；request 與 Node 數量不是固定比例。</td></tr>

<tr><td>是否 Throttled</td><td>是否用完 CPU limit 對應配額；同時區分 Node CPU 競爭與應用程式負載。</td></tr>

<tr><td>limits 是否正常套用</td><td>比對 chart、pipeline 產出、Deployment template 與實際 Pod 的 resources，不能只看設定檔。</td></tr>

</tbody>
</table>
</div>

<h3 class="kh-section">原始維運紀錄</h3>

<p>原稿記錄曾遇到 limits 沒有正常套用，當時在 Rancher 手動調整 limits；另記錄 chart 檔的 limits 需要使用 pipeline <code>v1.3.3-stable</code> 以上版本。</p>

<div class="kh-note"><p>以上是內部環境的原始觀察，不是 Kubernetes 的通用版本要求。尚未查核內部討論的完整內容，也未確認目前 pipeline 是否仍有相同限制。</p></div>

<p><a href="https://91app.slack.com/archives/CJHPX1DGF/p1746165782611889">內部討論來源：資源調整與 pipeline</a></p>

</div>
<!-- endtab -->

<!-- tab request 寫 500m 的意義-->

<div class="kubernetes-helm">

<h3 class="kh-section">request 寫 500m，代表什麼</h3>

<p><code>request: 500m</code> 表示排程時要計入 0.5 CPU 的需求，不是建立一台只有 0.5 CPU 的小主機。以下假設 Pod 只有一個應用容器。</p>

<div class="kh-code">
<div class="kh-code-label"><span>容器的 CPU 設定</span></div>
<pre class="kh-pre">resources:
  requests:
    cpu: 500m
  limits:
    cpu: 2000m</pre>
</div>

<div class="kh-table-scroll" role="region" aria-label="當下情況比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">當下情況</th><th scope="col">可能的 CPU 使用量</th></tr></thead>
<tbody>

<tr><td>沒什麼請求</td><td>可能只用 20m，不會固定消耗 500m。</td></tr>

<tr><td>工作變多，Node 有空閒 CPU</td><td>可以用到 800m、1500m。</td></tr>

<tr><td>用完 2000m limit 對應的 CPU 配額</td><td>受到 CPU limit 限速，等待後續配額週期。</td></tr>

</tbody>
</table>
</div>

<p>這個容器申請 0.5 CPU 的排程容量，最高允許使用 2 CPU；實際使用量取決於工作量與可用資源。一般情況下，這不代表綁定半顆專屬 CPU。</p>

<div class="kh-table-scroll" role="region" aria-label="request 的用途比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">request 的用途</th><th scope="col">影響</th></tr></thead>
<tbody>

<tr><td>排入 Node</td><td>Scheduler 確認單台 Node 的剩餘可排程容量足以容納 500m，並符合其他資源與排程條件。</td></tr>

<tr><td>CPU 發生競爭</td><td>影響容器取得 CPU 時間的相對權重，不是忙碌時固定限制在 500m。</td></tr>

<tr><td>HPA 使用 CPU Utilization</td><td>request 是使用率分母，例如實際 400m ÷ request 500m = 80%。</td></tr>

</tbody>
</table>
</div>

<h3 class="kh-section">訂位容量與實際使用量</h3>

<p>可以把 request 想成訂位，實際 CPU 使用量則是當下有多少人在使用。以下假設一台 Node 扣除其他需求後，有 <code>4000m</code> 可供這批 Pods 排程，且只考慮 CPU。</p>

<div class="kh-table-scroll" role="region" aria-label="情境比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">情境</th><th scope="col">結果</th></tr></thead>
<tbody>

<tr><td>每個 Pod request 為 500m</td><td>4000m ÷ 500m = 8，最多容納 8 個。</td></tr>

<tr><td>8 個 Pod 當下各只用 10m</td><td>實際合計 80m，但 requests 合計仍是 4000m。</td></tr>

<tr><td>再新增第 9 個相同的 Pod</td><td>這台 Node 的 CPU 排程容量已滿，需找其他符合條件的 Node。</td></tr>

</tbody>
</table>
</div>

<p>排程時按申報的需求計算，可以避免因平時使用量低就把太多 Pods 塞在同一台 Node。實際還要考慮 Memory、Pod 數量上限、系統保留資源及其他排程限制。</p>

<h3 class="kh-section">request 設太大或太小的影響</h3>

<p>設定 <code>requests.cpu: 500m</code> 後，Scheduler 尋找有足夠容量且符合條件的 Node。成功排入後，這份需求就會被計入；找不到合適 Node 時，Pod 可能維持 <code>Pending</code>。</p>

<div class="kh-note"><p>CPU request 若設得過大，會壓縮共用這批 Node 的其他服務新增 Pod 或擴容的空間。即使 Node 實際 CPU 使用率只有 10%，也可能因 requests 接近可排程容量而放不進新 Pod。若啟用 Node 自動擴縮，還可能提早新增 Node、增加成本。</p></div>

<p>request 設得過小，則可能讓太多 Pods 擠在一起，忙碌時競爭 CPU。request 是容量規劃與分配的依據，limit 是執行時的使用上限。</p>

<p><a href="https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/">Kubernetes：CPU 資源分配</a>；<a href="https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/">Kubernetes：HPA 計算方式</a></p>

</div>
<!-- endtab -->

<!-- tab limits-->

<div class="kubernetes-helm">

<h3 class="kh-section">排程只剩 1m，為什麼還能使用更多 CPU</h3>

<p>假設新的 Pod request 是 <code>500m</code>、limit 是 <code>1000m</code>，排入後 Node 的排程容量只剩 <code>1m</code>。這個數字代表尚未被 requests 占用的容量，不是 CPU 當下只剩 1m 能運算。</p>

<p>以下假設 Node 可排程 CPU 共 <code>2000m</code>。其他 Pods 雖然申報較高的需求，當下未必全部用完。</p>

<div class="kh-table-scroll" role="region" aria-label="項目比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">項目</th><th scope="col">CPU request</th><th scope="col">當下實際使用示例</th></tr></thead>
<tbody>

<tr><td>其他 Pods 合計</td><td>1499m</td><td>600m</td></tr>

<tr><td>新 Pod</td><td>500m</td><td>1000m</td></tr>

<tr><td>合計</td><td>1999m</td><td>1600m</td></tr>

</tbody>
</table>
</div>

<p>排程容量剩下 <code>2000m − 1999m = 1m</code>，但實際使用只有 <code>1600m</code>，所以此例中新 Pod 仍可使用到 <code>1000m</code>。這是假設當下有足夠 CPU 的示例，limit 不保證一定能取得這麼多 CPU。</p>

<h3 class="kh-section">其他 Pods 忙起來，是否就會 throttling</h3>

<div class="kh-table-scroll" role="region" aria-label="情況比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">情況</th><th scope="col">發生什麼事</th></tr></thead>
<tbody>

<tr><td>Node 的 CPU 不夠大家同時使用</td><td>發生 CPU 競爭，容器需等待 CPU 執行時間；request 影響分配權重，即使未達 limit 也可能變慢。</td></tr>

<tr><td>容器用完自己的 CPU limit 配額</td><td>發生 CPU throttling，等待後續配額週期；即使 Node 還有空閒 CPU，也可能發生。</td></tr>

</tbody>
</table>
</div>

<p>其他 Pods 忙起來，不代表這個 Pod 一定觸發 limit throttling。它可能只是分到的 CPU 時間減少，兩種情況也可能同時存在。request <code>500m</code> 並不是一忙起來就強制限制在 500m。</p>

<p><a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">Kubernetes：requests 與 limits 的執行方式</a></p>

</div>
<!-- endtab -->

<!-- tab Node-->

<div class="kubernetes-helm">

<h3 class="kh-section">Node 不屬於某個 namespace</h3>

<p>Node 屬於整個 Cluster，namespace 本身沒有固定分配幾台 Node。同一台 Node 可以同時執行不同 namespace 的 Pods。</p>

<div class="kh-table-scroll" role="region" aria-label="Node比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">Node</th><th scope="col">可能執行的 Pods</th></tr></thead>
<tbody>

<tr><td>Node 1</td><td>namespace A 的 Pod、namespace B 的 Pod</td></tr>

<tr><td>Node 2</td><td>namespace A 的 Pod、namespace C 的 Pod</td></tr>

<tr><td>Node 3</td><td>namespace B 的 Pod</td></tr>

</tbody>
</table>
</div>

<p><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes：Namespaces</a></p>

<h3 class="kh-section">Namespace 配額不是預留的 Node 容量</h3>

<p>Namespace 的 CPU／Memory request 上限通常由管理員透過 <code>ResourceQuota</code> 設定，不是每個 namespace 自動就有。以下是 namespace A 的配額片段。</p>

<div class="kh-code">
<div class="kh-code-label"><span>ResourceQuota 的 hard 設定片段</span></div>
<pre class="kh-pre">hard:
  requests.cpu: &quot;4&quot;
  requests.memory: 8Gi</pre>
</div>

<p>受配額計算的 Pods，其 CPU requests 合計不得超過 <code>4 CPU</code>，Memory requests 合計不得超過 <code>8Gi</code>。這是申請資源總額的上限，不表示已預留 4 CPU，也不表示分配了幾台 Node。</p>

<div class="kh-table-scroll" role="region" aria-label="阻擋位置比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">阻擋位置</th><th scope="col">情況</th><th scope="col">結果</th></tr></thead>
<tbody>

<tr><td>配額檢查</td><td>namespace 配額已滿，即使 Node 還有空間。</td><td>新 Pod 的建立請求被拒絕，不是先建立成 Pending。</td></tr>

<tr><td>排程</td><td>配額允許建立，但找不到符合需求的 Node。</td><td>Pod 已建立，可能維持 Pending。</td></tr>

</tbody>
</table>
</div>

<h3 class="kh-section">從配額檢查到 Node 擴容</h3>

<h4>Pod 建立與排程的不同關卡</h4>
<div class="kh-diagram">

{% mermaid %}
flowchart TB
Create["建立 Pod 的請求"] --> Quota{"配額允許嗎？"}
Quota -->|否| Reject["拒絕建立：Forbidden"]
Quota -->|是| Admit["Pod 建立成功"]
Admit --> Fit{"有合適 Node 且容量足夠？"}
Fit -->|是| Schedule["排程到 Node"]
Fit -->|否| Pending["Pending：等待排程"]
Pending --> Auto{"已啟用且可擴容？"}
Auto -->|是| New["新增合適 Node"]
New --> Fit
Auto -->|否| Wait["等待容量釋放或條件改善"]
{% endmermaid %}

</div>


<p>啟用 Cluster Autoscaler 或 Karpenter 等 Node 自動擴縮工具後，工具可評估排不進去的 Pods，判斷新增 Node 能否解決需求；符合擴容設定且未達上限時，才新增合適 Node，再由 Scheduler 排程。</p>

<div class="kh-note"><p>不是所有 Pending 都會觸發加 Node。排程條件無法滿足、已達擴容上限，或雲端容量不足，都可能無法擴容。減少 Node 則還需符合整併、搬移與中斷限制，不能只看 request 是否下降。</p></div>

<p><a href="https://kubernetes.io/docs/concepts/policy/resource-quotas/">Kubernetes：ResourceQuota</a>；<a href="https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/">Kubernetes：Node 自動擴縮</a></p>

</div>
<!-- endtab -->

<!-- tab HPA-->

<div class="kubernetes-helm">

<h3 class="kh-section">CPU Utilization 的分母是 request</h3>

<p>HPA 若使用 CPU <code>Utilization</code> 百分比，會將 CPU 使用量相對於 request 計算，再依符合條件的 Pods 彙整。以下用單一容器、資料齊全的 Pod 說明。</p>

<div class="kh-code">
<div class="kh-code-label"><span>單一 Pod 的使用率示意</span></div>
<pre class="kh-pre">HPA CPU 使用率 = 實際 CPU 使用量 ÷ CPU request × 100%</pre>
</div>

<div class="kh-table-scroll" role="region" aria-label="實際 CPU 使用量比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">實際 CPU 使用量</th><th scope="col">CPU request</th><th scope="col">相對使用率</th></tr></thead>
<tbody>

<tr><td>400m</td><td>500m</td><td>80%</td></tr>

<tr><td>400m</td><td>1000m</td><td>40%</td></tr>

</tbody>
</table>
</div>

<p>提高 request，一方面讓每個 Pod 占用更多排程容量，另一方面可能降低 HPA 算出的使用率。實際結果需一起看 request／limit、replicas／HPA、Node 規格與自動擴縮設定；不能直接推論 request 加倍就會多幾台 Node。</p>

<h3 class="kh-section">min 2、max 4 需要多少排程容量</h3>

<p>假設每個 Pod 的 CPU request 合計為 <code>500m</code>，HPA 設定 <code>minReplicas: 2</code>、<code>maxReplicas: 4</code>。這表示期望副本數在 2～4 之間調整，不保證當下每個副本都能成功排程或就緒。</p>

<div class="kh-table-scroll" role="region" aria-label="Pod 副本數比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">Pod 副本數</th><th scope="col">CPU request 總需求</th></tr></thead>
<tbody>

<tr><td>2</td><td>1000m</td></tr>

<tr><td>3</td><td>1500m</td></tr>

<tr><td>4</td><td>2000m</td></tr>

</tbody>
</table>
</div>

<div class="kh-table-scroll" role="region" aria-label="元件比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">元件</th><th scope="col">負責的事情</th></tr></thead>
<tbody>

<tr><td>HPA</td><td>根據指標與設定調整副本數；啟動時的初始數量也受 Deployment replicas 影響，HPA 會週期性調整。</td></tr>

<tr><td>Scheduler</td><td>選擇 Node；兩個 Pods 可以在同一台，也可以分布在不同 Node。成功排入的 request 會占用該 Node 的排程容量。</td></tr>

<tr><td>Node Autoscaler</td><td>評估是否需要及能否調整 Node 容量，不由 HPA 直接建立 Node。</td></tr>

</tbody>
</table>
</div>

<h3 class="kh-section">只夠一個 Pod 時，第二個會等待</h3>

<p>假設服務需要 2 個 Pods，每個 request 為 <code>500m</code>。只有一台符合條件的 Node 還有 <code>500m</code> 排程容量，其他 Node 都放不下。先排入的 Pod 可以啟動，另一個會因容量不足而等待。</p>

<h4>兩個期望副本，只有一個能排入</h4>
<div class="kh-diagram">

{% mermaid %}
flowchart TB
Desired["期望 2 個 Pods：各 request 500m"] --> A["Pod A"]
Desired --> B["Pod B"]
subgraph Node["唯一可用 Node：原剩餘 500m"]
Running["Pod A 排入：啟動後 Running"]
end
A -->|占用 500m 排程容量| Running
B -->|已無足夠容量| Pending["Pod B：Pending / Insufficient cpu"]
{% endmermaid %}

</div>
<p>兩個分支代表不同 Pod，不表示 HPA 指定誰先成功。假設沒有搶占等額外行為；Running 的 Pod 仍需通過就緒條件才能正常接流量。</p>

<div class="kh-note"><p>HPA 的 minReplicas: 2 是最低期望副本數，不是保證有 2 個可用副本。若 Node 自動擴縮允許新增合適 Node，第二個 Pod 才有機會排入；否則等待容量釋放。</p></div>

<p>CPU 容量不能跨 Node 湊給同一個 Pod。例如兩台 Node 各剩 <code>250m</code>，合計雖然是 500m，仍無法容納單一 request 為 500m 的 Pod。</p>

<p><a href="https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/">Kubernetes：Horizontal Pod Autoscaling</a></p>

</div>
<!-- endtab -->

<!-- tab Running and Ready-->

<div class="kubernetes-helm">

<h3 class="kh-section">執行階段與就緒條件分開看</h3>

<div class="kh-table-scroll" role="region" aria-label="欄位比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">欄位</th><th scope="col">意義</th></tr></thead>
<tbody>

<tr><td><code>Running</code></td><td>Pod 的執行階段。容器已建立，至少一個容器仍在執行，或正在啟動／重啟；不代表所有容器都健康。</td></tr>

<tr><td><code>Ready</code></td><td>Pod 的就緒條件。一般情況需各容器就緒，並符合已設定的 readiness gates 等條件，才適合接收一般 Service 流量。</td></tr>

</tbody>
</table>
</div>

<h4>Running 期間，Ready 可以來回變化</h4>
<div class="kh-diagram">

{% mermaid %}
flowchart TB
Pending["Pending：尚未進入執行階段"] -->|排程及啟動完成| Unready["Running + Ready=False"]
Unready -->|就緒檢查與條件通過| Ready["Running + Ready=True"]
Ready -->|就緒檢查達失敗門檻| Unready
{% endmermaid %}

</div>
<p>這是簡化的典型啟動與就緒變化，不是完整 Pod 生命週期。Ready 成為 True 後，Pod 仍是 Running；就緒失敗也不一定使程式退出。</p>

<h3 class="kh-section">三種 Running 但未 Ready 的情境</h3>

<div class="kh-table-scroll" role="region" aria-label="情境比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">情境</th><th scope="col">程式為何仍 Running</th><th scope="col">為何未 Ready</th></tr></thead>
<tbody>

<tr><td>剛啟動，還在初始化</td><td>API 程式已執行，正在載入設定或預熱資料。</td><td>readiness 可能尚未連通或回傳 503，完成初始化並通過檢查後才就緒。</td></tr>

<tr><td>必要依賴暫時故障</td><td>API 程式仍存活，也能接受 HTTP 連線，但必要資料庫連線失敗。</td><td>只有當 readiness 邏輯包含該依賴檢查時，才會反映成失敗，例如回傳 503；Kubernetes 不會自行判斷資料庫健康。</td></tr>

<tr><td>服務太忙，健康檢查逾時</td><td>CPU 競爭、throttling 或執行緒池耗盡，但程式沒有退出。</td><td>/health/ready 未能在設定時間內回應，失敗達門檻後變成未 Ready。</td></tr>

</tbody>
</table>
</div>

<p>一般 Service 會在就緒狀態更新後，停止將新流量導向未 Ready 的 Pod。readiness 失敗本身不會重啟容器，恢復通過檢查後可再次接流量；這不表示既有連線會立刻中斷。</p>

<div class="kh-note"><p>沒有設定 readinessProbe 時，Kubernetes 不會自動驗證 API 的業務功能，容器啟動後通常會被視為就緒；Pod 仍受其他就緒條件影響。本文描述一般 Service 行為，未涵蓋 publishNotReadyAddresses 等特殊設定。</p></div>

<p><a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/">Kubernetes：Pod 生命週期</a>；<a href="https://kubernetes.io/docs/concepts/workloads/pods/probes/">Kubernetes：探針行為</a></p>

</div>
<!-- endtab -->

{% endtabs %}
