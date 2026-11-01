---
title: remained-fail-pods
date: 2026-11-01 10:10:00
categories: kubernetes
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
tags:
    -
toc:
toc_number:
comments :
---

{% tabs remained-fail-pods %}

<!-- tab 事件背景-->
<style>
.kubernetes-helm{--kh-blue:#326de6;--kh-link:#2455b5;--kh-bg:#fff;--kh-ink:#333;--kh-soft:#eef4ff;--kh-line:#d5deed;--kh-code:#182235;--kh-code-ink:#f3f6fc;--kh-red:#b74745;--kh-red-soft:#fff1ef;--kh-amber:#a36a19;--kh-amber-soft:#fff6e7;--kh-green:#287558;--kh-green-soft:#edf8f0;background:var(--kh-bg);color:var(--kh-ink);padding:24px;font-family:'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif;line-height:1.8;overflow-wrap:anywhere}
.kubernetes-helm *{box-sizing:border-box}
.kubernetes-helm h2,.kubernetes-helm h3{color:var(--kh-ink);line-height:1.38;margin:0 0 15px;font-weight:800}
.kubernetes-helm h2{font-size:clamp(1.55rem,3.5vw,2.3rem)}
.kubernetes-helm h3{font-size:1.16rem}
.kubernetes-helm p{max-width:47em;margin:10px 0 18px}
.kubernetes-helm a{color:var(--kh-link);text-decoration:underline;text-underline-offset:3px}
.kubernetes-helm code{font-family:Consolas,monospace;background:var(--kh-soft);color:var(--kh-ink);padding:2px 5px;border-radius:3px;overflow-wrap:anywhere}
.kubernetes-helm .kh-hero{padding:8px 0 24px;margin-bottom:30px;border-bottom:3px solid var(--kh-blue)}
.kubernetes-helm .kh-emblem{display:block;width:55px;height:55px;margin-bottom:17px;background:var(--kh-blue);clip-path:polygon(50% 0,89% 19%,99% 61%,72% 96%,28% 96%,1% 61%,11% 19%)}
.kubernetes-helm .kh-eyebrow{display:block;color:var(--kh-blue);font-size:.79rem;font-weight:800;letter-spacing:.08em;margin-bottom:8px}
.kubernetes-helm .kh-section{padding-left:13px;border-left:5px solid var(--kh-blue);margin:27px 0 18px}
.kubernetes-helm .kh-note{padding:15px 18px;margin:22px 0;background:var(--kh-soft);border-left:4px solid var(--kh-blue);border-radius:4px;max-width:52em}
.kubernetes-helm .kh-note p{margin:0}
.kubernetes-helm .kh-note.red{background:var(--kh-red-soft);border-color:var(--kh-red)}
.kubernetes-helm .kh-note.green{background:var(--kh-green-soft);border-color:var(--kh-green)}
.kubernetes-helm .kh-source{font-size:.86rem;opacity:.82;margin-top:20px;border-top:1px solid var(--kh-line);padding-top:12px}
.kubernetes-helm .kh-timeline{margin:20px 0 30px;max-width:53em}
.kubernetes-helm .kh-timeline-row{display:grid;grid-template-columns:9em 1fr;gap:20px}
.kubernetes-helm .kh-timeline-time{font-size:.86rem;font-weight:800;color:var(--kh-blue);padding-top:2px;text-align:right}
.kubernetes-helm .kh-timeline-body{padding:0 0 23px 20px;border-left:2px solid var(--kh-line);position:relative}
.kubernetes-helm .kh-timeline-body:before{content:'';position:absolute;left:-6px;top:4px;width:10px;height:10px;background:var(--kh-blue);border-radius:50%}
.kubernetes-helm .kh-timeline-row.red .kh-timeline-body:before{background:var(--kh-red)}
.kubernetes-helm .kh-timeline-row.amber .kh-timeline-body:before{background:var(--kh-amber)}
.kubernetes-helm .kh-timeline-row.green .kh-timeline-body:before{background:var(--kh-green)}
.kubernetes-helm .kh-timeline-body strong{display:block;line-height:1.35}
.kubernetes-helm .kh-timeline-body p{margin:5px 0 0}
.kubernetes-helm .kh-table-scroll{max-width:100%;overflow-x:auto;margin:18px 0 24px}
#article-container .kubernetes-helm table.kh-table,.kubernetes-helm table.kh-table{width:auto;max-width:100%;margin:0;border-collapse:collapse;background:var(--kh-bg);color:var(--kh-ink)}
.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{padding:10px 14px;border:1px solid var(--kh-line);text-align:left;vertical-align:top;background:var(--kh-bg);color:var(--kh-ink)}
.kubernetes-helm .kh-table th{background:var(--kh-soft);font-weight:750}
.kubernetes-helm .kh-code{margin:20px 0 26px;background:var(--kh-code);color:var(--kh-code-ink);border-radius:4px;overflow:hidden}
.kubernetes-helm .kh-code-label{padding:8px 15px;border-bottom:1px solid #43516a;font-size:.82rem;letter-spacing:.04em}
#article-container .kubernetes-helm pre.kh-pre,.kubernetes-helm pre.kh-pre{margin:0!important;padding:16px!important;background:var(--kh-code)!important;color:var(--kh-code-ink)!important;border:0!important;border-radius:0!important;box-shadow:none!important;text-shadow:none!important;white-space:pre!important;overflow-x:auto!important;font:13px/1.7 Consolas,monospace!important}
.kubernetes-helm .kh-flow{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:22px 0 27px}
.kubernetes-helm .kh-flow-item{border-top:4px solid var(--kh-blue);padding:14px 0 0;min-width:0}
.kubernetes-helm .kh-flow-item.red{border-color:var(--kh-red)}
.kubernetes-helm .kh-flow-item.amber{border-color:var(--kh-amber)}
.kubernetes-helm .kh-flow-item.green{border-color:var(--kh-green)}
.kubernetes-helm .kh-flow-item b{display:block;margin-bottom:5px}
.kubernetes-helm .kh-flow-item p{margin:0;font-size:.94rem}
.kubernetes-helm .kh-flow-index{font-family:Consolas,monospace;color:var(--kh-blue);font-weight:800;font-size:.82rem;display:block;margin-bottom:8px}
.kubernetes-helm .kh-compare{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin:22px 0 26px}
.kubernetes-helm .kh-compare-col{border-top:4px solid var(--kh-line);padding-top:14px;min-width:0}
.kubernetes-helm .kh-compare-col.red{border-color:var(--kh-red)}
.kubernetes-helm .kh-compare-col.green{border-color:var(--kh-green)}
.kubernetes-helm .kh-compare-col p{margin:8px 0}
.kubernetes-helm .kh-loop{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin:24px 0 10px}
.kubernetes-helm .kh-loop-step{padding:13px 0;border-top:3px solid var(--kh-blue);position:relative;font-weight:750}
.kubernetes-helm .kh-loop-step.red{border-color:var(--kh-red)}
.kubernetes-helm .kh-loop-step.amber{border-color:var(--kh-amber)}
.kubernetes-helm .kh-loop-step:not(:last-child):after{content:'→';position:absolute;right:-13px;top:10px;color:var(--kh-blue)}
.kubernetes-helm .kh-loop-step small{display:block;font-size:.83rem;font-weight:400;margin-top:4px}
.kubernetes-helm .kh-rail{margin:20px 0 25px;border-left:3px solid var(--kh-line)}
.kubernetes-helm .kh-rail-row{display:grid;grid-template-columns:10em 1fr;gap:16px;padding:11px 14px;border-bottom:1px solid var(--kh-line)}
.kubernetes-helm .kh-rail-row b{color:var(--kh-blue)}
.kubernetes-helm .kh-rail-row.amber b{color:var(--kh-amber)}
.kubernetes-helm .kh-rail-row.red b{color:var(--kh-red)}
.kubernetes-helm .kh-gate{max-width:50em;margin:22px 0 26px}
.kubernetes-helm .kh-gate-head{border:2px solid var(--kh-blue);padding:12px 16px;font-weight:800;text-align:center;border-radius:4px}
.kubernetes-helm .kh-gate-branches{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:16px}
.kubernetes-helm .kh-gate-branch{padding:12px 0;border-top:4px solid var(--kh-green)}
.kubernetes-helm .kh-gate-branch.red{border-color:var(--kh-red)}
.kubernetes-helm .kh-gate-branch b{display:block}
.kubernetes-helm .kh-gate-branch p{margin:5px 0}
.kubernetes-helm .kh-mini-line{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:18px 0 26px}
.kubernetes-helm .kh-mini-line span{padding:7px 10px;background:var(--kh-soft);border-left:3px solid var(--kh-blue);font-weight:700}
.kubernetes-helm .kh-mini-line .green{background:var(--kh-green-soft);border-color:var(--kh-green)}
.kubernetes-helm .kh-mini-line em{font-style:normal;color:var(--kh-blue);font-weight:800}
.kubernetes-helm .kh-plain-list{max-width:48em;margin:18px 0 28px;padding:0;list-style:none;counter-reset:kh}
.kubernetes-helm .kh-plain-list li{counter-increment:kh;position:relative;padding:0 0 20px 42px;border-left:2px solid var(--kh-line);margin-left:13px}
.kubernetes-helm .kh-plain-list li:last-child{border-left:0}
.kubernetes-helm .kh-plain-list li:before{content:counter(kh);position:absolute;left:-15px;top:0;width:28px;height:28px;border-radius:50%;background:var(--kh-blue);color:#fff;text-align:center;line-height:28px;font-weight:800}
.kubernetes-helm .kh-plain-list li b{display:block;margin-bottom:3px}
.kubernetes-helm .kh-plain-list li p{margin:0}
[data-theme='dark'] .kubernetes-helm{--kh-blue:#7fa9ff;--kh-link:#a4c2ff;--kh-bg:#17202e;--kh-ink:#eef2f8;--kh-soft:#23334e;--kh-line:#52647f;--kh-red:#ff9993;--kh-red-soft:#382627;--kh-amber:#f0c079;--kh-amber-soft:#3b3021;--kh-green:#8fdbaf;--kh-green-soft:#1d352c}
@media(max-width:660px){.kubernetes-helm{padding:14px}.kubernetes-helm .kh-timeline-row{grid-template-columns:1fr;gap:0}.kubernetes-helm .kh-timeline-time{text-align:left;padding:0 0 5px 18px}.kubernetes-helm .kh-timeline-body{margin-left:5px;padding-left:13px}.kubernetes-helm .kh-flow,.kubernetes-helm .kh-compare,.kubernetes-helm .kh-gate-branches{grid-template-columns:1fr}.kubernetes-helm .kh-loop{grid-template-columns:1fr 1fr}.kubernetes-helm .kh-loop-step:not(:last-child):after{display:none}.kubernetes-helm .kh-rail-row{grid-template-columns:1fr;gap:2px}.kubernetes-helm .kh-table{min-width:680px}.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{padding:8px 10px}}
</style>
<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-emblem" aria-hidden="true"></span><span class="kh-eyebrow">Kubernetes / Incident</span><h2>五分鐘的排程，為什麼停了？</h2><p>排程表沒有寫錯，新的設定也部署成功，通知重試卻沒有持續執行。卡住的是前一次工作留下的 Job。</p></div>
<h3 class="kh-section">事件如何發生</h3>
<div class="kh-timeline">
<div class="kh-timeline-row"><div class="kh-timeline-time">10/26 至 10/29</div><div class="kh-timeline-body"><strong>三個 QA 環境留下舊 Job</strong><p>twqa、hkqa、myqa 各有舊 Job 未完成，仍引用舊映像與 <code>91app-build-site</code>。</p></div></div>
<div class="kh-timeline-row red"><div class="kh-timeline-time">Pod 啟動時</div><div class="kh-timeline-body"><strong>映像拉取失敗</strong><p>事件顯示 <code>authorization failed: no basic auth credentials</code>；容器未啟動，Pod 停在 <code>ImagePullBackOff</code>。</p></div></div>
<div class="kh-timeline-row amber"><div class="kh-timeline-time">重新部署後</div><div class="kh-timeline-body"><strong>新範本沒有替換舊 Job</strong><p>Pipeline 更新了 CronJob 的未來範本；已建立的 Job 與 Pod 仍保存舊設定。</p></div></div>
<div class="kh-timeline-row red"><div class="kh-timeline-time">每五分鐘</div><div class="kh-timeline-body"><strong>新一輪排程被略過</strong><p>舊 Job 持續 Active，<code>concurrencyPolicy: Forbid</code> 讓控制器記錄 <code>JobAlreadyActive</code>，不建立新的自動 Job。</p></div></div>
<div class="kh-timeline-row green"><div class="kh-timeline-time">10/29 16:15 起</div><div class="kh-timeline-body"><strong>連續自動執行恢復</strong><p>16:15、16:20、16:25 三個環境都出現成功的自動 Job。舊 Job 如何被清理，現有證據無法歸因。</p></div></div>
</div>
<div class="kh-note red"><p>這次的核心影響是自動 Job 沒有建立。通知 Queue 是否因此積壓，沒有業務資料可供確認。</p></div>
<h3 class="kh-section">三個環境當時停在哪裡</h3>
<div class="kh-table-scroll" role="region" aria-label="環境與最後一次舊 Job 排程" tabindex="0"><table class="kh-table"><thead><tr><th>環境</th><th>舊 Job</th><th>排程時間，台北時間</th></tr></thead><tbody><tr><td>twqa</td><td><code>notify-queue-retry-job-29882520</code></td><td>10/26 02:00</td></tr><tr><td>hkqa</td><td><code>notify-queue-retry-job-29886840</code></td><td>10/29 02:00</td></tr><tr><td>myqa</td><td><code>notify-queue-retry-job-29884210</code></td><td>10/27 06:10</td></tr></tbody></table></div>
<div class="kh-code"><div class="kh-code-label">Pod 事件中的關鍵訊息</div><pre class="kh-pre">Failed to pull image: pull access denied
authorization failed: no basic auth credentials</pre></div>
<p class="kh-source">證據範圍：2026-10-29 的 CronJob、Job、Pod 與事件查詢。認證失敗已確認，Secret 內容與實際清理操作者未取得。</p>
</div>
<!-- endtab -->

<!-- tab Cronjob,Job,Pod-->
<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-eyebrow">01 / 資源關係</span><h2>鬧鐘、工作單、執行者</h2><p>三層資源各做一件事。先知道誰建立誰，才能看懂為什麼修改排程設定沒有換掉舊 Pod。</p></div>
<div class="kh-flow" aria-label="CronJob 到 Pod 的建立順序"><div class="kh-flow-item"><span class="kh-flow-index">01 / 排程</span><b>CronJob</b><p>像鬧鐘，按 <code>*/5 * * * *</code> 決定何時開出一次工作。</p></div><div class="kh-flow-item"><span class="kh-flow-index">02 / 單次工作</span><b>Job</b><p>保存該次執行要用的映像、認證與 Pod 範本。</p></div><div class="kh-flow-item"><span class="kh-flow-index">03 / 執行</span><b>Pod</b><p>所在節點拉映像，啟動容器，實際執行程式。</p></div></div>
<h3 class="kh-section">部署改的是哪一份設定</h3>
<div class="kh-compare"><div class="kh-compare-col red"><h3>已建立的舊 Job</h3><p>仍引用 <code>91app-build-site</code> 和舊映像。重新部署不會改寫它，也不會替它換 Pod。</p></div><div class="kh-compare-col green"><h3>CronJob 的新範本</h3><p>已改用 <code>91app-build-site-dev</code> 和新映像，只交給往後新建立的 Job。</p></div></div>
<div class="kh-note"><p>舊 Job 一旦保存了舊範本，就像已印出的工作單。更新工作單模板，不會把已印出的那一張收回重印。</p></div>
</div>
<!-- endtab -->

<!-- tab ImagePullBackOff -->
<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-eyebrow">02 / 啟動失敗</span><h2><code>ImagePullBackOff</code> 是什麼？</h2><p>容器尚未開始執行。節點拉不到映像，先等待一段時間，之後再次嘗試。</p></div>
<div class="kh-loop" aria-label="映像拉取失敗後的重試循環"><div class="kh-loop-step">Pod 已建立<small>容器尚未啟動</small></div><div class="kh-loop-step red">拉取映像失敗<small>例如私有倉庫認證不足</small></div><div class="kh-loop-step amber">等待退避<small>間隔逐漸增加</small></div><div class="kh-loop-step">再次拉取<small>仍是同一個 Pod</small></div></div>
<div class="kh-note"><p><code>ImagePull</code> 指從映像倉庫取得映像；<code>BackOff</code> 指失敗後延後重試。等待間隔上限約 300 秒，不表示已放棄。若拉取條件一直沒改善，也沒有期限或外部清理，同一個 Pod 可能長時間留著反覆重試。</p></div>
<h3 class="kh-section">畫面上的狀態要分兩層看</h3>
<div class="kh-table-scroll" role="region" aria-label="Pod 與容器狀態區別" tabindex="0"><table class="kh-table"><thead><tr><th>觀察層級</th><th>當時看到</th><th>意義</th></tr></thead><tbody><tr><td>容器等待原因</td><td><code>ImagePullBackOff</code></td><td>映像還沒拉到，容器尚未啟動。</td></tr><tr><td>Pod phase</td><td><code>Pending</code></td><td>Pod 已存在，但尚未進入完成或失敗的終態。</td></tr><tr><td>與 <code>CrashLoopBackOff</code> 比較</td><td>不是本案狀態</td><td>後者通常是容器啟動後反覆退出；本案連容器都未啟動。</td></tr></tbody></table></div>
<p>映像名稱、tag、倉庫權限或網路都可能造成拉取失敗。本案的 Pod 事件只能證實沒有可用的基本認證；無法進一步判定舊 Secret 是不存在、過期或權限不足。</p>
<p class="kh-source"><a href="https://kubernetes.io/docs/concepts/containers/images/#imagepullbackoff">Kubernetes：ImagePullBackOff</a>；<a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase">Kubernetes：Pod 階段</a></p>
</div>
<!-- endtab -->

<!-- tab 為什麼 ImagePullBackOff 還算 Active-->
<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-eyebrow">03 / 狀態拆解</span><h2>拉取失敗，為什麼仍是 Active？</h2><p><code>ImagePullBackOff</code> 說的是容器等待原因。Job 的 Active 說的是它仍有尚未終止的 Pod。</p></div>
<div class="kh-rail" aria-label="容器到排程的狀態連鎖"><div class="kh-rail-row red"><b>容器</b><span>等待映像，狀態原因是 <code>ImagePullBackOff</code>。</span></div><div class="kh-rail-row amber"><b>Pod</b><span>仍在 <code>Pending</code>，沒有進入 <code>Failed</code>。</span></div><div class="kh-rail-row amber"><b>Job</b><span>還有一個未終止 Pod，顯示 <code>status.active: 1</code>。</span></div><div class="kh-rail-row red"><b>CronJob</b><span><code>Forbid</code> 發現舊 Job 仍 Active，略過下一次建立。</span></div></div>
<div class="kh-note red"><p><code>backoffLimit: 6</code> 不等於「拉映像失敗六次就結束」。這裡的 Pod 一直是 Pending，不能把映像拉取次數當成已失敗 Pod 次數。本案也沒有設定 <code>activeDeadlineSeconds</code> 來限制 Job 的執行時間。</p></div>
<div class="kh-mini-line"><span>拉取失敗</span><em>→</em><span>Pod Pending</span><em>→</em><span>Job Active</span><em>→</em><span>排程略過</span></div>
<p class="kh-source"><a href="https://kubernetes.io/docs/reference/kubernetes-api/batch/job-v1/#JobStatus">Kubernetes：Job status.active</a>；<a href="https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy">Kubernetes：Job backoffLimit</a></p>
</div>
<!-- endtab -->

<!-- tab 為什麼改 YAML 並重跑 pipeline，仍沒有新的自動 Job-->
<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-eyebrow">04 / 排程分支</span><h2>Pipeline 成功，為什麼沒產生新 Job？</h2><p>部署成功代表 CronJob 已拿到新範本。能不能建立下一次 Job，仍要看舊 Job 是否結束。</p></div>
<div class="kh-compare"><div class="kh-compare-col red"><h3>舊 Job 的設定</h3><p>映像：<code>vLATEST-p-7c2be9b0-dev-b20261010-0122</code></p><p>拉映像認證：<code>91app-build-site</code></p></div><div class="kh-compare-col green"><h3>更新後的 CronJob 範本</h3><p>映像：<code>vLATEST-p-9c1c0217-dev-b20261029-0647</code></p><p>拉映像認證：<code>91app-build-site-dev</code></p></div></div>
<div class="kh-gate" aria-label="Forbid 排程判斷"><div class="kh-gate-head">五分鐘到點：舊 Job 是否仍 Active？</div><div class="kh-gate-branches"><div class="kh-gate-branch red"><b>是：略過這次</b><p><code>Forbid</code> 記錄 <code>JobAlreadyActive</code>，新 Job 與新 Pod 都不會建立。</p></div><div class="kh-gate-branch"><b>否：建立新 Job</b><p>以更新後的 CronJob 範本建立 Job，再由 Job 建立 Pod。</p></div></div></div>
<p>另外直接建立的新 Job 曾成功完成，證明新範本可執行；它不會替舊 Active Job 解套。排程恢復須看連續的自動排程 Job，而非單次手動 Job。</p>
<div class="kh-mini-line"><span class="green">16:15 完成</span><em>→</em><span class="green">16:20 完成</span><em>→</em><span class="green">16:25 完成</span></div>
<p class="kh-source">以上時間為 2026-10-29 台北時間，三個環境均觀察到這三次自動排程成功。</p>
</div>
<!-- endtab -->

<!-- tab 如何確認 Job vs Pod 隸屬-->
<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-eyebrow">05 / 追蹤歸屬</span><h2>眼前的 Pod 是哪次 Job 建的？</h2><p>Pod 名稱可以快速辨識；要正式確認，查看 Pod YAML 的 <code>metadata.ownerReferences</code>。</p></div>
<div class="kh-code"><div class="kh-code-label">twqa 當時的資源樹</div><pre class="kh-pre">CronJob  notify-queue-retry-job
  └─ Job  notify-queue-retry-job-29882520
       └─ Pod  notify-queue-retry-job-29882520-8brlg</pre></div>
<div class="kh-rail"><div class="kh-rail-row"><b>Pod 名稱</b><span>前段通常沿用 Job 名稱；最後的 <code>8brlg</code> 是當次產生的後綴，不是 Job UID。</span></div><div class="kh-rail-row"><b>Pod ownerReferences</b><span><code>kind: Job</code> 與 <code>name</code> 指出真正所屬的 Job。</span></div><div class="kh-rail-row"><b>Job ownerReferences</b><span>再往上一層可查到它屬於哪個 CronJob。</span></div></div>
<p>這次後綴剛好是五碼，不能把固定五碼當成普遍規則。若同一 Job 重建 Pod，後綴也可能改變；ownerReferences 才是歸屬依據。</p>
<h3 class="kh-section">從 Rancher UI 查證</h3>
<ol class="kh-plain-list"><li><b>找到 Pod</b><p>選擇對應叢集與 <code>qa-regular-purchase-service</code> namespace，在 Workloads 的 Pods 清單點進該 Pod。</p></li><li><b>看擁有者</b><p>在詳情頁找 Owner／Controlled By；若介面沒有顯示，開啟 Pod YAML，查看 <code>metadata.ownerReferences</code> 的 <code>kind: Job</code> 與 <code>name</code>。</p></li><li><b>回查 Job</b><p>到 Jobs 清單搜尋該 <code>name</code>，再看 Job 的 ownerReferences，確認上層 CronJob。介面欄位名稱可能因 Rancher 版本而異。</p></li></ol>
<div class="kh-note"><p>上面的名稱是 10/29 的歷史例子。舊 Job 已不在後續查詢清單，現在搜尋可能得到 <code>NotFound</code>。</p></div>
</div>
<!-- endtab -->

<!-- tab Pipeline、部署與 Job 的關係-->
<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-eyebrow">06 / 交接位置</span><h2>Pipeline 到哪裡為止？</h2><p>Pipeline 負責部署排程資源。之後每五分鐘建立 Job 的工作，交給 Kubernetes 的 CronJob 控制器。</p></div>
<div class="kh-flow" aria-label="部署到執行的三階段"><div class="kh-flow-item"><span class="kh-flow-index">部署階段</span><b>GitLab pipeline</b><p>依 QA 部署設定與 Helm values 更新叢集裡的 CronJob。</p></div><div class="kh-flow-item"><span class="kh-flow-index">排程階段</span><b>CronJob 控制器</b><p>到點時檢查 <code>Forbid</code>，再決定是否建立一次 Job。</p></div><div class="kh-flow-item"><span class="kh-flow-index">執行階段</span><b>Job 與 Pod</b><p>Job 建立 Pod；節點拉映像並啟動程式。</p></div></div>
<div class="kh-note"><p>此專案的 <code>.gitlab-ci.yml</code> 引用 Nine1 共用模板。<code>nine1-devops-deployments.QA.json</code> 將三個環境的 <code>notify-queue-retry-job</code> 指定為 CronJob role。</p></div>
<div class="kh-mini-line"><span>Pipeline 更新 CronJob</span><em>→</em><span>控制器定時建立 Job</span><em>→</em><span>Job 建立 Pod</span></div>
<p>設定檔中的 <code>kind: deployment</code> 屬於 Nine1 DevOps 的部署格式，<code>apiVersion</code> 是 <code>nine1-devops/v1</code>；它不是 Kubernetes 的 Deployment 資源。</p>
</div>
<!-- endtab -->

<!-- tab  Kubernetes Deployment-->
<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-eyebrow">07 / 資源對照</span><h2>CronJob 不會先經過 Deployment</h2><p>Kubernetes Deployment 與 CronJob 是並列資源。前者維持常駐 Pod，後者定時建立一次性 Job。</p></div>
<div class="kh-compare"><div class="kh-compare-col"><h3>常駐工作負載</h3><div class="kh-mini-line"><span>Deployment</span><em>→</em><span>ReplicaSet</span><em>→</em><span>Pod</span></div><p>例如需持續提供服務的 API。更新 Pod 範本時，通常透過 rollout 逐步替換舊 Pod。</p></div><div class="kh-compare-col green"><h3>本案的定時工作</h3><div class="kh-mini-line"><span>CronJob</span><em>→</em><span>Job</span><em>→</em><span>Pod</span></div><p>每五分鐘嘗試開出一次 Job。更新範本只影響之後建立的 Job，不會替換舊 Job。</p></div></div>
<div class="kh-note"><p>這個 CronJob 的 Job 與 Pod 不由 Kubernetes Deployment 管理。不能套用 Deployment 更新後替換舊 Pod 的行為。</p></div>
<p class="kh-source"><a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/">Kubernetes：Deployment</a>；<a href="https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#modifying-a-cronjob">Kubernetes：CronJob 更新範本</a></p>
</div>
<!-- endtab -->

<!-- tab 下次發生時的處理方式-->


<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-eyebrow">08 / 排查路徑</span><h2>再遇到排程停住，從哪裡查？</h2><p>先確認 CronJob 與目前 Active Job，再查 Pod 事件。歷史 Job 名稱不可直接拿來刪除當下資源。</p></div>
<ol class="kh-plain-list"><li><b>看 CronJob</b><p>核對 <code>spec.schedule</code>、<code>spec.suspend</code>、<code>spec.concurrencyPolicy</code>、<code>status.active</code> 與 <code>lastScheduleTime</code>。</p></li><li><b>追 Active Job</b><p>查看 Job 的完整條件與 Pod。若 Pod 是 <code>ImagePullBackOff</code>，到 Events 找實際拉取錯誤。</p></li><li><b>確認範本差異</b><p>比對舊 Job 保存的 image、imagePullSecrets 與 CronJob 現行範本，分清新舊設定。</p></li><li><b>處理並驗證</b><p>確認舊 Job 無法完成且不需要保留執行後，清理舊 Job。觀察後續至少三個排程時點是否自動建立並完成 Job。</p></li></ol>
<div class="kh-code"><div class="kh-code-label">twqa 查詢示例</div><pre class="kh-pre">kubectl --context eks-ap-northeast-1-tw-91dev-tw-v2 -n qa-regular-purchase-service get cronjob notify-queue-retry-job -o yaml
kubectl --context eks-ap-northeast-1-tw-91dev-tw-v2 -n qa-regular-purchase-service describe cronjob notify-queue-retry-job
kubectl --context eks-ap-northeast-1-tw-91dev-tw-v2 -n qa-regular-purchase-service get jobs,pods -l app.kubernetes.io/instance=notify-queue-retry-job -o wide</pre></div>
<h3 class="kh-section">當時的舊 Job，僅供事件對照</h3>
<div class="kh-table-scroll" role="region" aria-label="歷史舊 Job 名稱" tabindex="0"><table class="kh-table"><thead><tr><th>環境</th><th>當時卡住的 Job</th><th>觀察</th></tr></thead><tbody><tr><td>twqa</td><td><code>notify-queue-retry-job-29882520</code><br><code>notify-queue-retry-job-1793256241585</code></td><td>舊映像與拉取設定；後者為額外殘留 Active Job。</td></tr><tr><td>hkqa</td><td><code>notify-queue-retry-job-29886840</code></td><td>Pod 拉取失敗。</td></tr><tr><td>myqa</td><td><code>notify-queue-retry-job-29884210</code></td><td>Pod 拉取失敗。</td></tr></tbody></table></div>
<div class="kh-note green"><p>驗證恢復要看自動排程的 Job 連續完成，以及 <code>lastScheduleTime</code> 持續向前更新；一次直接建立的 Job 成功不足以證明排程恢復。</p></div>
</div>


<!-- endtab -->

{% endtabs %}
