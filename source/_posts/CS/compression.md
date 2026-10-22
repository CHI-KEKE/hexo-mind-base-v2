---
title: Lossless Compression
date: 2026-09-06 11:23:03
categories: CS
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/cs/compress-1-landing.png
cover : https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/cs/compress-1-landing.png
tags:
toc:
toc_number:
comments :
---

{% tabs Lossless Compression %}

<!-- tab 為甚麼有不同格式的定義-->

<style>
#article-container{--cozy-paper:#fbf7ef;--cozy-surface:#fffdf8;--cozy-ink:#4a3a28;--cozy-muted:#6b5c46;--cozy-line:#e5d8c0;--cozy-green:#547a3d;--cozy-bear:#95613d;--cozy-code:#efe5d3;--cozy-node:#edf2e2;--cozy-edge:#6b7653;color:var(--cozy-ink);}
#article-container .tabs{border:1px solid var(--cozy-line);border-radius:22px;background:var(--cozy-paper);box-shadow:0 8px 28px rgba(90,70,40,.08);}
#article-container .tabs>.nav-tabs{padding:12px;gap:7px;background:var(--cozy-paper);border-bottom:1px dashed var(--cozy-line);}
#article-container .tabs>.nav-tabs>.tab{border:1px solid var(--cozy-line);border-radius:18px;background:var(--cozy-surface);color:var(--cozy-muted);font-size:13px;padding:7px 13px;line-height:1.65;transition:background .15s;}
#article-container .tabs>.nav-tabs>.tab.active{background:var(--cozy-green);border-color:var(--cozy-green);color:#fffdf3;}
#article-container .tabs>.nav-tabs>.tab:hover{border-color:var(--cozy-bear);}
#article-container .tabs>.nav-tabs>.tab:focus-visible{outline:3px solid var(--cozy-bear);outline-offset:2px;}
#article-container .tab-item-content{line-height:1.95;}
#article-container h2{color:var(--cozy-ink);font-size:1.3rem;margin:34px 0 20px;padding:0 0 12px;border-bottom:2px dashed var(--cozy-line);}
#article-container h2::before{content:'🌿';font-size:1rem;margin-right:10px;position:static;display:inline-block;}
#article-container h3{color:var(--cozy-bear);font-size:1.08rem;margin:26px 0 14px;}
#article-container a{color:var(--cozy-green);text-decoration:underline;text-decoration-color:var(--cozy-line);text-underline-offset:4px;}
#article-container strong{color:var(--cozy-ink);}
#article-container :not(pre)>code{color:var(--cozy-bear);background:var(--cozy-code);border-radius:6px;padding:2px 5px;overflow-wrap:anywhere;}
#article-container table{width:auto;max-width:100%;border-collapse:separate;border-spacing:0;border:1px solid var(--cozy-line);border-radius:14px;overflow:hidden;background:var(--cozy-surface);font-size:.9rem;}
#article-container table th{background:var(--cozy-node);color:var(--cozy-ink);font-weight:700;}
#article-container table td,#article-container table th{border:0;border-bottom:1px solid var(--cozy-line);padding:11px 14px;}
#article-container table tr:last-child td{border-bottom:0;}
#article-container table tr{background:transparent;}
#article-container table tr:nth-child(even){background:var(--cozy-paper);}
#article-container table tr:hover{background:var(--cozy-node);}
#article-container .highlight{border-radius:14px;border:1px solid var(--cozy-line);background:var(--cozy-surface);}
#article-container .highlight table{border:0;border-radius:0;background:transparent;}
#article-container .highlight td{border:0;padding:0;}
#article-container .highlight .highlight-tools{background:var(--cozy-node);color:var(--cozy-muted);}
#article-container .highlight .code{background:var(--cozy-surface);color:var(--cozy-ink);}
#article-container .highlight .gutter{background:var(--cozy-paper);color:var(--cozy-muted);}
#article-container .highlight pre{background:transparent;color:var(--cozy-ink);}
#article-container .cozy-hero{position:relative;overflow:hidden;border-radius:22px;padding:32px 30px 66px;margin:0 0 28px;background:radial-gradient(ellipse at 5% 10%,#88a86955,transparent 65%),linear-gradient(150deg,#6f9250,#547a3d 55%,#3f5f2e);color:#fbf8ef;box-shadow:0 8px 22px #3f5f2e22;}
#article-container .cozy-hero .ch-title{font-size:1.65rem;font-weight:750;line-height:1.55;margin-bottom:12px;color:#fff9eb;}
#article-container .cozy-hero .ch-desc{font-size:1rem;line-height:1.9;color:#f4f4e7;max-width:95%;}
#article-container .cozy-hero .ch-bear{position:absolute;bottom:12px;right:28px;font-size:2.2rem;}
#article-container .cozy-hero .ch-flower{position:absolute;bottom:20px;left:30px;letter-spacing:18px;opacity:.8;font-size:1.15rem;}
#article-container .tab-item-content:first-child>ul{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;padding:0;list-style:none;}
#article-container .tab-item-content:first-child>ul>li{margin:0;padding:18px 20px;border:1px solid var(--cozy-line);border-radius:20px;background:var(--cozy-surface);box-shadow:0 4px 12px #785a320a;}
#article-container .tab-item-content:first-child>ul>li::before{display:none;}
#article-container .tab-item-content:first-child>ul>li strong{display:block;margin-bottom:6px;color:var(--cozy-bear);}
#article-container .tab-item-content:first-child>ul>li:nth-child(3n)>strong{color:var(--cozy-green);}
#article-container ol{list-style:none;counter-reset:cozy-step;padding-left:46px;position:relative;}
#article-container ol::before{content:'';position:absolute;left:16px;top:10px;bottom:12px;width:2px;background:var(--cozy-line);}
#article-container ol>li{position:relative;counter-increment:cozy-step;margin:0 0 18px;padding:0 0 0 5px;}
#article-container ol>li::before{content:counter(cozy-step);position:absolute;left:-45px;top:0;width:31px;height:31px;line-height:29px;text-align:center;border:1px solid var(--cozy-bear);border-radius:50%;background:var(--cozy-surface);color:var(--cozy-bear);font-weight:700;}
#article-container .mermaid-wrap{border:1px solid var(--cozy-line);border-radius:18px;background:var(--cozy-surface);padding:18px 8px;margin:18px 0;box-shadow:0 4px 14px #785a3208;}
#article-container .mermaid-wrap svg .node rect,#article-container .mermaid-wrap svg .node polygon,#article-container .mermaid-wrap svg .node circle{fill:var(--cozy-node)!important;stroke:var(--cozy-green)!important;stroke-width:1.4px!important;}
#article-container .mermaid-wrap svg .node rect{rx:10px;ry:10px;}
#article-container .mermaid-wrap svg .nodeLabel,#article-container .mermaid-wrap svg .edgeLabel,#article-container .mermaid-wrap svg .edgeLabel p{color:var(--cozy-ink)!important;background:var(--cozy-surface)!important;}
#article-container .mermaid-wrap svg .flowchart-link{stroke:var(--cozy-edge)!important;}
#article-container .mermaid-wrap svg marker path{fill:var(--cozy-edge)!important;stroke:var(--cozy-edge)!important;}
#article-container .compression-wide-diagram{max-width:100%;overflow-x:auto;scrollbar-color:var(--cozy-bear) var(--cozy-paper);}
#article-container .compression-wide-diagram .mermaid-wrap{min-width:520px;}
#article-container .tab-to-top{background:var(--cozy-paper);}
#article-container .tab-to-top button{color:var(--cozy-green);}
[data-theme='dark'] #article-container{--cozy-paper:#252a22;--cozy-surface:#30372b;--cozy-ink:#f0e8d8;--cozy-muted:#d0c5b2;--cozy-line:#535b46;--cozy-green:#adc38b;--cozy-bear:#e1b48b;--cozy-code:#424334;--cozy-node:#414c35;--cozy-edge:#c6d4ae;}
[data-theme='dark'] #article-container .tabs>.nav-tabs>.tab.active{background:#547a3d;border-color:#adc38b;}
@media(max-width:600px){ #article-container .cozy-hero{padding:24px 20px 64px;}#article-container .cozy-hero .ch-title{font-size:1.35rem;}#article-container .cozy-hero .ch-desc{max-width:100%;}#article-container .tab-item-content:first-child>ul{grid-template-columns:1fr;}#article-container h2{font-size:1.18rem;}#article-container table td,#article-container table th{padding:9px 10px;}#article-container .tabs>.nav-tabs{padding:9px;gap:6px;}#article-container .tabs>.nav-tabs>.tab{font-size:12px;}}
</style>

<div class="cozy-hero">
<div class="ch-title">把資料縮小，把內容留下</div>
<div class="ch-desc">同一批檔案，寄給別人、長期備份與搬移 Linux 目錄時，適合的封裝方式可能不同。壓縮要在檔案大小、處理時間、記憶體用量與接收端支援之間取捨。</div>
<span class="ch-flower" aria-hidden="true">🌼 🌿 🌼</span><span class="ch-bear" aria-hidden="true">🐻</span>
</div>

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

- **儲存與傳輸量** 壓縮後還剩多少資料。
- **處理時間** 壓縮與解壓縮要分別量測。
- **資源成本** CPU、RAM 與磁碟 I/O 是否符合執行環境。
- **封裝功能** 是否需要加密、分卷、修復資訊與檔案權限。
- **讀取方式** 是否要串接串流，或只取出封存檔中的個別檔案。

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

這裡的 `image.jpg` 採 `Store` 只是示例，不是依副檔名必然採用的規則。封存與壓縮是兩個不同層次，因此 `.zip` 也可能沒有縮小內容。

<!-- endtab -->

<!-- tab RAR-->

`RAR` 是檔案格式，WinRAR 是可操作該格式的工具。兩個名稱分別代表封裝結果與使用軟體。

## 分卷與修復資訊

大型檔案可分成數個封存分卷，例如：

```bash
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

```bash
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

```bash
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

Huffman 編碼處理的是 literal、長度與距離符號，不是直接把整個 `INFO` 或 `/api/users` 當成單一符號。長度與距離可能還需額外 bits 才能表示確切值。

`DEFLATE` 允許不壓縮、固定 Huffman 碼，以及動態 Huffman 碼三種區塊。因此「每次都統計整份 log，再用新的 Huffman 碼壓一次」並不準確。[RFC 1951 §3.2](https://www.rfc-editor.org/rfc/rfc1951)

## Step 4：封裝、傳送與還原

壓縮區塊放入 ZIP 項目後，工具再組成封存檔。備份端使用相容解壓工具，才能依格式把資料還原成原始 bytes。資料傳輸機制是另一層責任，與 DEFLATE 如何編碼資料分開討論。

<!-- endtab -->

<!-- tab Huffman coding-->

`Huffman coding` 依符號權重配置不同長度的編碼，讓高頻符號取得較短或不長於低頻符號的碼。不同頻率的符號仍可能有相同碼長。[RFC 1951 §3.2.2](https://www.rfc-editor.org/rfc/rfc1951)

## 假設資料只有三種字元

以下資料只有三種字元，共 10 個：

```bash
AAAAAABBBC
```

| 字元 | 次數 | 固定長度碼 | 本例 Huffman 碼 | Huffman 資料位元數 |
| --- | --- | --- | --- | --- |
| `A` | 6 | `00` | `0` | 6 × 1 = 6 |
| `B` | 3 | `01` | `10` | 3 × 2 = 6 |
| `C` | 1 | `10` | `11` | 1 × 2 = 2 |
| 合計 | 10 | 20 bits |  | 14 bits |

固定長度碼需要 `10 × 2 = 20 bits`；本例的 Huffman 資料編碼需要 `6 × 1 + 3 × 2 + 1 × 2 = 14 bits`。

```bash
原始資料：AAAAAABBBC
逐字編碼：0 0 0 0 0 0 10 10 10 11
串接結果：00000010101011
```

這個比較只計算資料本身的碼長，尚未加入碼表、資料長度、封裝及 byte 對齊成本。若直接以 ASCII 儲存，10 個字元則是 80 bits；它與「三種符號各用 2 bits」是不同基準。

## 沒有分隔符號，如何知道字元邊界？

本例 `0`、`10`、`11` 具有 prefix-free 性質，任何一個完整碼都不是另一個碼的前綴。因此讀到 `0` 就能辨識 `A`，讀到 `1` 則還需再讀一個 bit

<!-- endtab -->

<!-- tab Huffman tree-->

高頻符號使用短碼，可以降低總位元數。接下來的問題是：長短不同的碼連在一起時，要如何辨識每個符號的邊界？二元樹可以同時表達碼長、可用前綴與解碼路徑。

前一頁使用三個符號示範位元數，本頁先用四個符號說明前綴限制，再完成一組四符號的 Huffman 建樹範例。

## 從變長編碼走到二元樹

1. 希望高頻符號使用較短的碼，讓每次出現時少占一些 bits。
2. 碼長不同後，必須設計能辨識符號邊界的規則。
3. 二進位碼每延伸一個 bit，只能接上 `0` 或 `1`。
4. 把相同前綴放在同一條路徑上，就形成二元樹。

### 前綴樹：每往下一層，就多一個 bit

<div class="compression-wide-diagram">

{% mermaid %}
flowchart TB
    Root["空前綴：0 bits"] -->|0| Zero["0：1 bit"]
    Root -->|1| One["1：1 bit"]
    Zero -->|0| ZeroZero["00：2 bits"]
    Zero -->|1| ZeroOne["01：2 bits"]
    One -->|0| OneZero["10：2 bits"]
    One -->|1| OneOne["11：2 bits"]
{% endmermaid %}

</div>

由根往下讀，邊上的 bit 依序串接成節點的前綴。圖只展開到深度 2；這是候選 bit 字串的結構，還不是已分配符號的 Huffman 碼表

| 碼長 | 所有候選字串 |
| --- | --- |
| 1 bit | `0`、`1` |
| 2 bits | `00`、`01`、`10`、`11` |
| 3 bits | `000`、`001`、`010`、`011`、`100`、`101`、`110`、`111` |

例如 `110` 就是從根沿著 `1`、`1`、`0` 走三條邊。以根的深度為 0，**碼長等於葉節點的深度**。

## Tree 表示「哪些 Code 還能使用」

先看一組示意頻率：`A = 8`、`B = 2`、`C = 1`、`D = 1`。假設把 `0` 分配給最常出現的 `A`，就不能再把 `00`、`01` 或任何以 `0` 開頭的較長碼分給其他符號。

這是 prefix-free 的限制：完整碼不能同時是另一個完整碼的前綴。對應到樹，就是符號放在葉節點，葉節點下方不再延伸其他符號。[IISc：Huffman Code Construction](https://gtl.csa.iisc.ac.in/dsa/node88.html)

| 已做的選擇 | 對其餘候選碼的影響 |
| --- | --- |
| `A = 0` | `00`、`01`、`000`、`001` 等不能再分配 |
| `1` 尚未分配給符號 | 可繼續延伸成 `10`、`11` |
| 再選 `B = 10` | `100`、`101` 等不能再分配 |
| `11` 仍未分配給符號 | 可延伸成 `C = 110`、`D = 111` |

這樣就得到一組可用碼：`A = 0`、`B = 10`、`C = 110`、`D = 111`，碼長分別是 1、2、3、3 bits。

### 前綴衝突會帶來什麼問題？

若同時指定 `A = 0` 與 `B = 01`，讀到第一個 `0` 時，就不能採用「遇到完整碼立即輸出」的解碼方式，因為它也可能是 `B` 的開頭。

如果又指定 `C = 1`，同一串 `01` 就能解成 `B`，也能解成 `A` 接 `C`，形成明確歧義。前綴衝突會破壞即時解碼；是否連整串資料都無法唯一解碼，則要看完整碼表。

## Tree 表示「Code 長度」

每個符號出現一次，就要付出一次碼長成本。因此在頻率固定時，可以用以下公式比較碼表：

**總資料位元數 = 各符號的「出現次數 × 碼長」加總。**

沿用剛才的示意頻率與碼表：

| 符號 | 次數 | 編碼 | 深度／碼長 | 資料位元數 |
| --- | --- | --- | --- | --- |
| `A` | 8 | `0` | 1 | 8 |
| `B` | 2 | `10` | 2 | 4 |
| `C` | 1 | `110` | 3 | 3 |
| `D` | 1 | `111` | 3 | 3 |
| 合計 | 12 |  |  | 18 bits |

高頻符號每多一層，增加的總成本就更多。「讓常見符號使用短碼」因此可以轉成「讓常見符號的葉節點靠近根」。不同頻率仍可能有相同深度，例如這裡的 `C` 與 `D`。

## Tree 表示「解碼流程」

編碼時，從根到符號葉節點的路徑決定碼字。解碼時，也從根出發，依收到的 bits 走到葉節點；走的是同一個方向，不是從葉節點反向走回根。

以 `C = 110` 為例：

| 步驟 | 讀到的 bit | 到達的位置 | 是否輸出符號 |
| --- | --- | --- | --- |
| 1 | `1` | 前綴 `1` | 否，繼續讀 |
| 2 | `1` | 前綴 `11` | 否，繼續讀 |
| 3 | `0` | 葉節點 `C` | 是，輸出後回到根 |

所以 `010110111` 可以依序切成 `0 / 10 / 110 / 111`，解成 `ABCD`。解碼端必須先知道碼表或等價的樹結構；實際格式也要交代資料結束位置，避免把填補 bits 當成內容。

## Huffman Algorithm：反覆合併最小權重

前面先指定碼表，說明樹能表達什麼。現在換成另一組教學頻率，讓演算法自動決定樹形：

| 符號 | 出現次數 |
| --- | --- |
| `A` | 50 |
| `B` | 30 |
| `C` | 15 |
| `D` | 5 |

從每個符號各自一棵樹開始，每輪選出權重最小的兩棵，合成新樹，再把它放回候選集合。新根的權重是兩棵子樹權重的總和，直到只剩一棵樹。[IISc：Huffman Code Construction](https://gtl.csa.iisc.ac.in/dsa/node88.html)

### 合併過程：每輪都重新比較候選權重

| 輪次 | 目前候選權重 | 選出的兩項 | 合併後留下 |
| --- | --- | --- | --- |
| 1 | `D:5`、`C:15`、`B:30`、`A:50` | `D:5` 與 `C:15` | `CD:20`、`B:30`、`A:50` |
| 2 | `CD:20`、`B:30`、`A:50` | `CD:20` 與 `B:30` | `BCD:50`、`A:50` |
| 3 | `BCD:50`、`A:50` | 剩下的兩棵樹 | `ABCD:100` |

`CD` 與 `BCD` 是內部群組，不是新增到原始資料的符號。群組仍保留自己的子樹，所以合併後不會失去各個符號。

### 最終編碼樹：由根向下讀出碼字

<div class="compression-wide-diagram">

{% mermaid %}
flowchart TB
    Root["總權重 100"] -->|0| A["A：50"]
    Root -->|1| BCD["BCD：50"]
    BCD -->|0| B["B：30"]
    BCD -->|1| CD["CD：20"]
    CD -->|0| C["C：15"]
    CD -->|1| D["D：5"]
{% endmermaid %}

</div>

建樹時由小樹往上合併，讀碼時則從根往下走。圖中的數字是頻率權重，邊上的 `0`、`1` 才是編碼；本例選擇左分支為 `0`、右分支為 `1`

| 符號 | 頻率 | 本例編碼 | 碼長 | 資料位元數 |
| --- | --- | --- | --- | --- |
| `A` | 50 | `0` | 1 | 50 |
| `B` | 30 | `10` | 2 | 60 |
| `C` | 15 | `110` | 3 | 45 |
| `D` | 5 | `111` | 3 | 15 |
| 合計 | 100 |  | 平均 1.7 bits／符號 | 170 bits |

這組資料若每個符號固定使用 2 bits，共需 200 bits；本例 Huffman 資料編碼是 170 bits，少了 30 bits。這裡仍只比較資料碼長，尚未計入碼表、封裝與對齊成本。

### 為什麼是合併最小的兩項？

合併兩棵子樹時，裡面每個符號的深度都會增加 1，所以新增成本就是兩棵子樹的權重總和。先讓小權重承擔這個成本，是理解 Huffman 貪婪選擇的切入點。

以本例核對，每輪新增成本是 `20`、`50`、`100`，加總恰好是 `170 bits`。這與最終碼表逐項計算的結果相同，因為每次合併增加的一層都會算進葉節點深度。

Huffman 的最適性針對給定頻率、逐符號的二元前綴碼，目標是最小化加權碼長；它不保證在所有壓縮方法或含封裝成本的檔案中都最小。相同權重可有不同合併選擇，左右分支也能交換，因此最佳碼表未必唯一。[IISc：Huffman Code Construction](https://gtl.csa.iisc.ac.in/dsa/node88.html)

<!-- endtab -->

{% endtabs %}
