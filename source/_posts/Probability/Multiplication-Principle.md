---
title: Multiplication Principle
date: 2026-06-12 16:49:03
categories: Probability
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/landing.png
tags:
    - 
toc:
toc_number:
comments :
---



{% tabs Multiplication Principle%}


<!-- tab 使用乘法原理-->

**最重要的判斷方法：**

> 這件事是不是由好幾個步驟完成，而且每一步都必須做？
> 如果是，就很可能用乘法原理。

```mermaid
flowchart LR
    Q["題目情境"] --> D{"每一步都必須做？"}
    D -->|"是（步驟 AND 步驟）"| M["乘法原理\n各步驟選擇數相乘"]
    D -->|"否（情況 OR 情況）"| A["加法原理\n各情況數相加"]

    style Q fill:#F5A623,color:#fff
    style D fill:#7B68EE,color:#fff
    style M fill:#5BA85B,color:#fff
    style A fill:#4A90D9,color:#fff
```



![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/many-steps.png)



**乘法 vs 加法 對照**

| 情境 | 結構 | 原理 | 算法 |
|:---|:---|:---:|:---:|
| 先選衣服，再選褲子，再選鞋 | A **且** B **且** C | 乘法 | 3 × 2 × 4 = 24 |
| 搭公車有 3 種，或搭捷運有 4 種 | A **或** B | 加法 | 3 + 4 = 7 |

> **乘法原理**是在數「連續步驟的組合」；**加法原理**是在數「互斥情況的合併」


![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/2_multi-and-added.png)


<!-- endtab -->



<!-- tab 360 正因數之和-->

因數個數公式的核心就是乘法原理。甚至可以說，因數個數公式根本就是乘法原理直接套用的結果


![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/3-count-of-factors-1.png)



## 具體範例：360 的因數個數

以 **360 = 2³ × 3² × 5¹** 為例，任何因數都長成 **2ᵃ × 3ᵇ × 5ᶜ**，其中：

| 指數 | 可選範圍 | 選擇數 |
|:---:|:---|:---:|
| a（2 的指數） | 0, 1, 2, 3 | **4** 種 |
| b（3 的指數） | 0, 1, 2 | **3** 種 |
| c（5 的指數） | 0, 1 | **2** 種 |

現在問：**可以產生多少個不同因數？**

這其實是在問「選一個 a **且** 選一個 b **且** 選一個 c，有多少種選法？」正是乘法原理：

**4 × 3 × 2 = 24 個因數**

## 三層推導結構

```mermaid
flowchart TD
    L1["① 質因數分解\nN = p₁^a₁ × p₂^a₂ × ⋯ × pₖ^aₖ\n→ 找出所有因數的生成規則"]
    L2["② 各指數獨立選擇\n每個質因數的指數可以分別選\na ∈ {0..a₁}, b ∈ {0..a₂}, ..."]
    L3["③ 問題本質\n選 a 且 選 b 且 選 c\n有多少種選法？"]
    L4["乘法原理\n(a₁+1)(a₂+1)⋯(aₖ+1)"]

    L1 --> L2
    L2 --> L3
    L3 --> L4

    style L1 fill:#F5A623,color:#fff
    style L2 fill:#4A90D9,color:#fff
    style L3 fill:#7B68EE,color:#fff
    style L4 fill:#5BA85B,color:#fff
```

以 360 代入：**(3+1)(2+1)(1+1) = 4 × 3 × 2 = 24**


![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/3-2-mult-result.png)


<!-- endtab -->



<!-- tab 排列-->

## 密碼組合

假設一組密碼有 4 位數，每一位都可以是 0 到 9。

每一位有 10 種選擇，所以共有：**10 × 10 × 10 × 10 = 10⁴ = 10000 種密碼**


![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/4-password-combination.png)



## 數字不能重複時

每選一位，剩餘可選數字就少一個：

| 位數 | 可選範圍 | 選擇數 |
|:---:|:---|:---:|
| 第 1 位 | 0–9 | 10 種 |
| 第 2 位 | 扣掉第 1 位 | 9 種 |
| 第 3 位 | 扣掉前兩位 | 8 種 |
| 第 4 位 | 扣掉前三位 | 7 種 |

**10 × 9 × 8 × 7 = 5040 種**

這就是**排列**的底層：每一步可選數遞減，但核心仍是乘法原理


![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/5-permutation.png)


<!-- endtab -->


<!-- tab 巢狀迴圈-->

```csharp
foreach (var shirt in shirts)           // 3 種
{
    foreach (var pants in pantsList)     // 2 種
    {
        foreach (var shoes in shoesList) // 4 種
        {
            count++;
        }
    }
}
```

總共跑幾次？**3 × 2 × 4 = 24**


| 迴圈層次 | 對應概念 | 選擇數 |
|:---:|:---|:---:|
| 最外層 | 第一步驟 | 3 |
| 中層 | 第二步驟 | 2 |
| 最內層 | 第三步驟 | 4 |
| **總執行次數** | **乘法原理** | **3 × 2 × 4 = 24** |

> 乘法原理其實就是：**巢狀迴圈的總組合數**



![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/6-nested-loop.png)


<!-- endtab -->



<!-- tab summary-->



![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/Multiplicity/final.png)




<!-- endtab -->


{% endtabs %}