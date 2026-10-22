---
title: symmetric-difference
date: 2026-05-22 20:54:03
categories: Probability
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/1_landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/1_landing.png
tags: 
    - 
toc:
toc_number:
comments :
---

{% tabs symmetric-difference%}

<!-- tab 本質-->

對稱差集就是拿來找出「兩邊各自有、但彼此沒有重疊」的資料，特別適合用來抓差異、比對變動、排除共同項目



![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/2_mean.png)


假設有兩個集合：

A = {1, 2, 3}
B = {3, 4, 5}


對稱差集會做這幾件事：

1. 先找出 A 裡面有，但 B 裡面沒有的東西 A - B = {1, 2}
2. 再找出 B 裡面有，但 A 裡面沒有的東西 B - A = {4, 5}
3. 把這兩邊的結果合起來 A △ B = {1, 2, 4, 5}

所以共同都有的 3 會被排除掉，因為它不是差異



![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/3_cal.png)



<!-- endtab -->


<!-- tab 會員標籤比對-->

oldTags = {"VIP", "Email", "Coupon"}
newTags = {"VIP", "SMS", "Coupon"}


對稱差集結果會是 {"Email", "SMS"}，也就是 Email 是舊資料有，但新資料沒有，而 SMS 是新資料有，但舊資料沒有，這種情況很適合用來判斷「資料到底變了哪些地方」


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/4_tags_example.png)


<!-- endtab -->

<!-- tab 資料同步-->

對稱差集可以快速知道「兩份資料哪裡不一樣」，很適合拿來做同步、更新、刪除判斷，像前端快取、後端資料庫、第三方 API 回傳資料，都可能有一份舊資料和一份新資料

localIds = {1, 2, 3, 4}
serverIds = {2, 3, 4, 5}

對稱差集是 {1, 5}

代表：

1 可能是本地端多出來的資料而 5 可能是伺服器新增的資料，這時候就可以進一步決定要刪掉、補上，或提示使用者


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/5_serverids.png)


<!-- endtab -->

<!-- tab Except vs Union vs SetEquals-->

## Except


```csharp
var exceptPages = compareSalePageIds.Except(extraSalePageIds)
    .Concat(extraSalePageIds.Except(compareSalePageIds));

```

假設

compareSalePageIds = [101, 102, 103];
extraSalePageIds = [102, 103, 104];

第一步 compareSalePageIds.Except(extraSalePageIds) 會得到 [101] 意思是 101 在 `compareSalePageIds` 裡有，但 `extraSalePageIds` 裡沒有
第二步，找出右邊有、左邊沒有的資料 `extraSalePageIds.Except(compareSalePageIds)` 這段會得到：[104] ，意思是 104 在 extraSalePageIds 裡有，但 compareSalePageIds 裡沒有
第三步：把兩邊差異合起來.Concat(...) 最後得到 [101, 104] 也就是兩邊所有不一致的商品 ID


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/6_except.png)



## Concat 跟 Union 要用哪個

如果前面兩段 Except 的結果理論上不會重疊，用 Concat 就夠；如果想保險去重，可以用 Union


```csharp
var diff = a.Except(b).Union(b.Except(a));
```


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/7_concat_except.png)


##　SetEquals

要拿差異明細才用對稱差集，只想知道兩邊是否一樣，用 SetEquals 會更直接，如果目的只是這兩份 SalePageId 是否完全相同那不一定要寫差集
可以先轉成 HashSet：

```csharp
var aSet = a.ToHashSet();
var bSet = b.ToHashSet();
var isSame = aSet.SetEquals(bSet);
```


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/8_setequals.png)



<!-- endtab -->


<!-- tab summary-->


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Probability/symmetric-diff/9_final.png)



<!-- endtab -->

{% endtabs %}