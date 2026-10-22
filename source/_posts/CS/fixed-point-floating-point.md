---
title: Fixed Point & Floating Point
date: 2026-08-26 18:17:03
categories: CS
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/cs/fixed-floating-point.png
cover : https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/cs/fixed-floating-point.png
tags:
toc:
toc_number:
comments :
---

{% tabs fixed-point-floating-point %}

<!-- tab 先理解二進位小數 -->

<style>
.fp{
display:block;
font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,'PingFang TC','Microsoft JhengHei',sans-serif;
background:radial-gradient(700px 400px at 90% -5%,rgba(255,182,72,.18),transparent 60%),radial-gradient(900px 500px at -5% 10%,rgba(124,108,247,.10),transparent 55%),#fbf9f4;
color:#1f2430!important;
line-height:1.75;
border-radius:20px;
padding:1px 0 28px;
margin:0 0 20px;
overflow:hidden;
--ink:#1f2430;--sub:#5b6472;--card:#fff;--line:#ece7dc;--brand:#ff6b4a;--brand2:#ffb648;--teal:#12a594;--violet:#7c6cf7;--shadow:0 10px 30px -12px rgba(31,36,48,.15);
}
.fp *{box-sizing:border-box}
.fp .fp-hero{padding:48px 6vw 34px;text-align:center}
.fp .fp-eyebrow{display:inline-block;font-size:.78rem;letter-spacing:.16em;color:var(--brand)!important;font-weight:700;margin-bottom:12px;background:rgba(255,107,74,.1);padding:6px 14px;border-radius:999px}
.fp .fp-hero h1{font-size:1.7rem;margin:0 0 12px;color:var(--ink)!important;font-weight:800}
.fp .fp-hero p{color:var(--sub)!important;max-width:720px;margin:0 auto}
.fp .fp-badges{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:20px}
.fp .fp-badge{background:var(--card);border:1px solid var(--line);padding:6px 14px;border-radius:999px;font-size:.8rem;color:var(--sub)!important;box-shadow:var(--shadow)}
.fp .fp-container{padding:0 5vw}
.fp section{margin-bottom:42px}
.fp .fp-section-head{display:flex;align-items:center;gap:12px;margin-bottom:18px}
.fp .fp-chip{flex:none;width:38px;height:38px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-weight:800;background:linear-gradient(135deg,#1f2430,#485068);color:#fff!important;box-shadow:var(--shadow)}
.fp .fp-section-head.ok .fp-chip{background:linear-gradient(135deg,#12a594,#5ee6bf)}
.fp .fp-section-head.warn .fp-chip{background:linear-gradient(135deg,#ff6b4a,#ffb648)}
.fp .fp-section-head.purple .fp-chip{background:linear-gradient(135deg,#7c6cf7,#a78bfa)}
.fp .fp-section-head h2{margin:0;font-size:1.3rem;font-weight:800;color:var(--ink)!important}
.fp h3{font-size:1.08rem;margin:26px 0 10px;color:var(--ink)!important;border-left:4px solid var(--brand);padding-left:10px}
.fp p{color:var(--sub)!important}
.fp .fp-card{background:var(--card);border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);padding:18px 22px;margin:14px 0}
.fp code{font-family:Consolas,'SFMono-Regular','Liberation Mono',Menlo,monospace;background:#f1eee6!important;color:#c2410c!important;padding:2px 7px;border-radius:6px;font-size:.88em;border:1px solid #e9e3d5}
.fp table{width:auto;max-width:100%;border-collapse:separate;border-spacing:0;background:var(--card)!important;border:1px solid var(--line);border-radius:16px;overflow:hidden;margin:14px 0 22px;font-size:.88rem;box-shadow:var(--shadow)}
.fp thead th{background:#f3f0e8!important;color:var(--ink)!important;text-align:left;padding:13px 16px;font-weight:800;border-bottom:1px solid var(--line)}
.fp tbody td{padding:13px 16px;border-bottom:1px solid var(--line);color:#3b4150!important;vertical-align:top;background:var(--card)!important}
.fp tbody tr:last-child td{border-bottom:none}
.fp .fp-callout{border-radius:16px;padding:18px 22px;margin:18px 0;border:1px solid transparent;display:flex;gap:14px}
.fp .fp-callout .fp-icon{font-size:1.3rem;flex:none}
.fp .fp-callout.info{background:#eff6ff;border-color:#bfdbfe}
.fp .fp-callout.warn{background:#fffbeb;border-color:#fde68a}
.fp .fp-callout.ok{background:#ecfdf5;border-color:#a7f3d0}
.fp .fp-callout p{margin:0;font-size:.92rem;color:#3b4150!important}
.fp .fp-callout strong{color:var(--ink)!important}
.fp .fp-summary-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:18px 0}
.fp .fp-box{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;box-shadow:var(--shadow);border-top:4px solid var(--brand)}
.fp .fp-box:nth-child(2){border-top-color:var(--brand2)}
.fp .fp-box:nth-child(3){border-top-color:var(--teal)}
.fp .fp-box h4{margin:0 0 8px;color:var(--ink)!important;font-size:.95rem}
.fp .fp-box p{margin:0;font-size:.87rem}
.fp .fp-steps{display:flex;flex-direction:column;gap:14px;margin:16px 0 22px}
.fp .fp-step{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 20px;position:relative;padding-left:60px;box-shadow:var(--shadow)}
.fp .fp-stepnum{position:absolute;left:16px;top:16px;width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff!important;font-weight:800;display:flex;align-items:center;justify-content:center}
.fp .fp-step-title{font-weight:700;color:var(--ink)!important;font-size:1rem;margin-bottom:4px}
.fp .fp-step p{margin:6px 0;font-size:.9rem}
.fp .fp-checklist{list-style:none;padding:0;margin:16px 0}
.fp .fp-checklist li{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px dashed var(--line);color:var(--sub)!important}
.fp .fp-checklist li:last-child{border-bottom:none}
.fp .fp-checklist li::before{content:"✓";flex:none;width:22px;height:22px;border-radius:7px;background:#dcfce7;color:#15803d!important;font-size:.75rem;display:flex;align-items:center;justify-content:center;margin-top:2px;font-weight:900}
@media (max-width:780px){.fp .fp-summary-grid{grid-template-columns:1fr}}
</style>

<div class="fp">
<div class="fp-hero">
<span class="fp-eyebrow">CS · NUMBER REPRESENTATION</span>
<h1>小數點放在哪裡，決定數值能表示什麼</h1>
<p>電腦只有有限的 bits，卻要表示從很小到很大的數字。理解二進位小數、fixed point 與 floating point，就能看懂精度、範圍與誤差從哪裡產生。</p>
<div class="fp-badges"><span class="fp-badge">Binary Fraction</span><span class="fp-badge">Fixed Point</span><span class="fp-badge">Floating Point</span></div>
</div>
<div class="fp-container">
<section>
<div class="fp-section-head"><div class="fp-chip">01</div><h2>二進位小數如何表示</h2></div>
<p>十進位小數的小數點後，每一格都有固定權重。第一格是 <code>1/10</code>，第二格是 <code>1/100</code>，第三格是 <code>1/1000</code>。</p>
<div class="fp-card">
<p><code>0.123 = 1 × 1/10 + 2 × 1/100 + 3 × 1/1000</code></p>
</div>
<p>二進位小數的規則完全相同，只是底數從 <code>10</code> 改成 <code>2</code>。因此小數點後第一格代表 <code>1/2</code>，第二格代表 <code>1/4</code>，第三格代表 <code>1/8</code>。</p>
<div class="fp-card">
<p><code>0.101₂ = 1 × 1/2 + 0 × 1/4 + 1 × 1/8 = 0.625₁₀</code></p>
</div>
<div class="fp-callout info"><span class="fp-icon">💡</span><p><strong>核心觀念：</strong>二進位小數就是用一連串的 <code>1/2ⁿ</code> 湊出目標數值。</p></div>
</section>
</div>
</div>

<!-- endtab -->

<!-- tab 為什麼 0.1 無法精確表示 -->

<div class="fp">
<div class="fp-container">
<section>
<div class="fp-section-head warn"><div class="fp-chip">02</div><h2>十進位的 0.1，為什麼會變成循環小數</h2></div>
<p>把十進位的 <code>0.1</code> 轉成二進位，本質上是在反覆檢查每個 <code>1/2ⁿ</code> 是否能放進剩餘值。</p>
<div class="fp-steps">
<div class="fp-step"><div class="fp-stepnum">1</div><div class="fp-step-title">檢查 <code>1/2 = 0.5</code></div><p><code>0.1 &lt; 0.5</code>，第一格放不下，所以是 <code>0</code>。</p></div>
<div class="fp-step"><div class="fp-stepnum">2</div><div class="fp-step-title">檢查 <code>1/4 = 0.25</code> 與 <code>1/8 = 0.125</code></div><p>兩者都比剩餘值大，所以第二格與第三格都是 <code>0</code>。</p></div>
<div class="fp-step"><div class="fp-stepnum">3</div><div class="fp-step-title">檢查 <code>1/16 = 0.0625</code></div><p><code>0.1 ≥ 0.0625</code>，第四格可以放入 <code>1</code>，剩下 <code>0.0375</code>。</p></div>
<div class="fp-step"><div class="fp-stepnum">4</div><div class="fp-step-title">繼續用後面的權重湊出剩餘值</div><p>第五格放入 <code>1/32</code>，第六格與第七格放入 <code>0</code>，第八格再放入 <code>1/256</code>。結果逐步形成 <code>0.0001100110011...</code>。</p></div>
</div>
<div class="fp-callout warn"><span class="fp-icon">⚠️</span><p><strong>為什麼會循環：</strong><code>0.1 = 1/10 = 1/(2 × 5)</code>。有限長度的二進位小數，其最簡分數的分母只能包含質因數 <code>2</code>。因數 <code>5</code> 無法被有限個二次方消除，因此 <code>0.1</code> 只能用無限循環的小數逼近。</p></div>
<table>
<thead><tr><th>十進位數值</th><th>二進位表示</th><th>原因</th></tr></thead>
<tbody><tr><td><code>0.75</code></td><td><code>0.11₂</code></td><td><code>0.75 = 1/2 + 1/4</code>，可以有限表示。</td></tr><tr><td><code>0.625</code></td><td><code>0.101₂</code></td><td><code>0.625 = 1/2 + 1/8</code>，可以有限表示。</td></tr><tr><td><code>0.1</code></td><td><code>0.000110011...₂</code></td><td>最簡分數分母含有因數 <code>5</code>，只能循環。</td></tr></tbody>
</table>
</section>
</div>
</div>

<!-- endtab -->

<!-- tab Fixed Point -->

<div class="fp">
<div class="fp-container">
<section>
<div class="fp-section-head ok"><div class="fp-chip">03</div><h2>Fixed point：小數點位置固定</h2></div>
<p><code>Fixed point</code> 的做法是先約定小數點永遠放在固定位置。例如使用 <code>xxxx.xxxx</code>，前 4 個 bits 表示整數，後 4 個 bits 表示小數。</p>
<div class="fp-card">
<p><code>0011.1000₂ = 0 × 8 + 0 × 4 + 1 × 2 + 1 × 1 + 1 × 1/2 = 3.5</code></p>
</div>
<div class="fp-summary-grid">
<div class="fp-box"><h4>固定精度</h4><p>小數點後有幾格，最小單位就固定。例如 4 個小數 bits 的最小單位是 <code>1/16</code>。</p></div>
<div class="fp-box"><h4>範圍受限</h4><p>若只有 4 個 bits 表示整數，最大值是 <code>15</code>。增加小數精度，就會減少整數範圍。</p></div>
<div class="fp-box"><h4>適合固定尺度</h4><p>金額、尺寸、感測值等需要固定小數位的資料，通常容易使用 fixed point 管理。</p></div>
</div>
<div class="fp-callout info"><span class="fp-icon">📌</span><p><strong>取捨關係：</strong>bits 總數固定時，分給整數的 bits 越多，能表示的範圍越大。分給小數的 bits 越多，精度越高。</p></div>
</section>
</div>
</div>

<!-- endtab -->

<!-- tab Floating Point -->

<div class="fp">
<div class="fp-container">
<section>
<div class="fp-section-head purple"><div class="fp-chip">04</div><h2>Floating point：讓小數點可以移動</h2></div>
<p><code>Floating point</code> 不固定小數點位置，而是把數值拆成有效數字與指數。概念上就像科學記號。</p>
<div class="fp-card">
<p><code>123000000 = 1.23 × 10⁸</code></p>
<p><code>0.000000123 = 1.23 × 10⁻⁷</code></p>
</div>
<p>兩個數值的有效數字都是 <code>1.23</code>，差異主要由指數決定。二進位 floating point 則使用類似 <code>1.xxxx₂ × 2ⁿ</code> 的形式。</p>
<table>
<thead><tr><th>欄位</th><th>用途</th></tr></thead>
<tbody><tr><td><code>sign</code></td><td>表示正數或負數。</td></tr><tr><td><code>exponent</code></td><td>決定二進位小數點要移動的數量級。</td></tr><tr><td><code>fraction</code></td><td>保存有效數字的精細程度。</td></tr></tbody>
</table>
<div class="fp-summary-grid">
<div class="fp-box"><h4>Fixed point</h4><p>小數點固定，精度與最小單位穩定，數值範圍比較容易不足。</p></div>
<div class="fp-box"><h4>Floating point</h4><p>小數點可以浮動，能涵蓋很大的數值範圍，但不同數量級的精度不相同。</p></div>
<div class="fp-box"><h4>實際差異</h4><p>Floating point 的相鄰可表示數字之間，距離會隨數值大小改變。</p></div>
</div>
<div class="fp-callout ok"><span class="fp-icon">✓</span><p><strong>總結：</strong>Floating point 的價值不只是表示小數，而是用有限 bits 同時涵蓋極小到極大的數值範圍。若需求是固定最小單位，fixed point 通常更容易控制。</p></div>
<ul class="fp-checklist"><li>二進位小數的每一格，代表一個 <code>1/2ⁿ</code>。</li><li>最簡分數的分母只含因數 <code>2</code>，才能用有限長度的二進位小數表示。</li><li><code>Fixed point</code> 以固定小數點換取穩定精度。</li><li><code>Floating point</code> 以有效數字加指數換取更大的數值範圍。</li></ul>
</section>
</div>
</div>

<!-- endtab -->

{% endtabs %}
