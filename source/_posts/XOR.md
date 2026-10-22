---
title: XOR
date: 2025-10-25 08:35:05
categories: 思索日和
top_img: https://github.com/CHI-KEKE/pics/blob/main/Logi/思索日和/Stamp.png?raw=true
cover : https://github.com/CHI-KEKE/pics/blob/main/Logi/思索日和/Stamp.png?raw=true
tags:
    - 思索日和
toc:
toc_number:
comments :
---

{% tabs XOR%}


<!-- tab XOR-->

人生就像一場不斷的 XOR。有時我們與他人相同，結果歸零；有時我們與他人不同，才激起新的火花

相異，並非衝突，而是彼此成就的起點。就像 XOR 的規則，唯有「不同」，才產生能量。在日常的重複中，我們不斷被抵銷；而在那些「不同」的瞬間，我們被記錄、被看見，也因此變得獨一無二



|  A  |  B  | A XOR B |
| :-: | :-: | :-----: |
|  0  |  0  |    0    |
|  0  |  1  |    1    |
|  1  |  0  |    1    |
|  1  |  1  |    0    |

當兩邊不一樣時，結果為 1；一樣時，結果為 0


![22](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/1__XOR_Life.png)


<!-- endtab -->

<!-- tab XOR 用在加密?-->

這裡有個非常巧妙的特性：XOR 運算是可逆的！

(原文 XOR 金鑰) XOR 金鑰 = 原文

```bash
原文：0101
金鑰：1100
加密：1001   (0101 XOR 1100)
解密：0101   (1001 XOR 1100)
```


XOR 本身不是安全的加密演算法，而是一個「運算工具」

- 可逆性 (Reversibility)：加密與解密使用相同操作
- 效率高 (Very fast)：只要位元運算，電腦超擅長
- 結合亂數金鑰後很強 (One-Time Pad 原理)：如果金鑰（Key）跟訊息一樣長，且完全隨機、只用一次，那麼用 XOR 加密後，理論上是無法破解的（這是密碼學的「完美保密性」）


![2](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/2__secret.png)

![d](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/2__recover_easy.png)


```csharp
async Task Main()
{
	string key = "abcd";
	string word = "Guan";

	// char 雖然看起來是「字元」，其實在 .NET 裡是一種 16-bit 的整數型別（Unicode code unit）。
	// 兩邊都是 char，C# 編譯器會自動提升 (promote) 這兩個 char 成為 int 再運算
	// CPU 的運算器（ALU）最常用、最高效的運算單位是 32 位元（int）。
	// 雖然有支援 8 - bit / 16 - bit 運算，但要加額外處理，反而慢。在運算前自動提升成 int，比直接處理小型別更有效率。
	// 保護程式設計師免於「溢位」錯誤
	var encrypted = new string(word.Select((ch,i) => (char)(ch^key[i])).ToArray());
	var decryped = new string(encrypted.Select((ch,i) => (char)(ch^key[i])).ToArray());
	Console.WriteLine($"原文: {word}");
	Console.WriteLine($"加密: {encrypted}");
	Console.WriteLine($"解密: {decryped}");
}
```

![a](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/2__ecvrypted_to_int.png)


<!-- endtab -->


<!-- tab 變數交換（Swap Without Temp）則-->

```csharp
int a = 5;
int b = 9;

a= a^b;
b = a^b;
a = a^b;  //// (a^b ^ a) xor 結果呈現出這兩個不同這件事, 再回頭 XOR, 就是把這個結果再問一次 a 誰跟你不同?
$"{a}, {b}".Dump();
```

a ^ b 是「我們兩個相同或不同」，再拿這個結果去跟 a 做 XOR，就是在問：「誰跟 a 不同或相同？」


![a](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/5_swap_trick.png)



<!-- endtab -->

<!-- tab 找出「唯一」的元素-->

假設有一個陣列，裡面除了某一個數字之外，其他的數字都出現兩次，怎麼快速找出那個「單一出現」的數？

```csharp
int[] nums = { 4, 1, 2, 1, 2 };
int result = 0;

foreach (var n in nums)
    result ^= n;

Console.WriteLine(result); // 4
```

![a](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/4_find_alone.png)


但它其實是一個「無需額外記憶體的抵銷機制」。換句話說：它能幫你在資料中「快速找出異常項」，而且不需要排序、不需要暫存空間、不需要 HashSet。

這種「靠位元邏輯自我抵銷」的思維，在「資料錯誤偵測」、「狀態配對」、「唯一識別」等場景中非常有用


![ss](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/3__self_destructive.png)


像是檔案比對 / 資料完整性驗證，在傳輸資料或同步檔案時，常要檢查哪個檔案、哪筆資料「多了」或「少了」。例如：伺服器上記錄了某批資料 ID


```csharp
int[] server = {1, 2, 3, 4, 5};
int[] client = {1, 2, 3, 5};

int result = 0;
foreach (var n in server) result ^= n;
foreach (var n in client) result ^= n;

Console.WriteLine(result); // 4
```
✅ 結果立刻告訴你少了哪個
👉 這比用集合比對更省記憶體、運算時間固定 (O(n))

<!-- endtab -->


<!-- tab 資料校驗（Checksum / Parity Bit）-->

XOR 的「抵銷性」讓它非常適合做資料驗證。舉例：在通訊協定中，一段資料的所有 bytes 會一起 XOR 出一個值作為「校驗位元」。接收端收到資料後再 XOR 一遍，如果結果為 0，代表資料沒壞。這個方法雖然不如 CRC 強大，但運算非常快、成本低


![a](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/6_find_lost.png)


<!-- endtab -->


<!-- tab Bit Mask 運算 / 條件切換-->

有時候你想「切換」某個 bit 的狀態（0↔1），就可以用 XOR：
```csharp
int flags = 0b_1010;
int mask = 0b_0100;

flags ^= mask; // 變成 0b_1110，切換第 3 個 bit
```

這常見於：

- 設備控制（開關狀態）
- 遊戲開發中的狀態旗標（Flags）
- 記憶體壓縮資料的位元操作

![4](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/7_toggle.png)




<!-- endtab -->

<!-- tab 記錄配對比對（找出未成對的紀錄）-->

你有一堆「登入」和「登出」紀錄，每個人都應該成對出現。但哪個人只登入沒登出？

```csharp
int[] logs = { 101, 205, 101, 305, 205 };
int result = 0;
foreach (var id in logs)
    result ^= id;
Console.WriteLine(result); // 305
```

👉 結果：305（那個沒登出的人）


![s](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/8_whos_not_off_work.png)


<!-- endtab -->

<!-- tab summary-->


![f](https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Logi/XOR/9_XOR_table.png)

<!-- endtab -->


{% endtabs %}