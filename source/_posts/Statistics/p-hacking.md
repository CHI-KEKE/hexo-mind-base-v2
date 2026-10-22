---
title: p-hacking
date: 2026-08-02 11:14:05
categories: Statistics
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/p-value/p-hacking-landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/p-value/p-hacking-landing.png
tags:
toc:
toc_number:
comments :
mathjax: true
---


{% tabs p-hacking%}



<!-- tab 實驗背景-->


實驗假設我們想要研發一種藥物，用來縮短感染某種病毒後的康復時間。研究人員製造了一批候選藥物（如 A 藥、B 藥，一直到 Z 藥），並將它們分別給予 3 位病患測試，同時記錄他們與另外 3 位「沒有吃藥」的病患在康復時間上的差異

<style>
.medchart-wrap { display: flex; flex-direction: column; gap: 28px; margin: 24px 0; }
.medchart {
background: #fbfaf6;
border: 1px solid #c9c3ae;
border-radius: 4px;
position: relative;
font-family: 'Courier New', 'Consolas', 'PingFang TC', monospace;
box-shadow: 0 1px 3px rgba(0,0,0,0.08);
padding-bottom: 4px;
}
.medchart::before {
content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 6px;
background: repeating-linear-gradient(180deg, #b9c9c6 0 10px, transparent 10px 20px);
}
.medchart-top {
display: flex; align-items: center; gap: 10px;
padding: 14px 20px 10px 26px; border-bottom: 2px solid #2f4f4f;
}
.medchart-cross { width: 26px; height: 26px; flex-shrink: 0; position: relative; }
.medchart-cross::before, .medchart-cross::after { content: ''; position: absolute; background: #3d6b66; }
.medchart-cross::before { left: 45%; top: 0; width: 12%; height: 100%; }
.medchart-cross::after  { top: 45%; left: 0; height: 12%; width: 100%; }
.medchart-title { font-weight: 700; font-size: 1.02rem; color: #2f4f4f; letter-spacing: 1px; }
.medchart-title small { display:block; font-weight:400; font-size:0.72rem; color:#8a9a97; letter-spacing:2px; margin-top:2px; }
.medchart-idbar { display: flex; flex-wrap: wrap; gap: 0; margin: 10px 20px 10px 26px; border: 1px solid #c9c3ae; }
.medchart-idbox { flex: 1; min-width: 140px; border-right: 1px dashed #c9c3ae; padding: 6px 12px; }
.medchart-idbox:last-child { border-right: none; }
.medchart-idbox .k { font-size: 0.68rem; color: #8a8272; letter-spacing: 1px; }
.medchart-idbox .v { font-size: 0.88rem; color: #2f2f2f; font-weight: 700; }
.medchart-field { margin: 0 20px 0 26px; padding: 10px 0; border-bottom: 1px dashed #d8d3c2; }
.medchart-field:last-of-type { border-bottom: none; }
.medchart-field .k {
display: inline-block; font-size: 0.72rem; color: #6b6250; letter-spacing: 2px;
border: 1px solid #c9c3ae; border-radius: 2px; padding: 1px 8px; margin-bottom: 6px; background: #f2efe4;
}
.medchart-field .v { font-size: 0.88rem; color: #2b2b2b; line-height: 1.9; }
.medchart-field .v code { background: #eef0eb; padding: 1px 6px; border-radius: 3px; font-size: 0.85em; color: #a3441e; }
.medchart-field ol, .medchart-field ul { margin: 4px 0 0; padding-left: 20px; }
.medchart-stamp {
display: inline-block; margin: 14px 20px 18px 26px; padding: 6px 16px;
border: 3px double #a3441e; color: #a3441e; font-weight: 700; font-size: 0.85rem;
letter-spacing: 2px; transform: rotate(-3deg); border-radius: 4px; background: rgba(163,68,30,0.04);
}
.case-timeline { position: relative; margin: 20px 0 30px; padding-left: 36px; }
.case-timeline::before {
content: ''; position: absolute; left: 9px; top: 4px; bottom: 4px; width: 2px;
background: repeating-linear-gradient(180deg, #b9c9c6 0 8px, transparent 8px 16px);
}
.tl-event { position: relative; margin-bottom: 18px; }
.tl-event:last-child { margin-bottom: 0; }
.tl-event::before {
content: ''; position: absolute; left: -31px; top: 3px; width: 12px; height: 12px;
border-radius: 50%; background: #3d6b66; border: 2px solid #fbfaf6; box-shadow: 0 0 0 1.5px #3d6b66;
}
.tl-event.warn::before   { background: #b8860b; box-shadow: 0 0 0 1.5px #b8860b; }
.tl-event.danger::before { background: #a3441e; box-shadow: 0 0 0 1.5px #a3441e; }
.tl-event.done::before   { background: #4f7942; box-shadow: 0 0 0 1.5px #4f7942; }
.tl-event .tl-card { background: #fbfaf6; border: 1px solid #d8d3c2; border-radius: 4px; padding: 8px 16px; }
.tl-event.warn .tl-card   { border-left: 3px solid #b8860b; }
.tl-event.danger .tl-card { border-left: 3px solid #a3441e; }
.tl-event.done .tl-card   { border-left: 3px solid #4f7942; }
.tl-head { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
.tl-head .tl-step {
font-family: 'Courier New', Consolas, monospace; font-size: 0.68rem; color: #8a8272;
border: 1px solid #c9c3ae; border-radius: 2px; padding: 0 6px; background: #f2efe4; flex-shrink: 0;
}
.tl-head .tl-title { font-weight: 700; color: #2f4f4f; font-size: 0.92rem; }
.tl-desc { font-size: 0.86rem; color: #2b2b2b; margin-top: 4px; line-height: 1.7; }
.tl-desc code { background: #eef0eb; padding: 1px 6px; border-radius: 3px; color: #a3441e; font-size: 0.85em; }
.plan-card { background: #fbfaf6; border: 1px solid #c9c3ae; border-radius: 4px; margin: 22px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.06); overflow: hidden; }
.plan-card .plan-head { display: flex; align-items: center; gap: 12px; padding: 12px 18px; background: #2f4f4f; color: #fbfaf6; }
.plan-card .plan-num {
font-family: 'Courier New', Consolas, monospace; font-weight: 700; font-size: 0.85rem;
border: 1px solid rgba(255,255,255,0.6); border-radius: 50%; width: 26px; height: 26px;
display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.plan-card .plan-title { font-weight: 700; font-size: 0.98rem; letter-spacing: 1px; }
.plan-card .plan-priority { font-size: 0.68rem; letter-spacing: 1px; padding: 2px 8px; border-radius: 10px; flex-shrink: 0; margin-left: auto; }
.plan-priority.high { background: #a3441e; color: #fff; }
.plan-priority.mid  { background: #b8860b; color: #fff; }
.plan-priority.low  { background: #6b8e6b; color: #fff; }
.plan-card .plan-body { padding: 16px 20px 18px; }
.plan-card .plan-body > p:first-child { margin-top: 0; }
.plan-card .plan-body code { color: #a3441e; background: #eef0eb; padding: 1px 6px; border-radius: 3px; }
.flow-note {
background: #fbfaf6; border: 1px dashed #c9c3ae; border-left: 4px solid #b8860b;
padding: 10px 18px; margin: 14px 0 20px; border-radius: 2px;
font-size: 0.92rem; color: #4a4636; line-height: 1.8;
}
.flow-note code { background: #eef0eb; padding: 1px 6px; border-radius: 3px; color: #a3441e; }
.flow-note.danger { background: #fbf1ee; border-color: #e0b8ab; border-left-color: #a3441e; color: #7a2e1f; }
.flow-note.danger code { background: #f3ded7; color: #8c2f1a; }
.flow-note.info { border-left-color: #3d6b66; }
</style>

<div class="medchart-wrap">
<div class="medchart">
<div class="medchart-top">
<div class="medchart-cross"></div>
<div class="medchart-title">測試案例：A 藥 ～ Y 藥（前 25 次測試）<small>MULTIPLE FAILED TRIALS</small></div>
</div>
<div class="medchart-idbar">
<div class="medchart-idbox"><div class="k">受試人數</div><div class="v">每種藥 3 人</div></div>
<div class="medchart-idbox"><div class="k">對照組</div><div class="v">3 人（未服藥）</div></div>
<div class="medchart-idbox"><div class="k">結果</div><div class="v">皆未達標</div></div>
</div>
<div class="medchart-field">
<div class="k">觀察紀錄</div>
<div class="v">逐一測試 A 藥、B 藥⋯⋯一路到 Y 藥，每一次計算出來的 <code>p 值</code>都大於 0.05，代表看不出這些藥物有比不吃藥更快恢復的證據</div>
</div>
<div class="medchart-field">
<div class="k">研究人員決策</div>
<div class="v">因為結果不理想，這些測試都沒有對外發表，研究人員直接接著測試下一款候選藥物</div>
</div>
</div>
<div class="medchart">
<div class="medchart-top">
<div class="medchart-cross"></div>
<div class="medchart-title">測試案例：Z 藥（第 26 次測試）<small>THE ONE THAT PASSED</small></div>
</div>
<div class="medchart-idbar">
<div class="medchart-idbox"><div class="k">受試人數</div><div class="v">3 人</div></div>
<div class="medchart-idbox"><div class="k">p 值</div><div class="v">0.02</div></div>
<div class="medchart-idbox"><div class="k">結果</div><div class="v">達標（&lt; 0.05）</div></div>
</div>
<div class="medchart-field">
<div class="k">觀察紀錄</div>
<div class="v">這一次算出的 <code>p 值</code>是 0.02，小於 0.05 這個顯著門檻</div>
</div>
<div class="medchart-field">
<div class="k">研究人員決策</div>
<div class="v">直接對外宣佈 Z 藥與不吃藥之間有顯著差異、判定 Z 藥有效，完全沒有提及前面 25 次失敗的測試</div>
</div>
<div class="medchart-stamp">結論標記：這就是典型的「挑櫻桃」（cherry-picking）</div>
</div>
</div>

<!-- endtab -->

<!-- tab 怎樣的實驗與結論推導會變成 P-hacking-->

## 隱瞞失敗數據只挑成功結果（多重檢定與挑櫻桃）

研究人員連續測試了許多藥物都發現沒效，直到不斷測試到 Z 藥時，才總算等到一次「看起來有效」的結果。下面的時序還原了這個過程：

<div class="case-timeline">
<div class="tl-event">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">連續測試多種候選藥物</span></div>
<div class="tl-desc">A 藥、B 藥⋯⋯一路測試下去，每一次的 <code>p 值</code>都大於 0.05，沒有一次達標</div>
</div>
</div>
<div class="tl-event">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">測試終於來到 Z 藥</span></div>
<div class="tl-desc">算出的 <code>p 值</code>為 0.02，小於 0.05 的標準</div>
</div>
</div>
<div class="tl-event danger">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">只公布 Z 藥的結果，宣稱藥物有效</span></div>
<div class="tl-desc">刻意只挑選（cherry-pick）看起來有效的單一數據來計算並報告 <code>p 值</code>，完全忽略前面所有失敗的測試</div>
</div>
</div>
</div>

<div class="flow-note danger">
⚠ 如果你做了 100 次測試，光靠隨機性就預期會有大約 5 次結果單純因為運氣而小於 0.05，也就是「假陽性」。這種做越多次測試、遇到假陽性機率就越高的現象，稱為<code>多重檢定問題</code>（multiple testing problem）。
</div>

## 看到 p 值接近達標，就「偷加數據」重新計算

研究人員原本依照設計好的樣本數完成測試，卻在看到 <code>p 值</code>差一點就達標時，動手腳讓它變得達標：

<div class="case-timeline">
<div class="tl-event">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">依原定樣本數完成測試</span></div>
<div class="tl-desc">計算出的 <code>p 值</code>是 0.06</div>
</div>
</div>
<div class="tl-event warn">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">結果非常接近 0.05，但沒有達標</span></div>
<div class="tl-desc">為了讓實驗結果看起來有效，研究人員不甘心就此結束</div>
</div>
</div>
<div class="tl-event warn">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">決定在兩組中各增加一筆觀測數據</span></div>
<div class="tl-desc">用追加樣本的方式，讓數字有機會往「顯著」的方向移動</div>
</div>
</div>
<div class="tl-event danger">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">重新計算得到 p 值 0.02，宣布顯著差異</span></div>
<div class="tl-desc">對外宣佈實驗出現顯著差異，藥物有效</div>
</div>
</div>
</div>

<div class="flow-note danger">
⚠ 0.05 這個顯著門檻的理論基礎，是建立在「只計算一次 <code>p 值</code>來做決定」的前提下。算出 0.06 後，為了讓 <code>p 值</code>變小而擅自增加數據並計算第二次，這種做法有極高的機率會產生假陽性的錯誤結果。
</div>

<!-- endtab -->

<!-- tab 正確的推導方法-->

針對測試多種藥物，研究人員絕對不能只挑好看的結果對外發表。正確的做法可以整理成下面兩個方案：

<div class="plan-card">
<div class="plan-head">
<div class="plan-num">1</div>
<div class="plan-title">誠實回報所有檢定結果，用偽發現率校正</div>
<span class="plan-priority high">優先度：高</span>
</div>
<div class="plan-body">

必須計算出每一次測試的 <code>p 值</code>，把所有結果都放進去，再用<code>偽發現率</code>（False Discovery Rate）這類的數學方法來校正所有的 <code>p 值</code>。這能將原本靠運氣過關的假陽性 <code>p 值</code>調整回大於 0.05，有效降低錯誤報告的機率。

也就是說，誠實地把這 100 次測試的 100 個 <code>p 值</code>（包含 A 藥的 0.86、某藥的 0.63、以及 Z 藥的 0.02 等），全部輸入到<code>偽發現率</code>的數學公式裡，公式會重新調整這些數字。原本 Z 藥看起來很漂亮的 <code>p 值</code>（0.02），經過校正後通常會變大，可能變成了 0.15。

</div>
</div>

<div class="plan-card">
<div class="plan-head">
<div class="plan-num">2</div>
<div class="plan-title">實驗前先做檢定力分析，決定正確樣本數</div>
<span class="plan-priority high">優先度：高</span>
</div>
<div class="plan-body">

絕對不能在看到 <code>p 值</code>接近 0.05 時就擅自增加觀測值。正確的做法是在實驗「開始之前」，就先進行<code>檢定力分析</code>（Power Analysis）來精確決定適當的樣本數（測試人數）。

如果已經做完實驗、且 <code>p 值</code>落在 0.05 邊緣，應該利用現有的數據去進行檢定力分析，藉此推算出未來若要進行新實驗時，真正需要的正確樣本數量。

</div>
</div>

<div class="flow-note info">
💡 想像自己是一個警察，工作是抓小偷，但監視器畫質很差，所以必須決定看到什麼程度才敢說「這就是小偷」。如果太嚴格、一定要看得超清楚才抓，結果很多真正的小偷都跑掉了，這就是<code>檢定力</code>（Power）低。如果太鬆、有點像就抓，很多無辜的人也會被抓，這就是 <code>Type I Error</code>（α）。統計就是一直在平衡「不要亂抓人（α）」與「不要放跑壞人（β）」，而 <code>Power</code> 就是抓到真正壞人的能力——<code>Power Analysis</code> 換成研究情境，就是在問「我要找多少受試者，才裝得起一台夠好的監視器？」
</div>

<!-- endtab -->

<!-- tab 常態分佈-->

假設我們去記錄一大群「完全沒有吃任何藥」的人感冒痊癒需要多久，並把這些時間畫成一個常態分佈圖（Normal Distribution）。這張時序還原了假陽性是怎麼一步步冒出來的：

<div class="case-timeline">
<div class="tl-event">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">沒吃藥的人，康復時間本來就有快有慢</span></div>
<div class="tl-desc">一般來說，大部分的人（約 95%）需要 5 到 15 天才能康復，但也有一小部分（約 2.5%）天生抵抗力強的人，不到 5 天就自己痊癒了，這是一個自然的隨機分佈</div>
</div>
</div>
<div class="tl-event">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">藥物若真的沒效，兩組人其實來自同一分佈</span></div>
<div class="tl-desc">吃這款藥的人，跟沒吃藥的人一模一樣，恢復時間數據完全來自於同一個常態分佈，只是隨機找了幾個人（例如 3 個人）當測試組</div>
</div>
</div>
<div class="tl-event warn">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">測試越多種藥，越容易巧合「中大獎」</span></div>
<div class="tl-desc">不斷找不同批的人來測試不同種（其實通通沒效）的藥物，遲早會剛好抽到一群天生恢復得很快的人吃某一種藥，又剛好抽到另一群恢復比較慢的人當對照組</div>
</div>
</div>
<div class="tl-event danger">
<div class="tl-card">
<div class="tl-head"><span class="tl-title">比較兩組數據，被誤判為藥物有效</span></div>
<div class="tl-desc">算出 <code>p 值</code>等於 0.02，小於 0.05 的顯著標準，看起來像「這兩組人應該來自不同的分佈，代表藥物有效」，但實際上這兩組人根本來自同一個分佈，純粹是人體恢復時間本來就有隨機性，加上做了非常多次測試，才碰巧抽出極端的結果，這就是所謂的<code>假陽性</code>（False positive）</div>
</div>
</div>
</div>

<!-- endtab -->


{% endtabs %}
