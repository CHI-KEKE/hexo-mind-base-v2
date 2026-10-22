---
title: Hypergeometric Distribution
date: 2026-07-21 08:45:05
categories: Statistics
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/hypergeometric-distribution/landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/hypergeometric-distribution/landing.png
tags:
toc:
toc_number:
comments :
mathjax: true
---

{% tabs hypothesis%}




<!-- tab 品管（Quality Control）-->

<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');
.ind-scope{--ind-bg:#1c1e22;--ind-panel:#24262b;--ind-card:#2f333a;--ind-line:#3a3f47;--ind-line2:#454b54;--ind-amber:#f2a900;--ind-red:#e2432b;--ind-green:#4caf6d;--ind-blue:#5b8db8;--ind-text:#e8e6df;--ind-sub:#9aa0a8;font-family:"Noto Sans TC",sans-serif;}
.ind-hero{background:linear-gradient(180deg,#2a2d33,#1c1e22);border:1px solid var(--ind-line2);border-radius:6px;padding:22px 26px;margin:6px 0 26px;position:relative;overflow:hidden;}
.ind-hero::before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(135deg,rgba(242,169,0,0.05) 0 10px,transparent 10px 20px);pointer-events:none;}
.ind-hero-eyebrow{display:inline-flex;align-items:center;gap:8px;font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:3px;font-size:12px;color:var(--ind-amber);text-transform:uppercase;}
.ind-hero-eyebrow::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--ind-amber);box-shadow:0 0 6px var(--ind-amber);}
.ind-hero-title{font-family:"Oswald",sans-serif;font-weight:700;font-size:22px;color:var(--ind-text);margin:10px 0 6px;letter-spacing:1px;}
.ind-hero-desc{color:var(--ind-sub);font-size:14px;line-height:1.7;margin:0;}
.ind-plate{display:flex;align-items:center;gap:14px;margin:34px 0 16px;padding-bottom:10px;border-bottom:2px solid var(--ind-line2);}
.ind-plate-num{flex:0 0 auto;font-family:"Share Tech Mono",Consolas,monospace;font-weight:700;font-size:13px;color:#1c1e22;background:var(--ind-amber);border-radius:3px;padding:5px 10px;letter-spacing:1px;}
.ind-plate-title{font-family:"Oswald",sans-serif;font-weight:600;font-size:18px;color:#24262b;letter-spacing:0.5px;}
.ind-plate--sub{margin:26px 0 14px;padding-bottom:8px;border-bottom:1px dashed var(--ind-line);}
.ind-plate--sub .ind-plate-num{background:var(--ind-blue);color:#12202b;font-size:12px;}
.ind-plate--sub .ind-plate-title{font-size:16px;color:#4a4f57;}
.ind-closing{text-align:center;padding:10px 0 4px;color:var(--ind-sub);font-family:"Share Tech Mono",Consolas,monospace;font-size:12px;letter-spacing:2px;text-transform:uppercase;}
.ind-panel{background:#24262b;border:1px solid #454b54;border-radius:4px;padding:18px 22px;margin:18px 0;color:#e8e6df;position:relative;padding-left:26px;}
.ind-panel::before{content:"";position:absolute;top:0;left:0;width:6px;height:100%;background:#f2a900;border-radius:4px 0 0 4px;}
.ind-panel.ind-panel--danger::before{background:#e2432b;}
.ind-panel.ind-panel--safe::before{background:#4caf6d;}
.ind-panel.ind-panel--info::before{background:#5b8db8;}
.ind-label{display:inline-block;font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:2px;font-size:12px;text-transform:uppercase;color:#f2a900;background:#2f333a;border:1px solid #454b54;padding:3px 10px;border-radius:2px;margin-bottom:10px;}
.ind-panel.ind-panel--danger .ind-label{color:#ff7a63;}
.ind-panel.ind-panel--safe .ind-label{color:#7fd99a;}
.ind-panel.ind-panel--info .ind-label{color:#8fc1e8;}
.ind-panel ol,.ind-panel ul{margin:6px 0;padding-left:20px;}
.ind-steps{display:flex;flex-direction:column;gap:0;margin:18px 0;}
.ind-step{display:flex;gap:16px;background:#24262b;border:1px solid #3a3f47;border-left:4px solid #5b8db8;border-radius:4px;padding:16px 20px;position:relative;}
.ind-step + .ind-step{margin-top:14px;}
.ind-step-num{flex:0 0 auto;width:38px;height:38px;border-radius:50%;background:#1c1e22;border:2px solid #5b8db8;color:#8fc1e8;font-family:"Share Tech Mono",Consolas,monospace;font-weight:700;font-size:16px;display:flex;align-items:center;justify-content:center;}
.ind-step-body{flex:1;color:#e8e6df;}
.ind-step-title{display:block;font-family:"Oswald",sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;color:#f2a900;text-transform:uppercase;margin-bottom:6px;}
.ind-step-desc{margin:0;line-height:1.7;color:#cfd3d8;}
.ind-step--legacy{border-left-color:#9aa0a8;}
.ind-step--legacy .ind-step-num{border-color:#9aa0a8;color:#c3c8ce;}
.ind-step--legacy .ind-step-title{color:#c3c8ce;}
.ind-panel p{margin:6px 0;}
.ind-readout{background:#1c1e22;border:1px solid #3a3f47;border-radius:4px;padding:14px 18px;margin:16px 0;font-family:"Share Tech Mono",Consolas,monospace;color:#cfd3d8;}
.ind-readout-line{display:flex;flex-wrap:wrap;align-items:center;gap:12px;padding:4px 0;}
.ind-readout-label{color:#9aa0a8;font-size:13px;min-width:180px;}
.ind-dots{letter-spacing:3px;font-size:16px;color:#e8e6df;}
.ind-dots--pass{color:#7fd99a;}
.ind-stamp-row{display:flex;gap:14px;flex-wrap:wrap;margin:20px 0;}
.ind-stamp{flex:1;min-width:160px;background:#2f333a;border:1px solid #454b54;border-top:4px solid #9aa0a8;border-radius:4px;padding:16px;text-align:center;}
.ind-stamp--danger{border-top-color:#e2432b;}
.ind-stamp--warn{border-top-color:#f2a900;}
.ind-stamp--safe{border-top-color:#4caf6d;}
.ind-stamp-tag{display:block;font-family:"Oswald",sans-serif;font-size:11px;letter-spacing:2px;color:#9aa0a8;text-transform:uppercase;margin-bottom:4px;}
.ind-stamp-title{display:block;font-family:"Oswald",sans-serif;font-weight:600;color:#e8e6df;font-size:16px;margin-bottom:10px;}
.ind-stamp-formula{color:#e8e6df;margin:8px 0;}
.ind-stamp-result{font-family:"Share Tech Mono",Consolas,monospace;font-size:26px;font-weight:700;margin:6px 0;}
.ind-stamp--danger .ind-stamp-result{color:#ff7a63;}
.ind-stamp--warn .ind-stamp-result{color:#f2a900;}
.ind-stamp--safe .ind-stamp-result{color:#7fd99a;}
.ind-stamp-verdict{font-size:13px;color:#9aa0a8;}
.ind-flow{background:#1c1e22;border:1px solid #3a3f47;border-radius:4px;padding:18px 22px;margin:18px 0;text-align:center;}
.ind-flow-step{display:inline-block;font-family:"Oswald",sans-serif;font-weight:500;color:#e8e6df;background:#2f333a;border:1px solid #454b54;border-radius:3px;padding:8px 16px;margin:2px 0;}
.ind-flow-arrow{color:#f2a900;font-size:18px;margin:2px 0;}
.ind-final-stamp{border:3px double #f2a900;border-radius:6px;padding:20px 26px;margin:24px 0;text-align:center;background:#24262b;}
.ind-final-stamp-label{font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:3px;font-size:13px;color:#f2a900;text-transform:uppercase;margin-bottom:8px;}
.ind-final-stamp-text{font-size:17px;color:#e8e6df;font-weight:500;}
</style>

我要抽多少個、而且都沒發現瑕疵，才能有足夠信心認為整批的瑕疵率低於某個門檻？這個問題在品管上叫做 <code>Acceptance Sampling</code>（允收抽樣）。

<div class="ind-scope">
<div class="ind-hero">
<span class="ind-hero-eyebrow">Acceptance Sampling · 允收抽樣</span>
<div class="ind-hero-title">從「抽幾件檢查」推導出「敢不敢驗收整批」</div>
<p class="ind-hero-desc">這篇要解決的問題只有一個：整批貨裡藏著看不見的瑕疵品，我們要抽多少件出來檢查，抽到 0 個瑕疵時，才有把握說「這批貨可以驗收」。下面用同一組情境，一步步把邏輯、算式、結論都走過一遍。</p>
</div>

<div class="ind-plate">
<span class="ind-plate-num">STAGE 01</span>
<span class="ind-plate-title">情境：1,000 件產品裡藏了 10 個瑕疵品</span>
</div>

假設有一批 1,000 個產品，裡面其實偷偷混了 990 個正常品、10 個瑕疵品，但你不知道是哪 10 個，只能隨機抽一些出來檢查。

<div class="ind-panel ind-panel--danger">
<span class="ind-label">⚠ 抽樣風險</span>
<p>雖然整批真的有 10 個瑕疵品，但抽樣時可能運氣很好，抽到的全部都是正常品——你看到全部正常，可能誤以為整批很好，但事實上瑕疵品只是沒被你抽中而已。</p>
</div>

例如只抽 5 個：

<div class="ind-readout">
<div class="ind-readout-line"><span class="ind-readout-label">整批（1,000 件示意，● 共 10 個）</span><span class="ind-dots">○○○●○○○○●○……</span></div>
<div class="ind-readout-line"><span class="ind-readout-label">實際抽到的 5 件</span><span class="ind-dots ind-dots--pass">○ ○ ○ ○ ○</span></div>
</div>

（○ 是正常品，● 是瑕疵品）

<div class="ind-plate">
<span class="ind-plate-num">STAGE 02</span>
<span class="ind-plate-title">「不得超過 5%」是什麼意思</span>
</div>

把「同樣的一批產品、同樣的抽法」想像重複做 100 次，而且這批產品每次都確實有 10 個瑕疵品。我希望在這 100 次抽樣中，最多只有大約 5 次會完全漏掉所有瑕疵品——也就是約 95 次至少抓到 1 個瑕疵品，最多約 5 次一個瑕疵品都沒抓到。寫成算式就是：

$$P(\text{完全沒抽到瑕疵} \mid \text{整批有 10 個瑕疵}) \le 5\%$$

這並不是說產品有 5% 瑕疵，而是「抽樣檢查漏掉不良批次的風險，最多接受 5%」。

<div class="ind-plate">
<span class="ind-plate-num">STAGE 03</span>
<span class="ind-plate-title">用比較小的例子直接算給你看</span>
</div>

假設有 10 顆球，正常 8 顆、瑕疵 2 顆。

<div class="ind-stamp-row">
<div class="ind-stamp ind-stamp--danger">
<span class="ind-stamp-tag">Sample 1</span>
<span class="ind-stamp-title">只抽 1 顆</span>
<div class="ind-stamp-formula">$\dfrac{\binom{8}{1}}{\binom{10}{1}}$</div>
<div class="ind-stamp-result">80%</div>
<span class="ind-stamp-verdict">明明有瑕疵，卻高機率看不見</span>
</div>
<div class="ind-stamp ind-stamp--warn">
<span class="ind-stamp-tag">Sample 2</span>
<span class="ind-stamp-title">抽 5 顆</span>
<div class="ind-stamp-formula">$\dfrac{\binom{8}{5}}{\binom{10}{5}}=\dfrac{56}{252}$</div>
<div class="ind-stamp-result">≈22.2%</div>
<span class="ind-stamp-verdict">仍有約兩成漏掉瑕疵品</span>
</div>
<div class="ind-stamp ind-stamp--safe">
<span class="ind-stamp-tag">Sample 3</span>
<span class="ind-stamp-title">抽 8 顆</span>
<div class="ind-stamp-formula">$\dfrac{\binom{8}{8}}{\binom{10}{8}}=\dfrac{1}{45}$</div>
<div class="ind-stamp-result">≈2.22%</div>
<span class="ind-stamp-verdict">已低於 5%，達標</span>
</div>
</div>

抽 8 顆時，完全沒抽到瑕疵就代表你剛好把 8 顆正常品全部抽走，機率只剩 <code>2.22%</code>，已經小於 5% 的門檻。反過來說，$1-2.22\%=97.78\%$，你有 97.78% 的機率至少抓到一顆瑕疵。

<div class="ind-plate">
<span class="ind-plate-num">STAGE 04</span>
<span class="ind-plate-title">回到 1,000 件產品的例子</span>
</div>

我們先假設一個需要排除的狀況：整批有 10 個瑕疵，也就是瑕疵率達到 1%。現在決定抽 n 個，希望這個抽樣計畫具有以下能力：

<div class="ind-flow">
<div class="ind-flow-step">假如整批真的有 10 個瑕疵</div>
<div class="ind-flow-arrow">↓</div>
<div class="ind-flow-step">抽 n 個時</div>
<div class="ind-flow-arrow">↓</div>
<div class="ind-flow-step">至少有 95% 機率抓到一個以上</div>
</div>

因為結果只有「抓到至少一個」和「完全沒抓到」兩種，$P(\text{抓到至少一個})+P(\text{完全沒抓到})=100\%$，所以「等價地說」就是：

$$P(\text{沒抓到}) \le 5\% \iff P(\text{至少抓到一個}) \ge 95\%$$

**為什麼先假設「真的有 10 個瑕疵」？** 這是在設定你想防守的品質底線。例如公司規定 1% 瑕疵率已經不可接受，對 1,000 個產品而言，1% 就是 10 個。因此設計抽樣方式時會問：如果有一批不合格產品真的含有 10 個瑕疵，我們的抽樣方法能不能以至少 95% 的機率把它抓出來？能抓出來，代表這套抽樣方法有足夠辨識能力；經常抓不出來，就代表抽得太少、這套方法不可靠。

<div class="ind-plate ind-plate--sub">
<span class="ind-plate-num">STAGE 04-A</span>
<span class="ind-plate-title">那到底該抽多少個？</span>
</div>

跟前面「10 顆球」的小例子邏輯完全一樣，只是母體從 10 顆換成 1,000 件、瑕疵從 2 個換成 10 個。抽 n 個時，完全沒抽到瑕疵的機率是：

$$P(\text{沒抓到}) = \dfrac{\binom{990}{n}}{\binom{1000}{n}} \le 5\%$$

這一步<code>不是人工一個一個帶入算出來的</code>——$\binom{990}{257}$、$\binom{1000}{257}$ 這種組合數，分子分母都是幾百位數的天文數字，人腦或計算機根本算不出來，實務上會這樣分工：

<div class="ind-steps">
<div class="ind-step">
<span class="ind-step-num">1</span>
<div class="ind-step-body">
<span class="ind-step-title">取 log，避免數字爆掉</span>
<p class="ind-step-desc">電腦不會真的把每個 $n$ 的組合數乘開，而是先取 <code>log</code>，把乘除變成加減：$\log\binom{a}{b}=\log a! - \log b! - \log(a-b)!$，數值才不會超出電腦能處理的範圍。</p>
</div>
</div>
<div class="ind-step">
<span class="ind-step-num">2</span>
<div class="ind-step-body">
<span class="ind-step-title">用二分搜尋，不用逐一硬試</span>
<p class="ind-step-desc">$P(\text{沒抓到})$ 會隨著 $n$ 增加而<code>單調遞減</code>（樣本抽得越多，完全漏網的機率當然越低），所以不需要從 $n=1$ 一路試到 $n=258$——用二分搜尋法，大約十幾次運算就能鎖定「第一個機率跌破 5% 的 $n$」，這也是 Excel 內建函式 <code>HYPGEOM.DIST</code> 在背後做的事。</p>
</div>
</div>
<div class="ind-step ind-step--legacy">
<span class="ind-step-num">3</span>
<div class="ind-step-body">
<span class="ind-step-title">電腦普及前：直接查表</span>
<p class="ind-step-desc">在還沒有電腦的年代，品管工程師是靠事先算好的<code>允收抽樣表</code>（例如 <code>MIL-STD-105E</code>、<code>ANSI/ASQ Z1.4</code>）直接查表決定 $n$，不需要每次臨時計算。</p>
</div>
</div>
</div>

用電腦跑出來的結果，剛好落在 $n=257$ 與 $n=258$ 的交界：

<div class="ind-stamp-row">
<div class="ind-stamp ind-stamp--danger">
<span class="ind-stamp-tag">n = 257</span>
<span class="ind-stamp-title">抽 257 件</span>
<div class="ind-stamp-result">5.048%</div>
<span class="ind-stamp-verdict">仍高於 5%，風險不合格</span>
</div>
<div class="ind-stamp ind-stamp--safe">
<span class="ind-stamp-tag">n = 258</span>
<span class="ind-stamp-title">抽 258 件</span>
<div class="ind-stamp-result">4.980%</div>
<span class="ind-stamp-verdict">首次低於 5%，達標</span>
</div>
</div>

也就是說，1,000 件產品中，<code>至少要抽 258 件</code>，才能保證「如果整批真的有 10 個瑕疵（瑕疵率 1%），完全抽不到瑕疵的機率不超過 5%」；抽 257 件則還差一點點，機率是 5.048%，仍未達標。

<div class="ind-plate">
<span class="ind-plate-num">STAGE 05</span>
<span class="ind-plate-title">最容易搞混的地方</span>
</div>

抽到 0 個瑕疵，<code>不是</code>直接證明整批瑕疵率低於 1%。比較精確的說法是：假如整批瑕疵率真的已達 1%，以目前的抽樣數量仍然抽到 0 個瑕疵的機率不到 5%。因此當你真的抽到 0 個時，就有理由認為「整批至少有 1% 瑕疵」這個假設不太符合觀察結果——整個邏輯和假設檢定非常像：

<div class="ind-flow">
<div class="ind-flow-step">先假設：整批有 10 個瑕疵</div>
<div class="ind-flow-arrow">↓</div>
<div class="ind-flow-step">計算：抽樣卻完全沒看到瑕疵有多罕見</div>
<div class="ind-flow-arrow">↓</div>
<div class="ind-flow-step">如果非常罕見（≤ 5%），實際又真的抽到 0 個</div>
<div class="ind-flow-arrow">↓</div>
<div class="ind-flow-step">有理由排除「整批有 10 個以上瑕疵」</div>
</div>

<div class="ind-final-stamp">
<span class="ind-final-stamp-label">驗收準則 · Acceptance Criterion</span>
<span class="ind-final-stamp-text">我們想讓壞批次成功蒙混過關的機率低於 5%。</span>
</div>

<div class="ind-closing">— End of Inspection Report —</div>
</div>

<!-- endtab -->


<!-- tab 撲克牌-->

<style>
.pk-scope{--pk-felt:#0b3d2e;--pk-felt2:#125843;--pk-line:rgba(212,175,55,0.4);--pk-gold:#d4af37;--pk-cream:#f5f1e6;--pk-red:#d1373f;--pk-black:#1c1c1c;--pk-sub:#bcd9cb;font-family:"Noto Sans TC",sans-serif;}
.pk-hero{background:linear-gradient(180deg,#0f4d38,#0b3d2e);border:1px solid var(--pk-line);border-radius:10px;padding:24px 28px;margin:6px 0 26px;position:relative;overflow:hidden;}
.pk-hero::before{content:"♠ ♥ ♦ ♣";position:absolute;right:18px;top:16px;font-size:22px;color:rgba(212,175,55,0.25);letter-spacing:6px;}
.pk-hero-eyebrow{display:inline-flex;align-items:center;gap:8px;font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:3px;font-size:12px;color:var(--pk-gold);text-transform:uppercase;}
.pk-hero-title{font-family:"Oswald",sans-serif;font-weight:700;font-size:21px;color:var(--pk-cream);margin:10px 0 6px;letter-spacing:0.5px;}
.pk-hero-desc{color:var(--pk-sub);font-size:14px;line-height:1.8;margin:0;}
.pk-stat-row{display:flex;flex-wrap:wrap;gap:14px;margin:20px 0;}
.pk-stat{flex:1;min-width:140px;background:#fffdf7;border:1px solid #e3d9b8;border-radius:8px;padding:14px 16px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,0.08);}
.pk-stat-num{display:block;font-family:"Oswald",sans-serif;font-weight:700;font-size:24px;color:var(--pk-black);}
.pk-stat-suit{font-size:18px;margin-left:4px;}
.pk-stat-suit.red{color:var(--pk-red);}
.pk-stat-suit.black{color:var(--pk-black);}
.pk-stat-label{display:block;font-size:12px;color:#7a7568;margin-top:6px;letter-spacing:0.5px;}
.pk-panel{background:#fffdf7;border:1px solid #e3d9b8;border-radius:8px;padding:18px 22px;margin:18px 0;position:relative;padding-left:26px;}
.pk-panel::before{content:"";position:absolute;top:0;left:0;width:6px;height:100%;background:var(--pk-gold);border-radius:8px 0 0 8px;}
.pk-panel p{margin:6px 0;line-height:1.8;color:#3a3a34;}
.pk-map-table{border-collapse:collapse;width:auto;max-width:100%;margin:14px 0;font-size:14px;}
.pk-map-table th,.pk-map-table td{border:1px solid #e3d9b8;padding:8px 14px;text-align:left;}
.pk-map-table th{background:#0b3d2e;color:var(--pk-cream);font-family:"Oswald",sans-serif;letter-spacing:0.5px;}
.pk-map-table td{background:#fffdf7;color:#3a3a34;}
.pk-map-table td code{color:var(--pk-red);}
.pk-card{background:#fffdf7;border:2px solid var(--pk-gold);border-radius:12px;padding:22px 26px;margin:22px 0;position:relative;box-shadow:0 4px 12px rgba(0,0,0,0.15);}
.pk-card::before{content:"♥";position:absolute;top:10px;left:14px;font-size:18px;color:var(--pk-red);}
.pk-card::after{content:"♥";position:absolute;bottom:10px;right:14px;font-size:18px;color:var(--pk-red);transform:rotate(180deg);}
.pk-card-label{font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:2px;font-size:12px;color:var(--pk-gold);text-transform:uppercase;text-align:center;background:#0b3d2e;display:inline-block;padding:4px 12px;border-radius:4px;}
.pk-card-labelwrap{text-align:center;margin-bottom:10px;}
.pk-card-formula{text-align:center;font-family:"Share Tech Mono",Consolas,monospace;font-size:16px;color:#3a3a34;margin:10px 0;line-height:2;}
.pk-dist{margin:20px 0;}
.pk-dist-row{display:flex;align-items:center;gap:10px;margin:6px 0;}
.pk-dist-k{width:78px;flex:0 0 auto;font-family:"Share Tech Mono",Consolas,monospace;font-size:13px;color:#3a3a34;}
.pk-dist-bar-wrap{flex:1;background:#efe9d8;border-radius:4px;overflow:hidden;height:22px;}
.pk-dist-bar{height:100%;background:linear-gradient(90deg,#125843,#1e7a5c);}
.pk-dist-row--hit .pk-dist-bar{background:linear-gradient(90deg,#d1373f,#e8626a);}
.pk-dist-row--hit .pk-dist-k{color:var(--pk-red);font-weight:700;}
.pk-dist-pct{width:64px;flex:0 0 auto;text-align:right;font-family:"Share Tech Mono",Consolas,monospace;font-size:13px;color:#3a3a34;}
.pk-final{border:3px double var(--pk-gold);border-radius:10px;padding:22px 28px;margin:26px 0;text-align:center;background:#0b3d2e;}
.pk-final-label{font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:3px;font-size:13px;color:var(--pk-gold);text-transform:uppercase;margin-bottom:8px;display:block;}
.pk-final-text{font-size:18px;color:var(--pk-cream);font-weight:600;}
.pk-final-sub{font-size:13px;color:var(--pk-sub);margin-top:6px;}
.pk-closing{text-align:center;padding:10px 0 4px;color:var(--pk-gold);font-family:"Share Tech Mono",Consolas,monospace;font-size:12px;letter-spacing:2px;text-transform:uppercase;}
</style>

換一個大家更有感覺的情境：撲克牌。同樣是「一批東西裡混著兩種類型，不放回地抽幾張」，只是這次我們關心的不是瑕疵品，而是抽到的花色。

<div class="pk-scope">
<div class="pk-hero">
<span class="pk-hero-eyebrow">Card Draw · 抽牌問題</span>
<div class="pk-hero-title">洗勻的一副牌，抽 5 張剛好湊到 3 張愛心的機率有多高？</div>
<p class="pk-hero-desc">拿一副完整的撲克牌（52 張，愛心 ♥ 有 13 張），洗勻後隨機抽出 5 張。想知道「剛好抽到 3 張愛心」的機率，跟前面瑕疵品的問題是同一套數學：整批東西只分兩種身分（愛心／不是愛心），抽出來的牌不放回去，所以每抽一張都會改變剩下牌堆的組成。</p>
</div>

<div class="pk-stat-row">
<div class="pk-stat"><span class="pk-stat-num">52</span><span class="pk-stat-label">整副牌總張數</span></div>
<div class="pk-stat"><span class="pk-stat-num">13<span class="pk-stat-suit red">♥</span></span><span class="pk-stat-label">愛心張數</span></div>
<div class="pk-stat"><span class="pk-stat-num">5</span><span class="pk-stat-label">實際抽出張數</span></div>
<div class="pk-stat"><span class="pk-stat-num">3<span class="pk-stat-suit red">♥</span></span><span class="pk-stat-label">想湊到的愛心張數</span></div>
</div>

<div class="pk-panel">
<p>這題符合超幾何分布的三個條件：<code>牌堆總數固定</code>（52 張）、<code>只分兩類</code>（愛心 13 張、非愛心 39 張），以及<code>抽出來不放回</code>（手上的 5 張牌不會再洗回牌堆）。只要這三點成立，不管是瑕疵品還是撲克牌，算法都長一樣。</p>
</div>

<table class="pk-map-table">
<tr><th>超幾何分布的符號</th><th>代表意義</th><th>對應到這副牌</th></tr>
<tr><td><code>N</code></td><td>整批東西的總數</td><td>52 張牌</td></tr>
<tr><td><code>K</code></td><td>整批裡「感興趣類型」的數量</td><td>13 張愛心</td></tr>
<tr><td><code>n</code></td><td>實際抽出的數量</td><td>5 張</td></tr>
<tr><td><code>k</code></td><td>想湊到「感興趣類型」的張數</td><td>3 張愛心</td></tr>
</table>

<div class="pk-card">
<div class="pk-card-labelwrap"><span class="pk-card-label">Formula · 算式</span></div>
<div class="pk-card-formula">P(剛好 3 張愛心) = C(13,3) × C(39,2) ÷ C(52,5)</div>
<div class="pk-card-formula">= 286 × 741 ÷ 2,598,960</div>
<div class="pk-card-formula">= 211,926 ÷ 2,598,960 ≈ <code>8.15%</code></div>
</div>

拆開來看這個算式在算什麼：<code>C(13,3)</code> 是「從 13 張愛心裡挑 3 張出來」的組合數，<code>C(39,2)</code> 是「從剩下 39 張非愛心裡挑 2 張湊滿 5 張手牌」的組合數，兩者相乘就是「剛好 3 張愛心、2 張非愛心」的所有可能手牌數；分母 <code>C(52,5)</code> 則是「從 52 張裡任意抽 5 張」的所有可能手牌總數，兩者相除就是機率。

<div class="pk-dist">
<div class="pk-dist-row"><span class="pk-dist-k">k = 0 張</span><div class="pk-dist-bar-wrap"><div class="pk-dist-bar" style="width:22.2%;"></div></div><span class="pk-dist-pct">22.15%</span></div>
<div class="pk-dist-row"><span class="pk-dist-k">k = 1 張</span><div class="pk-dist-bar-wrap"><div class="pk-dist-bar" style="width:41.1%;"></div></div><span class="pk-dist-pct">41.14%</span></div>
<div class="pk-dist-row"><span class="pk-dist-k">k = 2 張</span><div class="pk-dist-bar-wrap"><div class="pk-dist-bar" style="width:27.4%;"></div></div><span class="pk-dist-pct">27.43%</span></div>
<div class="pk-dist-row pk-dist-row--hit"><span class="pk-dist-k">k = 3 張 ★</span><div class="pk-dist-bar-wrap"><div class="pk-dist-bar" style="width:8.2%;"></div></div><span class="pk-dist-pct">8.15%</span></div>
<div class="pk-dist-row"><span class="pk-dist-k">k = 4 張</span><div class="pk-dist-bar-wrap"><div class="pk-dist-bar" style="width:1.1%;"></div></div><span class="pk-dist-pct">1.07%</span></div>
<div class="pk-dist-row"><span class="pk-dist-k">k = 5 張</span><div class="pk-dist-bar-wrap"><div class="pk-dist-bar" style="width:0.3%;"></div></div><span class="pk-dist-pct">0.05%</span></div>
</div>

把 k = 0 到 5 全部算完會發現：抽 5 張牌，最容易出現的其實是<code>剛好 1 張愛心</code>（41.14%），因為愛心只佔整副牌的四分之一左右；反而是「剛好 3 張」或更多愛心，因為要連續湊到偏離平均的張數，機率自然快速下滑。這也是超幾何分布的典型長相——中間某個值機率最高，往兩端遞減。

<div class="pk-final">
<span class="pk-final-label">Card Table Verdict · 結論</span>
<span class="pk-final-text">洗勻的一副牌抽 5 張，剛好湊到 3 張愛心的機率約 8.15%</span>
<div class="pk-final-sub">比抽到 1 張愛心（41.14%）低了整整 5 倍，但仍遠比抽到 4、5 張常見</div>
</div>

<div class="pk-closing">— Shuffle Up And Deal —</div>
</div>

<!-- endtab -->

<!-- tab 威力彩-->

<style>
.lp-scope{--lp-red:#c8102e;--lp-red-dark:#8f0c20;--lp-gold:#f2b705;--lp-gold-dark:#c8960c;--lp-cream:#fff8e7;--lp-ink:#2b241a;--lp-sub:#8a7a55;--lp-green:#2f9e5b;font-family:"Noto Sans TC",sans-serif;}
.lp-hero{background:linear-gradient(135deg,#c8102e,#8f0c20);border-radius:10px;padding:24px 28px;margin:6px 0 26px;position:relative;overflow:hidden;}
.lp-hero::before{content:"★ LOTTO ★ LOTTO ★";position:absolute;right:16px;top:14px;font-size:12px;letter-spacing:3px;color:rgba(255,248,231,0.25);}
.lp-hero-eyebrow{display:inline-flex;align-items:center;gap:8px;font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:3px;font-size:12px;color:var(--lp-gold);text-transform:uppercase;}
.lp-hero-title{font-family:"Oswald",sans-serif;font-weight:700;font-size:21px;color:var(--lp-cream);margin:10px 0 6px;letter-spacing:0.5px;}
.lp-hero-desc{color:#f0d9c8;font-size:14px;line-height:1.8;margin:0;}
.lp-stat-row{display:flex;flex-wrap:wrap;gap:14px;margin:20px 0;}
.lp-stat{flex:1;min-width:140px;background:var(--lp-cream);border:1px solid #e9d38f;border-radius:8px;padding:14px 16px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,0.08);}
.lp-stat-num{display:block;font-family:"Oswald",sans-serif;font-weight:700;font-size:24px;color:var(--lp-red);}
.lp-stat-label{display:block;font-size:12px;color:var(--lp-sub);margin-top:6px;letter-spacing:0.5px;}
.lp-panel{background:var(--lp-cream);border:1px solid #e9d38f;border-radius:8px;padding:18px 22px;margin:18px 0;position:relative;padding-left:26px;}
.lp-panel::before{content:"";position:absolute;top:0;left:0;width:6px;height:100%;background:var(--lp-red);border-radius:8px 0 0 8px;}
.lp-panel p{margin:6px 0;line-height:1.8;color:var(--lp-ink);}
.lp-ticket{background:var(--lp-cream);border:2px dashed var(--lp-gold-dark);border-radius:10px;padding:20px 24px;margin:20px 0;}
.lp-ticket-row{display:flex;align-items:center;gap:14px;margin:10px 0;flex-wrap:wrap;}
.lp-ticket-row-label{flex:0 0 96px;font-family:"Oswald",sans-serif;font-weight:700;font-size:13px;color:var(--lp-ink);letter-spacing:0.5px;}
.lp-ball{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;font-family:"Share Tech Mono",Consolas,monospace;font-weight:700;font-size:14px;background:#fff;border:2px solid #d8c48a;color:var(--lp-sub);}
.lp-ball--match{background:var(--lp-green);border-color:#1f7a44;color:#fff;box-shadow:0 0 0 3px rgba(47,158,91,0.2);}
.lp-ticket-note{text-align:center;font-size:13px;color:var(--lp-sub);margin-top:12px;}
.lp-map-table{border-collapse:collapse;width:auto;max-width:100%;margin:14px 0;font-size:14px;}
.lp-map-table th,.lp-map-table td{border:1px solid #e9d38f;padding:8px 14px;text-align:left;}
.lp-map-table th{background:var(--lp-red);color:var(--lp-cream);font-family:"Oswald",sans-serif;letter-spacing:0.5px;}
.lp-map-table td{background:var(--lp-cream);color:var(--lp-ink);}
.lp-map-table td code{color:var(--lp-red);}
.lp-card{background:var(--lp-cream);border:2px solid var(--lp-gold);border-radius:12px;padding:22px 26px;margin:22px 0;position:relative;box-shadow:0 4px 12px rgba(0,0,0,0.12);}
.lp-card-labelwrap{text-align:center;margin-bottom:10px;}
.lp-card-label{font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:2px;font-size:12px;color:var(--lp-gold);text-transform:uppercase;background:var(--lp-red);display:inline-block;padding:4px 12px;border-radius:4px;}
.lp-card-formula{text-align:center;font-family:"Share Tech Mono",Consolas,monospace;font-size:16px;color:var(--lp-ink);margin:10px 0;line-height:2;}
.lp-dist{margin:20px 0;}
.lp-dist-row{display:flex;align-items:center;gap:10px;margin:6px 0;}
.lp-dist-k{width:110px;flex:0 0 auto;font-family:"Share Tech Mono",Consolas,monospace;font-size:13px;color:var(--lp-ink);}
.lp-dist-bar-wrap{flex:1;background:#f1e5c2;border-radius:4px;overflow:hidden;height:22px;}
.lp-dist-bar{height:100%;background:linear-gradient(90deg,var(--lp-gold-dark),var(--lp-gold));}
.lp-dist-row--hit .lp-dist-bar{background:linear-gradient(90deg,var(--lp-red-dark),var(--lp-red));}
.lp-dist-row--hit .lp-dist-k{color:var(--lp-red);font-weight:700;}
.lp-dist-pct{width:74px;flex:0 0 auto;text-align:right;font-family:"Share Tech Mono",Consolas,monospace;font-size:13px;color:var(--lp-ink);}
.lp-final{border:3px double var(--lp-gold);border-radius:10px;padding:22px 28px;margin:26px 0;text-align:center;background:var(--lp-red);}
.lp-final-label{font-family:"Oswald",sans-serif;font-weight:700;letter-spacing:3px;font-size:13px;color:var(--lp-gold);text-transform:uppercase;margin-bottom:8px;display:block;}
.lp-final-text{font-size:18px;color:var(--lp-cream);font-weight:600;}
.lp-final-sub{font-size:13px;color:#f0d9c8;margin-top:6px;}
.lp-closing{text-align:center;padding:10px 0 4px;color:var(--lp-gold-dark);font-family:"Share Tech Mono",Consolas,monospace;font-size:12px;letter-spacing:2px;text-transform:uppercase;}
</style>

你自己選的號碼和開獎號碼各是一組固定的數字，比對兩邊「剛好對中幾個」，骨子裡還是同一套超幾何分布

<div class="lp-scope">
<div class="lp-hero">
<span class="lp-hero-eyebrow">Lottery Match · 威力彩對獎</span>
<div class="lp-hero-title">你選的 6 個號碼，剛好對中 4 個的機率有多低？</div>
<p class="lp-hero-desc">威力彩第一區從 38 個號碼裡開出 6 個號碼。你事先自己選了 6 個號碼，開獎後把你的號碼跟開出的 6 個號碼比對，看剛好對中幾個。這裡的「整批」是 38 個號碼、「感興趣的類型」是開獎開出的那 6 個號碼，跟前面瑕疵品、撲克牌的差別只在於這次「感興趣的類型」是由開獎機決定，不是我們自己指定。</p>
</div>

<div class="lp-stat-row">
<div class="lp-stat"><span class="lp-stat-num">38</span><span class="lp-stat-label">號碼總數（1~38）</span></div>
<div class="lp-stat"><span class="lp-stat-num">6</span><span class="lp-stat-label">開獎開出的號碼數</span></div>
<div class="lp-stat"><span class="lp-stat-num">6</span><span class="lp-stat-label">你自己選的號碼數</span></div>
<div class="lp-stat"><span class="lp-stat-num">4</span><span class="lp-stat-label">想對中的號碼數</span></div>
</div>

<div class="lp-panel">
<p>符合超幾何分布的原因跟前面一樣：<code>號碼池固定</code>（38 個號碼不會變）、<code>只分兩類</code>（開獎的 6 個號碼 vs 沒開出的 32 個號碼），而且<code>不會重複開獎</code>（同一期不會有兩顆一樣的號碼球）。差別只在於這次「哪 6 個是感興趣的類型」要等開獎才知道。</p>
</div>

<div class="lp-ticket">
<div class="lp-ticket-row">
<span class="lp-ticket-row-label">你選的號碼</span>
<span class="lp-ball lp-ball--match">05</span>
<span class="lp-ball lp-ball--match">12</span>
<span class="lp-ball lp-ball--match">19</span>
<span class="lp-ball lp-ball--match">24</span>
<span class="lp-ball">31</span>
<span class="lp-ball">36</span>
</div>
<div class="lp-ticket-row">
<span class="lp-ticket-row-label">開獎號碼</span>
<span class="lp-ball lp-ball--match">05</span>
<span class="lp-ball lp-ball--match">12</span>
<span class="lp-ball lp-ball--match">19</span>
<span class="lp-ball lp-ball--match">24</span>
<span class="lp-ball">08</span>
<span class="lp-ball">27</span>
</div>
<div class="lp-ticket-note">綠色球代表兩邊都有的號碼——這一組剛好對中 4 個</div>
</div>

<table class="lp-map-table">
<tr><th>超幾何分布的符號</th><th>代表意義</th><th>對應到威力彩</th></tr>
<tr><td><code>N</code></td><td>整批東西的總數</td><td>38 個號碼</td></tr>
<tr><td><code>K</code></td><td>整批裡「感興趣類型」的數量</td><td>開獎開出的 6 個號碼</td></tr>
<tr><td><code>n</code></td><td>實際抽出的數量</td><td>你自己選的 6 個號碼</td></tr>
<tr><td><code>k</code></td><td>想對中「感興趣類型」的數量</td><td>4 個對中的號碼</td></tr>
</table>

<div class="lp-card">
<div class="lp-card-labelwrap"><span class="lp-card-label">Formula · 算式</span></div>
<div class="lp-card-formula">P(剛好對中 4 個) = C(6,4) × C(32,2) ÷ C(38,6)</div>
<div class="lp-card-formula">= 15 × 496 ÷ 2,760,681</div>
<div class="lp-card-formula">= 7,440 ÷ 2,760,681 ≈ <code>0.27%</code></div>
</div>

這裡的 <code>C(6,4)</code> 是「開出的 6 個號碼裡，你剛好對中哪 4 個」的組合數；<code>C(32,2)</code> 是「你剩下 2 個號碼，剛好都落在沒開出的 32 個號碼裡」的組合數；分母 <code>C(38,6)</code> 則是「38 個號碼裡任選 6 個」的所有可能組合數，也就是開獎結果的全部可能性。

<div class="lp-dist">
<div class="lp-dist-row"><span class="lp-dist-k">對中 0 個</span><div class="lp-dist-bar-wrap"><div class="lp-dist-bar" style="width:32.8%;"></div></div><span class="lp-dist-pct">32.83%</span></div>
<div class="lp-dist-row"><span class="lp-dist-k">對中 1 個</span><div class="lp-dist-bar-wrap"><div class="lp-dist-bar" style="width:43.8%;"></div></div><span class="lp-dist-pct">43.77%</span></div>
<div class="lp-dist-row"><span class="lp-dist-k">對中 2 個</span><div class="lp-dist-bar-wrap"><div class="lp-dist-bar" style="width:19.5%;"></div></div><span class="lp-dist-pct">19.54%</span></div>
<div class="lp-dist-row"><span class="lp-dist-k">對中 3 個</span><div class="lp-dist-bar-wrap"><div class="lp-dist-bar" style="width:3.6%;"></div></div><span class="lp-dist-pct">3.59%</span></div>
<div class="lp-dist-row lp-dist-row--hit"><span class="lp-dist-k">對中 4 個 ★</span><div class="lp-dist-bar-wrap"><div class="lp-dist-bar" style="width:0.27%;"></div></div><span class="lp-dist-pct">0.27%</span></div>
<div class="lp-dist-row"><span class="lp-dist-k">對中 5 個</span><div class="lp-dist-bar-wrap"><div class="lp-dist-bar" style="width:0.05%;"></div></div><span class="lp-dist-pct">0.007%</span></div>
<div class="lp-dist-row"><span class="lp-dist-k">對中 6 個</span><div class="lp-dist-bar-wrap"><div class="lp-dist-bar" style="width:0.02%;"></div></div><span class="lp-dist-pct">0.00004%</span></div>
</div>

把完整分布攤開來看，就是彩券公司公告的中獎機率表：<code>對中 0～1 個</code>合計超過 76%，才是你每次對獎最常看到的結果；對中 4 個以上的機率已經低到千分之三以下，這也是為什麼威力彩把「對中 4 個」以上才設計成有獎金的門檻——機率池越往兩端（尤其是對中 6 個、也就是頭獎），下滑速度快到幾乎垂直。

<div class="lp-final">
<span class="lp-final-label">Draw Result · 結論</span>
<span class="lp-final-text">6 個號碼剛好對中 4 個的機率約 0.27%（約 371 分之 1）</span>
<div class="lp-final-sub">比對中 1 個（43.77%）低了超過 160 倍，越接近全對中，機率掉得越快</div>
</div>

<div class="lp-closing">— Good Luck, Draw Again Next Week —</div>
</div>

<!-- endtab -->


{% endtabs %}