---
title: Modulo - 2
date: 2026-04-26 09:16:03
categories: Mod
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/1_landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/1_landing.png
tags:
    - 思索日和
toc:
toc_number:
comments :
---


{% tabs Mod%}




<!-- tab 從「餘數」的角度看世界-->



餘數是在處理「週期性」問題，平常我們習慣用「直線」看數字，但餘數是在用「圓圈」看這些數字。例如一串數字 :　1,2,3,4,5,6...，mod 會說：跑到 5 之後回到 0，再重新開始，它的世界比較像時鐘：12,1,2,3,...,11,12，13 點其實就是 1 點，25 點也是 1 點，這就是餘數視角。若在擴展的話，資源、時間、位置或狀態，經過一段固定循環後，最後落在哪一格就是　`餘數角度`，餘數思維的現實用途，是把「一直增加的東西」轉成「循環中的位置」，讓你不用追整條歷史，只要知道現在落在哪一格



![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/2_modulo_is_cycle.png)



以 mod 5 為例：

原本你看到的是直線：

```bash
1,2,3,4,5,6,7,8,9...
```

餘數視角會把它變成循環：

```bash
0,1,2,3,4,0,1,2,3,4...
```

所以數字變大不是重點，重點是它目前停在哪一格，像 1,6,11,16，都停在「餘 1」這格，所以在 mod 5 世界裡它們是同一類




![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/3_belong_to_section.png)



## 星期幾

一個隨意的問題 : 今天是星期一，100 天後星期幾？

你不可能真的一天一天數到第 100 天，你會算

```bash
100 ÷ 7 = 14 餘 2
```


意思是 100 天等於完整過了 14 週，又多 2 天，所以星期一往後 2 天是星期三，這就是 mod 7。



![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/4_1_100days.png)



## 排班輪班


假設公司有 5 個人輪流值班：A,B,C,D,E,A,B,C,D,E...，而第 23 天誰值班？


```bash
23 ÷ 5 = 4 餘 3
```


它會落在第 3 個位置。所以是 C，這就是 mod 5



![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/4_2_work_shift.png)




## 程式設計裡的循環陣列

假設圖片輪播有 5 張

```bash
0,1,2,3,4
```


目前在第 4 張，按下一張要回到第 0 張：

(4+1) mod 5 = 0

mod 很常用在

- 輪播圖
- 遊戲地圖循環
- 排隊系統
- 任務輪詢
- 分組分流



![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/4_3_carousel.png)



<!-- endtab -->


<!-- tab n ^ 2 ÷ 5 的餘數-->


有這樣一個問題 : 請列舉 n ^ 2 除以 5 所得的餘數形成的集合


而看到「除以 5 的餘數」，代表世界只剩下 5 種狀態


```bash
0,1,2,3,4
```


因此 n 不需要想成 1、2、3、4、5、6、7……因為必定會有重複


應該是這樣 **忽略倍數，只看偏移量**

```bash

## 本來就是定義
n=5k, 5k+1, 5k+2, 5k+3, 5k+4
```


接著我們就只要看這 5 種狀態平方後會變成什麼餘數





![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/5_many_cases.png)



<!-- endtab -->


<!-- tab 為什麼題目要問 n 平方,為甚麼不是問 n-->


如果只問 n mod 5，那答案就是 n ≡ 0,1,2,3,4 (mod5)，因為任何整數除以 5，本來就只可能餘：{0,1,2,3,4}

但題目問的是：

n<sup>2</sup> mod 5


現實中的資料總是會先加工，再看餘數格，資料經過規則處理後，會落在哪一類？ 而 n<sup>2</sup> 是一個最簡單、最常見的「加工後看餘數」模型


我們先把 n 分成 5 種身份 0,1,2,3,4，再看它們平方後會去哪裡：

0<sup>2</sup> → 0
1<sup>2</sup> → 1
2<sup>2</sup> → 4
3<sup>2</sup> → 9 → 4
4<sup>2</sup> → 16 → 1

結果變成：

{0,1,4}



![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/6_real_would_be_added.png)



<!-- endtab -->



<!-- tab 資料分桶：使用者分到哪台伺服器-->


假設有 5 台伺服器 0,1,2,3,4，使用者 ID 先經過加工：hash(userId) 再取餘數：

```bash
serverIndex = hash(userId) % 5

```


加工後的數字 mod5，決定使用者落在哪台伺服器。這樣每個使用者就能穩定分配到某一台，不用人工決定



![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/8_load_balance.png)


<!-- endtab -->



<!-- tab 身分證、信用卡、條碼檢查碼-->

很多檢查碼會先把前面的數字「加權加工」，再取餘數。

簡化例子：

```bash
sum = d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4
check = sum % 10
```


先加工，再看除以 10 的餘數，如果最後餘數不符合規則，就代表號碼可能打錯。這就是用餘數來抓錯字、漏字、輸入錯誤




![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/Modulo/modulo-2/9_id_card.png)



<!-- endtab -->


{% endtabs %}