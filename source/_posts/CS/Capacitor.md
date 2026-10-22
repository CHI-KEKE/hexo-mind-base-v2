---
title: Capacitor
date: 2026-08-11 08:29:03
categories: CS
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/CS/capacitor-landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/CS/capacitor-landing.png
tags:
toc:
toc_number:
comments :
---

{% tabs Capacitor%}

<!-- tab 導體-->

<style>
.organic-hero { position:relative; overflow:hidden; border-radius:16px; padding:36px 40px; margin:24px 0 30px; background:linear-gradient(135deg, #2f4a3e 0%, #3f5c47 45%, #6b5a44 100%); color:#f5f1e6; }
.organic-hero .oh-leaf { position:absolute; font-size:2.6rem; opacity:0.32; filter:drop-shadow(0 2px 3px rgba(0,0,0,.25)); pointer-events:none; }
.organic-hero .oh-leaf.l1 { top:-10px; right:60px; transform:rotate(15deg); }
.organic-hero .oh-leaf.l2 { top:40px; right:6px; font-size:2rem; transform:rotate(-20deg); }
.organic-hero .oh-leaf.l3 { bottom:-14px; right:120px; font-size:2.2rem; opacity:0.22; transform:rotate(35deg); }
.organic-hero .oh-tag { display:inline-block; font-size:.72rem; letter-spacing:2px; text-transform:uppercase; background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.3); padding:3px 12px; border-radius:20px; margin-bottom:14px; }
.organic-hero .oh-title { margin:0 0 10px; font-size:1.4rem; font-weight:700; color:#f5f1e6; position:relative; z-index:1; }
.organic-hero .oh-desc { max-width:80%; font-size:.92rem; line-height:1.85; color:#e4e6dc; position:relative; z-index:1; }
.organic-hero .oh-desc code { background:rgba(255,255,255,.18); padding:1px 6px; border-radius:3px; color:#fdf6e3; }

.glass-feature-row { display:flex; flex-wrap:wrap; gap:18px; background:linear-gradient(135deg, rgba(47,74,62,.92), rgba(63,92,71,.9)); border-radius:14px; padding:24px 26px; margin:18px 0 28px; }
.glass-feature-row .gf-item { flex:1 1 150px; text-align:center; color:#eef0e6; }
.glass-feature-row .gf-icon { width:46px; height:46px; margin:0 auto 10px; border-radius:50%; border:1.5px solid rgba(255,255,255,.55); display:flex; align-items:center; justify-content:center; font-size:1.25rem; }
.glass-feature-row .gf-title { font-weight:700; font-size:.9rem; margin-bottom:6px; }
.glass-feature-row .gf-desc { font-size:.78rem; line-height:1.65; color:#cfd6c6; }
.glass-feature-row .gf-desc code { background:rgba(255,255,255,.2); padding:1px 5px; border-radius:3px; color:#fdf6e3; }
.glass-feature-row .gf-arrow { flex:0 0 auto; align-self:center; font-size:1.35rem; color:#e8dcb8; opacity:.85; }

.earth-line-steps { position:relative; margin:22px 0 30px; padding-left:56px; }
.earth-line-steps::before { content:''; position:absolute; left:19px; top:4px; bottom:4px; width:2px; background:linear-gradient(180deg, #5f8a56, #a2854f); opacity:.55; }
.earth-line-steps .ls-step { position:relative; margin-bottom:26px; }
.earth-line-steps .ls-step:last-child { margin-bottom:0; }
.earth-line-steps .ls-num { position:absolute; left:-56px; top:0; width:38px; height:38px; border-radius:50%; background:#fbfaf6; display:flex; align-items:center; justify-content:center; font-family:'Courier New', Consolas, monospace; font-weight:700; font-size:.82rem; z-index:2; box-shadow:0 2px 6px rgba(0,0,0,.15); }
.earth-line-steps .ls-step.leaf .ls-num { border:2px solid #3f6146; color:#3f6146; }
.earth-line-steps .ls-step.clay .ls-num { border:2px solid #5c4433; color:#5c4433; }
.earth-line-steps .ls-step.sand .ls-num { border:2px solid #a2854f; color:#8a6a3f; }
.earth-line-steps .ls-body { display:flex; align-items:center; flex-wrap:wrap; gap:10px; min-height:38px; }
.earth-line-steps .ls-title { font-weight:700; font-size:.95rem; color:#2f4f4f; padding:1px 3px; background-repeat:no-repeat; background-position:0 68%; background-size:100% 42%; }
.earth-line-steps .ls-step.leaf .ls-title { background-image:linear-gradient(rgba(95,138,86,.38), rgba(95,138,86,.38)); }
.earth-line-steps .ls-step.clay .ls-title { background-image:linear-gradient(rgba(138,106,82,.4), rgba(138,106,82,.4)); }
.earth-line-steps .ls-step.sand .ls-title { background-image:linear-gradient(rgba(199,168,105,.5), rgba(199,168,105,.5)); }
.earth-line-steps .ls-connector { flex:1 1 30px; height:0; border-bottom:1.5px dashed #c9c3ae; min-width:24px; }
.earth-line-steps .ls-desc { font-size:.82rem; color:#5a5648; line-height:1.6; }
.earth-line-steps .ls-desc code { background:#eef0eb; padding:1px 6px; border-radius:3px; color:#8a6a3f; font-size:.85em; }
</style>

<div class="organic-hero">
<span class="oh-leaf l1">🍃</span><span class="oh-leaf l2">🍂</span><span class="oh-leaf l3">🍃</span>
<div class="oh-tag">材料世界</div>
<div class="oh-title">導體</div>
<div class="oh-desc">有些材料裡面的電子很容易到處跑，這種材料就叫導體，例如銅、鋁、銀、金。</div>
</div>

金屬裡本來就有很多可以移動的電子，這些電子平常也不是完全不動，只是沒有一個共同的移動方向。導體之所以導電，是因為其中有一部分電子沒有被某一顆原子牢牢綁死，而是處在可以延伸遍布整個材料的電子狀態中，所以一旦整體電荷分布出現不平衡，這些電子就能重新分布。

在金屬裡，有一些電子的量子狀態是<code>離域（delocalized）</code>的。可以先把「離域」理解成這個電子的可存在狀態延伸到很多原子甚至整塊晶體，不適合再把它想成只屬於左邊某一顆原子。不過「自由」容易讓人誤會成電子完全不受任何東西影響，它們仍然處在晶格的量子環境中，只是沒有被某一顆特定原子局限住而已。

<!-- endtab -->


<!-- tab 絕緣體-->

<div class="organic-hero">
<span class="oh-leaf l1">🍂</span><span class="oh-leaf l2">🍂</span><span class="oh-leaf l3">🍃</span>
<div class="oh-tag">材料世界</div>
<div class="oh-title">絕緣體</div>
<div class="oh-desc">反過來，有些材料裡面的電荷很難長距離自由移動，這種材料就叫絕緣體，例如塑膠、玻璃、陶瓷、橡膠。</div>
</div>

在一般條件下，能參與導電的電子狀態，跟下一批「可以拿來導電」的可用狀態之間，隔著一段較大的能量差：

<div class="glass-feature-row">
<div class="gf-item">
<div class="gf-icon">●</div>
<div class="gf-title">電子目前待的狀態</div>
<div class="gf-desc">大部分電子都乖乖待在原本的狀態裡</div>
</div>
<div class="gf-arrow">⇡</div>
<div class="gf-item">
<div class="gf-icon">⚡</div>
<div class="gf-title">很大的能量門檻</div>
<div class="gf-desc">一般的小電壓提供的條件不足以讓大量電子跨過去</div>
</div>
<div class="gf-arrow">⇡</div>
<div class="gf-item">
<div class="gf-icon">○</div>
<div class="gf-title">可讓電子繼續導電的狀態</div>
<div class="gf-desc">電子跨過門檻後才能參與導電</div>
</div>
</div>

正因為這道門檻很大，電荷幾乎過不去，這也是為什麼<code>電容</code>會刻意在中間放一層絕緣層，就是要利用這個特性，故意不讓兩邊的電子直接穿過去。

<!-- endtab -->


<!-- tab 電子為什麼會移動-->

<div class="organic-hero">
<span class="oh-leaf l1">🍃</span><span class="oh-leaf l2">🍃</span><span class="oh-leaf l3">🍂</span>
<div class="oh-tag">驅動原理</div>
<div class="oh-title">電子為什麼會移動</div>
<div class="oh-desc">當一個地方電子很多、另一個地方電子很少時，只要中間出現可移動的路徑，電子就會重新分布，往更接近平衡的狀態發展。</div>
</div>

原本被強行做出來的電荷不均勻，會產生讓電荷重新排列的作用；導線只是提供它重新排列的通道，因為電荷系統本來就有往較低能量配置重新分布的傾向。用一條金屬線的例子來看整個過程：

<div class="earth-line-steps">
<div class="ls-step leaf">
<div class="ls-num">01</div>
<div class="ls-body"><span class="ls-title">兩端原本沒有明顯差異</span><span class="ls-connector"></span><span class="ls-desc">金屬線兩端（A、B）電子分布大致正常，彼此沒有誰多誰少的差別</span></div>
</div>
<div class="ls-step clay">
<div class="ls-num">02</div>
<div class="ls-body"><span class="ls-title">電池介入，兩端被「弄不平均」</span><span class="ls-connector"></span><span class="ls-desc">電池利用化學能，讓 A 端電子變多、B 端電子變少</span></div>
</div>
<div class="ls-step sand">
<div class="ls-num">03</div>
<div class="ls-body"><span class="ls-title">接上導體，電子重新排列</span><span class="ls-connector"></span><span class="ls-desc">電子沿著導體重新分布，往平衡的方向移動</span></div>
</div>
</div>

所以可以把「加電壓」很自然地理解成在電路的兩個位置製造出一個電荷／能量上的不均勻條件，這個不均勻會驅動導體裡能移動的電子重新分布，然後我們才把這個「兩個位置之間的能量差異」叫做電位差。

回到電容，電池會幫電容做同樣的事，只是中間換成絕緣層擋著：

<div class="earth-line-steps">
<div class="ls-step leaf">
<div class="ls-num">01</div>
<div class="ls-body"><span class="ls-title">電池把電荷分別堆到兩片極板</span><span class="ls-connector"></span><span class="ls-desc">左板電子變多、右板電子變少，中間隔著絕緣層</span></div>
</div>
<div class="ls-step clay">
<div class="ls-num">02</div>
<div class="ls-body"><span class="ls-title">電荷過不去，電場越來越強</span><span class="ls-connector"></span><span class="ls-desc">電容自己建立的電場越來越強，這種不平衡被絕緣層擋著保存下來</span></div>
</div>
<div class="ls-step sand">
<div class="ls-num">03</div>
<div class="ls-body"><span class="ls-title">外部接上燈泡，出現路徑</span><span class="ls-connector"></span><span class="ls-desc">電子較多的一側經過燈泡，補到缺電子的一側</span></div>
</div>
<div class="ls-step leaf">
<div class="ls-num">04</div>
<div class="ls-body"><span class="ls-title">差異逐漸縮小，趨於平衡</span><span class="ls-connector"></span><span class="ls-desc">這就是電容放電的過程</span></div>
</div>
</div>

<!-- endtab -->


<!-- tab 電容做什麼-->

<div class="organic-hero">
<span class="oh-leaf l1">🍃</span><span class="oh-leaf l2">🍂</span><span class="oh-leaf l3">🍃</span>
<div class="oh-tag">實際應用</div>
<div class="oh-title">電容做什麼</div>
<div class="oh-desc">電容有一個非常重要的特性，它可以很快吸收電荷，也可以很快釋放電荷，所以很適合處理「短時間變化」。</div>
</div>

以 <code>CPU</code> 旁邊的電源電容為例：

<div class="earth-line-steps">
<div class="ls-step leaf">
<div class="ls-num">01</div>
<div class="ls-body"><span class="ls-title">電源穩定供電</span><span class="ls-connector"></span><span class="ls-desc">CPU 平常吃電很穩，電源一直送電過去</span></div>
</div>
<div class="ls-step clay">
<div class="ls-num">02</div>
<div class="ls-body"><span class="ls-title">CPU 瞬間想多拿一大口電</span><span class="ls-connector"></span><span class="ls-desc">大量電晶體同時切換，CPU 突然想拿更多電流</span></div>
</div>
<div class="ls-step sand">
<div class="ls-num">03</div>
<div class="ls-body"><span class="ls-title">電源來不及補上，電壓開始掉</span><span class="ls-connector"></span><span class="ls-desc">導線本身有電阻、電感，來不及在瞬間補上</span></div>
</div>
<div class="ls-step leaf">
<div class="ls-num">04</div>
<div class="ls-body"><span class="ls-title">電容就近放電，補住壓降</span><span class="ls-connector"></span><span class="ls-desc">最近的電容先放電，減少電壓掉下去的幅度</span></div>
</div>
</div>

<!-- endtab -->


{% endtabs %}