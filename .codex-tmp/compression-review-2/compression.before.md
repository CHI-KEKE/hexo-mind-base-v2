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

{% tabs Lossless Compression %}

<!-- tab 為甚麼有不同格式的定義-->

<style>
.compression-wide-diagram{max-width:100%;overflow-x:auto;}
.compression-wide-diagram .mermaid-wrap{min-width:520px;}
</style>

同一批檔案，寄給別人、長期備份與搬移 Linux 目錄時，適合的封裝方式可能不同。壓縮要在檔案大小、處理時間、記憶體用量與接收端支援之間取捨。

假設備份一台伺服器，共有 10 GB 的紀錄檔：

| 檔案 | 大小 |
| --- | --- |
| `app.log` | 2 GB |
| `nginx.log` | 1 GB |
| `error.log` | 0.5 GB |
| `access.log` | 4 GB |
| 其他紀錄檔 | 2.5 GB |

## 格式比較：這批資料要拿來做什麼？

| 優先需求 | 可考慮的格式 | 選擇時要確認 |
| --- | --- | --- |
| 跨平台分享、方便接收端開啟 | ZIP | 接收工具支援的壓縮與加密方法 |
| 願意花時間換取更小的檔案 | 7z | 實際資料的壓縮結果、CPU 與 RAM 成本 |
| 大型資料分卷傳輸、加入修復資訊 | RAR | 工具支援、分卷與復原設定 |
| 打包 Linux 目錄、保留相關中繼資料 | tar.gz | 封存格式、權限與還原選項 |

這張表比較需求與取捨，不是壓縮率排行榜。各格式的功能說明與來源放在對應分頁。

## 評估壓縮時的幾個面向

- **儲存與傳輸量**：壓縮後還剩多少資料。
- **處理時間**：壓縮與解壓縮要分別量測。
- **資源成本**：CPU、RAM 與磁碟 I/O 是否符合執行環境。
- **封裝功能**：是否需要加密、分卷、修復資訊與檔案權限。
- **讀取方式**：是否要串接串流，或只取出封存檔中的個別檔案。

選擇格式後，還要決定壓縮方法與等級。同一個副檔名，可能因設定不同而得到不同結果。

<!-- endtab -->

<!-- tab ZIP：我最在意「大家都打得開」-->

`ZIP` 是規格公開且廣泛使用的封存格式，可以把多個檔案集中在一個 `.zip` 中。它支援不同壓縮方法，也可以直接儲存未壓縮內容。常見方法是 `DEFLATE`。[ZIP 格式規格](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)

## 從資料夾到 ZIP，再還原

{% mermaid %}
flowchart TB
    Files["原始檔案與目錄"] -->|封裝並選擇壓縮方法| Archive["logs.zip"]
    Archive -->|相容工具解壓與取出| Restored["還原檔案"]
{% endmermaid %}

由上往下讀，箭頭表示資料封裝與還原。圖中省略檔頭等格式細節，重點是解壓後的檔案內容能與原始 bytes 一致。

## C# 建立 ZIP

```csharp
using System.IO.Compression;

ZipFile.CreateFromDirectory("logs", "logs.zip");
```

這段程式將既有 `logs` 目錄封裝成 `logs.zip`，不需另外安裝 WinZip 或 WinRAR。目的檔案必須尚不存在；來源目錄也必須存在且可讀。[Microsoft API 文件](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zipfile.createfromdirectory)

`ZIP` 適合作為文件分享與下載的候選格式。不過接收端能開啟 `.zip`，不代表支援規格中的所有壓縮或加密方法，仍要配合實際工具確認。

<!-- endtab -->

<!-- tab 7z：我想把東西壓得更小-->

`7z` 是 7-Zip 使用的封存格式，支援 `LZMA`、`LZMA2` 等方法，以及 solid compression 等功能。[7z 格式說明](https://www.7-zip.org/7z.html)

## 壓縮結果必須跟資料與設定一起看

以下是假設的比較數字，用來說明容量差異，並非實測或效能保證：

| 項目 | 大小 | 相對原始大小 |
| --- | --- | --- |
| 原始資料 | 1,000 MB | 100% |
| 假設 ZIP 結果 | 650 MB | 65% |
| 假設 7z 結果 | 480 MB | 48% |

在這個假設中，每批資料相差 170 MB。批次很多時，容量差異會累積；但若壓縮時間或記憶體需求也增加，就要一起評估。

較大的字典等設定可能增加記憶體需求。Solid compression 可以讓多個檔案共用壓縮歷史，但取出其中較後面的檔案時，可能需要先解碼同一 solid block 的前段內容。[7z 格式說明](https://www.7-zip.org/7z.html)

因此比較時應使用同一批資料，記錄工具版本、方法、等級、壓縮時間、解壓時間與峰值 RAM，才能判斷是否符合備份需求。

<!-- endtab -->

<!-- tab ZIP 格式與壓縮方法-->

## 封存格式與演算法分別負責什麼？

| 層次 | 例子 | 負責的事情 |
| --- | --- | --- |
| 封存格式 | ZIP、7z、RAR、tar | 組織檔案、名稱與相關中繼資料 |
| 壓縮方法 | DEFLATE、LZMA2 | 將資料編碼成可還原的表示 |
| 使用工具 | 7-Zip、WinRAR、`ZipFile` | 讀寫所支援的格式與方法 |

`ZIP` 內各檔案可以獨立選擇壓縮方法。以下是簡化的格式關係示意，不表示實際位元組排列，也不是執行時序。[ZIP 格式規格](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)

<div class="compression-wide-diagram">

{% mermaid %}
flowchart TB
    Zip["ZIP 封存檔"] -->|包含| Log["app.log 項目"]
    Zip -->|包含| Image["image.jpg 項目"]
    Log -->|本例選用| Deflate["DEFLATE 壓縮資料"]
    Image -->|本例選用| Store["Store：不壓縮資料"]
{% endmermaid %}

</div>

窄螢幕可在圖內左右捲動。由上往下看包含與方法選擇。這裡的 `image.jpg` 採 `Store` 只是示例，不是依副檔名必然採用的規則。封存與壓縮是兩個不同層次，因此 `.zip` 也可能沒有縮小內容。

<!-- endtab -->

<!-- tab RAR-->

`RAR` 是檔案格式，WinRAR 是可操作該格式的工具。兩個名稱分別代表封裝結果與使用軟體。

## 分卷與修復資訊

大型檔案可分成數個封存分卷，例如：

```text
backup.part01.rar
backup.part02.rar
backup.part03.rar
```

分卷方便按容量限制傳輸或儲存。若加入 recovery record，封存檔會多帶一份修復用冗餘資料，可用來處理一定範圍的損壞；這會增加檔案大小，也不能保證修復任意損壞。[WinRAR 修復記錄說明](https://www.win-rar.com/recovery-record.html)

修復損壞與補回遺失的整個分卷是不同需求，設定時要分別確認工具的支援與限制。

## 解壓支援不等於壓縮器可自由重用

第三方工具可包含 RAR 解碼支援。以 7-Zip 所含的 unRAR 程式碼為例，其授權限制將該程式碼用於開發 RAR 壓縮演算法。因此，能解壓 `.rar` 不等於同一套程式碼也能拿來建立 RAR 壓縮器。[7-Zip 授權說明](https://www.7-zip.org/license.txt)

<!-- endtab -->

<!-- tab tar.gz-->

`project.tar.gz` 結合了兩個責任：`tar` 把檔案和目錄封裝成 archive，`gzip` 再壓縮這份資料流。[GNU tar 手冊](https://www.gnu.org/software/tar/manual/tar.html)

## 資料流：先打包，再壓縮

{% mermaid %}
flowchart TB
    Files["檔案、目錄與中繼資料"] -->|tar 封裝| Tar["tar 資料流"]
    Tar -->|gzip 壓縮| Gzip["project.tar.gz"]
{% endmermaid %}

由上往下讀，箭頭代表資料轉換。中間的 tar 資料流可以直接交給 gzip，不必先將 `project.tar` 寫入硬碟。

例如 GNU tar 可用以下指令建立 gzip 壓縮封存檔：

```bash
tar -czf project.tar.gz project/
```

`-c` 建立封存檔，`-z` 使用 gzip，`-f` 指定輸出名稱。此處是操作範例，未對實際資料執行備份。

## 同一種封裝，搭配不同壓縮器

| 封裝 | 壓縮器 | 常見副檔名 |
| --- | --- | --- |
| tar | gzip | `.tar.gz` |
| tar | bzip2 | `.tar.bz2` |
| tar | xz | `.tar.xz` |
| tar | zstd | `.tar.zst` |

這是可替換的組合，因此用對照表呈現，不把四個壓縮器畫成依序執行的步驟。

`tar` 可記錄檔案權限、目錄與 symbolic link 等資訊。實際還原結果仍受封存格式、選項、執行權限與目標檔案系統影響，不能僅憑副檔名保證完整保留所有系統資訊。[GNU tar 格式與選項](https://www.gnu.org/s/tar/manual/html_chapter/Formats.html)

<!-- endtab -->

<!-- tab 原理-->

非失真壓縮（lossless compression）要求解壓後，原始資料的每個 byte 都能完整還原。它利用可重複利用的模式或符號分布，改變資料的表示方式。

## 重複資料可以用次數描述

假設原始資料有 20 個 `A`：

```text
AAAAAAAAAAAAAAAAAAAA
```

教學上可以把它描述成「字元 A，重複 20 次」。這是 run-length encoding（RLE）的概念。解碼端必須知道次數與字元如何編碼，才能避免把原本就含有數字的資料誤讀。

| 內容 | 概念表示 | 還原結果 |
| --- | --- | --- |
| 20 個相連的 `A` | `(A, 20)` | 原本的 20 個 `A` |

這張表是概念示例，不是 ZIP 或 DEFLATE 的實際儲存語法。

## 壓縮後不一定更小

短資料的檔頭、碼表與封裝成本可能超過節省的空間；已壓縮或缺少可利用模式的資料也可能難以再縮小。

不存在能把每一種可能輸入都縮小的可逆演算法。同長度的原始資料種類，比所有更短表示能容納的種類還多，不可能讓它們全部一對一對應到更短結果。[RFC 1951](https://www.rfc-editor.org/rfc/rfc1951)

<!-- endtab -->

<!-- tab Web Server 的 log 打包成 ZIP，傳到備份伺服器-->

假設 Web Server 一天產生 500 MB 的 `access.log`，其中包含以下教學資料。日期、請求方法與路徑會反覆出現，但實際可壓縮程度仍取決於整份內容。

```text
2026-09-06 10:01:01 INFO GET /api/users 200
2026-09-06 10:01:02 INFO GET /api/users 200
2026-09-06 10:01:03 INFO GET /api/users 200
2026-09-06 10:01:04 INFO GET /api/products 200
```

## 備份資料往哪裡走？

{% mermaid %}
flowchart TB
    Log["Web Server：access.log"] -->|封裝與壓縮| Zip["access.zip"]
    Zip -->|傳送封存檔| Backup["備份伺服器：access.zip"]
{% endmermaid %}

由上往下讀，箭頭表示假設備份情境的資料移動。本圖未指定傳輸協定、重試或接收確認；保存 ZIP 也不代表已驗證能還原，完整備份作業還需另行驗證。

## Step 1：讀取原始 bytes

壓縮器處理的是 bytes，不需要先理解紀錄檔的業務意義。例如 `INFO` 在 ASCII 中，每個字元使用一個 byte：

| 字元 | 二進位 |
| --- | --- |
| `I` | `01001001` |
| `N` | `01001110` |
| `F` | `01000110` |
| `O` | `01001111` |

## Step 2：用 LZ77 表達重複片段

假設前面已輸出 `INFO GET /api/users 200`，後面又出現相同內容，就有機會改用「往回多少 bytes、複製多長」表示。

這段 ASCII 字串共 **23 bytes**，可以手算為 `4 + 1 + 3 + 1 + 10 + 1 + 3`。概念上可用 `(length = 23, distance = 實際回溯距離)` 代替重複片段；距離必須依當時位置計算，不能只憑字串內容填入。

若沒有可採用的匹配，就保留 literal，也就是直接表示原始 byte。這是教學上的處理概念，實際壓縮器會評估匹配與編碼成本。

## Step 3：編碼 literal 與 length/distance

<div class="compression-wide-diagram">

{% mermaid %}
flowchart TB
    Bytes["原始 bytes"] -->|尋找可用的歷史匹配| Match{"採用匹配？"}
    Match -->|是| Pair["length 與 distance"]
    Match -->|否| Literal["literal byte"]
    Pair --> Encode["Huffman 碼與必要的額外 bits"]
    Literal --> Encode
    Encode --> Output["DEFLATE 壓縮區塊資料"]
{% endmermaid %}

</div>

窄螢幕可在圖內左右捲動。由上往下讀，兩個分支代表單一位置的表示選擇。圖聚焦使用 Huffman 編碼的區塊，省略檔頭與區塊結束符號，也不包含不壓縮區塊。

Huffman 編碼處理的是 literal、長度與距離符號，不是直接把整個 `INFO` 或 `/api/users` 當成單一符號。長度與距離可能還需額外 bits 才能表示確切值。

`DEFLATE` 允許不壓縮、固定 Huffman 碼，以及動態 Huffman 碼三種區塊。因此「每次都統計整份 log，再用新的 Huffman 碼壓一次」並不準確。[RFC 1951 §3.2](https://www.rfc-editor.org/rfc/rfc1951)

## Step 4：封裝、傳送與還原

壓縮區塊放入 ZIP 項目後，工具再組成封存檔。備份端使用相容解壓工具，才能依格式把資料還原成原始 bytes。資料傳輸機制是另一層責任，與 DEFLATE 如何編碼資料分開討論。

<!-- endtab -->

<!-- tab Huffman coding-->

`Huffman coding` 依符號權重配置不同長度的編碼，讓高頻符號取得較短或不長於低頻符號的碼。不同頻率的符號仍可能有相同碼長。[RFC 1951 §3.2.2](https://www.rfc-editor.org/rfc/rfc1951)


## 假設資料只有三種字元

假設資料只有三種字元，共 10 個

```bash
AAAAAABBBC
```

| 字元 | 次數 | 固定長度碼 | 本例 Huffman 碼 | Huffman 資料位元數 |
| --- | --- | --- | --- | --- |
| `A` | 6 | `00` | `0` | 6 × 1 = 6 |
| `B` | 3 | `01` | `10` | 3 × 2 = 6 |
| `C` | 1 | `10` | `11` | 1 × 2 = 2 |
| 合計 | 10 | 20 bits |  | 14 bits |

固定長度碼需要 `10 × 2 = 20 bits`；本例的 Huffman 資料編碼需要 `6 × 1 + 3 × 2 + 1 × 2 = 14 bits`

```bash
原始資料：AAAAAABBBC
逐字編碼：0 0 0 0 0 0 10 10 10 11
串接結果：00000010101011
```

這個比較只計算資料本身的碼長，尚未加入碼表、資料長度、封裝及 byte 對齊成本。若直接以 ASCII 儲存，10 個字元則是 80 bits；它與「三種符號各用 2 bits」是不同基準。

## 沒有分隔符號，如何知道字元邊界？

本例 `0`、`10`、`11` 具有 prefix-free 性質，任何一個完整碼都不是另一個碼的前綴。因此讀到 `0` 就能辨識 `A`，讀到 `1` 則還需再讀一個 bit。下一個分頁把這個判斷畫成樹。


<!-- endtab -->

<!-- tab Huffman tree-->


思考歷程是這樣

```bash
我要壓縮
↓
高頻 Symbol 應該用短 Code
↓
所以不同 Symbol 的 Code 長度會不同
↓
那我要怎麼設計一組「不同長度、又能連續解碼」的 0/1 Code？
↓
開始思考所有可能的 bit prefix
↓
0、1
↓
00、01、10、11
↓
000、001、010、011...
↓
這些 prefix 天生就形成 Binary Tree

```

目前已經理解 A 很常出現 → Code 短，D 很少出現 → Code 長一點沒關係，所以我們想要

- A → 可能 1 bit
- B → 可能 2 bits
- C → 可能 3 bits
- D → 可能 3 bits


問題變成「有哪些 bit Code 可以分？」


我們開始列所有可能的 binary string


長度 1

```bash
0
1
```

長度 2

```bash
00
01
10
11
```

長度 3

```bash
000
001
010
011
100
101
110
111
```


加一個 bit，其實只有兩種可能，原本的 Code + 0、原本的 Code + 1，這就是 Binary Tree，當我們把所有可能的 Code 畫出來，就能呈現出所有可能的 binary prefix code，每往下一層多使用 1 bit，所以 Tree depth = Code length，因此高頻 Symbol 表示 Code 要短，也就代表 Code length 要小，轉換成 Tree 就是 Tree depth 要小，因此把它放得靠近 Root


```bash
                    ""
                 /      \
               0          1
             /  \        /  \
           00    01    10    11
          / \    / \    / \    / \
       000 001 010 011 100 101 110 111

```


現在我們有

```bash
A = 8 次
B = 2 次
C = 1 次
D = 1 次
```

想讓 A 只使用一個 bit，那可以從 A = 0 開始。畫到 Tree

```bash
             root
            /
           A
           0
```

但這時候有一件非常重要的事情發生，那就是

```bash
00
01
000
001
010
011
...
```

全部不能再分給其他 Symbol，假設 A = 0，而 B = 01，今天收到 01，讀到第一個 0 時 0 = A，可是繼續讀又有 01 = B，邊界就產生歧義，也就是說 A 已經是 Leaf!


## Tree 表示「Code 長度」


每往下一層就多付 1 bit，所以 Tree 的深度直接等於這個 Symbol 的儲存成本。我們原本的思考是怎麼讓高頻資料用比較少 bit 會變成怎麼讓高頻 Symbol 靠近 Root？ 因為「最佳 bit 長度」這種抽象問題，現在變成「怎麼安排 Tree」這種結構問題。



## Tree 表示「哪些 Code 還能使用」

某個節點一旦分配給 Symbol，它下面整個 subtree 都必須封掉，Tree 可以直接把 Prefix 衝突變成結構限制。例如 A = 0 則代表

```bash
       0 ← A
      / \
     X   X
```

00、01、000……全部不能用了，所以所有 Symbol 放 Leaf


## 3. Tree 表示「解碼流程」

編碼時 root-to-leaf 是 Code，解碼時拿 Code 反過來走同一條路，因此同一個結構同時描述了編碼規則與解碼規則。例如 C = 110 就是


```bash
root
 ↓ 1
右
 ↓ 1
右
 ↓ 0
左
 ↓
C
```


所以收到 110，解碼器完全不用猜 Code 長度


## Huffman Algorithm


A = 50
B = 30
C = 15
D = 5

如果有兩個 Symbol 必須被安排到最深處，直覺上應該選 C = 15、D = 5，然後讓它們成為 siblings：

```bash
       ●
      / \
     C   D
```

一旦 C、D 成為 siblings，它們共同的父節點可以看成一個「群組」C + D = 15 + 5 = 20

於是原問題

A = 50
B = 30
C = 15
D = 5

縮小成

A = 50
B = 30
CD = 20


接著繼續做同樣的事情


<!-- endtab -->


{% endtabs %}
