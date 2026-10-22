---
title: Bijection
date: 2026-05-15 16:30:05
categories: 
top_img: https://github.com/CHI-KEKE/pics/blob/main/Logi/思索日和/Stamp.png?raw=true
cover : https://github.com/CHI-KEKE/pics/blob/main/Logi/思索日和/Stamp.png?raw=true
tags:
    - 
toc:
toc_number:
comments :
---

{% tabs Bijection%}

<!-- tab 本質-->


我們發現兩個問題之間，存在某種可規則化的轉換


例如

- 微積分曲線下面積 ↔ 極限和
- 線性代數矩陣 ↔ 線性變換
- Lambda Calculus 程式 ↔ 數學函數
- Compiler AST ↔ Machine Code
- JSON serialization Object ↔ String

都是這種思想



![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/1_what_is_bijection.png)



<!-- endtab -->


<!-- tab 座位-->

新人團體兩康舉辦演唱會，甲乙丙丁四名觀眾買的座位在同一列，且該列共有 13 個座位

她們到場後發現，該列只有她們 4 人進場觀賞，該列其他 9 個位子都空著。在主辦單位未強制對號入座的情況下，她們想要舒服地分散坐，每兩人之間至少相隔兩個空位以上，則符合條件的入座方式共有 ______ 種

這題目顯然是相當有病的，坐就對了誰管他有幾種...


![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/2_case1_concert.png)


## 題目拆解

遇到奇怪的題目，第一件要做的事情就是確認理解

首先題目條件是


- 13 個位置

_ _ _ _ _ _ _ _ _ _ _ _ _


- 4 個人 : 甲乙丙丁
- 而要求是 : 任兩人之間至少隔 2 個空位。

也就是說會長這樣 : 人 _ _ 人


## 初始條件告訴了我們甚麼


是這樣的，我們先把最直覺的結果畫出來，因為 4 個人之間有 3 個間隔，而要求是說，每個間隔至少要 2 個空位，我們可以先畫出


人 _ _ 人 _ _ 人 _ _ 人


從這張圖，可以看出這已經用掉 4 個人、6 個空位總共 10 格，而這是我們不會動的一個模板初始狀態



![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/2_case1_template.png)



## 推論的條件

因為總共有 13 格，若扣除下來 13 - 10 = 3，我們可以知道剩下 3 個空位可以自由放! 所以我們可以將問題轉換成


**自由空位可以放哪？有幾種可能？**


## 自由空位可以放哪？

人 □□ 人 □□ 人 □□ 人


3 個自由空位，只能丟進 5 個 gap 區域


這就是：

隔板法
x1 + x2 + x3 + x4 + x5 = 3

也就是說，如果

```bash
x₁=1
x₂=0
x₃=2
x₄=0
x₅=0
```

代表最左邊放1格 : _ 人
第一二人間不加：人 _ _ 人
第二三人間多2格：人 _ _ _ _ 人


最後會得到 : _ 人 _ _ 人 _ _ _ _ 人 _ _ 人



![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/2_case1_3_where_freeseat_go.png)



走到這裡，我們問題變成「3 個自由位子，4 個人，這 7 個選項裡，我要挑哪 4 個作為隔板」

例如 : ● | ● ● | | |


\[\binom{3+5-1}{5-1}=\binom{7}{4}=35\]




但...還沒完！上面只是座位形狀，甲乙丙丁還可以交換，所以 4! = 24


最終答案

35 × 4! = 35×24 = 840


## 一一對應


世界 A : 合法座位排列
世界 B : 5 個 gap 分 3 個球

它們本質上是同一個結構


原本問題很難

13 格裡塞 4 人 且彼此距離 >= 3

但我們建立對應，把合法座位安排對應成

5 個 gap 分 3 個球
+
4 人排列


也就是每一種合法座位 ↔ 唯一的一組(空格分配, 人員排列)，而反過來也成立

因此這其實就是雙射（bijection）


![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/2_case1_4_c74.png)


<!-- endtab -->


<!-- tab NBA-->

在 2015 年的美國職業籃球比賽（NBA）中，是由騎士隊與勇士隊爭奪總冠軍（七戰四勝制）。

若今已比賽三場，由勇士隊取得 2 勝 1 負領先，且在往後的比賽有 K 種情形可以決定出冠軍（比賽沒有和局），則 K 之值為下列哪一個選項？



![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/3_case2_1_nba.png)


## 一一對應


7 戰 4 勝，可以想成「不用比完」，「任一隊4勝」，比賽就結束，而現在已經有2個O，1個X，只要再出現2個O或3個X，比賽就結束
，變成考慮OOXXX的排列，多排的，相當於假裝有比，例如出現：OXOXX，其實在OXO比賽就結束了，後面的XX沒有用，這其實就是一一對應原理的應用  


「2O3X 不是代表真的會打滿 5 場，而是一種 representation（表示法）。」

真正的系列賽可能只打 OO 就結束了，但我們故意把它表示成 OOXXX


原本的世界觀系列賽可能長度是 2、3、4、5 不好數

但如果全部統一成2個O + 3個X，問題就突然變成**固定長度排列問題**


![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/3_case2_2_bijection_to_ghostgame.png)



## 有沒有可能兩個不同系列賽結果，最後補成同一個排列？

例如 OO 跟 XOO 會不會都變 XOOXX？

答案是不可能，因為補法是固定的，如果真正系列賽是 OO 那已經用了 2 個 O 還沒用任何 X，所以只能補 XXX，得到 OOXXX，不可能補成 XOOXX，因為那代表前面曾出現一個 X，但原系列賽沒有，所以每個真實系列賽只能生成一個唯一排列，再反過來給 X O O X X 也能唯一還原


## 列出所有對應

| 真實系列賽 | 補完後的 2O3X 排列 |
|---|---|
| OO | OOXXX |
| OXO | OXOXX |
| XOO | XOOXX |
| OXXO | OXXOX |
| XOXO | XOXOX |
| XXOO | XXOOX |
| XXX | XXXOO |
| OXXX | OXXXO |
| XOXX | XOXXO |
| XXOX | XXOXO |

所以總共就是 10 種，對應到排列數 5! / (2!3!) = 10，我們可以觀察右邊每一個都是剛好 2 個 O、3 個 X，而左邊就是「讀到第 2 個 O 或第 3 個 X 時立刻停止」



![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/3_case2_4_calculate_solid.png)


## 「停止點」是唯一的


我們直接看右邊某個排列 X O X X O，現在從左往右讀

第1步 X，X 數 = 1 還沒結束
第2步 XO，O 數 = 1，還沒結束
第3步 XOX，X 數 = 2，還沒結束
第4步 XOXX，X數=3！遊戲立刻結束

所以真正系列賽一定是 XOXX，後面的 O，自動知道只是補的。

這個停止位置永遠只有一個，因為不可能同時第一次達到第 2 個 O 又第一次達到第 3 個 X 在不同地方，所以每個 2O3X 排列，都能唯一切開。


![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/3_case2_3_stoppoint_only.png)



<!-- endtab -->





<!-- tab summary-->



![b](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Bijection/final.png)




<!-- endtab -->


{% endtabs %}


