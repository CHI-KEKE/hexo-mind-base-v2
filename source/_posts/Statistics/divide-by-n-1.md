---
title: Why Dividing by N Underestimates Variance
date: 2026-06-17 16:45:05
categories: Statistics
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/landing.png
tags:
toc:
toc_number:
comments :
mathjax: true
---

{% tabs Why Dividing by N Underestimates Variance%}

<!-- tab 變異數-->


**變異數**在算什麼？它在算「**資料點與平均值之間的距離平方的平均**」。資料點離平均值越遠，變異數越大；離得越近，變異數越小


我們真正想知道的是全部資料圍繞在「母體平均數」周圍的變異程度。但現實中幾乎沒有足夠的時間與金錢去測量母體中的每一個個體，所以必須用抽樣資料來**估計**母體的變異數。



## 公式的兩個版本

理想上，真正的母體變異數是用**母體平均數 $\mu$** 計算的：

> 母體變異數 $\sigma^2 = \dfrac{\sum (x - \mu)^2}{N}$

但現實中我們只有樣本，只能算出**樣本平均數 $\bar{x}$**，並用它代替 $\mu$：

```text
樣本資料

0        10        20        30        40
|---------|---------|---------|---------|
   ●          ●    ●     ●      ●
   4         14   18    24     30

                 ↑
          樣本平均數 x̄ = 17.6

每個樣本點到 x̄ 的距離：
  4  ──────────→ 17.6
 14  ────→        17.6
 18       ←──     17.6
 24       ←────   17.6
 30       ←──────────  17.6
```


## 為什麼分母要用 n−1？

課堂上會發現，母體變異數與樣本變異數在分母有所差異：

> $\dfrac{\sum (x - \bar{x})^2}{n}$ **＜** $\dfrac{\sum (x - \bar{x})^2}{n-1}$

除以 $n-1$ 是在**補償**一個系統性偏差：我們計算的是「樣本點到 $\bar{x}$ 的距離」，而不是「樣本點到真正母體平均數 $\mu$ 的距離」。由於 $\bar{x}$ 是這批樣本自己算出來的，它天生會偏向這批樣本，導致平方距離總和偏小。用 $n-1$ 可以把估計值拉回來


但「**一定會偏小**」嗎？偏小的原因是什麼？為什麼剛好是 $n-1$？


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/1-variances.png)

<!-- endtab -->

<!-- tab 「樣本平均數」會讓距離看起來最短-->

這是最重要的一點！數學上可以證明：對於任何一組抽樣資料，「樣本平均數」剛好會讓所有資料點的距離平方和「**最小**」。換句話說，不管你拿什麼數字當中心點，用樣本平均數算出來的結果，永遠是所有選擇裡最小的


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/2-only-do-withxbar.png)



## Step 1｜設定一個「未知的中心點 V」

先假裝不知道用誰當中心點算出來的距離最小，設定一個未知數值 $V$。

我們的問題是：

> $V$ 要是多少，才能讓 $\dfrac{\sum(X - V)^2}{n}$ 的值最小？


## Step 2｜畫出 U 型曲線，尋找「谷底」

把各種不同的 $V$ 值代入，把對應的變異數畫在圖表上，會形成一條 U 型曲線

例如
```text

0        10        20        30        40
|---------|---------|---------|---------|
  ●          ●    ●     ●   ●
  4         14   18    24  29


Variance
400 | ●
300 |
250 |     ●
200 |
136 |          ●
100 |              ●  ● ● ●      ●
  0 +--------------------------------
     0     5    10    15 20   25   40
```


- **U 型曲線的最底端**＝ 變異數最小的地方
- 在數學裡，谷底的特徵是**斜率為零**（因為谷底是平的）



![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/3-lowest-point.png)


## Step 3｜用微積分找「斜率為零」的點

現在我們的問題是當 $V$ 改變時，這整個值會怎麼變？這就是「對 $V$ 求導」


#### 3-1｜把 $\frac{1}{n}$ 提到外面

$\frac{1}{n}$ 只是固定倍數，微分時可以先放外面： $\frac{d}{dV}\left[\frac{1}{n}\sum(X-V)^2\right] = \frac{1}{n} \cdot \frac{d}{dV}\left[\sum(X-V)^2\right]$

> 整包東西都除以 $n$，微分結果也會除以 $n$。

#### 3-2｜對總和微分 → 拆成每項各自微分

$\sum(X-V)^2$ 展開是： $（x_1-V)^2 + (x_2-V)^2 + \cdots + (x_n-V)^2$

微分有個規則：**一堆東西相加的微分 = 每一項各自微分後再相加**

$$\frac{d}{dV}\left[\sum(X-V)^2\right] = \sum \frac{d}{dV}(X-V)^2$$


#### 3-3｜用 Chain Rule 微分 $(X-V)^2$

$(X-V)^2$ 有兩層結構：

| 層 | 內容 |
|----|------|
| 外層 | $(\cdot)^2$，某個東西的平方 |
| 內層 | $u = X - V$ |

令 $u = X - V$，則原式為 $u^2$。Chain Rule 說 : $\frac{d}{dV}\, u^2 = \underbrace{\frac{d}{du}\, u^2}_{\text{外層對 }u\text{ 微分}} \cdot \underbrace{\frac{du}{dV}}_{\text{內層對 }V\text{ 微分}}$

**外層微分：** $\frac{d}{du}\, u^2 = 2u = 2(X-V)$

**內層微分：** $X$ 是固定的資料點，對 $V$ 來說是常數，所以 $\frac{d}{dV}(X - V) = -1$

> $V$ 增加 1，$X - V$ 就減少 1。

**合併（Chain Rule 結果）：** :  $\frac{d}{dV}(X-V)^2 = 2(X-V) \cdot (-1) = -2(X-V)$

> 這就是 Chain Rule 產生負號的地方。


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/4-chain-rule.png)


#### 3-4｜代回整個式子，整理斜率

$$\frac{d}{dV}\left[\frac{1}{n}\sum(X-V)^2\right]
= \frac{1}{n} \cdot \sum\frac{d}{dV}(X-V)^2
= \frac{1}{n} \cdot \sum\left[-2(X-V)\right]
= \frac{-2}{n}\sum(X-V)$$


#### 3-5｜令斜率為零，找谷底

> 斜率公式：$\dfrac{d}{dV}\left[\frac{1}{n}\sum(X-V)^2\right] = \dfrac{-2}{n}\sum(X-V)$

令斜率等於零：$\dfrac{-2}{n}\sum(X-V) = 0$

兩邊乘以 $\dfrac{n}{-2}$ 消去係數：$\quad \sum(X-V) = 0$

> 白話：把每個資料點 $X$ 減去 $V$ 之後全部加起來，等於 0。


## Step 4｜解出 V

展開 $\sum(X - V) = 0$  :  $\sum X - nV = 0$

移項解出 $V$：$\quad V = \dfrac{\sum X}{n}$


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/4-2-chain-rule.png)


## 🎯 結論

「所有資料點的總和除以資料總數 $n$」——這完全就是**樣本平均數 $\bar{X}$** 的計算公式！

數學直接證明了：不管你有多少筆資料，只要你想找讓「距離平方和最小」的中心點，答案永遠都是樣本平均數 $\bar{X}$。

<!-- endtab -->

<!-- tab 為什麼這樣會造成「低估」-->

## 關鍵前提

從上一個 tab 我們知道：**用 $\bar{x}$ 算出的變異數，是所有可能的中心點中最小的。**

而抽樣出來的 $\bar{x}$，幾乎不可能剛好等於真正的母體平均數 $\mu$。


## 推論

| 情境 | 使用的中心點 | 算出的變異數 |
|------|------------|------------|
| 理想（不可得） | 母體平均數 $\mu$ | **較大**（真實值）|
| 現實（我們只有這個） | 樣本平均數 $\bar{x}$ | **較小**（最小值）|

由於 $\bar{x}$ 算出的距離平方和天生偏小，直接除以 $n$ 得到的變異數，會比真正的母體變異數還要**低估**。


> 用樣本平均數 $\bar{x}$ 取代母體平均數 $\mu$ 計算變異數，會造成**系統性低估**

因此，直接把總和除以 $n$，算出來的數字會比實際的母體變異數小——這就是所謂的「**低估（underestimation）**」

<!-- endtab -->


<!-- tab 為甚麼是 n-1-->


## Step 1｜拆解每筆資料的偏差

對每一筆資料 $x_i$，它和真正母體平均 $\mu$ 的距離可以拆成兩段：

$$x_i - \mu = \underbrace{(x_i - \bar{x})}_{\text{資料到樣本平均}} + \underbrace{(\bar{x} - \mu)}_{\text{樣本平均到母體平均}}$$






## Step 2｜兩邊平方，展開

用 $(a+b)^2 = a^2 + 2ab + b^2$：$(x_i - \mu)^2 = (x_i-\bar{x})^2 + 2(x_i-\bar{x})(\bar{x}-\mu) + (\bar{x}-\mu)^2$


## Step 3｜對所有資料加總

$\sum(x_i-\mu)^2 = \sum(x_i-\bar{x})^2 + 2(\bar{x}-\mu)\sum(x_i-\bar{x}) + n(\bar{x}-\mu)^2$

**中間那項消失：** $\sum(x_i-\bar{x}) = 0$

> 所有資料減去自己的平均數，偏差總和恆等於 0。

所以化簡為： $\sum(x_i-\mu)^2 = \sum(x_i-\bar{x})^2 + n(\bar{x}-\mu)^2$


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/5-1-xbar-mu-extend-add.png)



## Step 4｜移項，看少掉多少

$$\sum(x_i-\bar{x})^2 = \sum(x_i-\mu)^2 - n(\bar{x}-\mu)^2$$

> 用 $\bar{x}$ 算出來的平方距離總和，比用 $\mu$ 算少掉了 $n(\bar{x}-\mu)^2$。


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/5-2-xbar-loss-miu-one-item.png)


## Step 5｜取期望值，計算「平均少多少」

**左側（用 $\mu$ 計算的完整平方距離）：**

每一筆資料平均貢獻一份 $\sigma^2$，$n$ 筆合計： $E\left[\sum(x_i-\mu)^2\right] = n\sigma^2$

**少掉的那塊（$\bar{x}$ 偏離 $\mu$ 的誤差）：**

樣本平均 $\bar{x}$ 本身的變異數是 $\dfrac{\sigma^2}{n}$，所以： $E\left[n(\bar{x}-\mu)^2\right] = n \cdot \frac{\sigma^2}{n} = \sigma^2$


## Step 6｜得出結論

$$E\left[\sum(x_i-\bar{x})^2\right] = n\sigma^2 - \sigma^2 = (n-1)\sigma^2$$

| 情境 | 平方距離總和的期望值 |
|------|---------------------|
| 用真正 $\mu$ 計算 | $n\sigma^2$ |
| 用樣本 $\bar{x}$ 計算 | $(n-1)\sigma^2$（少掉一份）|

因此，要從 $\sum(x_i-\bar{x})^2$ 還原回 $\sigma^2$，必須除以 $(n-1)$：

$$\boxed{s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}}$$



![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/5-3-sigma.png)



<!-- endtab -->


<!-- tab summary-->

![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/6-correction.png)




![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Statistics/Bessels-Correction/table.png)


<!-- endtab -->



{% endtabs %} 