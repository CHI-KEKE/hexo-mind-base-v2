---
title: Lossless Compression
date: 2026-09-06 11:23:03
categories: CS
top_img: 
cover : 
tags:
toc:
toc_number:
comments :
---

{% tabs Lossless Compression%}


<!-- tab 為甚麼有不同格式的定義-->


最簡單的答案是壓縮沒有一個方法可以同時做到「壓得最小、壓得最快、解壓最快、最省 RAM、相容性最好、功能最多」

所以 ZIP 很普及，依然會有人針對不同需求設計 RAR、7z、tar.gz

假設現在要備份一台 Server 總共 10 GB 的資料

```bash
/var/log/
├── app.log          2 GB
├── nginx.log        1 GB
├── error.log        500 MB
├── access.log       4 GB
└── ...
```


我們最在意傳給 Windows 使用者，他點兩下就能打開，那就是 ZIP ，或者是不在乎相容性，我只希望 10 GB 可以盡可能壓小，那可能選 7z，另一個 Linux 管理員則可能說，我要保留 Linux 的檔案權限、symbolic link、目錄資訊，而且最好能接到 shell pipeline，就會選擇 tar.gz，壓縮本身就是一個 trade-off 問題

```bash
                 壓縮率
                   ▲
                   │
                   │
CPU 使用量 ◄───────┼───────► 壓縮速度
                   │
                   │
                   ▼
               RAM 使用量
```


另外還有

- 相容性
- 分卷能力
- 錯誤恢復
- 加密
- 檔案權限
- 隨機存取
- Streaming


工程上很難把所有旋鈕同時拉到最好


<!-- endtab -->




<!-- tab ZIP - 我最在意「大家都打得開」-->

ZIP 是一種非常普及、開放且支援度很高的壓縮檔格式


```bash
很多檔案
   │
   ▼
┌───────────────┐
│ ZIP 打包/壓縮 │
└───────────────┘
   │
   ▼
Project.zip
   │
   │ 解壓縮
   ▼
原本的所有檔案
```


Windows、macOS、Linux 幾乎都可以直接處理 ZIP，ZIP 內部可以使用不同的壓縮方法，其中最經典的是 DEFLATE。DEFLATE 又可以粗略理解成兩個重要概念

```bash
DEFLATE
   │
   ├── LZ77
   │     找出「前面出現過的重複資料」
   │
   └── Huffman Coding
         常出現的符號 → 用較短的 bit 表示
```


ZIP 最大優勢是相容性，它最早是 Phil Katz 在 1989 年開發 PKZIP 時推出的格式，後來 ZIP 格式規格公開，很多軟體都能自己實作。所以

```bash
Windows ─┐
macOS   ─┤
Linux   ─┤
7-Zip   ─┼── 都可以讀寫 .zip
WinRAR  ─┤
Java    ─┤
.NET    ─┘
```


例如用 C#
```csharp
ZipFile.CreateFromDirectory("logs", "logs.zip");
```


.NET 自己就能產生 ZIP，不需要安裝 WinZip 或 WinRAR。所以可以把 ZIP 想成大家都知道規格，因此不同軟體都能產生與讀取的檔案格式。有點類似 JSON，JSON 是一個格式Chrome 可以處理、C# 可以處理、Python 可以處理、Java 可以處理、Node.js 可以處理

今天假設寄出 `logs.zip`通常不用先問對方「你電腦有裝某某解壓軟體嗎？」因為 Windows、macOS、Linux，以及大量程式語言都有 ZIP 支援。所以 ZIP 很適合跨平台分享、軟體下載、Email 附件、一般文件、網站提供下載，它的定位可以想成壓縮界的最大公約數



<!-- endtab -->




<!-- tab 7z - 我想把東西壓得更小-->

接著假設遇到原始資料有 1000 MB，今天可能用 ZIP 只能壓到 650 MB，但使用 7z 則可以達到 480 MB，那當要存幾 TB 的備份時，差距就可能很重要。


7z 是 7-Zip 的原生格式之一，常搭配 LZMA / LZMA2 等壓縮方法，它願意付出一些代價，例如

```bash
更複雜的壓縮
       ↓
可能花更多 CPU
       ↓
可能使用更多 RAM
       ↓
換取更好的壓縮率
```

因此7z 常被選來追求較高壓縮率，實際壓縮率仍然高度取決於資料內容與設定。




<!-- endtab -->




<!-- tab ZIP - 我最在意「大家都打得開」-->



<!-- endtab -->


<!-- tab RAR-->

RAR 是 Eugene Roshal 開發的格式。常看到 WinRAR，RAR 與 WinRAR 的關係非常密切。大致可以理解

- RAR = 檔案格式
- WinRAR = 一套壓縮/解壓縮軟體


第三方程式可以支援解壓 RAR，所以你用 7-Zip 等工具也可能開得了 .rar。但 RAR 的壓縮器受到授權限制，因此不像 ZIP 那樣可以自由地自己實作一個相容的 RAR 壓縮器。


而 RAR 長期很受歡迎的一個原因是，它在「大型檔案封裝與散布」方面提供了不少實用功能。以前下載大型檔案，可能看過

```bash
movie.part01.rar
movie.part02.rar
movie.part03.rar
movie.part04.rar
movie.part05.rar
```


這就是分卷壓縮。例如將 20 GB 每份切成 2 GB，並且也以 recovery record 等損壞恢復能力聞名。它的價值是「我要把大型資料封裝、分割、傳輸，而且希望有額外的恢復能力。」


<!-- endtab -->




<!-- tab tar.gz-->

tar.gz 最有趣，因為它是「兩個工具合作」，我們看到 `project.tar.gz` 其實可以拆成

```bash
project
   │
   │ tar
   ▼
project.tar
   │
   │ gzip
   ▼
project.tar.gz
```


tar 主要負責打包。例如

```bash
a.txt
b.txt
c.txt
images/
config/

```

經過 tar 後

```bash
a.txt ───┐
b.txt ───┤
c.txt ───┼──→ project.tar
images/ ─┤
config/ ─┘
```


把很多檔案變成一個 archive，然後 gzip 再負責

```bash
project.tar
     │
     │ gzip 壓縮
     ▼
project.tar.gz
```


所以 tar 把這堆檔案包起來，而 gzip 把這包資料壓小，這也是 Linux / Unix 世界很典型的設計思維，就是每個工具負責一件事情，再組合起來，因此我們可能還會看到 .tar.gz、.tar.bz2、.tar.xz、.tar.zst

因為

```bash
             ┌─ gzip
             │
tar ─────────┼─ bzip2
             │
             ├─ xz
             │
             └─ zstd
```

前面的 tar 可以保持不變，後面的壓縮器可以換


<!-- endtab -->




<!-- tab 原理-->



假設原始資料是：

AAAAAAAAAAAAAAAAAAAA

總共有 20 個 A。

與其真的記錄 20 次 A，我們可以改成：

A × 20

意思是：

「接下來有 20 個 A。」

於是原本需要描述：

AAAAAAAAAAAAAAAAAAAA

現在只需要描述：

20A

解壓縮程式看到 20A，就知道要把它恢復成 20 個 A。

我們沒有刪除資訊，而是找到資料中的規律，用更短的方法描述它。

這就是理解非失真壓縮非常重要的起點：

非失真壓縮的本質，可以理解成「尋找資料中的規律與重複，然後用更有效率的方式描述它」。

但如果資料看起來接近完全隨機：

G7#q2L@9xP!4mZ8...

幾乎找不到可以利用的規律，就很難再縮小。







<!-- endtab -->




<!-- tab Web Server 的 log 打包成 ZIP，傳到備份伺服器-->


例如一天下來產生了一個 500 MB 的 access.log


裡面可能有幾百萬行

```bash

2026-09-06 10:01:01 INFO GET /api/users 200
2026-09-06 10:01:02 INFO GET /api/users 200
2026-09-06 10:01:03 INFO GET /api/users 200
2026-09-06 10:01:04 INFO GET /api/products 200
2026-09-06 10:01:05 INFO GET /api/users 200
...

```


你應該馬上可以這些內容大量重複

```bash
2026-09-06
INFO
GET
/api/users
200
```

因此雖然這個 log 是 500 MB，但它並不代表裡面存在 500 MB「完全不同的資訊」。


## Step 1：原始資料存在硬碟

假設簡化成這份檔案 server.log

```bash
10:01 INFO GET /api/users 200
10:02 INFO GET /api/users 200
10:03 INFO GET /api/users 200
10:04 INFO GET /api/products 200
10:05 INFO GET /api/users 200
```


電腦底層其實會把文字轉成 bytes，例如 ASCII 中

```bash
I = 01001001
N = 01001110
F = 01000110
O = 01001111
```


所以硬碟真正保存的是大量 bit。


## Step 2：執行 ZIP


ZIP 開始讀取原始 bytes，它並不知道「喔，這是一份 server log。」

它只看到

```bash
...INFO GET /api/users 200...
...INFO GET /api/users 200...
...INFO GET /api/users 200...
```

然後發現「欸，這串 bytes 我剛剛看過。」


## Step 3：DEFLATE / LZ77 找到重複資料

第一次的 `INFO GET /api/users 200` ，沒有辦法參考前面的資料，所以需要記錄。但第二次又遇到 `INFO GET /api/users 200`，壓縮器發現前面不久才出現過完全相同的 bytes。所以概念上不再寫一次，而是寫 `<往前 X bytes，複製 23 bytes>`

因此經過 LZ77 後，概念上變成

```bash
10:01 INFO GET /api/users 200
10:02 <copy previous INFO GET /api/users 200>
10:03 <copy previous INFO GET /api/users 200>

```


真實格式當然不是英文 copy previous，而是用很精簡的 binary 編碼表示 length + distance，這時候資料已經開始縮小


## Step 4：Huffman 再壓一次

接下來 ZIP 還會觀察「哪些符號最常出現？」例如 log 裡

```bash
INFO
GET
200
/api/
```

相關的 bytes 或 LZ77 產生的符號可能非常頻繁。因此套用一個想法是，常出現的符號 → 用較短的 bit 表示，少出現的符號 → 可以用較長的 bit 表示

假設只是教學用的簡化例子

```bash
A → 0
B → 10
C → 110
D → 111
```

如果 A 超級常出現，就只需要 0，而不是每次都使用固定 8 bits，因此 DEFLATE 大致形成兩層

```bash
原始 bytes
     ↓
LZ77
找出重複資料
     ↓
literal + length/distance
     ↓
Huffman coding
常見符號用較短 bit 表示
     ↓
compressed data

```

這才比較接近 ZIP 真正在做的事情



<!-- endtab -->



<!-- tab Huffman coding-->


出現越頻繁的資料，用越短的 bit 表示；越少出現的資料，可以用比較長的 bit 表示


假設有一段資料總共 10 個字元

```bash
AAAAAABBBC
```

統計出現次數

```bash
字元	次數
A	    6
B	    3
C   	1
```

我們很單純地固定用 2 bits 表示

```bash
A = 00
B = 01
C = 10
```

那 AAAAAABBBC 需要 10 × 2 bits = 20 bits


## Huffman 的想法


```bash
A 出現 6 次  ← 超常出現
B 出現 3 次
C 出現 1 次  ← 很少出現
```

所以可以讓 A 特別短，例如

```bash
A = 0
B = 10
C = 11
```


AAAAAABBBC => 00000010101011

只有 6 × 1 + 3 × 2 + 1 × 2 = 14 bits


這就是壓縮


<!-- endtab -->



<!-- tab Huffman tree-->

## tree

當一個判斷做完之後，會根據結果進入下一層判斷，而且這種「選擇 → 再選擇」會持續展開時，就很適合想到 Tree


## Huffman Coding

```bash
讀一個 bit
    ↓
是 0 還是 1？
   /      \
  0        1
 ↓          ↓
可能結束   繼續判斷
            ↓
          0 or 1？
          /    \
         0      1
```


## 高頻率放淺、低頻率放深


Tree 的深度就是編碼長度，所以只要控制字元在 Tree 裡的位置，就等於直接控制它需要幾個 bits。


<!-- endtab -->


{% endtabs %}
