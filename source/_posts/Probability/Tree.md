---
title: Tree
date: 2026-05-01 20:54:03
categories: Probability
top_img: https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/landing.png?raw=true
cover : https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/landing.png?raw=true
tags: 
    - 
toc:
toc_number:
comments :
---

{% tabs Tree%}

<!-- tab 本質-->

當事情是「從一個起點，一路分岔出多種可能」，樹就是最自然、最不容易混亂的表達方式


- 有一個起點（Root），所有事情從這裡開始

- 每個節點代表一個狀態，例如：選擇到一半、走到某個資料夾

- 每條邊代表一個「選擇 / 行為」，做一個決定 → 走到下一個狀態

- 往下展開成多層結構，每一層代表「更深入一步」，葉節點（Leaf）代表結果或終點，一條完整路徑 = 一個完整結果


![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/1_problem_is_branches.png?raw=true)


例如玩 RPG 遊戲選劇情

- 開始 → 幫村民 / 不幫
- 幫村民 → 拿獎勵 / 被騙
- 不幫 → 直接離開

每一條路線就是一條「從 root 走到 leaf 的路徑」



問題一旦有「選擇」，就不再是線性的了


![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/2_what_forms_a_tree.png?raw=true)


<!-- endtab -->

<!-- tab DFS（Depth-First Search）-->

DFS 的本質是，先把一條路走到底，再回頭試別條，不同可能一條一條試完，當我們要「找所有可能」或「找到一個解就好」，DFS 是最直覺的走法

1. 從 root 開始，選一條路一直往下走，走到底（或不合法）就回頭（backtrack）
2. 換下一條路
3. 重複直到全部走完

很像在走迷宮時，先一路衝到底，撞牆再回來換路



![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/3_what_is_dfs.png?raw=true)



## 工作順序

Excel 排法常是人工調整順序，局部看起來合理，但問題是一改某個任務，可能會影響後面 10 個，沒有自動檢查「是否違反依賴」


假設

A：寫 API
B：設計 DB
C：寫 UI
D：需求確認
```bash
A → B → D
A → C → D
```

- API 不能寫 → 去看 DB
- DB 不能寫 → 去確認需求
- 需求 OK → ✔
- 回來 DB → ✔
- 回 API → 還有 UI
- UI OK → ✔
- 回 API → ✔


最終紀錄（完成順序）（後序）

```bash
D → B → C → A
```

「執行順序」

```bash
A → C → B → D
```


當我們遇到問題時，可能這樣想

- 這是不是很多「任務 / 事情」？
- 它們之間有沒有「前後依賴」？（A 一定要在 B 前）
- 我要不要排一個「合法順序」？

三個都是 YES → 幾乎可以直接判定這是 `Topological Sort`



![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/5_topological.png?raw=true)



## 選課系統

資料結構 → 先修課
演算法 → 要先修資料結構

要排「修課順序」

## 程式建置（build system）


編譯 A 前要先編譯 B
B 又依賴 C

- makefile
- npm build
- CI/CD pipeline

這都在做拓樸排序



![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/6_topological_cases.png?raw=true)



## call stack

```csharp
void DFS(string node)
{
    foreach (var next in graph[node])
    {
        DFS(next);
    }
}
```


假設 A → B → D

我們呼叫 DFS("A");

則流程是


1. 呼叫 DFS(A) -> stack: [A]
2. A 裡面呼叫 DFS(B) -> stack: [A, B]
3. B 裡面呼叫 DFS(D) -> stack: [A, B, D]
4. D 沒有下一個節點，函式結束 return -> stack: [A, B]   ← 這裡就是自動 pop D
5. B 也結束 return -> stack: [A]      ← 自動 pop B
6. A 結束 return -> stack: []       ← 自動 pop A



![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/4_call_stack.png?raw=true)



手動 stack 版
```csharp
void DFS(string start)
{
    var stack = new Stack<string>();
    stack.Push(start);

    while (stack.Count > 0)
    {
        var node = stack.Pop();
        foreach (var next in graph[node])
        {
            stack.Push(next);
        }
    }
}
```


<!-- endtab -->

<!-- tab 決策樹（Decision Tree）-->

決策樹的本質是把「怎麼做選擇」變成一個可以重複使用的判斷流程，當我們需要「根據條件做判斷」，而且規則很多，用樹會比 if-else 清楚


- 每個節點是一個「問題」（例如：收入 > 5 萬？）

- 每條邊是「答案」（是 / 否）

- 一路往下判斷，最後落在一個結果（分類 / 決策）

本質其實就是結構化的 if-else，但更清楚、可視化




![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/7_options_to_tree.png?raw=true)



## 決策樹和分類的關係

分類其實是「把一個連續又混亂的空間，切成幾塊有意義的區域」，可以想像，每個人是空間中的一個點（收入、信用…），而分類就是在畫界線，決策樹是一種「切空間的方法」，分類是「切完之後要做的事」，每一個節點的問題，都是在幫你把資料空間切一刀


分類在做的是「我用收入 + 信用，可不可以判斷這個人會不會違約？」



![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/8_categories.png?raw=true)



<!-- endtab -->

<!-- tab 檔案系統（資料夾結構）-->

資料夾結構的本質是用層級來管理東西，讓我們知道「東西在哪一層、屬於誰」，當資料很多，如果全部放平面，可能會完全找不到


- 最上層（Root）例如：C 槽 / 主目錄
- 裡面有資料夾（子節點），每個資料夾可以再放資料夾
- 檔案是葉節點

例如：

- /photos
  - /2025
    - img1.jpg

這就是一棵樹





![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/9_files.png?raw=true)



<!-- endtab -->


<!-- tab summary-->


![2](https://github.com/CHI-KEKE/pics/blob/main/Probability/tree/tree.png?raw=true)


<!-- endtab -->


{% endtabs %}