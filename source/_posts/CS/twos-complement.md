---
title: 二補數（Two's Complement）
date: 2026-08-19 08:30:03
categories: CS
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/CS/twos-complement.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/CS/twos-complement.png
tags:
toc:
toc_number:
comments :
---

{% tabs Complement%}

<!-- tab 為什麼需要二補數-->

<style>
.hkr{
  display:block;
  font-family:Consolas,'SFMono-Regular','Courier New',Menlo,monospace;
  background:#05080a;
  color:#d7ffe4!important;
  line-height:1.75;
  border-radius:14px;
  padding:1px 0 28px;
  margin:0 0 20px;
  overflow:hidden;
  --ink:#d7ffe4; --sub:#7fdba0; --card:#0d1710; --line:rgba(0,255,106,.28);
  --green:#00ff6a; --green-bright:#7dffb0; --green-dim:#00b34c; --danger:#ff4d5e; --warn:#ffcc33; --info:#33e0ff;
  --glow:0 0 18px rgba(0,255,106,.22);
}
.hkr *{box-sizing:border-box;}
.hkr a{color:var(--green-bright)!important;text-decoration:none;}
.hkr a:hover{text-decoration:underline;}
.hkr .hkr-hero{padding:50px 6vw 34px;text-align:center;position:relative;overflow:hidden;background:linear-gradient(180deg,#050807,#0a140d 70%,#05080a);border-bottom:1px solid var(--line);}
.hkr .hkr-hero::before{content:"01001101 01100001 01110100 01110010 01101001 01111000 00100000 01000111 01110010 01100101 01100101 01101110\A 11010010 00101101 01011010 10100101 01101001 00110101 01100101 01100100 00100000 01000011 01101111 01100100 01100101\A 01010111 01100001 01101011 01100101 00100000 01110101 01110000 00101100 00100000 01001110 01100101 01101111 00101110\A 00110010 00110000 00110011 00110101 00100000 01001111 01110110 01100101 01110010 01100110 01101100 01101111 01110111\A";white-space:pre;position:absolute;inset:0;text-align:center;font-size:.72rem;letter-spacing:.28em;line-height:2.2;color:var(--green)!important;opacity:.16;pointer-events:none;padding-top:10px;}
.hkr .hkr-eyebrow{display:inline-block;position:relative;font-size:.76rem;letter-spacing:.14em;color:var(--green-bright)!important;text-transform:uppercase;font-weight:700;margin-bottom:14px;background:rgba(0,255,106,.08);border:1px solid var(--line);padding:5px 14px;border-radius:4px;}
.hkr .hkr-hero h1{position:relative;font-size:1.7rem;margin:0 0 12px;color:var(--green-bright)!important;font-weight:800;text-shadow:0 0 18px rgba(0,255,106,.55),0 0 4px rgba(0,255,106,.8);}
.hkr .hkr-hero p{position:relative;color:var(--sub)!important;max-width:700px;margin:0 auto;font-size:.98rem;}
.hkr .hkr-badges{position:relative;display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:20px;}
.hkr .hkr-badge{background:rgba(0,255,106,.06);border:1px solid var(--line);padding:6px 14px;border-radius:4px;font-size:.78rem;color:var(--sub)!important;}
.hkr .hkr-container{padding:0 5vw;}
.hkr section{margin-bottom:44px;}
.hkr .hkr-section-head{display:flex;align-items:center;gap:12px;margin-bottom:18px;}
.hkr .hkr-section-head .hkr-chip{flex:none;min-width:38px;height:38px;padding:0 10px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-weight:800;background:rgba(0,255,106,.1);border:1px solid var(--green-dim);color:var(--green-bright)!important;font-size:.95rem;box-shadow:var(--glow);}
.hkr .hkr-section-head.info .hkr-chip{border-color:var(--info);color:var(--info)!important;background:rgba(51,224,255,.1);}
.hkr .hkr-section-head.danger .hkr-chip{border-color:var(--danger);color:var(--danger)!important;background:rgba(255,77,94,.1);}
.hkr .hkr-section-head.warn .hkr-chip{border-color:var(--warn);color:var(--warn)!important;background:rgba(255,204,51,.1);}
.hkr .hkr-section-head h2{margin:0;font-size:1.28rem;font-weight:800;color:var(--ink)!important;}
.hkr h3{font-size:1.04rem;margin:26px 0 10px;color:var(--green-bright)!important;border-left:3px solid var(--green-dim);padding-left:10px;}
.hkr p{color:var(--sub)!important;}
.hkr .hkr-card{background:var(--card);border:1px solid var(--line);border-radius:10px;box-shadow:var(--glow);padding:18px 22px;margin:14px 0;}
.hkr table{width:auto;max-width:100%;border-collapse:separate;border-spacing:0;background:var(--card)!important;border:1px solid var(--line);border-radius:10px;overflow:hidden;margin:14px 0 22px;font-size:.86rem;box-shadow:var(--glow);}
.hkr thead th{background:rgba(0,255,106,.08)!important;color:var(--green-bright)!important;text-align:left;padding:12px 16px;font-weight:800;border-bottom:1px solid var(--line);}
.hkr tbody td{padding:12px 16px;border-bottom:1px solid var(--line);color:var(--sub)!important;vertical-align:top;background:var(--card)!important;}
.hkr tbody tr:last-child td{border-bottom:none;}
.hkr tbody tr:hover td{background:rgba(0,255,106,.04)!important;}
.hkr tbody td strong{color:var(--ink)!important;}
.hkr tbody td code{color:var(--green-bright)!important;}
.hkr code{font-family:Consolas,'SFMono-Regular','Courier New',Menlo,monospace;background:rgba(0,255,106,.1)!important;color:var(--green-bright)!important;padding:2px 7px;border-radius:5px;font-size:.88em;border:1px solid var(--line);}
.hkr .hkr-term{background:#000000!important;border:1px solid var(--line);border-radius:10px;overflow:hidden;margin:16px 0;box-shadow:var(--glow);}
.hkr .hkr-term-bar{display:flex;align-items:center;gap:8px;padding:9px 14px;background:#0a0f0b;border-bottom:1px solid var(--line);}
.hkr .hkr-term-dot{width:10px;height:10px;border-radius:50%;flex:none;background:#3a3f3a;}
.hkr .hkr-term-dot.r{background:#ff5f56;} .hkr .hkr-term-dot.y{background:#ffbd2e;} .hkr .hkr-term-dot.g{background:#27c93f;}
.hkr .hkr-term-title{margin-left:6px;font-size:.72rem;color:var(--sub)!important;letter-spacing:.04em;}
.hkr pre.hkr-pre{background:#000000!important;border:none;border-radius:0;padding:18px 20px;overflow-x:auto;margin:0;color:#c8ffe0!important;font-size:.86rem!important;line-height:1.75!important;font-family:Consolas,'SFMono-Regular','Courier New',Menlo,monospace!important;white-space:pre!important;}
.hkr .kw{color:var(--green-bright)!important;font-weight:700;} .hkr .str{color:#7dffb0!important;} .hkr .cm{color:#4f8a6a!important;font-style:italic;} .hkr .fn{color:#33e0ff!important;} .hkr .type{color:#ffcc33!important;} .hkr .num{color:#7dffb0!important;} .hkr .op{color:#ff8ad1!important;}
.hkr .hkr-callout{border-radius:10px;padding:16px 20px;margin:18px 0;border:1px solid transparent;display:flex;gap:14px;}
.hkr .hkr-callout .hkr-icon{font-size:1.2rem;flex:none;}
.hkr .hkr-callout.info{background:rgba(51,224,255,.08);border-color:rgba(51,224,255,.35);}
.hkr .hkr-callout.warn{background:rgba(255,204,51,.08);border-color:rgba(255,204,51,.35);}
.hkr .hkr-callout.danger{background:rgba(255,77,94,.08);border-color:rgba(255,77,94,.35);}
.hkr .hkr-callout.ok{background:rgba(0,255,106,.08);border-color:rgba(0,255,106,.35);}
.hkr .hkr-callout p{margin:0;font-size:.92rem;color:var(--sub)!important;}
.hkr .hkr-callout strong{color:var(--ink)!important;}
.hkr .hkr-tag{display:inline-block;font-size:.7rem;font-weight:800;padding:3px 11px;border-radius:4px;letter-spacing:.02em;border:1px solid transparent;}
.hkr .hkr-tag.danger{background:rgba(255,77,94,.14)!important;color:var(--danger)!important;border-color:rgba(255,77,94,.4);}
.hkr .hkr-tag.ok{background:rgba(0,255,106,.14)!important;color:var(--green-bright)!important;border-color:rgba(0,255,106,.4);}
.hkr .hkr-tag.warn{background:rgba(255,204,51,.14)!important;color:var(--warn)!important;border-color:rgba(255,204,51,.4);}
.hkr .hkr-tag.info{background:rgba(51,224,255,.14)!important;color:var(--info)!important;border-color:rgba(51,224,255,.4);}
.hkr .hkr-summary-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:18px 0;}
.hkr .hkr-summary-grid .hkr-box{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px 20px;box-shadow:var(--glow);border-top:3px solid var(--green-dim);position:relative;overflow:hidden;}
.hkr .hkr-summary-grid .hkr-box.info{border-top-color:var(--info);}
.hkr .hkr-summary-grid .hkr-box.danger{border-top-color:var(--danger);}
.hkr .hkr-summary-grid .hkr-box.warn{border-top-color:var(--warn);}
.hkr .hkr-summary-grid .hkr-box h4{margin:0 0 8px;color:var(--green-bright)!important;font-size:.84rem;text-transform:uppercase;letter-spacing:.04em;}
.hkr .hkr-summary-grid .hkr-box p{margin:0;font-size:.86rem;color:var(--sub)!important;}
@media (max-width:780px){.hkr .hkr-summary-grid{grid-template-columns:1fr;}}
.hkr .hkr-flow{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:20px 0;}
.hkr .hkr-flow .hkr-step{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:9px 16px;font-size:.84rem;font-weight:700;color:var(--ink)!important;box-shadow:var(--glow);}
.hkr .hkr-flow .hkr-step.cond{background:rgba(255,204,51,.08);border-color:rgba(255,204,51,.4);color:var(--warn)!important;}
.hkr .hkr-flow .hkr-step.danger{background:rgba(255,77,94,.08);border-color:rgba(255,77,94,.4);color:var(--danger)!important;}
.hkr .hkr-flow .hkr-arrow{color:var(--green)!important;font-size:1.2rem;font-weight:900;}
.hkr .hkr-steps{display:flex;flex-direction:column;gap:14px;margin:16px 0 22px;}
.hkr .hkr-stepcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px 20px;position:relative;padding-left:60px;box-shadow:var(--glow);}
.hkr .hkr-stepcard .hkr-stepnum{position:absolute;left:16px;top:16px;width:30px;height:30px;border-radius:50%;background:rgba(0,255,106,.12);border:1px solid var(--green-dim);color:var(--green-bright)!important;font-weight:800;font-size:.88rem;display:flex;align-items:center;justify-content:center;}
.hkr .hkr-stepcard.cond .hkr-stepnum{background:rgba(255,204,51,.12);border-color:var(--warn);color:var(--warn)!important;}
.hkr .hkr-stepcard .hkr-step-title{font-weight:700;color:var(--ink)!important;font-size:.98rem;margin-bottom:4px;display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.hkr .hkr-stepcard p{margin:6px 0;font-size:.88rem;color:var(--sub)!important;}
.hkr .hkr-checklist{list-style:none;padding:0;margin:16px 0;}
.hkr .hkr-checklist li{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px dashed var(--line);color:var(--sub)!important;}
.hkr .hkr-checklist li:last-child{border-bottom:none;}
.hkr .hkr-checklist li::before{content:"✓";flex:none;width:22px;height:22px;border-radius:5px;background:rgba(0,255,106,.12);color:var(--green-bright)!important;font-size:.75rem;display:flex;align-items:center;justify-content:center;margin-top:2px;font-weight:900;border:1px solid var(--green-dim);}
.hkr .hkr-evidence{border:1px solid var(--line);background:var(--card);border-radius:10px;box-shadow:var(--glow);padding:18px 20px;margin:16px 0 22px;}
.hkr .hkr-evidence .hkr-evidence-head{display:flex;align-items:center;gap:8px;margin-bottom:10px;}
.hkr .hkr-evidence .hkr-evidence-head .hkr-tag{background:rgba(255,77,94,.16)!important;color:var(--danger)!important;border-color:rgba(255,77,94,.45);}
.hkr .hkr-rain-divider{display:flex;align-items:center;gap:10px;justify-content:center;margin:36px 0;color:var(--green-dim)!important;font-size:.85rem;letter-spacing:.3em;}
.hkr .hkr-rain-divider::before,.hkr .hkr-rain-divider::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--line) 40%,var(--line) 60%,transparent);}
.hkr footer{text-align:center;padding:30px 5vw 6px;color:var(--sub)!important;font-size:.8rem;border-top:1px solid var(--line);margin-top:8px;}
</style>

<div class="hkr">
<div class="hkr-hero">
<span class="hkr-eyebrow">root@alu:~$ two's complement</span>
<h1>二補數：把減法偽裝成加法的把戲</h1>
<p>CPU 裡其實只有一顆加法器，卻能算出減法、算出負數。祕密就藏在一段固定的位元轉換規則裡。</p>
<div class="hkr-badges">
<span class="hkr-badge">Two's Complement</span>
<span class="hkr-badge">Signed / Unsigned</span>
<span class="hkr-badge">Integer Overflow</span>
</div>
</div>
<div class="hkr-container">

<section>
<div class="hkr-section-head">
<div class="hkr-chip">&gt;_</div>
<h2>為什麼需要二補數</h2>
</div>

<p>電路設計上，CPU 真正負責四則運算的硬體只有一顆加法器，並沒有天生內建的減法電路。如果只支援正數的加法，那麼要處理「減法」與「負數」，就變成一項額外的需求。設計上大致只有兩條路：另外造一顆專門的減法電路，或是想辦法讓負數本身也能透過同一顆加法器直接被算出正確答案。</p>

<p>後者聽起來比較划算，但要成立必須先解決一個問題：負數在位元層面該怎麼表示，才能讓現有的二進位加法器不需要任何修改，直接把結果加出來就是對的。</p>

<h3>一個直覺但行不通的做法</h3>

<p>如果直接用「符號位加大小」的方式表示負數，也就是最高位當作正負號，其餘位元照原本的大小表示，例如 <code>-5</code> 表示成 <code>1000 0101</code>（最高位 <code>1</code> 代表負，其餘 <code>000 0101</code> 是 <code>5</code>），拿去跟 <code>5 = 0000 0101</code> 做一般的二進位加法：</p>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">naive.sim</span></div>
<pre class="hkr-pre">  <span class="num">0000 0101</span>   <span class="cm">// 5</span>
+ <span class="num">1000 0101</span>   <span class="cm">// 符號位+大小表示的 -5</span>
-------------
  <span class="num">1000 1010</span>   <span class="cm">// 按同一套規則解讀 = -10</span></pre>
</div>

<p>加法器完全不知道最高位是特殊的符號位，只是照一般規則把每一位加起來，得到的 <code>1000 1010</code> 若照同一套解讀方式，會被念成 <code>-10</code>。但數學上 <code>5 + (-5)</code> 應該是 <code>0</code>，結果完全錯誤。這代表「符號位加大小」這種表示法沒辦法直接套用一般的二進位加法器，必須額外判斷符號位、另外處理進位，等於還是要多一套邏輯。</p>

<div class="hkr-flow">
<div class="hkr-step">需要負數</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step cond">符號位+大小表示法</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step danger">一般加法器算出錯誤答案</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step">還需要另一套規則</div>
</div>

<div class="hkr-callout warn">
<span class="hkr-icon">!</span>
<p><strong>真正的需求：</strong>必須找到一套負數的位元表示規則，讓現有的二進位加法器完全不用修改，直接把兩個數字的 bits 加起來，就能得到正確答案。這正是二補數要解決的問題。</p>
</div>

<p>在拆解二補數實際怎麼算之前，先建立一個更基礎的概念：同一串 bits 該怎麼被解讀成數字，也就是接下來要談的 <code>signed</code> 與 <code>unsigned</code>。</p>

</section>

</div>
</div>

<!-- endtab -->

<!-- tab Signed Unsigned-->

<div class="hkr">
<div class="hkr-container">

<section>
<div class="hkr-section-head info">
<div class="hkr-chip">&gt;_</div>
<h2>Signed 與 Unsigned</h2>
</div>

<p><code>signed</code> 跟 <code>unsigned</code> 其實是在告訴電腦：「同一串 bits，要用哪一套規則解讀成數字」。<code>unsigned</code> 把全部空間都拿來表示 <code>0</code> 和正數，<code>signed</code> 則通常採用二補數規則，讓同樣的 bits 可以同時涵蓋負數、<code>0</code>、正數。</p>

<table>
<thead><tr><th>8 bit 樣式</th><th>signed 二補數解讀</th><th>備註</th></tr></thead>
<tbody>
<tr><td><code>1111 1111</code></td><td><code>-1</code></td><td>定義起點</td></tr>
<tr><td><code>1111 1110</code></td><td><code>-2</code></td><td>比 -1 再倒退一格</td></tr>
<tr><td><code>1000 0001</code></td><td><code>-127</code></td><td>逼近最負值</td></tr>
<tr><td><code>1000 0000</code></td><td><code>-128</code></td><td>signed 8 bit 能表示的最負值</td></tr>
<tr><td><code>0000 0000</code></td><td><code>0</code></td><td>零點</td></tr>
<tr><td><code>0111 1110</code></td><td><code>126</code></td><td>逼近最大正數</td></tr>
<tr><td><code>0111 1111</code></td><td><code>127</code></td><td>signed 8 bit 能表示的最大正數</td></tr>
</tbody>
</table>

<div class="hkr-evidence">
<div class="hkr-evidence-head">
<span class="hkr-tag info">同一串 bits</span>
<strong>1111 1111 到底是多少</strong>
</div>
<p>若用 <code>unsigned</code> 解讀，這串 bits 是 <code>255</code>；若用 <code>signed</code> 二補數解讀，同一串 bits 卻是 <code>-1</code>。bits 本身完全沒有改變，改變的只是解讀規則。</p>
</div>

<div class="hkr-callout info">
<span class="hkr-icon">i</span>
<p><strong>本質：</strong><code>signed</code> / <code>unsigned</code> 其實就是一份「bit pattern 對應到數值」的解讀規則，ALU 算出來的 bits 完全相同，但程式認為它代表多少，會因為 <code>signed</code> 或 <code>unsigned</code> 而不同。</p>
</div>

<p>假設記憶體裡真的存著 <code>1111 1111</code>，硬體本身看到的就只有這 8 個 bits，它並沒有額外標記「這是 -1」或「這是 255」，要看使用哪種型別去解讀。</p>

<p>那麼問題來了：<code>signed</code> 二補數這份解讀規則，實際上是怎麼從一個正數推出對應的負數表示的？接下來就是二補數真正的計算規則。</p>

</section>

</div>
</div>

<!-- endtab -->

<!-- tab 為什麼是反轉 + 1-->

<div class="hkr">
<div class="hkr-container">

<section>
<div class="hkr-section-head">
<div class="hkr-chip">&gt;_</div>
<h2>二補數怎麼算：反轉再加 1</h2>
</div>

<p>二補數的規則很固定：把一個正數的每一位反轉，再加 <code>1</code>，就能得到它對應的負數表示。以 <code>5</code> 為例：</p>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">negate.sim</span></div>
<pre class="hkr-pre"><span class="type">5</span>       = <span class="num">0000 0101</span>
反轉     = <span class="num">1111 1010</span>
+1      = <span class="num">1111 1011</span></pre>
</div>

<p>所以 <code>-5 = 1111 1011</code>。接下來驗證這個結果是否成立，把 <code>5</code> 跟這個 <code>-5</code> 相加：</p>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">alu.sim</span></div>
<pre class="hkr-pre">  <span class="num">0000 0101</span>   <span class="cm">// 5</span>
+ <span class="num">1111 1011</span>   <span class="cm">// -5</span>
-------------
<span class="op">1</span> <span class="num">0000 0000</span></pre>
</div>

<p>因為暫存器只有 8 bit，最左邊多出來的那個 <code>1</code> 會被直接丟掉，只留下 <code>0000 0000</code>，也就是 <code>0</code>。<code>5 + (-5) = 0</code> 完全正確，而且從頭到尾只用了同一顆加法器，沒有另外造任何減法電路。</p>

<div class="hkr-flow">
<div class="hkr-step">5 + (-5)</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step">最高位多出一個 1</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step cond">超出 8 bit 直接捨去</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step">結果 = 0</div>
</div>

<h3>減法也能套用同一套邏輯</h3>

<p>例如 <code>5 - 3</code> 可以先轉換成 <code>5 + (-3)</code>，一樣先用「反轉再加 1」找出 <code>-3</code>：</p>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">negate.sim</span></div>
<pre class="hkr-pre"><span class="type">3</span>       = <span class="num">0000 0011</span>
反轉     = <span class="num">1111 1100</span>
+1      = <span class="num">1111 1101</span></pre>
</div>

<p>所以 <code>-3 = 1111 1101</code>，接著把 <code>5</code> 跟 <code>-3</code> 相加：</p>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">alu.sim</span></div>
<pre class="hkr-pre">  <span class="num">0000 0101</span>   <span class="cm">// 5</span>
+ <span class="num">1111 1101</span>   <span class="cm">// -3</span>
-------------
<span class="op">1</span> <span class="num">0000 0010</span></pre>
</div>

<p>留下 8 bit 之後是 <code>0000 0010 = 2</code>，所以 <code>5 - 3 = 2</code>，答案完全正確。</p>

<div class="hkr-callout ok">
<span class="hkr-icon">✓</span>
<p><strong>核心概念：</strong>二補數的本質，就是想辦法把「減法問題」轉換成 CPU 原本就很擅長的「加法問題」，讓硬體不用多長一顆專門處理減法的電路。</p>
</div>

<h3>為什麼偏偏是「反轉再加 1」</h3>

<p>反轉每一個位元，其實只能幫忙算到 <code>255 - x</code>，但要湊出負數真正需要的是 <code>256 - x</code>，所以最後差的那個 <code>1</code>，就是靠額外加 1 補上去的。</p>

<div class="hkr-steps">
<div class="hkr-stepcard">
<div class="hkr-stepnum">1</div>
<div class="hkr-step-title">目標：找出讓 5 歸零繞回的那個數</div>
<p>已知 <code>5 = 0000 0101</code>，希望找到一個值 <code>?</code>，使得 <code>5 + ? = 256</code>，所以 <code>? = 256 - 5 = 251</code>。</p>
</div>
<div class="hkr-stepcard cond">
<div class="hkr-stepnum">2</div>
<div class="hkr-step-title">但「反轉 5」實際上只算出 255 - 5</div>
<p>因為 <code>1111 1111 = 255</code>，把每一位反轉等同於用 <code>255</code> 去減，反轉後的值是 <code>250</code>，離目標的 <code>251</code> 還差 <code>1</code>。</p>
</div>
<div class="hkr-stepcard">
<div class="hkr-stepnum">3</div>
<div class="hkr-step-title">補上那差的 1</div>
<p><code>反轉 + 1 = 250 + 1 = 251</code>，正好等於 <code>256 - 5</code>，也就是二補數表示法裡的 <code>-5</code>。</p>
</div>
</div>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">proof.sim</span></div>
<pre class="hkr-pre">  <span class="num">1111 1111</span>  <span class="cm">// 255</span>
- <span class="num">0000 0101</span>  <span class="cm">// 5</span>
-------------
  <span class="num">1111 1010</span>  <span class="cm">// 反轉結果 = 255 - 5 = 250</span></pre>
</div>

<p>整理成一個關係式：<code>反轉 + 1 = (255 - x) + 1 = 256 - x</code>。</p>

<h3>為什麼偏偏要湊到 256</h3>

<p>因為 8 bit 只能保存 <code>0 ~ 255</code> 這個範圍，一旦數值來到 <code>256</code>，二進位會變成 <code>1 0000 0000</code>，超出的最高位放不下，只留下 8 bit 的 <code>0000 0000</code>，等於 <code>256</code> 會直接繞回 <code>0</code>。這正是能夠成立 <code>5 + (-5) = 5 + 251 = 256</code>，而 8 bit 只留下 <code>0000 0000</code>，也就是 <code>0</code> 的原因。</p>

<div class="hkr-callout info">
<span class="hkr-icon">i</span>
<p><strong>換一個位元寬度驗證：</strong>如果是 4 bit（<code>2^4 = 16</code>），要表示 <code>-5</code> 就要湊到 <code>16 - 5 = 11</code>。</p>
</div>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">4bit.sim</span></div>
<pre class="hkr-pre"><span class="type">5</span>  = <span class="num">0101</span>
反轉 = <span class="num">1010</span>      <span class="cm">// 10</span>
+1  = <span class="num">1011</span>      <span class="cm">// 11</span></pre>
</div>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">4bit.sim</span></div>
<pre class="hkr-pre">  <span class="num">0101</span>   <span class="cm">// 5</span>
+ <span class="num">1011</span>   <span class="cm">// -5</span>
------
<span class="op">1</span> <span class="num">0000</span>   <span class="cm">// 只保留 4 bit 之後 = 0000</span></pre>
</div>

<p>所以「二補數反轉再加 1」可以記成一條固定的因果鏈：</p>

<div class="hkr-flow">
<div class="hkr-step">N bit 在 2^N 會繞回 0</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step">-x 需要湊到 2^N - x</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step cond">反轉只能得到 2^N - 1 - x</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step">還差 1</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step">所以要 +1</div>
</div>

</section>

</div>
</div>

<!-- endtab -->

<!-- tab overflow-->

<div class="hkr">
<div class="hkr-container">

<section>
<div class="hkr-section-head danger">
<div class="hkr-chip">&gt;_</div>
<h2>Integer Overflow</h2>
</div>

<p><code>signed</code> 與 <code>unsigned</code> 的可表示範圍不同，所以同一個位元運算，可能對 <code>signed</code> 而言已經溢位，對 <code>unsigned</code> 卻完全正常。以 8-bit <code>signed</code> 為例，它裝不下 <code>128</code>，留下來的 <code>1000 0000</code> 按 <code>signed</code> 二補數規則會被解讀成 <code>-128</code>。</p>

<div class="hkr-callout danger">
<span class="hkr-icon">!</span>
<p><strong>Overflow 發生後：</strong>真正的數學答案沒有被完整保留下來。ALU 會留下低位的 N bits，並額外產生一個 overflow 訊號，後續要怎麼處理，交由 CPU 指令、程式語言或程式本身決定。</p>
</div>

<div class="hkr-steps">
<div class="hkr-stepcard">
<div class="hkr-stepnum">1</div>
<div class="hkr-step-title">ALU 照樣完成位元加法</div>
<p>ALU 不會因為數值看起來偏大就拒絕運算，它仍然完成 <code>0111 1111 + 0000 0001</code> 這組位元加法，得到 <code>1000 0000</code>。</p>
</div>
<div class="hkr-stepcard danger">
<div class="hkr-stepnum">2</div>
<div class="hkr-step-title">結果的 bits 被錯誤解讀</div>
<p>把 <code>1000 0000</code> 以 8-bit signed 二補數解讀，會得到 <code>-128</code>。但數學上真正的答案是 <code>127 + 1 = 128</code>，這個 <code>-128</code> 已經無法代表真正的答案。</p>
</div>
<div class="hkr-stepcard danger">
<div class="hkr-stepnum">3</div>
<div class="hkr-step-title">ALU 同時偵測到 overflow</div>
<p>ALU 除了輸出 <code>Result</code>，通常還會同時產生 <code>Overflow = 1</code> 這個狀態訊號，意思是「若把這次運算當成 signed integer，Result 已經無法正確表示真正答案」。</p>
</div>
</div>

<div class="hkr-term">
<div class="hkr-term-bar"><span class="hkr-term-dot r"></span><span class="hkr-term-dot y"></span><span class="hkr-term-dot g"></span><span class="hkr-term-title">alu.diagram</span></div>
<pre class="hkr-pre">              <span class="fn">ALU</span>
        +--------------+
<span class="num">127</span> ---&gt;|              |---&gt; <span class="type">Result</span> = <span class="num">1000 0000</span>
  <span class="num">1</span> ---&gt;|    <span class="fn">Adder</span>    |
        |              |---&gt; <span class="type">Overflow</span> = <span class="num">1</span>
        +--------------+</pre>
</div>

<p>可以把 <code>Result</code> 和 <code>Overflow</code> 看成兩份不同的資訊：<code>Result</code> 回答「這次硬體算完，留下哪些 bits」，<code>Overflow</code> 回答「這些 bits 還能不能正確代表 signed 數學上的答案」。</p>

<div class="hkr-rain-divider"><span>01 10 01</span></div>

<div class="hkr-evidence">
<div class="hkr-evidence-head">
<span class="hkr-tag danger">真實案例</span>
<strong>Ariane 5 首飛失敗（1996）</strong>
</div>
<p>1996 年 6 月 4 日，European Space Agency 的 Ariane 5 火箭首次飛行，在升空大約 37 秒後失去導引資訊，偏離航線，最終解體並自毀。ESA 的調查指出，問題鏈條源自慣性參考系統的軟體設計，其中涉及數值轉換時發生的 operand error。</p>
<p>最值得注意的地方在於，程式把一個較大範圍的數值塞進較小範圍的整數表示，實際數值超出目標型別能表示的範圍後觸發例外，而錯誤處理與備援設計又讓問題一路擴散到飛行控制。這跟前面提到的「8-bit signed 只能表示 -128 到 127」是同一類核心問題，只是 Ariane 5 實際系統的資料型別與軟體流程遠比 8-bit 範例複雜。</p>
</div>

<p>可以先用熟悉的 8-bit 假想版本理解這個問題。假設有一個較大的數值 <code>velocity = 200</code>，硬要把它放進 8-bit signed，但 8-bit signed 只能表示 <code>-128 ~ 127</code>：</p>

<div class="hkr-flow">
<div class="hkr-step">velocity = 200</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step cond">想塞進 signed 8-bit</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step cond">最大只能到 127</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step danger">超出可表示範圍</div>
<div class="hkr-arrow">→</div>
<div class="hkr-step danger">Overflow / conversion error</div>
</div>

<p>Ariane 5 的實際問題涉及把 64-bit 浮點值轉換成 16-bit signed integer，其中一個轉換值超出了 16-bit signed integer 能表示的範圍，引發 operand error。調查報告還指出，相關保護沒有覆蓋這個變數，因為設計時認為它在預期操作範圍內不會出問題。</p>

<div class="hkr-steps">
<div class="hkr-stepcard danger">
<div class="hkr-stepnum">1</div>
<div class="hkr-step-title">數值超出目標整數範圍</div>
<p>數值轉換發生 operand error，觸發軟體 exception。</p>
</div>
<div class="hkr-stepcard danger">
<div class="hkr-stepnum">2</div>
<div class="hkr-step-title">慣性參考系統停止正常工作</div>
<p>備援系統遇到相同的轉換問題，也一併失效。</p>
</div>
<div class="hkr-stepcard danger">
<div class="hkr-stepnum">3</div>
<div class="hkr-step-title">飛行器失去有效導引與姿態資訊</div>
<p>控制系統收到異常資訊，噴嘴大幅偏轉。</p>
</div>
<div class="hkr-stepcard danger">
<div class="hkr-stepnum">4</div>
<div class="hkr-step-title">結構解體、自毀</div>
<p>火箭急劇偏離航線，結構承受巨大空氣動力負載，最終解體並觸發自毀。</p>
</div>
</div>

<p>ESA 的正式調查確認，兩套慣性參考系統幾乎同時失效，最終造成導引與姿態資訊完全喪失。</p>

<ul class="hkr-checklist">
<li>ALU 永遠會把運算算完，不會因為數值「看起來太大」就自動停下來</li>
<li>overflow 是額外的狀態訊號，真正要不要處理，取決於上層程式或硬體保護機制</li>
<li>把大範圍數值硬塞進小範圍整數型別，是實際系統中真正發生過重大事故的根因之一</li>
</ul>

<p>參考資料：<a href="https://hackmd.io/@RinHizakura/r12IHulaY" target="_blank">https://hackmd.io/@RinHizakura/r12IHulaY</a></p>

</section>

<footer>整理自 Two's Complement / Signed Overflow 筆記</footer>

</div>
</div>

<!-- endtab -->

{% endtabs %}
