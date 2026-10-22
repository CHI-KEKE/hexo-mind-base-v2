---
title: p-value
date: 2026-07-28 08:32:05
categories: Statistics
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/p-value/landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/p-value/landing.png
tags:
toc:
toc_number:
comments :
mathjax: true
---

<style>
.pv-row { display: flex; align-items: center; gap: 14px; margin: 20px 0 8px; flex-wrap: wrap; }
.pv-card { flex: 1; min-width: 130px; background: #fbfaf6; border: 1px solid #c9c3ae; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); padding: 14px 10px; text-align: center; }
.pv-card .pv-icon { font-size: 1.5rem; line-height: 1; }
.pv-card .pv-value { font-weight: 700; font-size: 1.05rem; color: #2f4f4f; margin-top: 6px; }
.pv-card .pv-label { font-size: 0.74rem; color: #8a8272; margin-top: 3px; letter-spacing: 0.5px; }
.pv-card.pv-sum { background: #f2efe4; border-color: #2f4f4f; }
.pv-card.pv-sum .pv-value { color: #a3441e; font-size: 1.15rem; }
.pv-op { font-size: 1.3rem; font-weight: 700; color: #a3441e; flex-shrink: 0; }

.pv-verdict { display: flex; align-items: center; gap: 10px; margin: 10px 0 22px; padding: 10px 18px; border-radius: 2px; font-size: 0.92rem; line-height: 1.7; }
.pv-verdict .pv-vicon { font-size: 1.2rem; flex-shrink: 0; }
.pv-verdict.reject { background: #fbf1ee; border-left: 4px solid #a3441e; color: #7a2e1f; }
.pv-verdict.keep { background: #eef3ec; border-left: 4px solid #6b8e6b; color: #34513a; }
.pv-verdict.border { background: #fdf6e3; border-left: 4px solid #b8860b; color: #6b5210; }
.pv-verdict code { background: rgba(0,0,0,0.06); padding: 1px 6px; border-radius: 3px; }

.pv-bar-card { background: #fbfaf6; border: 1px solid #c9c3ae; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); padding: 16px 20px 18px; margin: 20px 0 14px; }
.pv-bar-title { font-weight: 700; color: #2f4f4f; font-size: 0.95rem; margin-bottom: 10px; letter-spacing: 0.5px; }
.pv-bar { display: flex; height: 30px; border-radius: 4px; overflow: hidden; border: 1px solid #c9c3ae; }
.pv-seg.safe { background: #e3ddc9; }
.pv-seg.count { background: #5b7c99; }
.pv-legend { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 10px; font-size: 0.8rem; color: #4a4636; }
.pv-legend .pv-dot { display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 5px; vertical-align: -1px; }
.pv-legend .pv-dot.safe { background: #e3ddc9; border: 1px solid #c9c3ae; }
.pv-legend .pv-dot.count { background: #5b7c99; }

.pv-duel-grid { display: flex; gap: 20px; margin: 20px 0 10px; flex-wrap: wrap; }
.pv-duel-card { flex: 1; min-width: 260px; background: #fbfaf6; border: 1px solid #c9c3ae; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); overflow: hidden; }
.pv-duel-card .pv-duel-head { display: flex; align-items: center; gap: 10px; padding: 12px 18px; color: #fff; font-weight: 700; letter-spacing: 1px; }
.pv-duel-card.safe .pv-duel-head { background: #6b8e6b; }
.pv-duel-card.danger .pv-duel-head { background: #a3441e; }
.pv-duel-card .pv-duel-body { padding: 14px 18px 16px; font-size: 0.9rem; line-height: 1.8; color: #2b2b2b; }
.pv-duel-card .pv-duel-body code { background: #eef0eb; padding: 1px 6px; border-radius: 3px; color: #a3441e; }

.flow-note { background: #fbfaf6; border: 1px dashed #c9c3ae; border-left: 4px solid #b8860b; padding: 10px 18px; margin: 14px 0 20px; border-radius: 2px; font-size: 0.92rem; color: #4a4636; line-height: 1.8; }
.flow-note code { background: #eef0eb; padding: 1px 6px; border-radius: 3px; color: #a3441e; }
.flow-note.danger { background: #fbf1ee; border-color: #e0b8ab; border-left-color: #a3441e; color: #7a2e1f; }
.flow-note.danger code { background: #f3ded7; color: #8c2f1a; }
</style>

{% tabs p-value%}

<!-- tab 🪙 硬幣：離散資料的 p 值-->

假設連續擲一枚硬幣兩次，結果都出現正面，那「這枚硬幣是不是怪怪的？」但統計學一開始的預設立場恰恰相反，它會先假設「這枚硬幣跟一般正常的硬幣沒有任何不同」，這個預設假設就叫做<code>虛無假說（H0）</code>。

我們計算 `P 值` 的目的，就是為了測試這個虛無假說站不站得住腳。只有當算出來的 `P 值`「很小」時，我們才能推翻虛無假說，證明這枚硬幣真的不太一樣。

單看「連續擲兩次都正面」這件事，發生的機率是 0.25（因為總共只有正正、正反、反正、反反這四種可能）。但真正的 `P 值`並不是只看這一個數字，而是要把三種情況的機率通通加起來：

<div class="pv-row">
<div class="pv-card">
<div class="pv-icon">🪙🪙</div>
<div class="pv-value">0.25</div>
<div class="pv-label">觀測值本身<br>（兩次正面）</div>
</div>
<div class="pv-op">+</div>
<div class="pv-card">
<div class="pv-icon">🪙🪙</div>
<div class="pv-value">0.25</div>
<div class="pv-label">同等罕見<br>（兩次反面）</div>
</div>
<div class="pv-op">+</div>
<div class="pv-card">
<div class="pv-icon">➖</div>
<div class="pv-value">0</div>
<div class="pv-label">更極端情況<br>（擲兩次已無更極端）</div>
</div>
<div class="pv-op">=</div>
<div class="pv-card pv-sum">
<div class="pv-icon">🎯</div>
<div class="pv-value">0.5</div>
<div class="pv-label">最終 P 值</div>
</div>
</div>

<div class="pv-verdict keep">
<span class="pv-vicon">✅</span>
<span><code>P = 0.5</code> 大於顯著水準 <code>α = 0.05</code>，所以我們無法拒絕虛無假說——這枚硬幣連續擲出兩次正面，其實一點也不特別。</span>
</div>

**為什麼要把「同等罕見」和「更罕見」的機率都加進去？**

想像你送愛人一朵花，說它是「全世界獨一無二、沒有其他花跟它一樣罕見」，對方會覺得這朵花非常特別。但如果你補一句「其實還有別的顏色跟它一樣罕見」，或是「有很多花比這朵更罕見」，這朵花在對方心中瞬間就沒那麼特別了。

<div class="flow-note">
💡 統計學計算 <code>P 值</code>時，就是抱著同樣的邏輯：把「跟觀測結果一樣罕見」以及「比觀測結果更罕見」的所有機率全部算進去，才能嚴格檢驗這個結果在整體情境中是不是「真的夠特別」。
</div>

換一個規模更大的例子：如果連續擲 5 次硬幣，出現 4 次正面、1 次反面，這個結果特別嗎？在總共 32 種可能的結果中：

<div class="pv-row">
<div class="pv-card">
<div class="pv-icon">🪙×5</div>
<div class="pv-value">5/32</div>
<div class="pv-label">觀測值<br>（4正1反）</div>
</div>
<div class="pv-op">+</div>
<div class="pv-card">
<div class="pv-icon">🪙×5</div>
<div class="pv-value">5/32</div>
<div class="pv-label">同等罕見<br>（1正4反）</div>
</div>
<div class="pv-op">+</div>
<div class="pv-card">
<div class="pv-icon">🪙×5</div>
<div class="pv-value">2/32</div>
<div class="pv-label">更罕見<br>（全正或全反）</div>
</div>
<div class="pv-op">=</div>
<div class="pv-card pv-sum">
<div class="pv-icon">🎯</div>
<div class="pv-value">0.375</div>
<div class="pv-label">最終 P 值</div>
</div>
</div>

<div class="pv-verdict keep">
<span class="pv-vicon">✅</span>
<span><code>P = 0.375</code> 一樣大於 <code>0.05</code>，這個看似「4 勝 1 敗」有點特別的結果，在統計上依然不足以證明這枚硬幣有問題。</span>
</div>

這兩個例子告訴我們同一件事，不能只看單一結果發生的機率，必須把「跟它一樣罕見」與「比它更罕見」的所有可能性都納入考量，才能客觀判斷一件事到底特不特別

<!-- endtab -->

<!-- tab 📏 身高：連續資料的 p 值-->

從擲硬幣（一個結果一個結果數得出來）換成測量身高，因身高有無限多種可能的數值，沒辦法像硬幣那樣一一列舉出來。這時就要換一套工具，把所有可能的身高畫成一條<code>統計分佈曲線</code>，用「曲線下的面積」來代表機率，再用面積加總算出 `P 值`


**案例 A：觀測值離平均很遠**

假設某個母體的平均身高是 155.7 公分，我們量到一位身高 142 公分的女性，這個數字算不算特別？在這個分佈中，身高小於或等於 142 公分（這一側更極端）的面積佔 2.5%；而依照前面「同等或更罕見都要加總」的邏輯，另一側同樣遠離平均值（也就是身高大於或等於 169 公分）的面積 2.5% 也要一併算入。

<div class="pv-bar-card">
<div class="pv-bar-title">身高 142 公分 vs. 平均 155.7 公分</div>
<div class="pv-bar">
<div class="pv-seg count" style="width: 2.5%;"></div>
<div class="pv-seg safe" style="width: 95%;"></div>
<div class="pv-seg count" style="width: 2.5%;"></div>
</div>
<div class="pv-legend">
<span><span class="pv-dot count"></span>計入 P 值的兩側極端區域：2.5% + 2.5%</span>
<span><span class="pv-dot safe"></span>安全區（未計入）：95%</span>
</div>
</div>

<div class="pv-verdict border">
<span class="pv-vicon">⚖️</span>
<span>兩側加總 <code>P = 0.05</code>，剛好卡在顯著水準的邊界上，結果算是模稜兩可。</span>
</div>

如果觀測到的身高更矮，是 141 公分，兩側極端面積相加會變成 <code>0.016 + 0.016 = 0.03</code>。

<div class="pv-verdict reject">
<span class="pv-vicon">🚩</span>
<span><code>P = 0.03</code> 小於 <code>0.05</code>，我們可以拒絕虛無假說，這個身高很可能真的不屬於原本這個分佈。</span>
</div>

**案例 B：觀測值就在平均附近（最反直覺的一段）**

假設量到的身高落在 155.4 到 156 公分之間，剛好卡在平均值正中央。單看這個狹窄區間本身發生的機率其實不高，只有 4%——這就跟擲硬幣時某些特定組合看起來機率很低是一樣的道理。但計算 `P 值`時，還是得把「距離平均值更遠」的所有機率都算進去；而這個區間正好在正中央，代表左右兩側幾乎所有的身高數值，都比它更遠離平均值、也就是更極端。

<div class="pv-bar-card">
<div class="pv-bar-title">身高 155.4～156 公分（貼近平均值 155.7 公分）</div>
<div class="pv-bar">
<div class="pv-seg count" style="width: 48%;"></div>
<div class="pv-seg count" style="width: 4%;"></div>
<div class="pv-seg count" style="width: 48%;"></div>
</div>
<div class="pv-legend">
<span><span class="pv-dot count"></span>觀測區間本身：4%</span>
<span><span class="pv-dot count"></span>左側更極端：48%　右側更極端：48%</span>
</div>
</div>

<div class="pv-verdict keep">
<span class="pv-vicon">✅</span>
<span><code>P = 0.04 + 0.48 + 0.48 = 1.0</code>，代表整個分佈裡幾乎所有數值都「一樣罕見或更罕見」，這個結果一點也不特別，完全符合原本的分佈。</span>
</div>

這一段完美呼應了前面「送花」與「擲硬幣」的邏輯，只是把計算方式換成了曲線下的「面積」，就算某個特定區間本身機率很低（例如 4%），只要整體分佈中還存在大量比它更極端的情況，`P 值`就會因為加總這些情況而衝到接近 1。這也證明了一件事——越靠近平均值的觀測結果，在統計上反而越不特別

<!-- endtab -->

<!-- tab 💊 單尾 P 值的陷阱-->

假設藥廠正在測試一款新藥（我們姑且叫它 Super Drug），目的是想知道這款藥能不能縮短病人的恢復天數。

<div class="pv-row">
<div class="pv-card">
<div class="pv-icon">💊⚡</div>
<div class="pv-value">4.5 天</div>
<div class="pv-label">藥效很好<br>恢復大幅縮短</div>
</div>
<div class="pv-card">
<div class="pv-icon">💊⚠️</div>
<div class="pv-value">15.5 天</div>
<div class="pv-label">出現嚴重副作用<br>恢復大幅拉長</div>
</div>
</div>

同樣的新藥，可能帶來完全相反的兩種結果，讓病人好得特別快，或是讓病情變得更糟。用什麼方式檢定，會直接決定我們有沒有辦法及時發現「這款藥其實在傷害病人」

<div class="pv-duel-grid">
<div class="pv-duel-card safe">
<div class="pv-duel-head">🛡️ 雙尾檢定：兩個方向都不放過</div>
<div class="pv-duel-body">
不管新藥是讓恢復期變短還是變長，雙尾檢定都會把兩側極端的機率加總：<code>0.016 + 0.016 = 0.03</code>。<br><br>
<code>P = 0.03</code> 小於 <code>0.05</code>，成功偵測出「這款藥引發了不尋常的結果」，無論它是變好還是變壞，都逃不過雙尾檢定的眼睛
</div>
</div>
<div class="pv-duel-card danger">
<div class="pv-duel-head">⚠️ 單尾檢定：只盯著一個方向看</div>
<div class="pv-duel-body">
計算單尾 <code>P 值</code>前，必須先預設「期待的方向」。這裡我們只預期新藥會「縮短」恢復期，於是只看分佈左側（時間變短）的極端情況。<br><br>
如果藥物真的有效（4.5 天），單尾 <code>P 值</code> 是 <code>0.016</code>，看起來沒問題。<br><br>
但如果藥物其實讓病人平均要 15.5 天才能恢復，單尾檢定只會把「小於 15.5 天」這個符合預期方向的龐大面積整個加總起來，算出高達 <code>P = 0.98</code>。
</div>
</div>
</div>

<div class="flow-note danger">
☠️ <code>P = 0.98</code> 遠大於 <code>0.05</code>，單尾檢定會告訴我們「沒有發現異常」，這代表我們會完全錯過「藥物正在讓病情惡化」這個重大警訊。
</div>

這就是為什麼單尾 `P 值`一旦方向設反了或只看單一方向，它可以讓一個正在傷害病人的藥物，看起來完全風平浪靜。**除非有非常明確、無可爭議的理由只關心單一方向，否則單尾檢定應該盡量避免使用**，雙尾檢定才是比較安全、也比較誠實的預設選擇。

<!-- endtab -->

{% endtabs %}
