---
title: Flip-Flop - 讓電路記住一件事情
date: 2026-08-08 09:47:03
categories: CS
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/CS/flip-flop-landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/CS/flip-flop-landing.png
tags:
toc:
toc_number:
comments :
---

{% tabs Flip-Flop%}

<!-- tab 保存狀態-->

<style>
.cyber-card{background:linear-gradient(180deg,#0d1410,#0a0f0c);border:1px solid rgba(57,255,136,.35);border-radius:14px;padding:22px 24px;margin:22px 0;box-shadow:0 0 22px rgba(57,255,136,.08),inset 0 0 30px rgba(0,0,0,.4);color:#c9ffe0;}
.cyber-card-title{display:flex;align-items:center;gap:10px;font-weight:700;font-size:1.05em;color:#39ff88;text-shadow:0 0 10px rgba(57,255,136,.55);letter-spacing:1px;margin-bottom:14px;padding-bottom:10px;border-bottom:1px dashed rgba(57,255,136,.3);}
.cyber-card-title .cyber-icon{font-size:1.2em;}
.cyber-card p{margin:10px 0;line-height:1.9;}
.cyber-note{background:rgba(57,255,136,.07);border-left:3px solid #39ff88;border-radius:0 8px 8px 0;padding:12px 16px;margin:16px 0;color:#eafff2;line-height:1.8;}
.cyber-note b{color:#39ff88;}
.cyber-note.warn{background:rgba(255,189,46,.08);border-left-color:#ffbd2e;color:#ffe9b8;}
.cyber-note.warn b{color:#ffbd2e;}
.cyber-table-wrap{display:inline-block;max-width:100%;overflow-x:auto;border:1px solid rgba(57,255,136,.35);border-radius:10px;margin:14px 0;background:#0a0f0c;}
.cyber-table{width:auto;border-collapse:collapse;color:#c9ffe0;}
.cyber-table th{background:rgba(57,255,136,.15);color:#39ff88;font-weight:700;padding:10px 18px;border-bottom:1px solid rgba(57,255,136,.35);white-space:nowrap;}
.cyber-table td{padding:9px 18px;border-bottom:1px solid rgba(57,255,136,.12);white-space:nowrap;}
.cyber-table tr:last-child td{border-bottom:none;}
.cyber-terminal{border:1px solid rgba(57,255,136,.4);border-radius:10px;overflow:hidden;margin:16px 0;background:#050805;box-shadow:0 0 20px rgba(57,255,136,.08);}
.cyber-terminal-bar{background:#0d130f;padding:8px 14px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(57,255,136,.25);}
.cyber-dot{width:10px;height:10px;border-radius:50%;display:inline-block;background:#39ff88;}
.cyber-dot.d2{opacity:.6;}
.cyber-dot.d3{opacity:.3;}
.cyber-terminal-title{margin-left:6px;color:#7fffb0;font-family:Consolas,monospace;font-size:.85em;letter-spacing:1px;}
.cyber-terminal-pre{margin:0!important;padding:16px 18px!important;background:transparent!important;border:none!important;box-shadow:none!important;color:#39ff88!important;font-family:Consolas,'Courier New',monospace!important;white-space:pre!important;line-height:1.6!important;text-shadow:0 0 6px rgba(57,255,136,.35)!important;}
.cyber-terminal-pre .sig1{color:#ff8a80!important;font-weight:700;text-shadow:0 0 6px rgba(255,138,128,.5)!important;}
.cyber-terminal-pre .sig0{color:#39ff88!important;font-weight:700;}
.cyber-terminal-pre .siglabel{color:#7fffb0!important;text-shadow:none!important;}
.cyber-flow{display:flex;flex-direction:column;gap:0;margin:16px 0;}
.cyber-flow-step{display:flex;align-items:center;gap:14px;background:rgba(57,255,136,.06);border:1px solid rgba(57,255,136,.3);border-radius:8px;padding:10px 16px;}
.cyber-flow-label{color:#7fffb0;font-size:.85em;letter-spacing:1px;min-width:70px;}
.cyber-flow-value{color:#eafff2;font-family:Consolas,monospace;font-size:1.05em;font-weight:700;}
.cyber-flow-arrow{color:#39ff88;padding:6px 0 6px 20px;font-size:.85em;opacity:.85;}
.cyber-badge{display:inline-block;background:rgba(57,255,136,.15);color:#39ff88;border:1px solid rgba(57,255,136,.4);border-radius:6px;padding:2px 10px;font-size:.8em;font-weight:700;letter-spacing:1px;margin-right:8px;}
.cyber-chip-row{margin:10px 0 4px;}
.cyber-chip{display:inline-block;font-family:Consolas,monospace;font-size:.8em;padding:3px 12px;border-radius:20px;margin:0 8px 8px 0;border:1px solid;background:#0a0f0c;}
.cyber-chip.neutral{color:#7fffb0;border-color:rgba(57,255,136,.4);}
.cyber-chip.write{color:#ff8a80;border-color:rgba(255,138,128,.5);}
.cyber-chip.hold{color:#ffbd2e;border-color:rgba(255,189,46,.5);}
.cyber-chip.stable{color:#39ff88;border-color:rgba(57,255,136,.5);text-shadow:0 0 6px rgba(57,255,136,.35);}
</style>

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>Logic Gate 只認得「現在」</div>
<p>在網路上搜尋邏輯閘，可以找到 <code>AND</code>、<code>OR</code>、<code>NOT</code>、<code>NOR</code>、<code>XOR</code> 這些能「計算」的元件，舉例來說：</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">combinational-logic.sim</span></div>
<pre class="cyber-terminal-pre"><span class="siglabel">A</span> = <span class="sig1">1</span>
<span class="siglabel">B</span> = <span class="sig0">0</span>

<span class="siglabel">A AND B</span> = <span class="sig0">0</span></pre>
</div>
<p>它們的共同特性是：現在**輸入是多少，輸出就由它決定**，把輸入改掉，輸出就跟著改掉，完全沒有「之前發生過什麼」的概念。</p>
</div>

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>問題：算完的結果要留在哪裡</div>
<p>若要做計算機，就會遇到 <code>3 + 5 = 8</code> 這種情況，算出 <code>8</code> 之後，下一步可能還要 <code>8 + 7</code>，因此我們需要某種東西，能讓算出的 <code>8</code> 被留著。</p>
<div class="cyber-note warn"><b>💡</b> 問題就變成：怎麼讓電路具有記憶？</div>
</div>

<!-- endtab -->


<!-- tab Feedback-->

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>普通電路：一路往前</div>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">straight-through.circuit</span></div>
<pre class="cyber-terminal-pre"><span class="siglabel">輸入</span>
 ↓
Gate
 ↓
<span class="siglabel">輸出</span></pre>
</div>
</div>

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>把輸出接回輸入</div>
<p>如果我們把輸出接回自己的輸入呢？就變成：</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">feedback.circuit</span></div>
<pre class="cyber-terminal-pre">        ┌──────────┐
        ↓          │
<span class="siglabel">輸入</span> → Gate → <span class="siglabel">輸出</span> ┘</pre>
</div>
<p>這叫 <code>Feedback</code>（回授），這個想法很重要，因為現在上一刻的輸出變成下一刻的輸入，也就是過去的狀態開始有能力影響現在，而這便是記憶出現的基礎。</p>
</div>

<!-- endtab -->


<!-- tab 兩顆 NOR 交叉 Feedback-->

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>兩顆 NOR 的接法</div>
<p>我們先拿兩顆 <code>NOR</code>。每顆 <code>NOR</code> 都有兩個輸入、一個輸出，我們這樣定義：</p>
<div class="cyber-chip-row"><span class="cyber-chip neutral">NOR 1 輸入：S、Q̅</span><span class="cyber-chip neutral">NOR 1 輸出：Q</span></div>
<div class="cyber-chip-row"><span class="cyber-chip neutral">NOR 2 輸入：R、Q</span><span class="cyber-chip neutral">NOR 2 輸出：Q̅</span></div>

```bash
         ┌─────────────┐
S ──────→│             │
Q̅ ─────→│    NOR 1    ├────→ Q
         └─────────────┘


         ┌─────────────┐
R ──────→│             │
Q ──────→│    NOR 2    ├────→ Q̅
         └─────────────┘
```


<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>互相餵對方：Cross-coupled</div>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">cross-coupled.circuit</span></div>
<pre class="cyber-terminal-pre">        ┌────────────────┐
        ↓                │
<span class="siglabel">S</span> → NOR 1 → <span class="siglabel">Q</span> → NOR 2 ← <span class="siglabel">R</span>
    ↑              │
    └──── <span class="siglabel">Q̅</span> ←─────┘</pre>
</div>
<p>這就是 <code>Cross-coupled NOR gates</code>，兩顆 <code>NOR</code> 互相交叉回授。這組電路有個正式名字，叫 <code>SR Latch</code>（<code>S</code> = Set、<code>R</code> = Reset）。</p>
</div>


```bash
                  ┌────────────────────────┐
                  │                        │
                  │                        ▼
              ┌─────────┐             ┌─────────┐
S ───────────→│  NOR 1  │─── Q ─────→│  NOR 2  │←──────── R
              └─────────┘             └─────────┘
                  ▲                        │
                  │                        │
                  └──────── Q̅ ────────────┘
```

</div>

<!-- endtab -->


<!-- tab 為什麼這東西可以「記住」-->

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>穩定狀態下的循環</div>
<p>假設目前：</p>
<div class="cyber-chip-row"><span class="cyber-chip stable">Q = 0</span><span class="cyber-chip stable">Q̅ = 1</span></div>
<p>然後我們讓：</p>
<div class="cyber-chip-row"><span class="cyber-chip hold">S = 0</span><span class="cyber-chip hold">R = 0</span></div>
<p>看看會發生什麼。</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">nor-1.eval</span></div>
<pre class="cyber-terminal-pre"><span class="siglabel">S</span>  = <span class="sig0">0</span>
<span class="siglabel">Q̅</span> = <span class="sig1">1</span>

NOR(0,1) = <span class="sig0">0</span>  →  <span class="siglabel">Q</span> = <span class="sig0">0</span></pre>
</div>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">nor-2.eval</span></div>
<pre class="cyber-terminal-pre"><span class="siglabel">R</span> = <span class="sig0">0</span>
<span class="siglabel">Q</span> = <span class="sig0">0</span>

NOR(0,0) = <span class="sig1">1</span>  →  <span class="siglabel">Q̅</span> = <span class="sig1">1</span></pre>
</div>
<p>結果 <code>Q = 0</code>、<code>Q̅ = 1</code>，完全沒有變。而且它會一直這樣循環下去：</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">steady-state.loop</span></div>
<pre class="cyber-terminal-pre"><span class="sig0">Q=0</span> → 讓 <span class="sig1">Q̅=1</span> → 又讓 <span class="sig0">Q=0</span> → ...（穩定狀態）</pre>
</div>
</div>

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>寫入一次，看它是否記住</div>
<p>接著我們實際做一次「寫入」，假設：</p>
<div class="cyber-chip-row"><span class="cyber-chip write">S = 1</span><span class="cyber-chip hold">R = 0</span></div>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">write.eval</span></div>
<pre class="cyber-terminal-pre">NOR 1：NOR(1, ?) = <span class="sig0">0</span>  →  <span class="siglabel">Q</span> = <span class="sig0">0</span>
NOR 2：NOR(0, 0) = <span class="sig1">1</span>  →  <span class="siglabel">Q̅</span> = <span class="sig1">1</span></pre>
</div>
<p>我們可以把這一步理解成：把 <code>Q</code> 設成 <code>0</code>。</p>
<p><b>真正的「記住」發生在下一步。</b> 現在把剛才的 <code>S = 1</code> 撤掉，變成：</p>
<div class="cyber-chip-row"><span class="cyber-chip hold">S = 0</span><span class="cyber-chip hold">R = 0</span></div>
<p>注意，現在已經沒有外部輸入在說「<code>Q</code> 給我等於 <code>0</code>！」，可是 <code>Q</code> 依然是 <code>0</code>。為什麼？因為：</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">retain.loop</span></div>
<pre class="cyber-terminal-pre"><span class="sig0">Q=0</span> → 使 <span class="sig1">Q̅=1</span> → <span class="sig1">Q̅=1</span> → 又使 <span class="sig0">Q=0</span> → 循環

寫入時： S=1 R=0  →  Q=0
放開後： S=0 R=0  →  Q=0
過一段時間後： S=0 R=0  →  Q=0</pre>
</div>
<p>這個「外面的寫入訊號消失了，<code>Q</code> 卻還維持著」，就是記憶。假設我只告訴你 <code>S = 0</code>、<code>R = 0</code>，然後問「<code>Q</code> 是多少？」這其實答不出來，它可能是 <code>0</code>，也可能是 <code>1</code>，因為要知道的是它之前被設定成什麼。</p>
<div class="cyber-table-wrap">
<table class="cyber-table">
<tr><th>元件</th><th>輸出取決於</th></tr>
<tr><td>普通 Logic Gate</td><td>現在輸入</td></tr>
<tr><td><code>Latch</code></td><td>現在輸入 + 之前狀態</td></tr>
</table>
</div>
<div class="cyber-note">這就是「記憶」的本質。</div>
</div>

<!-- endtab -->


<!-- tab 如果我改 R，狀態不就變了-->

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>需要能寫、也需要能保持</div>
<p>而且這正是我們希望它具有的能力。如果記憶體寫入一次之後永遠不能修改，那也沒什麼用。所以我們需要兩種能力：</p>
<div class="cyber-chip-row"><span class="cyber-chip write">① 我想寫入時 → 可以改變 Q</span><span class="cyber-chip hold">② 我不想寫入時 → Q 自己維持</span></div>
<p><code>SR Latch</code> 的 <code>S</code>、<code>R</code> 就是控制它的外部輸入。在 Hold 狀態下，你必須確保 <code>S</code>、<code>R</code> 都維持在正確的非作用狀態。</p>
</div>

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>S／R 一旦亂變，資料就跟著亂變</div>
<p>對這個 NOR <code>SR Latch</code> 來說：</p>
<div class="cyber-chip-row"><span class="cyber-chip hold">S = 0</span><span class="cyber-chip hold">R = 0</span></div>
<p>代表「不要改資料」。如果外部突然變成：</p>
<div class="cyber-chip-row"><span class="cyber-chip write">R = 1</span></div>
<p>那就是在要求 <code>Latch</code> 改變狀態。所以其實已經發現 <code>SR Latch</code> 的一個工程問題：既然 <code>S</code>／<code>R</code> 可以直接影響記憶，就必須非常小心控制它們，避免不小心觸發寫入。</p>
<div class="cyber-note warn">這個問題會直接帶我們走向後面的 <code>D Latch</code> 和 <code>Flip-Flop</code>。</div>
</div>

<!-- endtab -->


<!-- tab Clock to Flip-Flop-->

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>只准在指定的那一刻寫入</div>
<p>既然 <code>Latch</code> 已經能記，為什麼還需要 <code>Flip-Flop</code>？因為剛才已經發現問題「我要如何確保 <code>S</code>／<code>R</code> 不會亂變？」</p>
<p>我們真正希望的是外面的資料可以一直變（<code>0 → 1 → 0 → 1 → 0 → 1</code>），但記憶元件不要一直跟著亂變。我們希望能說「現在才准你存！」。例如資料 <code>D</code> 是</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">data.waveform</span></div>
<pre class="cyber-terminal-pre"><span class="siglabel">D</span>:  0 ── 1 ── 0 ── 1 ── <span class="sig1">1</span>
                        ↑
                     就這一刻，我只想記住這瞬間的 <span class="sig1">1</span></pre>
</div>
<p>所以我們需要另外一個控制訊號，這就是 <code>Clock</code>。以最常見的 <code>D Flip-Flop</code> 來看：</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">d-flip-flop.block</span></div>
<pre class="cyber-terminal-pre">         ┌───────────────┐
<span class="siglabel">D</span>   ────→│               │
         │ D Flip-Flop   ├────→ <span class="siglabel">Q</span>
<span class="siglabel">CLK</span> ────→│               │
         └───────────────┘</pre>
</div>
<p>你只需要關心：<code>D</code> = 想存什麼、<code>CLK</code> = 什麼時候存、<code>Q</code> = 現在存著什麼。例如目前 <code>Q = 0</code>，外面的 <code>D</code> 可以一直變（<code>0 → 1 → 0 → 1 → 1</code>），<code>Q</code> 不需要每次都跟著變，直到 <code>Clock</code> 的指定邊緣：</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">clock.waveform</span></div>
<pre class="cyber-terminal-pre"><span class="siglabel">CLK</span>: ________|‾‾‾‾
              ↑
            就現在，假設這一刻 <span class="siglabel">D</span> = <span class="sig1">1</span>，Flip-Flop 就捕捉 <span class="siglabel">Q</span> = <span class="sig1">1</span>，然後繼續保持</pre>
</div>
<div class="cyber-note">可以把它想成：<code>Clock</code> 在某個瞬間喊「拍照！」，<code>Flip-Flop</code> 把當下 <code>D</code> 的值拍下來，然後維持這個值。</div>
</div>

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>一層一層疊上去的抽象</div>
<p>完整 <code>Flip-Flop</code> 需要更多電路來控制，是一層一層疊上去的：</p>
<div class="cyber-flow">
<div class="cyber-flow-step"><span class="cyber-flow-label">Gate</span><span class="cyber-flow-value">基本 Logic Gates</span></div>
<div class="cyber-flow-arrow">↓ 加入 Feedback</div>
<div class="cyber-flow-step"><span class="cyber-flow-label">Latch</span><span class="cyber-flow-value">Cross-coupled NOR</span></div>
<div class="cyber-flow-arrow">↓ 加入資料與時間控制</div>
<div class="cyber-flow-step"><span class="cyber-flow-label">Flip-Flop</span><span class="cyber-flow-value">D + CLK → Q</span></div>
</div>
<p>例如一個 <code>D Flip-Flop</code> 的內部實作，可以由多個 Gate／<code>Latch</code> 組成，但對 CPU 設計者來說，可以把它抽象成：</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">ff.abstract</span></div>
<pre class="cyber-terminal-pre">         ┌──────┐
<span class="siglabel">D</span>   ────→│  FF  │────→ <span class="siglabel">Q</span>
<span class="siglabel">CLK</span> ────→│      │
         └──────┘</pre>
</div>
<p>只需要知道：一個 <code>FF</code> 可以保存 1 bit，並且在指定 <code>Clock edge</code> 更新。</p>
</div>

<div class="cyber-card">
<div class="cyber-card-title"><span class="cyber-icon">▸</span>很多 Flip-Flop 組成 Register</div>
<p>假設 CPU 想保存 <code>0101</code>，可以使用四個 <code>Flip-Flop</code>：</p>
<div class="cyber-terminal">
<div class="cyber-terminal-bar"><span class="cyber-dot"></span><span class="cyber-dot d2"></span><span class="cyber-dot d3"></span><span class="cyber-terminal-title">register.block</span></div>
<pre class="cyber-terminal-pre"><span class="siglabel">D3</span> ──→ [FF] ──→ <span class="siglabel">Q3</span> = <span class="sig0">0</span>
<span class="siglabel">D2</span> ──→ [FF] ──→ <span class="siglabel">Q2</span> = <span class="sig1">1</span>
<span class="siglabel">D1</span> ──→ [FF] ──→ <span class="siglabel">Q1</span> = <span class="sig0">0</span>
<span class="siglabel">D0</span> ──→ [FF] ──→ <span class="siglabel">Q0</span> = <span class="sig1">1</span>
         ↑
         │
       Clock</pre>
</div>
<p>四個一起就是 <code>0 1 0 1</code>，也就是十進位的 <code>5</code>。這組東西就是 <code>Register</code>（暫存器）</p>
<div class="cyber-table-wrap">
<table class="cyber-table">
<tr><th>Flip-Flop 數量</th><th>可保存位元</th></tr>
<tr><td>1 個</td><td>1 bit</td></tr>
<tr><td>8 個</td><td>8 bits</td></tr>
<tr><td>64 個</td><td>64 bits</td></tr>
<tr><td>很多個組合</td><td><code>Register</code>（暫存器）</td></tr>
</table>
</div>
</div>

<!-- endtab -->

{% endtabs %}