---
title: Throttled
date: 2026-10-13 08:39:00
categories: kubernetes
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
tags:
    - 
toc:
toc_number:
comments :
---


{% tabs Throttled%}


<!-- tab CPU-->

<style>
.kubernetes-helm{--kh-blue:#326de6;--kh-link:#2455b5;--kh-bg:#fff;--kh-ink:#333;--kh-soft:#eef4ff;--kh-line:#d5deed;--kh-code:#182235;--kh-code-ink:#f3f6fc;background:var(--kh-bg);color:var(--kh-ink);padding:24px;font-family:'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif;line-height:1.85;overflow-wrap:anywhere;}
.kubernetes-helm *{box-sizing:border-box;}
#article-container .kubernetes-helm h2,#article-container .kubernetes-helm h3,.kubernetes-helm h2,.kubernetes-helm h3{color:var(--kh-ink);line-height:1.4;font-weight:800;margin:0 0 16px;}
.kubernetes-helm p{margin:12px 0;}
.kubernetes-helm code{font-family:Consolas,monospace;background:var(--kh-soft);color:inherit;padding:2px 5px;border-radius:3px;}
.kubernetes-helm .kh-hero{padding:28px 0 32px;margin-bottom:28px;border-bottom:3px solid var(--kh-blue);}
.kubernetes-helm .kh-emblem{display:block;width:58px;height:58px;margin-bottom:20px;background:var(--kh-blue);clip-path:polygon(50% 0,89% 19%,99% 61%,72% 96%,28% 96%,1% 61%,11% 19%);}
.kubernetes-helm .kh-hero h2{font-size:clamp(1.6rem,4vw,2.6rem);letter-spacing:-.02em;}
.kubernetes-helm .kh-hero p{max-width:46em;}
.kubernetes-helm .kh-section{padding-left:14px;border-left:5px solid var(--kh-blue);margin-top:30px;}
.kubernetes-helm .kh-code{margin:24px 0;background:var(--kh-code);color:var(--kh-code-ink);border-radius:4px;overflow:hidden;}
.kubernetes-helm .kh-code-label{padding:8px 16px;border-bottom:1px solid #43516a;font-size:.85rem;}
#article-container .kubernetes-helm pre.kh-pre,.kubernetes-helm pre.kh-pre{margin:0!important;padding:18px!important;background:var(--kh-code)!important;color:var(--kh-code-ink)!important;border:0!important;border-radius:0!important;box-shadow:none!important;text-shadow:none!important;white-space:pre!important;overflow-x:auto!important;font:14px/1.8 Consolas,monospace!important;}
.kubernetes-helm .kh-steps{margin:18px 0 26px;padding-left:1.5em;}
.kubernetes-helm .kh-steps li{margin:8px 0;padding-left:6px;}
.kubernetes-helm .kh-flow{display:flex;align-items:stretch;gap:10px;margin:22px 0;}
.kubernetes-helm .kh-flow-step{flex:1;min-width:0;padding:16px;border:1px solid var(--kh-line);border-top:4px solid var(--kh-blue);border-radius:4px;background:var(--kh-bg);text-align:center;}
.kubernetes-helm .kh-flow-step strong,.kubernetes-helm .kh-flow-step span{display:block;}
.kubernetes-helm .kh-flow-step span{margin-top:4px;color:var(--kh-link);font-family:Consolas,monospace;font-size:.88rem;}
.kubernetes-helm .kh-flow-arrow{display:flex;align-items:center;color:var(--kh-blue);font-size:1.5rem;font-weight:800;}
.kubernetes-helm .kh-note{padding:16px 20px;margin:22px 0;background:var(--kh-soft);border-left:4px solid var(--kh-blue);border-radius:4px;}
.kubernetes-helm .kh-chip{margin:22px 0;padding:20px;border:2px solid var(--kh-blue);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-chip-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:16px;}
.kubernetes-helm .kh-chip-head strong{font-size:1.08rem;}
.kubernetes-helm .kh-chip-head span{color:var(--kh-link);font-family:Consolas,monospace;font-size:.88rem;}
.kubernetes-helm .kh-core-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;}
.kubernetes-helm .kh-core{padding:16px 10px;border:1px solid var(--kh-line);border-top:4px solid var(--kh-blue);border-radius:4px;background:var(--kh-soft);text-align:center;}
.kubernetes-helm .kh-core strong,.kubernetes-helm .kh-core span{display:block;}
.kubernetes-helm .kh-core span{margin-top:4px;font-size:.86rem;}
.kubernetes-helm .kh-clock{margin:22px 0;padding:18px 20px;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-clock-value{display:block;margin:6px 0;color:var(--kh-link);font:700 clamp(1.15rem,3vw,1.55rem)/1.4 Consolas,monospace;}
.kubernetes-helm .kh-spec-bar{display:flex;align-items:center;gap:0;margin:22px 0;border-top:1px solid var(--kh-line);border-bottom:1px solid var(--kh-line);}
.kubernetes-helm .kh-spec-item{flex:1;padding:14px 18px;border-right:1px solid var(--kh-line);}
.kubernetes-helm .kh-spec-item:last-child{border-right:0;}
.kubernetes-helm .kh-spec-item strong,.kubernetes-helm .kh-spec-item span{display:block;}
.kubernetes-helm .kh-spec-item strong{color:var(--kh-link);font:700 1.05rem/1.5 Consolas,monospace;}
.kubernetes-helm .kh-spec-item span{margin-top:3px;font-size:.86rem;}
.kubernetes-helm .kh-cache-tree{margin:22px 0;padding:22px;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-tree-node{max-width:360px;margin:0 auto;padding:13px 18px;border:2px solid var(--kh-blue);border-radius:4px;background:var(--kh-soft);text-align:center;font-weight:700;}
.kubernetes-helm .kh-tree-node.decision{background:var(--kh-bg);}
.kubernetes-helm .kh-tree-arrow{display:block;margin:6px auto;color:var(--kh-blue);font-size:1.35rem;font-weight:800;text-align:center;}
.kubernetes-helm .kh-branches{position:relative;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:12px;padding-top:22px;}
.kubernetes-helm .kh-branches::before{content:"";position:absolute;top:0;left:25%;right:25%;border-top:2px solid var(--kh-blue);}
.kubernetes-helm .kh-branches::after{content:"";position:absolute;top:-12px;left:50%;height:12px;border-left:2px solid var(--kh-blue);}
.kubernetes-helm .kh-branch{position:relative;padding:16px;border:1px solid var(--kh-line);border-top:4px solid var(--kh-blue);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-branch::before{content:"";position:absolute;top:-26px;left:50%;height:22px;border-left:2px solid var(--kh-blue);}
.kubernetes-helm .kh-branch-label{display:inline-block;margin-bottom:10px;padding:3px 8px;background:var(--kh-soft);color:var(--kh-link);border-radius:3px;font-weight:700;}
.kubernetes-helm .kh-branch strong,.kubernetes-helm .kh-branch span{display:block;}
.kubernetes-helm .kh-branch span{margin-top:5px;}
.kubernetes-helm .kh-table-scroll{max-width:100%;overflow-x:auto;margin:22px 0;}
#article-container .kubernetes-helm table.kh-table,.kubernetes-helm table.kh-table{width:100%;margin:0;border-collapse:collapse;table-layout:auto;background:var(--kh-bg);color:var(--kh-ink);}
.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{padding:12px 16px;border:1px solid var(--kh-line);text-align:left;vertical-align:top;background:var(--kh-bg);color:var(--kh-ink);}
.kubernetes-helm .kh-table th{background:var(--kh-soft);font-weight:700;}
.kubernetes-helm .kh-compare-table th:first-child,.kubernetes-helm .kh-compare-table td:first-child{width:24%;white-space:nowrap;overflow-wrap:normal;word-break:normal;}
.kubernetes-helm .kh-compare-table th:nth-child(2),.kubernetes-helm .kh-compare-table td:nth-child(2){width:33%;}
.kubernetes-helm .kh-compare-table th:nth-child(3),.kubernetes-helm .kh-compare-table td:nth-child(3){width:43%;}
.kubernetes-helm .kh-app-row{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:22px 0;}
.kubernetes-helm .kh-app{padding:14px 12px;border:1px solid var(--kh-line);border-top:4px solid var(--kh-blue);border-radius:4px;background:var(--kh-bg);text-align:center;}
.kubernetes-helm .kh-app strong,.kubernetes-helm .kh-app span{display:block;}
.kubernetes-helm .kh-app span{margin-top:4px;color:var(--kh-link);font-size:.82rem;}
.kubernetes-helm .kh-timeslice-scroll{max-width:100%;overflow-x:auto;margin:22px 0;padding-bottom:4px;}
.kubernetes-helm .kh-timeslice{min-width:680px;padding:18px;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-time-axis{margin-bottom:10px;color:var(--kh-link);font:700 .86rem/1.5 Consolas,monospace;text-align:right;}
.kubernetes-helm .kh-quantum-track{display:grid;grid-template-columns:repeat(4,minmax(150px,1fr));border:2px solid var(--kh-blue);border-radius:4px;overflow:hidden;}
.kubernetes-helm .kh-quantum{position:relative;padding:15px 12px;background:var(--kh-soft);text-align:center;}
.kubernetes-helm .kh-quantum+.kh-quantum{border-left:3px solid var(--kh-blue);}
.kubernetes-helm .kh-quantum strong,.kubernetes-helm .kh-quantum span{display:block;}
.kubernetes-helm .kh-quantum span{margin-bottom:4px;color:var(--kh-link);font:700 .8rem/1.4 Consolas,monospace;}
.kubernetes-helm .kh-switch-legend{margin-top:12px;font-size:.88rem;}
.kubernetes-helm .kh-switch-mark{display:inline-block;width:22px;margin-right:7px;border-top:3px solid var(--kh-blue);vertical-align:middle;}
.kubernetes-helm .kh-formula{margin:22px 0;padding:18px;border:2px solid var(--kh-blue);border-radius:4px;background:var(--kh-soft);color:var(--kh-link);font:800 clamp(1.2rem,4vw,1.65rem)/1.4 Consolas,monospace;text-align:center;}
.kubernetes-helm .kh-unit-table th:first-child,.kubernetes-helm .kh-unit-table td:first-child{width:42%;white-space:nowrap;}
.kubernetes-helm .kh-resource-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:22px 0;}
.kubernetes-helm .kh-resource-card{padding:18px;border:1px solid var(--kh-line);border-top:4px solid var(--kh-blue);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-resource-card strong,.kubernetes-helm .kh-resource-card span{display:block;}
.kubernetes-helm .kh-resource-card strong{color:var(--kh-link);font:700 1rem/1.5 Consolas,monospace;}
.kubernetes-helm .kh-resource-card span{margin-top:8px;}
.kubernetes-helm .kh-quota{margin:22px 0;padding:20px;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-quota-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:14px;}
.kubernetes-helm .kh-quota-head strong{font-size:1.05rem;}
.kubernetes-helm .kh-quota-head span{color:var(--kh-link);font:700 .88rem/1.5 Consolas,monospace;}
.kubernetes-helm .kh-period-track{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));border:2px solid var(--kh-blue);border-radius:4px;overflow:hidden;}
.kubernetes-helm .kh-period-segment{min-height:92px;padding:15px 12px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
.kubernetes-helm .kh-period-segment strong,.kubernetes-helm .kh-period-segment span{display:block;}
.kubernetes-helm .kh-period-segment span{margin-top:4px;font:700 .84rem/1.5 Consolas,monospace;}
.kubernetes-helm .kh-period-run{background:var(--kh-soft);}
.kubernetes-helm .kh-period-wait{border-left:2px solid var(--kh-blue);background:var(--kh-bg);}
.kubernetes-helm .kh-thread-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:16px;}
.kubernetes-helm .kh-thread-card{padding:13px;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-soft);text-align:center;}
.kubernetes-helm .kh-thread-card strong,.kubernetes-helm .kh-thread-card span{display:block;}
.kubernetes-helm .kh-thread-card span{margin-top:3px;color:var(--kh-link);font-size:.85rem;}
.kubernetes-helm .kh-shared-budget{margin-top:10px;padding:13px;border:2px solid var(--kh-blue);border-radius:4px;text-align:center;font-weight:700;}
.kubernetes-helm .kh-sim-assumptions{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:22px 0;}
.kubernetes-helm .kh-sim-assumption{padding:16px;border:1px solid var(--kh-line);border-top:4px solid var(--kh-blue);border-radius:4px;background:var(--kh-bg);text-align:center;}
.kubernetes-helm .kh-sim-assumption strong,.kubernetes-helm .kh-sim-assumption span{display:block;}
.kubernetes-helm .kh-sim-assumption strong{color:var(--kh-link);font:700 1rem/1.5 Consolas,monospace;}
.kubernetes-helm .kh-sim-assumption span{margin-top:5px;font-size:.88rem;}
.kubernetes-helm .kh-sim-case{margin:18px 0;padding:18px;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-sim-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:14px;}
.kubernetes-helm .kh-sim-head strong{font:800 1.12rem/1.4 Consolas,monospace;color:var(--kh-link);}
.kubernetes-helm .kh-sim-head span{font-size:.88rem;}
.kubernetes-helm .kh-core-lanes{display:grid;gap:8px;}
.kubernetes-helm .kh-core-lane{display:grid;grid-template-columns:78px minmax(0,1fr);align-items:center;gap:10px;}
.kubernetes-helm .kh-core-lane>span{font:700 .82rem/1.4 Consolas,monospace;white-space:nowrap;}
.kubernetes-helm .kh-lane-track{height:24px;border:1px solid var(--kh-line);border-radius:3px;background:var(--kh-soft);overflow:hidden;}
.kubernetes-helm .kh-lane-fill{height:100%;background:var(--kh-blue);}
.kubernetes-helm .kh-fill-50{width:50%;}
.kubernetes-helm .kh-fill-100{width:100%;}
.kubernetes-helm .kh-sim-caption{margin:12px 0 0;font-size:.88rem;}
.kubernetes-helm .kh-sim-table{min-width:660px;}
.kubernetes-helm .kh-sim-table th:first-child,.kubernetes-helm .kh-sim-table td:first-child{white-space:nowrap;}
.kubernetes-helm .kh-ceiling{margin:22px 0;padding:18px;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-ceiling-row{display:grid;grid-template-columns:190px minmax(0,1fr);align-items:center;gap:12px;margin:10px 0;}
.kubernetes-helm .kh-ceiling-label strong,.kubernetes-helm .kh-ceiling-label span{display:block;}
.kubernetes-helm .kh-ceiling-label span{margin-top:3px;color:var(--kh-link);font:700 .82rem/1.4 Consolas,monospace;}
.kubernetes-helm .kh-ceiling-track{height:28px;border:1px solid var(--kh-line);border-radius:3px;background:var(--kh-soft);overflow:hidden;}
.kubernetes-helm .kh-ceiling-fill{height:100%;display:flex;align-items:center;justify-content:center;background:var(--kh-blue);color:#fff;font:700 .8rem/1 Consolas,monospace;}
.kubernetes-helm .kh-question{margin:22px 0;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-bg);overflow:hidden;}
.kubernetes-helm .kh-question>strong{display:block;padding:16px 18px;background:var(--kh-soft);}
.kubernetes-helm .kh-options{margin:0;padding:14px 20px 14px 42px;}
.kubernetes-helm .kh-options li{margin:7px 0;padding-left:4px;}
.kubernetes-helm details.kh-answer{border-top:1px solid var(--kh-line);}
.kubernetes-helm details.kh-answer summary{padding:13px 18px;color:var(--kh-link);font-weight:700;cursor:pointer;}
.kubernetes-helm .kh-answer-body{padding:2px 18px 16px;}
.kubernetes-helm .kh-factor-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:22px 0;}
.kubernetes-helm .kh-factor{padding:17px;border:1px solid var(--kh-line);border-top:4px solid var(--kh-blue);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-factor strong,.kubernetes-helm .kh-factor span{display:block;}
.kubernetes-helm .kh-factor span{margin-top:6px;font-size:.9rem;}
.kubernetes-helm .kh-thread-scroll,.kubernetes-helm .kh-response-scroll{max-width:100%;overflow-x:auto;margin:22px 0;padding-bottom:4px;}
.kubernetes-helm .kh-thread-period{min-width:680px;padding:18px;border:1px solid var(--kh-line);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-thread-period-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:14px;}
.kubernetes-helm .kh-thread-period-head strong{font-size:1.05rem;}
.kubernetes-helm .kh-thread-period-head span{color:var(--kh-link);font:700 .86rem/1.5 Consolas,monospace;}
.kubernetes-helm .kh-thread-line{display:grid;grid-template-columns:86px minmax(0,1fr);align-items:center;gap:10px;margin:9px 0;}
.kubernetes-helm .kh-thread-line>strong{font:700 .82rem/1.4 Consolas,monospace;}
.kubernetes-helm .kh-thread-track{display:grid;grid-template-columns:1fr 3fr;min-height:40px;border:1px solid var(--kh-line);border-radius:3px;overflow:hidden;}
.kubernetes-helm .kh-thread-run,.kubernetes-helm .kh-thread-stop{display:flex;align-items:center;justify-content:center;padding:8px;text-align:center;font-size:.82rem;}
.kubernetes-helm .kh-thread-run{background:var(--kh-blue);color:#fff;font-weight:700;}
.kubernetes-helm .kh-thread-stop{background:var(--kh-bg);border-left:2px solid var(--kh-blue);}
.kubernetes-helm .kh-thread-axis{display:grid;grid-template-columns:86px 1fr 3fr;gap:10px;margin-top:10px;color:var(--kh-link);font:700 .78rem/1.4 Consolas,monospace;}
.kubernetes-helm .kh-thread-axis span:nth-child(2){text-align:left;}
.kubernetes-helm .kh-thread-axis span:nth-child(3){display:flex;justify-content:space-between;}
.kubernetes-helm .kh-symptom-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:22px 0;}
.kubernetes-helm .kh-symptom{padding:16px;border:1px solid var(--kh-line);border-left:4px solid var(--kh-blue);border-radius:4px;background:var(--kh-bg);}
.kubernetes-helm .kh-symptom strong,.kubernetes-helm .kh-symptom span{display:block;}
.kubernetes-helm .kh-symptom span{margin-top:5px;font-size:.9rem;}
.kubernetes-helm .kh-response-track{min-width:680px;display:grid;grid-template-columns:repeat(5,minmax(130px,1fr));border:2px solid var(--kh-blue);border-radius:4px;overflow:hidden;}
.kubernetes-helm .kh-response-step{min-height:86px;padding:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:var(--kh-bg);text-align:center;}
.kubernetes-helm .kh-response-step+.kh-response-step{border-left:1px solid var(--kh-line);}
.kubernetes-helm .kh-response-step.run{background:var(--kh-soft);}
.kubernetes-helm .kh-response-step strong,.kubernetes-helm .kh-response-step span{display:block;}
.kubernetes-helm .kh-response-step span{margin-top:4px;color:var(--kh-link);font:700 .8rem/1.4 Consolas,monospace;}
.kubernetes-helm .kh-metric-table{min-width:760px;}
[data-theme='dark'] .kubernetes-helm{--kh-blue:#7fa9ff;--kh-link:#a4c2ff;--kh-bg:#17202e;--kh-ink:#eef2f8;--kh-soft:#23334e;--kh-line:#52647f;}
@media(max-width:600px){.kubernetes-helm{padding:16px;}.kubernetes-helm .kh-hero{padding:16px 0 24px;}.kubernetes-helm .kh-flow{flex-direction:column;}.kubernetes-helm .kh-flow-arrow{justify-content:center;transform:rotate(90deg);}.kubernetes-helm .kh-note{padding:14px;}.kubernetes-helm .kh-chip-head{display:block;}.kubernetes-helm .kh-chip-head span{display:block;margin-top:4px;}.kubernetes-helm .kh-core-grid{grid-template-columns:repeat(2,minmax(0,1fr));}.kubernetes-helm .kh-spec-bar{display:block;}.kubernetes-helm .kh-spec-item{border-right:0;border-bottom:1px solid var(--kh-line);}.kubernetes-helm .kh-spec-item:last-child{border-bottom:0;}.kubernetes-helm .kh-branches{grid-template-columns:1fr;padding-top:14px;padding-left:18px;}.kubernetes-helm .kh-branches::before{top:0;bottom:0;left:4px;right:auto;border-top:0;border-left:2px solid var(--kh-blue);}.kubernetes-helm .kh-branches::after{top:-12px;left:4px;height:12px;}.kubernetes-helm .kh-branch::before{top:22px;left:-18px;width:18px;height:0;border-top:2px solid var(--kh-blue);border-left:0;}.kubernetes-helm .kh-app-row{grid-template-columns:repeat(2,minmax(0,1fr));}.kubernetes-helm table.kh-table{min-width:680px;}.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{padding:10px;min-width:8em;}.kubernetes-helm table.kh-unit-table,.kubernetes-helm table.kh-time-table{min-width:0;}.kubernetes-helm .kh-unit-table th,.kubernetes-helm .kh-unit-table td,.kubernetes-helm .kh-time-table th,.kubernetes-helm .kh-time-table td{min-width:0;}.kubernetes-helm .kh-resource-grid,.kubernetes-helm .kh-thread-grid{grid-template-columns:1fr;}.kubernetes-helm .kh-quota-head{display:block;}.kubernetes-helm .kh-quota-head span{display:block;margin-top:4px;}.kubernetes-helm .kh-period-segment{padding:12px 8px;}.kubernetes-helm .kh-sim-assumptions{grid-template-columns:1fr;}.kubernetes-helm .kh-sim-head{display:block;}.kubernetes-helm .kh-sim-head span{display:block;margin-top:4px;}.kubernetes-helm .kh-core-lane{grid-template-columns:62px minmax(0,1fr);gap:8px;}.kubernetes-helm .kh-ceiling-row{grid-template-columns:1fr;}.kubernetes-helm .kh-ceiling-track{height:26px;}.kubernetes-helm .kh-factor-grid,.kubernetes-helm .kh-symptom-grid{grid-template-columns:1fr;}.kubernetes-helm .kh-question>strong{padding:14px;}.kubernetes-helm .kh-options{padding:12px 14px 12px 34px;}}
</style>
<div class="kubernetes-helm">
<div class="kh-hero">
<span class="kh-emblem" aria-hidden="true"></span>
<h2>CPU 如何執行一段程式？</h2>
<p>一段看似簡單的 <code>C#</code> 加法，並不是由處理器直接閱讀原始碼。程式經過編譯與執行階段處理後，會轉換成 <code>CPU</code> 能執行的機器指令。理解這段過程，是後續認識 <code>Kubernetes</code> CPU 額度與 <code>Throttling</code> 的起點。</p>
</div>
<p><code>CPU</code>（<code>Central Processing Unit</code>，中央處理器）是負責執行機器指令的硬體。以下列 <code>C#</code> 程式為例，程式的目標是將兩個整數相加：</p>
<div class="kh-code">
<div class="kh-code-label">C# 加法範例</div>
<pre class="kh-pre">int a = 10;
int b = 20;
int result = a + b;</pre>
</div>
<h3 class="kh-section">從原始碼到 CPU 動作</h3>
<p>這段程式經過編譯與執行階段處理後，最終會轉換成 CPU 能理解的機器指令。若暫時省略底層細節，可以把處理動作整理成四個步驟：</p>
<ol class="kh-steps">
<li>把數值 <code>10</code> 放進暫存器。</li>
<li>把數值 <code>20</code> 放進另一個暫存器。</li>
<li>執行加法運算。</li>
<li>保存運算結果。</li>
</ol>
<h3 class="kh-section">CPU 的基本指令循環</h3>
<div class="kh-flow" role="list" aria-label="CPU 基本指令循環">
<div class="kh-flow-step" role="listitem"><strong>取得指令</strong><span>Fetch</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step" role="listitem"><strong>解碼指令</strong><span>Decode</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step" role="listitem"><strong>執行指令</strong><span>Execute</span></div>
</div>
<div class="kh-note">
<strong>這是一個用來建立概念的簡化模型</strong>
<p>現代 <code>CPU</code> 會使用 <code>Pipeline</code>、<code>亂序執行</code>等技術，讓多個指令的不同處理階段彼此重疊。因此，實際運作會比 <code>Fetch → Decode → Execute</code> 更複雜。</p>
</div>
</div>

<!-- endtab -->


<!-- tab CPU Core-->


<div class="kubernetes-helm">
<div class="kh-hero">
<h2>一顆 CPU 裡面有什麼？</h2>
<p>一顆 <code>CPU</code> 晶片可以包含多個 <code>Core</code>。每個 <code>Core</code> 都具備執行機器指令的能力，因此 <code>Core</code> 數量會影響處理器能同時推進多少工作，但實際效果仍取決於程式能否平行執行。</p>
</div>
<h3 class="kh-section">CPU 晶片與 Core</h3>
<p>以下是一顆四核心 <code>CPU</code> 的簡化示意。外框代表整顆 CPU 晶片，裡面的四個區塊代表四個實體 <code>Core</code>。</p>
<div class="kh-chip" role="img" aria-label="一顆 CPU 晶片包含四個實體 Core 的示意圖">
<div class="kh-chip-head"><strong>CPU 晶片</strong><span>4 Physical Cores</span></div>
<div class="kh-core-grid">
<div class="kh-core"><strong>Core 1</strong><span>執行指令</span></div>
<div class="kh-core"><strong>Core 2</strong><span>執行指令</span></div>
<div class="kh-core"><strong>Core 3</strong><span>執行指令</span></div>
<div class="kh-core"><strong>Core 4</strong><span>執行指令</span></div>
</div>
</div>
<p>假設一個 <code>C#</code> 程式有四個可以同時進行計算的 <code>Thread</code>，作業系統就有機會把它們安排到四個不同的 <code>Core</code> 上執行。這不代表四個 Thread 一定會永遠固定在四個 Core，實際安排仍由作業系統的 <code>CPU Scheduler</code> 決定。</p>
<h3 class="kh-section">時脈頻率代表運作節奏</h3>
<p>時脈頻率可以想成 <code>Core</code> 內部協調工作的節拍。規格中的 <code>GHz</code> 用來描述每秒有多少個時脈週期。</p>
<div class="kh-clock">
<strong>以 3.5 GHz 為例</strong>
<span class="kh-clock-value">3.5 GHz = 每秒 35 億個時脈週期</span>
<p>這表示 <code>Core</code> 運作在該頻率時，每秒會經過約 35 億個時脈週期。它不代表每秒一定完成 35 億條指令，因為不同指令需要的週期數不同，現代 <code>CPU</code> 也可能讓多條指令的處理階段彼此重疊。</p>
</div>
<div class="kh-note">
<strong>GHz 不是把所有 Core 的數字直接相加</strong>
<p>四核心的 <code>3.5 GHz</code> CPU，不應解讀成一顆 <code>14 GHz</code> 的 CPU。<code>3.5 GHz</code> 描述的是核心運作時的時脈頻率，而且實際頻率還可能受到省電模式、溫度與加速機制影響而變動。</p>
</div>
<h3 class="kh-section">Thread 與 Core 的關係</h3>
<p><code>Core</code> 是實際執行指令的硬體。程式中的 <code>Thread</code> 則是可以被作業系統排程的執行單位。作業系統會把準備執行的 Thread 安排到可用的 <code>Logical CPU</code> 上，再由背後的實體 Core 執行工作。</p>
<h3 class="kh-section">SMT 為什麼會增加 Logical CPU？</h3>
<p><code>SMT</code> 的完整名稱是 <code>Simultaneous Multithreading</code>。它讓一個實體 <code>Core</code> 同時保留多組硬體執行狀態，並向作業系統呈現多個 <code>Logical CPU</code>。</p>
<p>可以把一個 <code>Core</code> 想成一座有多種設備的工作台。當第一個 <code>Thread</code> 正在等待資料，部分設備可能暫時沒有工作。<code>SMT</code> 讓第二個 Thread 有機會使用這些空閒資源，使同一個 Core 的利用率更高。</p>
<div class="kh-note">
<strong>Intel Hyper-Threading 是 SMT 的一種實作</strong>
<p>假設一顆 Intel CPU 有 4 個實體 <code>Core</code>，而且每個 Core 透過 <code>Hyper-Threading</code> 提供 2 個 <code>Logical CPU</code>，作業系統就會看到 8 個 Logical CPU。這仍然不是 8 個完整的實體 Core，因為同一個 Core 提供的兩個 Logical CPU 會共享部分執行單元、<code>Cache</code> 與其他硬體資源，所以效能通常不會直接變成兩倍。</p>
</div>
<h3 class="kh-section">名詞放在一起比較</h3>
<div class="kh-table-scroll" role="region" aria-label="CPU、Core、Thread 與 SMT 名詞比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">名詞</th><th scope="col">白話說明</th><th scope="col">例子</th></tr></thead>
<tbody>
<tr><th scope="row"><code>CPU</code></th><td>安裝在電腦或伺服器中的整顆處理器晶片。</td><td>一顆晶片內含 4 個實體 Core。</td></tr>
<tr><th scope="row"><code>Core</code></th><td>實際執行機器指令的硬體核心。</td><td>四個 Core 可以同時推進多個可平行的工作。</td></tr>
<tr><th scope="row"><code>Thread</code></th><td>程式中可以被作業系統排程的執行單位。</td><td>四個 CPU 密集型 Thread 可能被安排到四個 Core。</td></tr>
<tr><th scope="row"><code>Logical CPU</code></th><td>作業系統可以安排 Thread 的邏輯執行位置。</td><td>啟用雙路 SMT 的四核心 CPU 可能呈現 8 個 Logical CPU。</td></tr>
<tr><th scope="row"><code>SMT</code></th><td>讓一個 Core 同時處理多個硬體 Thread 的技術。</td><td>一個 Core 對作業系統呈現 2 個 Logical CPU。</td></tr>
<tr><th scope="row"><code>Hyper-Threading</code></th><td>Intel 對 SMT 技術的實作名稱。</td><td>兩個 Logical CPU 仍會共享同一個 Core 的部分資源。</td></tr>
</tbody>
</table>
</div>
<div class="kh-note">
<strong>判斷 CPU 效能需要同時看多項條件</strong>
<p>Core 數量、Logical CPU 數量與時脈頻率都只描述處理器的一部分。程式的平行能力、CPU 架構、指令種類、Cache 與記憶體存取，同樣會影響最後的執行速度。</p>
</div>
</div>






<!-- endtab -->



<!-- tab CPU 的速度怎麼決定-->


<div class="kubernetes-helm">
<div class="kh-hero">
<h2>CPU 的速度不只看 GHz</h2>
<p>處理器規格經常列出 <code>Core</code> 數量與時脈頻率，但兩顆同樣標示 <code>3.5 GHz</code> 的 <code>CPU</code>，完成同一份工作所需的時間仍可能不同。時脈只描述運作節奏，真正的速度還取決於每個週期完成多少工作，以及取得資料時需要等待多久。</p>
</div>
<h3 class="kh-section">先讀懂規格上的數字</h3>
<p>以下是一組常見的處理器規格寫法：</p>
<div class="kh-spec-bar" role="list" aria-label="CPU 規格範例">
<div class="kh-spec-item" role="listitem"><strong>Intel CPU</strong><span>處理器系列</span></div>
<div class="kh-spec-item" role="listitem"><strong>8 Cores</strong><span>實體核心數量</span></div>
<div class="kh-spec-item" role="listitem"><strong>3.5 GHz</strong><span>時脈頻率</span></div>
</div>
<p>上一個 tab 已說明，<code>GHz</code> 是時脈頻率的單位。當 <code>Core</code> 運作在 <code>3.5 GHz</code> 時，每秒大約會經過 35 億個時脈週期。</p>
<div class="kh-clock">
<strong>時脈頻率</strong>
<span class="kh-clock-value">3.5 GHz = 每秒 35 億個時脈週期</span>
<p>這個數字代表節奏有多快，不代表每秒固定完成 35 億條指令。</p>
</div>
<h3 class="kh-section">一個週期不等於一條指令</h3>
<p>不同指令需要的處理時間不同。有些指令可能跨越多個週期，現代 <code>CPU</code> 也能透過 <code>Pipeline</code>、平行執行單元與亂序執行，讓多條指令的不同階段同時推進。因此，不能把時脈週期數直接當成完成的指令數。</p>
<p><code>IPC</code> 是 <code>Instructions Per Cycle</code> 的縮寫，用來描述特定工作負載下，每個時脈週期平均完成多少條指令。<code>IPC</code> 不是永遠固定的數字，它會隨 <code>CPU</code> 架構、指令組合與資料等待情況改變。</p>
<h3 class="kh-section">GHz 較低也可能完成更多工作</h3>
<p>以下比較刻意忽略 <code>Cache Miss</code>、分支預測錯誤與其他停頓，只用「時脈頻率乘以 <code>IPC</code>」建立基本概念：</p>
<div class="kh-table-scroll" role="region" aria-label="時脈頻率與 IPC 簡化比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">假想處理器</th><th scope="col">時脈頻率</th><th scope="col">平均 IPC</th><th scope="col">簡化計算結果</th></tr></thead>
<tbody>
<tr><th scope="row">CPU A</th><td><code>3.5 GHz</code></td><td><code>2</code></td><td>每秒約完成 70 億條指令</td></tr>
<tr><th scope="row">CPU B</th><td><code>3.0 GHz</code></td><td><code>3</code></td><td>每秒約完成 90 億條指令</td></tr>
</tbody>
</table>
</div>
<div class="kh-note">
<strong>這是用來理解乘法關係的簡化例子</strong>
<p>只有在相同工作負載、單一 <code>Core</code>、資料供應充足，而且沒有額外停頓時，這個比較才具有概念上的意義。真實程式不能只用 <code>GHz × IPC</code> 判斷完整效能。</p>
</div>
<h3 class="kh-section">影響 CPU 效能的主要因素</h3>
<div class="kh-table-scroll" role="region" aria-label="CPU 效能因素比較" tabindex="0">
<table class="kh-table">
<thead><tr><th scope="col">因素</th><th scope="col">白話說明</th><th scope="col">可能造成的影響</th></tr></thead>
<tbody>
<tr><th scope="row"><code>時脈頻率</code></th><td><code>Core</code> 每秒經過多少個運作節拍。</td><td>其他條件相同時，較高的時脈通常能提供更多處理機會。</td></tr>
<tr><th scope="row"><code>IPC</code></th><td>每個時脈週期平均完成多少條指令。</td><td>較高的 <code>IPC</code> 代表每個節拍能推進更多工作。</td></tr>
<tr><th scope="row"><code>指令種類</code></th><td>加法、除法、向量運算與資料載入的複雜度不同。</td><td>不同指令可能需要不同數量的週期與執行資源。</td></tr>
<tr><th scope="row"><code>CPU 架構</code></th><td><code>Pipeline</code>、執行單元與亂序執行能力的設計不同。</td><td>同樣的 <code>GHz</code> 可能產生不同的 <code>IPC</code> 與實際效能。</td></tr>
<tr><th scope="row"><code>Cache</code></th><td>放在 <code>Core</code> 附近、容量較小但速度較快的資料暫存區。</td><td>需要的資料已在 <code>Cache</code> 時，<code>CPU</code> 可以減少等待。</td></tr>
<tr><th scope="row"><code>記憶體存取</code></th><td>資料不在 <code>Cache</code> 時，需要向主記憶體讀取。</td><td><code>CPU</code> 可能因等待資料而無法持續執行後續指令。</td></tr>
</tbody>
</table>
</div>
<h3 class="kh-section">Cache 是否命中會改變等待時間</h3>
<p><code>CPU</code> 執行指令時經常需要讀取資料。資料是否已經在 <code>Cache</code> 中，會形成兩條不同路徑：</p>
<div class="kh-cache-tree" role="img" aria-label="CPU 需要資料時，Cache Hit 與 Cache Miss 的處理分支">
<div class="kh-tree-node">CPU 需要讀取資料</div>
<span class="kh-tree-arrow" aria-hidden="true">↓</span>
<div class="kh-tree-node decision">Cache 裡有需要的資料嗎？</div>
<div class="kh-branches">
<div class="kh-branch">
<span class="kh-branch-label">是，Cache Hit</span>
<strong>從 Cache 取得資料</strong>
<span>等待時間較短，CPU 可以較快繼續執行。</span>
</div>
<div class="kh-branch">
<span class="kh-branch-label">否，Cache Miss</span>
<strong>向主記憶體讀取資料</strong>
<span>等待時間較長，資料回來後才能繼續執行。</span>
</div>
</div>
</div>
<h3 class="kh-section">Kubernetes 的 1000m 不是固定運算次數</h3>
<div class="kh-note">
<strong>CPU 額度衡量的是可使用的 CPU 時間</strong>
<p><code>Kubernetes</code> 的 <code>1000m</code> 不能直接換算成「每秒可以執行幾次加法」。不同 <code>CPU</code> 的時脈、<code>IPC</code>、架構、指令種類、<code>Cache</code> 與記憶體等待時間都不同，因此相同的 <code>CPU</code> 時間不保證完成相同數量的工作。</p>
</div>
</div>



<!-- endtab -->




<!-- tab 為什麼 CPU 可以同時執行很多程式-->


<div class="kubernetes-helm">
<div class="kh-hero">
<h2>一個 Core 為什麼能同時應付多個程式？</h2>
<p>假設電腦只有一個 <code>Core</code>，而且暫時不考慮 <code>SMT</code>，作業系統只看到一個可排程的 <code>Logical CPU</code>。畫面上仍能同時開啟瀏覽器、音樂播放器、開發工具與 API，原因不是單一執行單元在同一瞬間完成四份工作，而是它在不同工作之間快速切換。</p>
</div>
<h3 class="kh-section">四個程式都可能需要 CPU</h3>
<div class="kh-app-row" role="list" aria-label="同時開啟的四個程式">
<div class="kh-app" role="listitem"><strong>Chrome</strong><span>瀏覽器</span></div>
<div class="kh-app" role="listitem"><strong>Spotify</strong><span>音樂播放器</span></div>
<div class="kh-app" role="listitem"><strong>Visual Studio</strong><span>開發工具</span></div>
<div class="kh-app" role="listitem"><strong>.NET API</strong><span>後端服務</span></div>
</div>
<p>一個程式可以包含一個或多個 <code>Thread</code>。作業系統實際排程的是已經準備好執行的 <code>Thread</code>，而不是把整個程式一次交給 <code>CPU</code>。</p>
<h3 class="kh-section">CPU Scheduler 決定下一個執行者</h3>
<div class="kh-flow" role="img" aria-label="可執行 Thread 經過 CPU Scheduler 取得 Logical CPU">
<div class="kh-flow-step"><strong>等待執行</strong><span>Runnable Threads</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step"><strong>選擇下一個 Thread</strong><span>CPU Scheduler</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step"><strong>取得處理時間</strong><span>1 Logical CPU</span></div>
</div>
<p><code>CPU Scheduler</code> 是作業系統的一部分。它會根據可執行狀態、優先順序與其他排程條件，決定接下來由哪個 <code>Thread</code> 使用處理器。這張圖只保留核心關係，實際排程不一定按照固定順序輪流。</p>
<h3 class="kh-section">Time Sharing 讓多個工作輪流前進</h3>
<p><code>Time Sharing</code> 稱為分時共享。每個 <code>Thread</code> 取得一小段處理時間，時間到、主動等待，或作業系統決定改派其他工作時，下一個 <code>Thread</code> 會接著執行。</p>
<div class="kh-timeslice-scroll" role="region" aria-label="單一 Logical CPU 的時間片示意" tabindex="0">
<div class="kh-timeslice">
<div class="kh-time-axis">時間向右 →</div>
<div class="kh-quantum-track">
<div class="kh-quantum"><span>時間片 1</span><strong>Chrome Thread</strong></div>
<div class="kh-quantum"><span>時間片 2</span><strong>Spotify Thread</strong></div>
<div class="kh-quantum"><span>時間片 3</span><strong>Visual Studio Thread</strong></div>
<div class="kh-quantum"><span>時間片 4</span><strong>.NET API Thread</strong></div>
</div>
<div class="kh-switch-legend"><span class="kh-switch-mark" aria-hidden="true"></span>每條藍色分隔線代表一次工作切換，也就是 <code>Context Switch</code>。</div>
</div>
</div>
<div class="kh-note">
<strong>這是用來觀察輪流執行的簡化時間軸</strong>
<p>真實順序由作業系統決定。同一個 <code>Thread</code> 可能連續取得時間，也可能因等待網路、磁碟或其他事件而暫時不需要 <code>CPU</code>。因此，排程不一定會完整走過四個程式後才回到第一個程式。</p>
</div>
<h3 class="kh-section">Context Switch 保存目前進度，再換下一個 Thread</h3>
<div class="kh-flow" role="list" aria-label="Context Switch 的三個概念步驟">
<div class="kh-flow-step" role="listitem"><strong>暫停目前工作</strong><span>Pause</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step" role="listitem"><strong>保存並載入狀態</strong><span>Save / Restore</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step" role="listitem"><strong>繼續下一個 Thread</strong><span>Resume</span></div>
</div>
<p>作業系統會保存目前 <code>Thread</code> 的必要執行狀態，例如程式計數器與暫存器內容，再恢復下一個 <code>Thread</code> 先前保存的狀態。這樣才能從正確的位置繼續執行。</p>
<div class="kh-note">
<strong>切換本身也需要時間</strong>
<p><code>Context Switch</code> 不是應用程式的實際工作。切換過度頻繁時，保存狀態、恢復狀態與重新取得資料都可能增加額外成本。</p>
</div>
<h3 class="kh-section">Concurrency 與 Parallelism 不相同</h3>
<div class="kh-table-scroll" role="region" aria-label="Concurrency 與 Parallelism 比較" tabindex="0">
<table class="kh-table kh-compare-table">
<thead><tr><th scope="col">概念</th><th scope="col">白話說明</th><th scope="col">執行情況</th></tr></thead>
<tbody>
<tr><th scope="row"><code>Concurrency</code><br>並發</th><td>多個工作都在一段時間內持續推進。</td><td>單一 <code>Logical CPU</code> 可以透過 <code>Time Sharing</code> 快速輪流執行。</td></tr>
<tr><th scope="row"><code>Parallelism</code><br>並行</th><td>多個工作在同一個瞬間真正同時執行。</td><td>需要多個可同時執行的 <code>Core</code> 或 <code>Logical CPU</code>。</td></tr>
</tbody>
</table>
</div>
<p>單一 <code>Logical CPU</code> 上的多工主要是並發。切換速度夠快，加上部分 <code>Thread</code> 經常在等待輸入輸出，因此使用體感會像多個程式同時運作。多個 <code>Core</code> 或 <code>Logical CPU</code> 則能讓多個 <code>Thread</code> 在同一時間真正並行。</p>
<h3 class="kh-section">CPU Scheduler 與 Kubernetes Scheduler 負責不同工作</h3>
<div class="kh-note">
<strong>兩個 Scheduler 的排程層級不同</strong>
<p>作業系統的 <code>CPU Scheduler</code> 決定哪個 <code>Thread</code> 取得 <code>Logical CPU</code>。<code>Kubernetes Scheduler</code> 則決定尚未排程的 <code>Pod</code> 應該放到哪一個 <code>Node</code>。兩者名稱相似，但處理的對象與範圍不同。</p>
</div>
</div>
<!-- endtab -->





<!-- tab Kubernetes 的 1000m-->


<div class="kubernetes-helm">
<div class="kh-hero">
<h2>Kubernetes 的 1000m 代表多少 CPU？</h2>
<p><code>Kubernetes</code> 用 <code>CPU</code> 單位描述容器需要或最多可以使用多少處理能力，也常用 <code>m</code> 表示 <code>millicpu</code>，也就是千分之一個 <code>CPU</code>。這個單位描述的是一段時間內可使用的運算能力，不是固定的指令數，也不是把某顆實體核心切成幾塊。</p>
</div>
<h3 class="kh-section">CPU 單位換算</h3>
<div class="kh-table-scroll" role="region" aria-label="Kubernetes CPU 單位換算" tabindex="0">
<table class="kh-table kh-unit-table">
<thead><tr><th scope="col">Kubernetes 設定</th><th scope="col">代表的 CPU</th></tr></thead>
<tbody>
<tr><th scope="row"><code>100m</code></th><td><code>0.1 CPU</code></td></tr>
<tr><th scope="row"><code>250m</code></th><td><code>0.25 CPU</code></td></tr>
<tr><th scope="row"><code>500m</code></th><td><code>0.5 CPU</code></td></tr>
<tr><th scope="row"><code>1000m</code></th><td><code>1 CPU</code></td></tr>
<tr><th scope="row"><code>2000m</code></th><td><code>2 CPU</code></td></tr>
<tr><th scope="row"><code>4000m</code></th><td><code>4 CPU</code></td></tr>
</tbody>
</table>
</div>
<div class="kh-formula" role="img" aria-label="1000 millicpu 等於 1 CPU">1000m = 1 CPU</div>
<h3 class="kh-section">0.5 CPU 不是半顆實體核心</h3>
<p><code>0.5 CPU</code> 可以理解為一份「CPU 執行時間額度」。它沒有指定只能使用某一顆核心的左半邊或右半邊，也不代表容器會固定綁在某顆核心上。</p>
<div class="kh-note">
<strong>額度是按時間累積，不是按核心形狀切割</strong>
<p>假設一個 <code>Logical CPU</code> 在 <code>100ms</code> 內最多能提供 <code>100ms</code> 的 CPU 執行時間，平均 <code>0.5 CPU</code> 就相當於在同一段時間內使用 <code>50ms</code> 的 CPU 執行時間。</p>
</div>
<h3 class="kh-section">requests 與 limits 的 500m 意義不同</h3>
<p>以下設定同時把 <code>requests.cpu</code> 與 <code>limits.cpu</code> 設為 <code>500m</code>：</p>
<div class="kh-code">
<div class="kh-code-label">Container CPU 資源設定</div>
<pre class="kh-pre">resources:
  requests:
    cpu: 500m
  limits:
    cpu: 500m</pre>
</div>
<div class="kh-resource-grid" role="list" aria-label="CPU requests 與 limits 的差異">
<div class="kh-resource-card" role="listitem"><strong>requests.cpu: 500m</strong><span><code>Kubernetes Scheduler</code> 選擇 <code>Node</code> 時，會把這個容器計為需要 <code>0.5 CPU</code>。這個值用於排程計算，本身不是執行時的最高用量。</span></div>
<div class="kh-resource-card" role="listitem"><strong>limits.cpu: 500m</strong><span>容器最多只能取得平均 <code>0.5 CPU</code> 的運算能力。Linux 會以 <code>cgroup</code> CPU 頻寬控制限制用量，超過額度時可能發生 <code>Throttling</code>。</span></div>
</div>
<h3 class="kh-section">100ms 週期中的 500m 額度</h3>
<p>假設 Linux 的 <code>CFS bandwidth period</code> 設為 <code>100ms</code>，而容器的 CPU 上限是 <code>500m</code>。概念上，每個週期會有 <code>50ms</code> 的 CPU 執行時間額度。</p>
<div class="kh-quota" role="img" aria-label="500m 在 100 毫秒週期內使用 50 毫秒 CPU 執行時間的示意">
<div class="kh-quota-head"><strong>一個 100ms 週期</strong><span>limit: 500m</span></div>
<div class="kh-period-track">
<div class="kh-period-segment kh-period-run"><strong>可以執行</strong><span>50ms CPU time</span></div>
<div class="kh-period-segment kh-period-wait"><strong>額度耗盡後等待</strong><span>直到下個週期補充額度</span></div>
</div>
</div>
<p>如果只有一個持續運算的 <code>Thread</code>，它可以在某個 <code>Logical CPU</code> 上連續執行約 <code>50ms</code>，接著因額度耗盡而等待下一個週期。這是為了理解額度所做的簡化示意，實際執行時間仍會受到作業系統排程與其他工作影響。</p>
<h3 class="kh-section">多個 Thread 會共用同一份額度</h3>
<p>容器內有多個 <code>Thread</code> 時，它們消耗的是同一份 CPU 額度。如果兩個 <code>Thread</code> 分別在兩個 <code>Logical CPU</code> 上並行，每經過 <code>1ms</code> 的實際時間，合計可能消耗約 <code>2ms</code> 的 CPU 執行時間。</p>
<div class="kh-quota" role="img" aria-label="兩個 Thread 共用 Container 的 500m CPU 額度">
<div class="kh-thread-grid">
<div class="kh-thread-card"><strong>Thread A</strong><span>消耗 CPU time</span></div>
<div class="kh-thread-card"><strong>Thread B</strong><span>消耗 CPU time</span></div>
</div>
<div class="kh-shared-budget">共同消耗 Container 的 500m 額度</div>
</div>
<p>以上述 <code>50ms</code> 額度為例，如果兩個 <code>Thread</code> 都能持續並行，額度可能在約 <code>25ms</code> 的實際時間內用完。這也是多執行緒程式可能更快遇到 <code>CPU Throttling</code> 的原因。</p>
<h3 class="kh-section">1000m 是一顆邏輯 CPU 全程工作的能力</h3>
<p>假設只有一個程式使用一顆 <code>Logical CPU</code>，而且程式持續運算，經過時間與累積 CPU 執行時間會同步增加：</p>
<div class="kh-table-scroll" role="region" aria-label="經過時間與 CPU 執行時間對照" tabindex="0">
<table class="kh-table kh-time-table">
<thead><tr><th scope="col">經過時間</th><th scope="col">CPU 執行時間</th></tr></thead>
<tbody>
<tr><td><code>1 秒</code></td><td><code>1 秒</code></td></tr>
<tr><td><code>2 秒</code></td><td><code>2 秒</code></td></tr>
<tr><td><code>3 秒</code></td><td><code>3 秒</code></td></tr>
</tbody>
</table>
</div>
<p>在這個情境下，該 <code>Logical CPU</code> 可以用 <code>100%</code> 的時間執行程式。<code>Kubernetes</code> 把這樣的 CPU 使用能力表示為：</p>
<div class="kh-formula" role="img" aria-label="1 CPU 等於 1000 millicpu">1 CPU = 1000m</div>
<div class="kh-note">
<strong>1000m 描述的是 CPU 時間速率</strong>
<p><code>1000m</code> 表示在一段時間內，最多取得相當於一顆 <code>Logical CPU</code> 全程工作的 CPU 時間。它不保證固定綁定某顆核心，也不保證在不同處理器上完成相同數量的指令。</p>
</div>
</div>
<!-- endtab -->






<!-- tab 實際模擬：500m、1000m、2000m-->


<div class="kubernetes-helm">
<div class="kh-hero">
<h2>實際比較 500m、1000m、2000m 與 4000m</h2>
<p>CPU Limit 增加時，容器每秒可以累積的 CPU 執行時間也會增加。不過，程式必須有足夠的平行運算能力，而且 <code>Node</code> 也要有足夠的 <code>Logical CPU</code>，才有機會真正用滿這些額度。</p>
</div>
<h3 class="kh-section">模擬條件</h3>
<div class="kh-sim-assumptions" role="list" aria-label="CPU Limit 模擬條件">
<div class="kh-sim-assumption" role="listitem"><strong>4 Logical CPU</strong><span>Node 可同時提供四條執行資源</span></div>
<div class="kh-sim-assumption" role="listitem"><strong>足夠多的 Thread</strong><span>程式具備平行運算能力</span></div>
<div class="kh-sim-assumption" role="listitem"><strong>觀察 1 秒</strong><span>CPU 持續有工作可以執行</span></div>
</div>
<div class="kh-note">
<strong>軌道圖呈現的是其中一種可能分配</strong>
<p>為了看清楚數值，以下把 CPU 時間集中畫在特定 <code>Logical CPU</code> 上。實際執行時，作業系統可能讓 <code>Thread</code> 在不同核心之間切換，只要一秒內累積的總 CPU 執行時間沒有超過額度即可。</p>
</div>
<h3 class="kh-section">500m：每秒最多累積 0.5 秒 CPU time</h3>
<div class="kh-sim-case" role="img" aria-label="500m 在四顆 Logical CPU 上的一種分配示意">
<div class="kh-sim-head"><strong>limit: 500m</strong><span>平均相當於 0.5 Logical CPU</span></div>
<div class="kh-core-lanes">
<div class="kh-core-lane"><span>CPU 1</span><div class="kh-lane-track"><div class="kh-lane-fill kh-fill-50"></div></div></div>
<div class="kh-core-lane"><span>CPU 2</span><div class="kh-lane-track"></div></div>
<div class="kh-core-lane"><span>CPU 3</span><div class="kh-lane-track"></div></div>
<div class="kh-core-lane"><span>CPU 4</span><div class="kh-lane-track"></div></div>
</div>
<p class="kh-sim-caption"><code>1 秒</code>內最多累積 <code>0.5 秒</code>的 CPU 執行時間。</p>
</div>
<h3 class="kh-section">1000m：每秒最多累積 1 秒 CPU time</h3>
<div class="kh-sim-case" role="img" aria-label="1000m 在四顆 Logical CPU 上的一種分配示意">
<div class="kh-sim-head"><strong>limit: 1000m</strong><span>平均相當於 1 Logical CPU</span></div>
<div class="kh-core-lanes">
<div class="kh-core-lane"><span>CPU 1</span><div class="kh-lane-track"><div class="kh-lane-fill kh-fill-100"></div></div></div>
<div class="kh-core-lane"><span>CPU 2</span><div class="kh-lane-track"></div></div>
<div class="kh-core-lane"><span>CPU 3</span><div class="kh-lane-track"></div></div>
<div class="kh-core-lane"><span>CPU 4</span><div class="kh-lane-track"></div></div>
</div>
<p class="kh-sim-caption"><code>1 秒</code>內最多累積 <code>1 秒</code>的 CPU 執行時間。</p>
</div>
<h3 class="kh-section">2000m：每秒最多累積 2 秒 CPU time</h3>
<div class="kh-sim-case" role="img" aria-label="2000m 在四顆 Logical CPU 上的一種分配示意">
<div class="kh-sim-head"><strong>limit: 2000m</strong><span>平均相當於 2 Logical CPU</span></div>
<div class="kh-core-lanes">
<div class="kh-core-lane"><span>CPU 1</span><div class="kh-lane-track"><div class="kh-lane-fill kh-fill-100"></div></div></div>
<div class="kh-core-lane"><span>CPU 2</span><div class="kh-lane-track"><div class="kh-lane-fill kh-fill-100"></div></div></div>
<div class="kh-core-lane"><span>CPU 3</span><div class="kh-lane-track"></div></div>
<div class="kh-core-lane"><span>CPU 4</span><div class="kh-lane-track"></div></div>
</div>
<p class="kh-sim-caption"><code>1 秒</code>內最多累積 <code>2 秒</code>的 CPU 執行時間。</p>
</div>
<h3 class="kh-section">4000m：每秒最多累積 4 秒 CPU time</h3>
<div class="kh-sim-case" role="img" aria-label="4000m 在四顆 Logical CPU 上的一種分配示意">
<div class="kh-sim-head"><strong>limit: 4000m</strong><span>平均相當於 4 Logical CPU</span></div>
<div class="kh-core-lanes">
<div class="kh-core-lane"><span>CPU 1</span><div class="kh-lane-track"><div class="kh-lane-fill kh-fill-100"></div></div></div>
<div class="kh-core-lane"><span>CPU 2</span><div class="kh-lane-track"><div class="kh-lane-fill kh-fill-100"></div></div></div>
<div class="kh-core-lane"><span>CPU 3</span><div class="kh-lane-track"><div class="kh-lane-fill kh-fill-100"></div></div></div>
<div class="kh-core-lane"><span>CPU 4</span><div class="kh-lane-track"><div class="kh-lane-fill kh-fill-100"></div></div></div>
</div>
<p class="kh-sim-caption"><code>1 秒</code>內最多累積 <code>4 秒</code>的 CPU 執行時間。</p>
</div>
<h3 class="kh-section">四種 Limit 放在一起比較</h3>
<div class="kh-table-scroll" role="region" aria-label="500m 到 4000m 的 CPU Limit 比較" tabindex="0">
<table class="kh-table kh-sim-table">
<thead><tr><th scope="col">CPU Limit</th><th scope="col">1 秒內最多 CPU time</th><th scope="col">平均相當於</th><th scope="col">充分利用的前提</th></tr></thead>
<tbody>
<tr><th scope="row"><code>500m</code></th><td><code>0.5 秒</code></td><td><code>0.5 Logical CPU</code></td><td>一個持續運算的 <code>Thread</code> 即可使用</td></tr>
<tr><th scope="row"><code>1000m</code></th><td><code>1 秒</code></td><td><code>1 Logical CPU</code></td><td>一個持續運算的 <code>Thread</code> 即可使用</td></tr>
<tr><th scope="row"><code>2000m</code></th><td><code>2 秒</code></td><td><code>2 Logical CPU</code></td><td>需要至少兩份可並行的 CPU 工作</td></tr>
<tr><th scope="row"><code>4000m</code></th><td><code>4 秒</code></td><td><code>4 Logical CPU</code></td><td>需要至少四份可並行的 CPU 工作</td></tr>
</tbody>
</table>
</div>
<h3 class="kh-section">2000m 不保證單一 Thread 快兩倍</h3>
<p><code>CPU Limit</code> 表示容器最多可以使用多少 CPU 時間，不代表單一工作會自動拆到多顆 <code>Logical CPU</code> 同時執行。假設 <code>C#</code> 程式只有一個 <code>Thread</code> 持續進行 CPU 密集運算，同一瞬間通常只能在一顆 <code>Logical CPU</code> 上執行。</p>
<div class="kh-ceiling" role="img" aria-label="2000m CPU Limit 與單一 Thread 約 1000m 使用上限的比較">
<div class="kh-ceiling-row">
<div class="kh-ceiling-label"><strong>Container Limit</strong><span>2000m</span></div>
<div class="kh-ceiling-track"><div class="kh-ceiling-fill kh-fill-100">2000m</div></div>
</div>
<div class="kh-ceiling-row">
<div class="kh-ceiling-label"><strong>單一 CPU 密集型 Thread</strong><span>約 1000m</span></div>
<div class="kh-ceiling-track"><div class="kh-ceiling-fill kh-fill-50">1000m</div></div>
</div>
</div>
<div class="kh-note">
<strong>Limit 是上限，不是效能保證</strong>
<p>即使設定 <code>2000m</code>，單一 CPU 密集型 <code>Thread</code> 仍可能只使用約 <code>1000m</code>。要利用超過一顆 <code>Logical CPU</code> 的運算能力，程式本身必須能把工作拆成多個可同時執行的部分。</p>
</div>
</div>
<!-- endtab -->





<!-- tab Thread, Nodes-->


<div class="kubernetes-helm">
<div class="kh-hero">
<h2>Thread、Node 與 CPU Limit 如何共同決定用量？</h2>
<p>容器實際能使用多少 CPU，不只看設定的 <code>CPU Limit</code>。<code>Node</code> 能提供多少 <code>Logical CPU</code>，以及程式能否把工作拆成多個可並行的 <code>Thread</code>，都會形成上限。</p>
</div>
<h3 class="kh-section">四個 Thread 共用 1000m</h3>
<p>假設 <code>Node</code> 有 <code>4</code> 個 <code>Logical CPU</code>，<code>C# Worker</code> 有 <code>4</code> 個 <code>Thread</code> 同時執行大量計算，而容器設定如下：</p>
<div class="kh-code">
<div class="kh-code-label">Container CPU Limit</div>
<pre class="kh-pre">limits:
  cpu: 1000m</pre>
</div>
<p>即使四個 <code>Thread</code> 都很忙，容器在長時間平均下仍然只能使用相當於一顆 <code>Logical CPU</code> 的運算時間。它們可能輪流取得 CPU，也可能短暫並行、快速耗盡額度，接著一起被 <code>Throttle</code>。</p>
<div class="kh-formula" role="img" aria-label="1000m 表示每經過一秒可使用一秒 CPU 執行時間">1000m = 每 1 秒可使用 1 秒 CPU time</div>
<h3 class="kh-section">硬體數量也會形成上限</h3>
<div class="kh-question">
<strong>容器的 <code>limits.cpu</code> 是 <code>2000m</code>，但 <code>Node</code> 只有一顆 <code>Logical CPU</code>，實際能使用多少？</strong>
<details class="kh-answer" open>
<summary>查看答案</summary>
<div class="kh-answer-body">
<p>實際最多約為 <code>1000m</code>。<code>2000m</code> 允許每秒最多累積兩秒 CPU 執行時間，但一顆 <code>Logical CPU</code> 每秒最多只能提供一秒 CPU 執行時間。設定允許的額度高於硬體容量時，硬體仍是最後的上限。</p>
</div>
</details>
</div>
<h3 class="kh-section">單一 Thread 也會形成上限</h3>
<p>假設 <code>Node</code> 有 <code>4 Core</code>，容器的設定如下，而 <code>C#</code> 程式只有一個 <code>Thread</code> 持續執行 CPU 密集型計算：</p>
<div class="kh-code">
<div class="kh-code-label">單一 Thread 情境</div>
<pre class="kh-pre">resources:
  limits:
    cpu: 2000m</pre>
</div>
<div class="kh-question">
<strong>這個容器實際上最多會使用多少 CPU？</strong>
<ol class="kh-options" type="A">
<li><code>1000m</code></li>
<li><code>2000m</code></li>
<li><code>4000m</code></li>
</ol>
<details class="kh-answer">
<summary>查看答案</summary>
<div class="kh-answer-body">
<p>答案是 <code>A. 1000m</code>。單一持續運算的 <code>Thread</code> 同一瞬間通常只能在一顆 <code>Logical CPU</code> 上執行。即使 <code>Node</code> 有四顆核心，而且容器允許使用 <code>2000m</code>，單一 <code>Thread</code> 仍只能累積約 <code>1000m</code> 的 CPU 使用量。</p>
</div>
</details>
</div>
<div class="kh-table-scroll" role="region" aria-label="單一 Thread CPU 使用條件整理" tabindex="0">
<table class="kh-table kh-unit-table">
<thead><tr><th scope="col">條件</th><th scope="col">數量</th></tr></thead>
<tbody>
<tr><th scope="row"><code>Node</code> 可用 CPU</th><td><code>4000m</code></td></tr>
<tr><th scope="row">容器 CPU Limit</th><td><code>2000m</code></td></tr>
<tr><th scope="row">CPU 密集型 Thread</th><td><code>1</code></td></tr>
<tr><th scope="row">實際最大 CPU 使用量</th><td>約 <code>1000m</code></td></tr>
</tbody>
</table>
</div>
<h3 class="kh-section">實際用量受到三個條件限制</h3>
<div class="kh-factor-grid" role="list" aria-label="影響 CPU 使用量的三個條件">
<div class="kh-factor" role="listitem"><strong>硬體資源</strong><span><code>Node</code> 有多少可用的 <code>Logical CPU</code>。</span></div>
<div class="kh-factor" role="listitem"><strong>程式平行能力</strong><span>有多少 <code>Thread</code> 或工作可以同時進行運算。</span></div>
<div class="kh-factor" role="listitem"><strong>CPU Limit</strong><span>容器最多允許累積多少 CPU 執行時間。</span></div>
</div>
<h3 class="kh-section">四個 Thread 如何耗盡一個 100ms 額度？</h3>
<div class="kh-question">
<strong><code>Node</code> 有四顆核心、容器 Limit 是 <code>1000m</code>，而四個 <code>Thread</code> 同時執行 CPU 密集型運算，Linux 可能如何處理？</strong>
<ol class="kh-options" type="A">
<li>只允許其中一個 <code>Thread</code> 執行，其他三個等待。</li>
<li>四個 <code>Thread</code> 可以同時執行，但會快速耗盡 CPU 額度，接著全部被 <code>Throttle</code>。</li>
<li>四個 <code>Thread</code> 持續執行，每個 <code>Thread</code> 的運算速度自動降低為 <code>25%</code>。</li>
</ol>
<details class="kh-answer" open>
<summary>查看答案</summary>
<div class="kh-answer-body">
<p>答案是 <code>B</code>。假設 Linux 的 <code>CPU quota period</code> 是 <code>100ms</code>，<code>1000m</code> 代表這個週期合計有 <code>100ms</code> 的 CPU 執行時間。四個 <code>Thread</code> 若分別在四顆 <code>Logical CPU</code> 上並行，每個執行約 <code>25ms</code> 就會共同用完額度。</p>
</div>
</details>
</div>
<div class="kh-formula" role="img" aria-label="1000m 等於每個 100 毫秒週期有 100 毫秒 CPU 執行時間">1000m = 100ms CPU time ÷ 100ms period</div>
<div class="kh-formula" role="img" aria-label="四個 Thread 各執行 25 毫秒等於 100 毫秒 CPU 執行時間">4 Threads × 25ms = 100ms CPU time</div>
<div class="kh-thread-scroll" role="region" aria-label="四個 Thread 在 25 毫秒內耗盡 CPU 額度的時間軸" tabindex="0">
<div class="kh-thread-period">
<div class="kh-thread-period-head"><strong>一個 100ms quota period</strong><span>Container limit: 1000m</span></div>
<div class="kh-thread-line"><strong>Thread 1</strong><div class="kh-thread-track"><div class="kh-thread-run">執行 25ms</div><div class="kh-thread-stop">Throttled 75ms</div></div></div>
<div class="kh-thread-line"><strong>Thread 2</strong><div class="kh-thread-track"><div class="kh-thread-run">執行 25ms</div><div class="kh-thread-stop">Throttled 75ms</div></div></div>
<div class="kh-thread-line"><strong>Thread 3</strong><div class="kh-thread-track"><div class="kh-thread-run">執行 25ms</div><div class="kh-thread-stop">Throttled 75ms</div></div></div>
<div class="kh-thread-line"><strong>Thread 4</strong><div class="kh-thread-track"><div class="kh-thread-run">執行 25ms</div><div class="kh-thread-stop">Throttled 75ms</div></div></div>
<div class="kh-thread-axis"><span></span><span>0ms</span><span><span>25ms</span><span>100ms</span></span></div>
</div>
</div>
<p>經過約 <code>25ms</code> 後，容器已經累積使用完整的 <code>100ms</code> CPU 額度。接下來約 <code>75ms</code>，受限制的 <code>Thread</code> 會等待下一個週期補充額度。</p>
<div class="kh-note">
<strong>CPU Limit 限制的是整個容器的累積 CPU time</strong>
<p><code>Thread</code> 數量增加不會增加 CPU 額度。多個 <code>Thread</code> 並行只會讓同一份額度更快被消耗完。</p>
</div>
</div>

<!-- endtab -->





<!-- tab Throttling-->


<div class="kubernetes-helm">
<div class="kh-hero">
<h2>CPU Throttling 發生時，程式並沒有被殺掉</h2>
<p>當容器想使用的 CPU 超過設定上限時，Linux 會暫時限制受管制的 <code>Thread</code>，等下一個額度週期再繼續執行。工作仍然存在，但完成時間可能被拉長。</p>
</div>
<h3 class="kh-section">從一個 .NET API 情境開始</h3>
<p>假設 <code>.NET API</code> 容器的 CPU request 是 <code>500m</code>，CPU limit 是 <code>1000m</code>：</p>
<div class="kh-code">
<div class="kh-code-label">.NET API CPU 資源設定</div>
<pre class="kh-pre">resources:
  requests:
    cpu: 500m
  limits:
    cpu: 1000m</pre>
</div>
<div class="kh-question">
<strong>大量 API Request 同時進入，CPU 使用需求達到 <code>3000m</code> 時，容器會被殺掉嗎？</strong>
<details class="kh-answer" open>
<summary>查看答案</summary>
<div class="kh-answer-body">
<p>不會只因 CPU 需求超過 Limit 就被殺掉。Linux 會透過 CPU throttling 暫時限制執行，讓受限制的 <code>Thread</code> 等待下一次可用額度。這和記憶體超過上限後可能發生的 <code>OOMKilled</code> 不同。</p>
</div>
</details>
</div>
<div class="kh-formula" role="img" aria-label="CPU Throttling 表示工作仍在但必須等待 CPU 額度">CPU Throttling = 工作仍在，等待 CPU 額度</div>
<h3 class="kh-section">額度耗盡後會反覆等待與繼續</h3>
<div class="kh-flow" role="list" aria-label="CPU Throttling 的循環流程">
<div class="kh-flow-step" role="listitem"><strong>執行工作</strong><span>消耗 CPU quota</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step" role="listitem"><strong>額度耗盡</strong><span>Quota exhausted</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step" role="listitem"><strong>暫停排程</strong><span>Throttled</span></div>
<span class="kh-flow-arrow" aria-hidden="true">→</span>
<div class="kh-flow-step" role="listitem"><strong>下個週期繼續</strong><span>Quota refilled</span></div>
</div>
<p>程式需要 <code>3000m</code> 的運算能力時，Linux 會先允許容器執行並消耗額度。該週期的額度用完後，受限制的 <code>Thread</code> 暫時停止排程；下一個週期補充額度後再繼續，如此反覆直到工作完成。</p>
<h3 class="kh-section">CPU time 不等於 Response Time</h3>
<p>假設一個 API 的計算總共需要 <code>100ms CPU time</code>。如果 CPU Limit 讓這些計算必須跨越多個週期，實際經過的 <code>Response Time</code> 可能變成 <code>200ms</code>、<code>300ms</code>，甚至更久。</p>
<div class="kh-response-scroll" role="region" aria-label="CPU Throttling 拉長 Response Time 的示意" tabindex="0">
<div class="kh-response-track">
<div class="kh-response-step run"><strong>執行一部分</strong><span>消耗 CPU time</span></div>
<div class="kh-response-step"><strong>等待額度</strong><span>Throttled</span></div>
<div class="kh-response-step run"><strong>繼續執行</strong><span>消耗 CPU time</span></div>
<div class="kh-response-step"><strong>再次等待</strong><span>Throttled</span></div>
<div class="kh-response-step run"><strong>工作完成</strong><span>Response returned</span></div>
</div>
</div>
<div class="kh-note">
<strong>CPU 工作量相同，牆上時鐘經過的時間可能更長</strong>
<p><code>CPU time</code> 計算實際在 CPU 上執行的時間；<code>Response Time</code> 還包含等待 CPU 額度、排程、輸入輸出與其他延遲。Throttling 增加的是等待時間，因此 API 延遲可能上升。</p>
</div>
<h3 class="kh-section">Grafana 上可能同時出現的現象</h3>
<div class="kh-symptom-grid" role="list" aria-label="CPU Throttling 的觀察現象">
<div class="kh-symptom" role="listitem"><strong>Pod 仍在執行</strong><span>沒有因 CPU Limit 而出現 <code>OOMKilled</code>。</span></div>
<div class="kh-symptom" role="listitem"><strong>CPU Usage 接近 Limit</strong><span>容器持續想使用可取得的 CPU 額度。</span></div>
<div class="kh-symptom" role="listitem"><strong>API Response Time 上升</strong><span>部分計算時間被拆到後續週期。</span></div>
<div class="kh-symptom" role="listitem"><strong>嚴重時出現 Timeout</strong><span>程式仍存活，但回應沒有在期限內完成。</span></div>
</div>
<h3 class="kh-section">requests 不會直接觸發 Throttling</h3>
<div class="kh-resource-grid" role="list" aria-label="CPU request 與 limit 對 Throttling 的影響">
<div class="kh-resource-card" role="listitem"><strong>requests.cpu: 500m</strong><span>主要供 <code>Kubernetes Scheduler</code> 排程時計算資源需求。使用量超過 <code>500m</code>，不代表立刻發生 Throttling。</span></div>
<div class="kh-resource-card" role="listitem"><strong>limits.cpu: 1000m</strong><span>這是 Linux 執行時限制 CPU 用量的上限。容器耗盡該週期額度後，才會因 CPU quota 被 Throttle。</span></div>
</div>
<h3 class="kh-section">排查 EKS API 效能時可觀察的 Metrics</h3>
<div class="kh-table-scroll" role="region" aria-label="CPU Throttling 監控指標" tabindex="0">
<table class="kh-table kh-metric-table">
<thead><tr><th scope="col">Metric</th><th scope="col">代表意義</th><th scope="col">判讀方向</th></tr></thead>
<tbody>
<tr><th scope="row"><code>container_cpu_cfs_throttled_periods_total</code></th><td>累積發生 Throttling 的 CPU enforcement period 數量。</td><td>持續增加表示容器反覆在週期內耗盡 CPU 額度。</td></tr>
<tr><th scope="row"><code>container_cpu_cfs_throttled_seconds_total</code></th><td>容器累積被 Throttle 的時間。</td><td>搭配變化速率觀察等待 CPU 額度的時間是否持續增加。</td></tr>
</tbody>
</table>
</div>
<p>在 <code>EKS</code> 排查 API 效能時，可把這兩項 Metrics 與 <code>CPU Usage</code>、<code>CPU Limit</code>、<code>Response Time</code> 和 <code>Timeout</code> 放在同一段時間範圍內比較。單看 CPU Usage 接近上限，無法判斷延遲是否確實由 Throttling 造成。</p>
</div>
<!-- endtab --> 





{% endtabs %}
