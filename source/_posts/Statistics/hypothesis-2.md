---
title: hypothesis - 國旅太貴 vs 出國旅遊
date: 2026-06-28 10:04:05
categories: Statistics
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/hypothesis-1/flight-landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/hypothesis-1/flight-landing.png
tags:
toc:
toc_number:
comments :
mathjax: true
---

{% tabs hypothesis%}

<!-- tab 直覺的推論-->

<style>
.bp-navy { background: #0b3d59; }
.bp-card { background: #fdfbf3; border: 2px solid #0b3d59; border-radius: 6px; box-shadow: 0 3px 8px rgba(11,61,89,0.15); position: relative; overflow: hidden; margin: 20px 0; }
.bp-livery { height: 6px; background: repeating-linear-gradient(45deg, #d9662c, #d9662c 10px, #0b3d59 10px, #0b3d59 20px); }
.bp-head { display: flex; justify-content: space-between; align-items: center; padding: 10px 18px; background: #0b3d59; color: #fdfbf3; }
.bp-head .bp-route { font-family: 'Courier New', Consolas, monospace; font-weight: 700; font-size: 1.05rem; letter-spacing: 2px; display: flex; align-items: center; gap: 8px; }
.bp-head .bp-route .bp-plane { color: #f2a15c; }
.bp-head .bp-label { font-size: 0.65rem; letter-spacing: 1.5px; opacity: 0.85; text-transform: uppercase; }
.bp-body { padding: 14px 18px 6px; font-size: 0.9rem; line-height: 1.85; color: #2b2b2b; }
.bp-perf { border-top: 2px dashed #c9c3ae; margin: 10px 18px 0; position: relative; }
.bp-perf .bp-scissor { position: absolute; left: -6px; top: -9px; font-size: 0.75rem; color: #9a927a; background: #fdfbf3; padding: 0 2px; }
.bp-footer { display: flex; justify-content: space-between; padding: 8px 18px 12px; margin-top: 4px; border-top: 1px dashed #d8d3c2; font-family: 'Courier New', Consolas, monospace; font-size: 0.62rem; color: #8a8272; letter-spacing: 1.5px; text-transform: uppercase; }
.tag-note { background: #fdfbf3; border: 2px dashed #0b3d59; border-radius: 4px 14px 14px 4px; padding: 10px 18px 10px 38px; margin: 18px 0 22px; position: relative; font-size: 0.9rem; color: #2b3a42; line-height: 1.8; }
.tag-note::before { content: '🏷️'; position: absolute; left: 8px; top: 9px; font-size: 1rem; }
.tag-note.warn { border-color: #d99a3d; background: #fdf6ea; }
.tag-note.danger { border-color: #c0503a; background: #fbeee8; }
.tag-note code { background: #eaf4fa; padding: 1px 6px; border-radius: 3px; color: #d9662c; }
.tv-itinerary { margin: 12px 0 24px; border: 2px solid #0b3d59; border-radius: 4px; overflow: hidden; display: inline-block; max-width: 100%; }
.tv-itinerary table { width: auto; border-collapse: collapse; font-size: 0.86rem; margin: 0 !important; font-family: 'Courier New', Consolas, monospace; }
.tv-itinerary th { background: #0b3d59; color: #fdfbf3; padding: 9px 12px; text-align: left; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; font-size: 0.78rem; }
.tv-itinerary td { padding: 9px 12px; border-top: 1px dashed #d8d3c2; vertical-align: top; color: #2b3a42; }
.tv-itinerary tr:nth-child(even) td { background: #f7f3e6; }
.bp-grid { display: flex; gap: 20px; margin: 20px 0 24px; flex-wrap: wrap; }
.bp-grid .bp-card { flex: 1; min-width: 260px; margin: 0; }
.bp-card.h1 .bp-head { background: #d9662c; }
.bp-card.h1 .bp-livery { background: repeating-linear-gradient(45deg, #0b3d59, #0b3d59 10px, #d9662c 10px, #d9662c 20px); }
.stamp { display: inline-block; border: 3px double; border-radius: 8px; padding: 3px 12px; font-weight: 800; letter-spacing: 2px; transform: rotate(-6deg); font-family: 'Courier New', Consolas, monospace; text-transform: uppercase; font-size: 0.78rem; margin-bottom: 8px; }
.stamp.approve { color: #2f7a4f; border-color: #2f7a4f; }
.stamp.reject { color: #c0392b; border-color: #c0392b; }
.flight-path { position: relative; margin: 22px 0 30px; padding-left: 40px; }
.flight-path::before { content: ''; position: absolute; left: 11px; top: 6px; bottom: 6px; width: 2px; background: repeating-linear-gradient(180deg, #cfe0e8 0 8px, transparent 8px 16px); }
.fp-leg { position: relative; margin-bottom: 18px; }
.fp-leg:last-child { margin-bottom: 0; }
.fp-leg::before { content: '✈'; position: absolute; left: -38px; top: 0; width: 22px; height: 22px; border-radius: 50%; background: #0b3d59; color: #fdfbf3; font-size: 0.75rem; display: flex; align-items: center; justify-content: center; transform: rotate(90deg); }
.fp-leg.warn::before { background: #d99a3d; }
.fp-leg.done::before { background: #2f7a4f; }
.fp-leg .fp-card { background: #fdfbf3; border: 1px solid #d8d3c2; border-radius: 4px; padding: 8px 16px; }
.fp-leg.warn .fp-card { border-left: 3px solid #d99a3d; }
.fp-leg.done .fp-card { border-left: 3px solid #2f7a4f; }
.fp-title { font-weight: 700; color: #0b3d59; font-size: 0.92rem; }
.fp-desc { font-size: 0.86rem; color: #2b3a42; margin-top: 4px; line-height: 1.7; }
.gate-flow { margin: 18px 0 26px; }
.gate-row { display: flex; align-items: center; gap: 12px; background: #fdfbf3; border: 1px solid #d8d3c2; border-radius: 4px; padding: 8px 16px; margin-bottom: 6px; font-size: 0.88rem; color: #2b3a42; font-family: 'Courier New', Consolas, monospace; }
.gate-row .gate-tag { font-weight: 700; color: #fdfbf3; background: #0b3d59; border-radius: 3px; padding: 2px 8px; flex-shrink: 0; font-size: 0.72rem; letter-spacing: 1px; }
.gate-arrow { text-align: center; color: #cfe0e8; font-size: 0.9rem; margin: -2px 0; }
</style>

<div class="bp-card">
<div class="bp-livery"></div>
<div class="bp-head">
<span class="bp-route"><span class="bp-plane">✈</span>國旅<span class="bp-plane">→</span>出國</span>
<span class="bp-label">Boarding · 因果推論</span>
</div>
<div class="bp-body">
很多人看到「近年出國旅遊的人變多了，而且國旅住宿很貴」，就直接下結論：「因為國旅太貴，所以大家都跑去出國。」這是一個很好的「<code>因果推論（Causal Inference）</code>」案例，但從科學角度，這個結論還不能成立——因為我們只看到了「相關（correlation）」，並沒有證明「因果（causation）」。這張登機證，還不能直接放行登機。
</div>
</div>

<!-- endtab -->

<!-- tab 第一步：先提出假設-->

要檢驗這個說法是否成立，第一步是把直覺的猜測，轉換成兩張可以被檢定的「假設」

<div class="bp-grid">

<div class="bp-card">
<div class="bp-livery"></div>
<div class="bp-head"><span class="bp-route">GATE H0</span><span class="bp-label">虛無假設</span></div>
<div class="bp-body">國旅住宿價格，不會影響民眾是否選擇出國。</div>
<div class="bp-footer"><span>候補中</span><span>PENDING</span></div>
</div>

<div class="bp-card h1">
<div class="bp-livery"></div>
<div class="bp-head"><span class="bp-route">GATE H1</span><span class="bp-label">研究假設</span></div>
<div class="bp-body">國旅住宿越貴，民眾越傾向出國。</div>
<div class="bp-footer"><span>候補中</span><span>PENDING</span></div>
</div>

</div>

<!-- endtab -->

<!-- tab 第二步：蒐集資料-->

有了假設後，接下來要蒐集實際資料來檢驗。例如蒐集最近十年的「出入境紀錄」：

<div class="tv-itinerary">

| 年份 | 國旅住宿均價 | 出國人次 |
|:---|---:|---:|
| 2016 | 2500 | 1200萬 |
| 2017 | 2600 | 1300萬 |
| 2018 | 2800 | 1450萬 |
| 2019 | 3200 | 1700萬 |

</div>

如果只看到「房價上升、出國也上升」，只能說兩者<code>有相關</code>，還不能說誰造成誰，這張行程表本身，還不足以當作相關證據

<!-- endtab -->

<!-- tab 第三步：排除其他可能原因-->

因為還有很多變數也可能影響出國意願，不能一看到相關就直接歸因給住宿價格。這些都是可能同時影響「出國登機率」的隨機因素

<div class="gate-flow">
<div class="gate-row"><span class="gate-tag">FACTOR</span>機票變便宜</div>
<div class="gate-row"><span class="gate-tag">FACTOR</span>廉價航空增加</div>
<div class="gate-row"><span class="gate-tag">FACTOR</span>匯率改善</div>
<div class="gate-row"><span class="gate-tag">FACTOR</span>疫情解封</div>
<div class="gate-row"><span class="gate-tag">FACTOR</span>薪資提高</div>
<div class="gate-row"><span class="gate-tag">FACTOR</span>特休增加</div>
<div class="gate-row"><span class="gate-tag">FACTOR</span>日本匯率大跌</div>
</div>

<div class="tag-note warn">
💡 舉例來說：如果日本旅遊突然便宜 30%，即使國旅住宿完全沒漲，大家仍然可能大量跑去日本。所以不能直接怪住宿太貴。
</div>

<!-- endtab -->

<!-- tab 第四步：建立統計模型-->

排除了直覺的干擾因素後，下一步是用統計模型同時控制這些變數，看看國旅房價是否還有獨立的影響力。例如做多元迴歸（<code>Multiple Regression</code>）：

$$
出國人數 = \beta_0 + \beta_1(國旅房價) + \beta_2(機票價格) + \beta_3(匯率) + \beta_4(平均薪資) + \cdots
$$


如果控制其他因素後，國旅房價仍然有顯著影響，而且 <code>p-value &lt; 0.05</code> 且 <code>β1 &gt; 0</code>，就可以說在控制其他因素後，國旅房價越高，出國比例確實越高


<div class="tag-note warn">
⚠ 注意這仍然只是「有證據支持影響」，而不是絕對證明因果關係
</div>

<!-- endtab -->

<!-- tab 第五步：最好找到自然實驗（Natural Experiment）-->

比起單純做迴歸，找到一個「自然實驗」情境會更有說服力，也就是現實中剛好出現了近似對照組的情況，像追蹤兩班平行航班的乘客動向

<div class="flight-path">

<div class="fp-leg">
<div class="fp-card">
<div class="fp-title">情境設定</div>
<div class="fp-desc">某一年，只有某些縣市因大型活動導致住宿價格暴漲，其他縣市價格維持平穩。</div>
</div>
</div>

<div class="fp-leg warn">
<div class="fp-card">
<div class="fp-title">比較兩組</div>
<div class="fp-desc">拿「房價暴漲的縣市」和「房價沒有漲的縣市」對照，觀察居民出國比例是否有明顯不同。</div>
</div>
</div>

<div class="fp-leg done">
<div class="fp-card">
<div class="fp-title">推論因果</div>
<div class="fp-desc">如果只有房價暴漲的地方，居民出國率也跟著一起上升，就更接近「房價真的造成了出國」這個因果推論。</div>
</div>
</div>

</div>

<!-- endtab -->

<!-- tab 第六步：最強的證據——直接問旅客-->

最直接的做法，就是跳過推論、直接問旅客本人。例如在機場出境大廳調查一萬位旅客：「今年沒有國旅的主要原因？」結果如下

<div class="tv-itinerary">

| 原因 | 比例 |
|:---|---:|
| 住宿太貴 | 52% |
| 想出國 | 18% |
| 國內景點玩膩 | 10% |
| 交通問題 | 8% |
| 其他 | 12% |

</div>

<div class="tag-note">
如果超過一半的人都直接回答「住宿太貴」，那就是非常直接的證據，不需要再繞一大圈統計模型推論
</div>

<!-- endtab -->

<!-- tab 這裡的 p value 是什麼-->

這裡的 <code>p-value</code> 資料是「旅遊行為」。假設我們做了一份大型調查，訪問了 10,000 個人，並把人分成兩組來比較

<div class="tv-itinerary">

| 住宿感受 | 出國 | 沒出國 | 總計 |
|:---|---:|---:|---:|
| 覺得很貴 | 4200 | 1800 | 6000 |
| 覺得不貴 | 1800 | 2200 | 4000 |

</div>

可以看到，覺得住宿很貴的人有 70% 出國，覺得住宿不貴的人只有 45% 出國，看起來差很多。
但問題來了：這 70% 和 45% 的差距，是真的因為住宿價格嗎？還是只是剛好抽到這 10,000 人運氣不好？

<div class="bp-grid">

<div class="bp-card">
<div class="bp-livery"></div>
<div class="bp-head"><span class="bp-route">STEP 1</span><span class="bp-label">先建立假設</span></div>
<div class="bp-body">H0（虛無假設）：住宿價格其實跟出不出國沒有關係。意思是真正母體裡，兩組出國比例其實是一樣的，只是抽樣時剛好抽到 70% 和 45%。</div>
<div class="bp-footer"><span>基準艙</span><span>BASELINE</span></div>
</div>

<div class="bp-card h1">
<div class="bp-livery"></div>
<div class="bp-head"><span class="bp-route">STEP 2</span><span class="bp-label">p-value 回答什麼</span></div>
<div class="bp-body">如果 H0 是真的（住宿價格完全沒有影響），那麼像現在看到這麼大的差距（70% vs 45%），純粹因為抽樣誤差而發生的機率有多大？</div>
<div class="bp-footer"><span>檢查中</span><span>CHECKING</span></div>
</div>

</div>

拿兩種計算結果來對照，就能看出 p-value 怎麼影響我們最終「放行」還是「攔下」這個假設：

<div class="bp-grid">

<div class="bp-card">
<div class="bp-livery"></div>
<div class="bp-head"><span class="bp-route">p = 0.18</span><span class="bp-label">抽樣運氣範圍內</span></div>
<div class="bp-body">
<span class="stamp approve">正常登機</span><br>
如果住宿價格根本沒有影響，還看到現在這麼大的差距，有 18% 的機率只是抽樣運氣造成。18% 不算罕見，因此<code>不能拒絕 H0</code>。
</div>
<div class="bp-footer"><span>H0 保留</span><span>KEEP</span></div>
</div>

<div class="bp-card h1">
<div class="bp-livery"></div>
<div class="bp-head"><span class="bp-route">p = 0.002</span><span class="bp-label">極端罕見</span></div>
<div class="bp-body">
<span class="stamp reject">登機門關閉</span><br>
如果住宿價格真的沒有影響，卻還抽到 70% vs 45% 這種差距，只有 0.2% 的機率會發生。這非常罕見，因此我們會想「既然這麼罕見，也許 H0 根本不是真的」，於是<code>拒絕 H0</code>。
</div>
<div class="bp-footer"><span>H0 出局</span><span>REJECT</span></div>
</div>

</div>

<div class="tag-note danger">
⚠ 但要注意一件更重要的事：即使最後算出 <code>p &lt; 0.001</code>，我們也不能直接說「住宿太貴導致大家出國」。這個檢定只能告訴我們「住宿價格」和「是否出國」之間存在統計上顯著的關聯，並沒有排除其他可能因素，例如：常出國的人本來就比較容易覺得國旅住宿貴、收入較高的人既願意出國也對國旅價格更敏感、廉價航空與匯率與疫情解封等因素同時影響了出國意願。因此，p-value 是判斷「這個關聯是否可能只是巧合」的工具，不是判斷「因果」的工具。
</div>

<!-- endtab -->

<!-- tab p-value 會怎麼算-->

真正數學上可利用統計分布來計算。像這個例子通常會用「兩比例 z 檢定（<code>Two-proportion z-test</code>）」或「卡方檢定（<code>Chi-square test</code>）」。整體計算流程，就像一段航班的登機報到流程

<div class="gate-flow">

<div class="gate-row"><span class="gate-tag">CHECK-IN</span>先算 70% 和 50% 差多少</div>
<div class="gate-arrow">↓</div>
<div class="gate-row"><span class="gate-tag">SECURITY</span>再算抽樣本來應該有多少誤差（標準誤）</div>
<div class="gate-arrow">↓</div>
<div class="gate-row"><span class="gate-tag">BOARDING</span>把差距除以標準誤，得到 <code>z = 4.3</code></div>
<div class="gate-arrow">↓</div>
<div class="gate-row"><span class="gate-tag">TAKEOFF</span>再去查常態分布，得到 <code>p = 0.00002</code></div>

</div>

你可以把它想成：<code>差距 ÷ 抽樣本來就會有的誤差 = z 值</code>。

<div class="bp-grid">

<div class="bp-card">
<div class="bp-livery"></div>
<div class="bp-head"><span class="bp-route">z 很小</span><span class="bp-label">差距只有一點點</span></div>
<div class="bp-body"><span class="stamp approve">正常登機</span><br>p 很大，代表這個差距只是抽樣誤差造成的。</div>
<div class="bp-footer"><span>H0 保留</span><span>KEEP</span></div>
</div>

<div class="bp-card h1">
<div class="bp-livery"></div>
<div class="bp-head"><span class="bp-route">z 很大</span><span class="bp-label">差距遠大於誤差</span></div>
<div class="bp-body"><span class="stamp reject">登機門關閉</span><br>p 很小，代表這個差距不像只是抽樣造成的。</div>
<div class="bp-footer"><span>H0 出局</span><span>REJECT</span></div>
</div>

</div>

<!-- endtab -->

{% endtabs %}
