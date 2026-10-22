---
title: hypothesis - 新冠特效藥
date: 2026-06-28 10:04:05
categories: Statistics
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/landing.png
tags:
toc:
toc_number:
comments :
mathjax: true
---

{% tabs hypothesis%}




<!-- tab 新冠特效藥是否有效？-->

<style>
.step-banner { display: flex; align-items: center; gap: 12px; background: #f2efe4; border-left: 4px solid #3d6b66; padding: 10px 18px; margin: 0 0 20px; border-radius: 2px; }
.step-banner .step-tag { font-family: 'Courier New', Consolas, monospace; font-size: 0.72rem; font-weight: 700; color: #fbfaf6; background: #3d6b66; border-radius: 2px; padding: 3px 10px; flex-shrink: 0; letter-spacing: 1px; }
.step-banner .step-title { font-weight: 700; color: #2f4f4f; font-size: 0.98rem; letter-spacing: 0.5px; }
.step-banner.warn { border-left-color: #b8860b; }
.step-banner.warn .step-tag { background: #b8860b; }
.step-banner.done { border-left-color: #4f7942; }
.step-banner.done .step-tag { background: #4f7942; }

.flow-note {
  background: #fbfaf6; border: 1px dashed #c9c3ae; border-left: 4px solid #b8860b;
  padding: 10px 18px; margin: 14px 0 20px; border-radius: 2px;
  font-size: 0.92rem; color: #4a4636; line-height: 1.8;
}
.flow-note code { background: #eef0eb; padding: 1px 6px; border-radius: 3px; color: #a3441e; }
.flow-note.done { background: #f4f8f1; border-color: #b9d1a8; border-left-color: #4f7942; color: #33502b; }
.flow-note.done code { background: #e6efdf; color: #3d6220; }

.flow-table-wrap { margin: 12px 0 24px; border: 1px solid #c9c3ae; border-radius: 2px; overflow: hidden; display: inline-block; max-width: 100%; }
.flow-table-wrap table { width: auto; border-collapse: collapse; font-size: 0.86rem; margin: 0 !important; }
.flow-table-wrap th { background: #2f4f4f; color: #fbfaf6; padding: 9px 12px; text-align: left; font-weight: 600; letter-spacing: 0.5px; }
.flow-table-wrap td { padding: 9px 12px; border-top: 1px solid #e3ddc9; vertical-align: top; color: #2b2b2b; }
.flow-table-wrap tr:nth-child(even) td { background: #f7f5ec; }
.flow-table-wrap td code, .flow-table-wrap th code { background: #eef0eb; padding: 1px 6px; border-radius: 3px; color: #a3441e; font-size: 0.85em; }
</style>

<div class="step-banner">
<span class="step-tag">STEP 1</span>
<span class="step-title">新冠特效藥是否有效？</span>
</div>

假設某製藥公司研發了一款新冠病毒特效藥，目前已進入臨床試驗。

**已知條件：**

<div class="flow-table-wrap">
<table>
<tr><th>項目</th><th>數值</th></tr>
<tr><td>新冠患者自然痊癒的平均時間（母體平均數）</td><td>$\mu_0 = 72$ 小時</td></tr>
<tr><td>母體標準差</td><td>$\sigma = 8$ 小時</td></tr>
<tr><td>臨床試驗樣本數</td><td>$n = 100$</td></tr>
<tr><td>樣本平均痊癒時間</td><td>$\bar{x} = 69.6$ 小時</td></tr>
</table>
</div>

**問題：這款藥物是否真的有效？**


<!-- endtab -->



<!-- tab 建立假設-->

<div class="step-banner">
<span class="step-tag">STEP 2</span>
<span class="step-title">建立假設</span>
</div>

**虛無假設（$H_0$）：** 藥物無效，平均痊癒時間仍然是 72 小時。

$$H_0 : \mu = 72$$

**對立假設（$H_a$）：** 藥物有效，平均痊癒時間不是 72 小時。

$$H_a : \mu \neq 72$$

如果研究目的明確是「縮短痊癒時間」，也可以設定為**單尾檢定**：$H_a : \mu < 72$

<div class="flow-note">
💡 <strong>什麼是單尾檢定（One-tailed Test）？</strong>
單尾檢定是指對立假設只關心<strong>單一方向</strong>的差異，例如「比較小」或「比較大」，而不是「不一樣就好」。
<ul>
<li><strong>雙尾檢定（Two-tailed Test）</strong>：$H_a : \mu \neq 72$，只在意平均痊癒時間<strong>有沒有改變</strong>，不管是變快還是變慢，兩邊都算異常。</li>
<li><strong>單尾檢定（One-tailed Test）</strong>：$H_a : \mu < 72$，只在意平均痊癒時間<strong>是否縮短</strong>。如果藥物讓病人好得更慢（$\mu > 72$），對研究目的來說沒有意義，因此不列入考慮範圍。</li>
</ul>
實務上的差別在於「極端值」怎麼算：
<table>
<tr><th>檢定方式</th><th>極端結果的定義</th><th>P 值計算</th></tr>
<tr><td>雙尾</td><td>比 $\bar{x}$ 更遠離 72（不論偏左或偏右）</td><td>左右兩側機率相加</td></tr>
<tr><td>單尾</td><td>只看比 $\bar{x}$ 更小（偏向研究關心的方向）</td><td>只計算單一側的機率</td></tr>
</table>
因為單尾檢定只看一側，同樣的顯著水準 $\alpha$ 下，<strong>單尾檢定比雙尾檢定更容易拒絕 $H_0$</strong>（P 值只有雙尾的一半，見下一段落的比較）。但前提是研究者必須<strong>在看到資料之前</strong>就有充分理由只關心某一個方向，不能為了讓結果「看起來顯著」而事後改用單尾檢定。
</div>

<!-- endtab -->



<!-- tab 假設 $H_0$ 成立，建立抽樣分布-->

<div class="step-banner">
<span class="step-tag">STEP 3</span>
<span class="step-title">假設 $H_0$ 成立，建立抽樣分布</span>
</div>

假設藥物真的沒有作用，即 $\mu = 72$。

在此前提下，樣本平均數的標準誤為：

$$SE = \frac{\sigma}{\sqrt{n}} = \frac{8}{\sqrt{100}} = 0.8 \text{ 小時}$$

意思是：如果藥物真的沒有效果，重複抽 100 位病患做臨床試驗很多次，每次算出來的樣本平均痊癒時間，大約會在 72 小時上下**波動 0.8 小時**左右。

因此，抽樣分布為：

$$\bar{X} \sim N(72,\ 0.8)$$



<div class="flow-note">
💡 <strong>什麼是標準誤（Standard Error）？</strong>
如果我們重複抽樣很多次，每次都算出一個「樣本平均數」，這些樣本平均數彼此之間<strong>會差多少</strong>。
<ul>
<li>母體標準差 $\sigma$ 描述的是<strong>個別數值</strong>（例如每個病患的痊癒時間）跟母體平均數之間的差異程度。</li>
<li>標準誤 $SE$ 描述的是<strong>樣本平均數</strong>（不是個別數值）跟母體平均數之間的差異程度。</li>
</ul>
因為樣本平均數是很多人的數值平均出來的，極端值會互相抵消，所以樣本平均數的波動會比個別數值小很多；樣本數 $n$ 越大，平均效果越明顯，標準誤就越小，也就是樣本平均數會越穩定、越貼近母體平均數。
</div>

<div class="flow-note">
💡 <strong>為什麼公式是 $\sigma$ 除以 $\sqrt{n}$？</strong>
樣本平均數其實就是把 $n$ 個獨立觀測值加總後除以 $n$：

$$\bar{X} = \frac{X_1 + X_2 + \dots + X_n}{n}$$

<ul>
<li><strong>變異數可以直接相加</strong>：每個 $X_i$ 互相獨立，變異數都是 $\sigma^2$，加總後的變異數是 $n\sigma^2$。</li>
<li><strong>除以常數要平方</strong>：$\bar{X}$ 是總和除以 $n$，而變異數的縮放規則是除以常數的<strong>平方</strong>，所以 $\text{Var}(\bar{X}) = \dfrac{n\sigma^2}{n^2} = \dfrac{\sigma^2}{n}$。</li>
<li><strong>開根號還原成標準差</strong>：$SE = \sqrt{\dfrac{\sigma^2}{n}} = \dfrac{\sigma}{\sqrt{n}}$。</li>
</ul>
直觀理解：$n$ 個獨立誤差有正有負，加總後不會單純線性放大，而是以 $\sqrt{n}$ 的速度成長；但分母是除以 $n$，兩者相除只剩下 $\dfrac{1}{\sqrt{n}}$ 的縮小效果。這也是為什麼樣本數要變成 4 倍，標準誤才會縮小成一半，而不是等比例縮小。
</div>

<div class="flow-note">
💡 <strong>補充：為什麼「獨立變數的變異數可以直接相加」？</strong>
以兩個獨立變數 $X_1, X_2$（平均數分別是 $\mu_1, \mu_2$）為例，令 $S = X_1 + X_2$，變異數的定義是 $\text{Var}(X) = E[(X-\mu)^2]$，代入展開：

$$\text{Var}(S) = E\big[((X_1-\mu_1)+(X_2-\mu_2))^2\big]$$

利用 $(a+b)^2 = a^2+2ab+b^2$ 展開：

$$= \text{Var}(X_1) + 2\,\underbrace{E[(X_1-\mu_1)(X_2-\mu_2)]}_{\text{Cov}(X_1,X_2)} + \text{Var}(X_2)$$

<strong>關鍵在中間的交叉項</strong> $\text{Cov}(X_1,X_2)$（共變異數），代表兩個變數是否會一起偏高或偏低：
<ul>
<li>如果 $X_1, X_2$ <strong>互相獨立</strong>，$X_1$ 偏離平均數的方向跟 $X_2$ 完全無關，有時同向、有時反向，長期平均下來會<strong>剛好抵消成 0</strong>，即 $\text{Cov}(X_1,X_2)=0$。</li>
<li>交叉項消失後，只剩下 $\text{Var}(S) = \text{Var}(X_1)+\text{Var}(X_2)$。</li>
</ul>
把同樣的邏輯推廣到 $n$ 個獨立變數，展開後所有交叉項在獨立假設下都是 0，只留下每個變數自己的變異數：

$$\text{Var}(X_1+\dots+X_n) = \text{Var}(X_1)+\dots+\text{Var}(X_n)$$

<strong>為什麼每個 $X_i$ 的變異數都是 $\sigma^2$？</strong> 因為 $X_1,\dots,X_n$（每位受試者的痊癒時間）都是從<strong>同一個母體</strong>隨機抽出來的觀測值，各自服從同樣的母體分布，因此都擁有母體的平均數 $\mu$ 與變異數 $\sigma^2$。所以：

$$\text{Var}(X_1+\dots+X_n) = \underbrace{\sigma^2+\dots+\sigma^2}_{n\ 項} = n\sigma^2$$

直觀理解：若變數不獨立（例如同一批病患互相影響病情），偏差可能會「同向疊加」而非「隨機抵消」，變異數就會大於 $n\sigma^2$。獨立性正是保證波動能互相抵消、讓標準誤只以 $\sqrt{n}$ 成長的數學根源。
</div>

<!-- endtab -->



<!-- tab 計算 Z 分數-->

<div class="step-banner">
<span class="step-tag">STEP 4</span>
<span class="step-title">計算 Z 分數</span>
</div>

臨床試驗得到 $\bar{x} = 69.6$，比預期的 72 小時少了：

$$72 - 69.6 = 2.4 \text{ 小時}$$

換算成 Z 分數：

$$Z = \frac{\bar{x} - \mu_0}{SE} = \frac{69.6 - 72}{0.8} = -3$$

代表樣本平均比預期低了 **3 個標準誤**。

<div class="flow-note">
💡 <strong>什麼是 Z 分數（Z-score）？</strong>
Z 分數是一種<strong>共通的度量單位</strong>，把「原本的差距（小時）」換算成「差了幾個標準誤」，方便判斷這個差距到底算不算大。

$$Z = \frac{\text{觀察值} - \text{期望值}}{\text{標準誤}}$$

<ul>
<li>分子 $\bar{x} - \mu_0 = -2.4$：樣本平均數跟「藥物無效」時預期的平均數，差了幾小時。</li>
<li>分母 $SE = 0.8$：如果藥物真的無效，樣本平均數本來就會有的自然波動幅度。</li>
<li>兩者相除，就是把「差了 2.4 小時」換算成「差了幾個波動單位」。</li>
</ul>
這裡算出 $Z = -3$，代表這次觀察到的樣本平均數，比「藥物無效」的預期值<strong>低了 3 個標準誤</strong>。根據常態分布的特性，樣本平均數落在 ±3 個標準誤之外是非常罕見的情況（機率不到 1%），因此這個結果相當不尋常，暗示藥物無效的假設可能站不住腳——這也是下一步計算 P 值的基礎。
</div>

<!-- endtab -->



<!-- tab 計算 P 值（P-value）-->

<div class="step-banner warn">
<span class="step-tag">STEP 5</span>
<span class="step-title">計算 P 值（P-value）</span>
</div>

若 $H_0$ 為真，觀察到 $\bar{x} = 69.6$ 或更極端結果的機率約為

<div class="flow-table-wrap">
<table>
<tr><th>檢定方式</th><th>P 值</th></tr>
<tr><td>單尾（$\mu < 72$）</td><td>約 $0.135\%$</td></tr>
<tr><td>雙尾（$\mu \neq 72$）</td><td>約 $0.27\%$（≈ $0.3\%$）</td></tr>
</table>
</div>

$$P \approx 0.003$$

<div class="flow-note">
💡 <strong>P 值是怎麼算出來的？</strong>
關鍵在於前一步算出的 <strong>Z 分數</strong>：$Z = -3$。P 值是拿這個 Z 分數去查「標準常態分布表」（或用電腦計算常態分布的累積機率），查出「Z 分數落在這個值以外」的機率有多少。

<ol>
<li><strong>查表得到單尾機率</strong>：查標準常態分布表可以知道，$Z \leq -3$（也就是樣本平均數比預期低 3 個標準誤以上）發生的機率大約是 $0.135\%$。這代表：如果藥物真的沒效，重複做很多次臨床試驗，大概每 1000 次裡只有 1.35 次會偶然出現「比預期低 3 個標準誤」這麼誇張的結果。</li>
<li><strong>雙尾再乘以 2</strong>：因為常態分布左右對稱，雙尾檢定同時把「太低」和「太高」都算成異常，所以要把單尾的機率乘以 2：$0.135\% \times 2 = 0.27\% \approx 0.3\%$。</li>
</ol>

白話理解：Z 分數告訴我們「這次結果偏離預期多遠」，P 值則是把這個「偏離程度」翻譯成「機率有多小」。<strong>Z 分數絕對值越大 → 查表得到的 P 值就越小 → 代表這個結果越不可能是巧合</strong>，也就越有理由懷疑 $H_0$（藥物無效）不成立。
</div>

<!-- endtab -->



<!-- tab 與顯著水準比較-->

<div class="step-banner done">
<span class="step-tag">STEP 6</span>
<span class="step-title">與顯著水準比較</span>
</div>

研究人員事先設定：

- **信心水準（Confidence Level）**：$99.5\%$
- **顯著水準（Significance Level）**：$\alpha = 0.5\% = 0.005$

<div class="flow-note">
💡 <strong>信心水準是什麼？</strong>
信心水準代表「我們願意有多確定，才要下判斷」，是研究人員事先設定的<strong>容錯標準</strong>。
白話舉例：如果信心水準設為 $99.5\%$，代表我們要求「就算重複做這個實驗很多次，也只允許最多 $0.5\%$ 的機率誤判（把沒效的藥當成有效）」。信心水準越高，代表我們對結論越謹慎、越不容易誤判。
兩者的關係很簡單：

$$\text{信心水準} + \alpha（顯著水準） = 100\%$$

也就是說，信心水準 $99.5\%$ 對應的顯著水準就是 $\alpha = 100\% - 99.5\% = 0.5\%$。之後我們就是拿計算出來的 P 值，跟這個 $\alpha$ 做比較，決定要不要拒絕 $H_0$。
</div>

因為

$$P = 0.003 < \alpha = 0.005$$

結論：**拒絕 $H_0$（Reject $H_0$）**

<div class="flow-note done">
✅ 在藥物無效的前提下，出現這樣的結果只有約 <strong>0.3%</strong> 的機率，因此有足夠證據認為藥物確實產生了效果。
</div>

<!-- endtab -->



<!-- tab 如何正確解讀 P 值？-->

<div class="step-banner">
<span class="step-tag">STEP 7</span>
<span class="step-title">如何正確解讀 P 值？</span>
</div>

<div class="flow-note">
假設藥物根本沒有效（$H_0$ 成立），卻仍然觀察到平均痊癒時間只有 $69.6$ 小時（或更極端）的機率只有約 <strong>0.3%</strong>。
</div>

因此，這個結果太不尋常了，不太可能只是隨機抽樣造成，所以**拒絕 $H_0$**。


<!-- endtab -->



{% endtabs %}