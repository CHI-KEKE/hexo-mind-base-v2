---
title: RAM and Pointer
date: 2026-08-15 10:39:03
categories: CS
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/CS/memory-pointer-landing.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/CS/memory-pointer-landing.png
tags:
toc:
toc_number:
comments :
---

{% tabs RAM and Pointer%}

<!-- tab 打開一個遊戲-->

<style>
.cozy-hero { position:relative; overflow:hidden; border-radius:20px; padding:34px 38px; margin:24px 0 30px; background:radial-gradient(circle at 15% 20%, rgba(255,255,255,.10) 0, transparent 45%), linear-gradient(150deg, #6f9250 0%, #547a3d 55%, #3f5f2e 100%); color:#fbf8ef; }
.cozy-hero .ch-dot { position:absolute; font-size:1.4rem; opacity:.55; pointer-events:none; }
.cozy-hero .ch-dot.d1 { top:16px; right:70px; }
.cozy-hero .ch-dot.d2 { bottom:20px; right:26px; font-size:1.1rem; opacity:.4; }
.cozy-hero .ch-dot.d3 { top:50%; right:130px; font-size:.9rem; opacity:.35; }
.cozy-hero .ch-bear { position:absolute; bottom:10px; right:96px; font-size:2.1rem; opacity:.9; filter:drop-shadow(0 3px 4px rgba(0,0,0,.2)); pointer-events:none; }
.cozy-hero .ch-tag { display:inline-block; font-size:.72rem; letter-spacing:2px; text-transform:uppercase; background:rgba(255,255,255,.16); border:1px solid rgba(255,255,255,.32); padding:3px 12px; border-radius:20px; margin-bottom:14px; }
.cozy-hero .ch-title { margin:0 0 10px; font-size:1.4rem; font-weight:700; position:relative; z-index:1; }
.cozy-hero .ch-desc { max-width:80%; font-size:.92rem; line-height:1.85; color:#eef1e2; position:relative; z-index:1; }
.cozy-hero .ch-desc code { background:rgba(255,255,255,.2); padding:1px 6px; border-radius:3px; color:#fffaf0; }
.cozy-feature-row { display:flex; flex-wrap:wrap; gap:16px; margin:18px 0 28px; }
.cozy-feature-row .cf-item { flex:1 1 160px; background:#fbf7ef; border:1px solid #ecdfc9; border-radius:18px; padding:20px 18px; text-align:center; box-shadow:0 4px 12px rgba(120,90,50,.08); }
.cozy-feature-row .cf-icon { width:44px; height:44px; margin:0 auto 10px; border-radius:50%; background:#c48a5e; color:#fff8ea; display:flex; align-items:center; justify-content:center; font-size:1.15rem; }
.cozy-feature-row .cf-title { font-weight:700; font-size:.92rem; color:#4a3a28; margin-bottom:6px; }
.cozy-feature-row .cf-desc { font-size:.8rem; line-height:1.7; color:#6b5c46; }
.cozy-feature-row .cf-desc code { background:#f1e6d2; padding:1px 6px; border-radius:3px; color:#8a5a2e; }
.cozy-card-grid { display:flex; flex-wrap:wrap; gap:16px; margin:16px 0 26px; }
.cozy-card { flex:1 1 220px; border-radius:22px; padding:20px 20px 22px; box-shadow:0 6px 14px rgba(90,70,40,.14); }
.cozy-card.bear { background:linear-gradient(155deg,#c48a5e,#a06a41); color:#fff8ea; }
.cozy-card.cream { background:#fbf7ef; border:1px solid #ecdfc9; color:#4a3a28; }
.cozy-card.moss { background:linear-gradient(155deg,#7a9a5e,#57753f); color:#f4f7ea; }
.cozy-card .cc-badge { display:inline-flex; align-items:center; justify-content:center; width:32px; height:32px; border-radius:50%; background:rgba(0,0,0,.14); font-size:.9rem; margin-bottom:10px; }
.cozy-card.cream .cc-badge { background:#f1e6d2; }
.cozy-card .cc-title { font-weight:700; font-size:.96rem; margin-bottom:6px; }
.cozy-card .cc-desc { font-size:.82rem; line-height:1.75; }
.cozy-card.bear .cc-desc code, .cozy-card.moss .cc-desc code { background:rgba(255,255,255,.22); padding:1px 6px; border-radius:3px; color:#fffaf0; font-size:.85em; }
.cozy-card.cream .cc-desc code { background:#f1e6d2; padding:1px 6px; border-radius:3px; color:#8a5a2e; font-size:.85em; }
.cozy-line-steps { position:relative; margin:22px 0 30px; padding-left:56px; }
.cozy-line-steps::before { content:''; position:absolute; left:19px; top:4px; bottom:4px; width:2px; background:linear-gradient(180deg, #c48a5e, #7a9a5e); opacity:.55; }
.cozy-line-steps .cl-step { position:relative; margin-bottom:26px; }
.cozy-line-steps .cl-step:last-child { margin-bottom:0; }
.cozy-line-steps .cl-num { position:absolute; left:-56px; top:0; width:38px; height:38px; border-radius:50%; background:#fbf7ef; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:.9rem; z-index:2; box-shadow:0 2px 6px rgba(90,70,40,.18); }
.cozy-line-steps .cl-step.bear .cl-num { border:2px solid #a06a41; color:#a06a41; }
.cozy-line-steps .cl-step.moss .cl-num { border:2px solid #57753f; color:#57753f; }
.cozy-line-steps .cl-body { display:flex; align-items:center; flex-wrap:wrap; gap:10px; min-height:38px; }
.cozy-line-steps .cl-title { font-weight:700; font-size:.95rem; color:#4a3a28; }
.cozy-line-steps .cl-connector { flex:1 1 30px; height:0; border-bottom:1.5px dashed #d8c9ab; min-width:24px; }
.cozy-line-steps .cl-desc { font-size:.82rem; color:#6b5c46; line-height:1.6; }
.cozy-line-steps .cl-desc code { background:#f1e6d2; padding:1px 6px; border-radius:3px; color:#8a5a2e; font-size:.85em; }
.cozy-diagram { background:#fbf7ef; border:1px solid #ecdfc9; border-radius:14px; padding:16px 20px; margin:14px 0 22px; font-family: Consolas, monospace; font-size:.8rem; line-height:1.7; color:#4a3a28; white-space:pre; overflow-x:auto; box-shadow:0 4px 10px rgba(120,90,50,.06); }
.cozy-bullet-card { background:#fbf7ef; border:1px solid #ecdfc9; border-radius:16px; padding:18px 22px; margin:14px 0 22px; }
.cozy-bullet-card .bc-title { font-weight:700; font-size:.92rem; color:#4a3a28; margin-bottom:8px; }
.cozy-bullet-card ul { margin:0; padding-left:20px; }
.cozy-bullet-card li { font-size:.84rem; line-height:1.9; color:#6b5c46; }
.cozy-bullet-card code { background:#f1e6d2; padding:1px 6px; border-radius:3px; color:#8a5a2e; font-size:.85em; }
.cozy-bear-divider { display:flex; align-items:center; gap:14px; margin:26px 0; }
.cozy-bear-divider::before, .cozy-bear-divider::after { content:''; flex:1; height:2px; background:linear-gradient(90deg, transparent, #c48a5e, #7a9a5e, transparent); opacity:.45; }
.cozy-bear-divider .bd-icon { font-size:1.5rem; flex:0 0 auto; }
</style>

今天打開一個遊戲，這個很日常的動作背後，其實就是 RAM（記憶體）開始忙碌的過程。用五個步驟拆開來看

<div class="cozy-hero">
<span class="ch-dot d1">🎮</span><span class="ch-dot d2">🌿</span><span class="ch-dot d3">🌼</span><span class="ch-bear">🐻</span>
<div class="ch-tag">情境導覽</div>
<div class="ch-title">從打開一個遊戲，認識 RAM 的角色</div>
<div class="ch-desc">遊戲原本安靜地待在 SSD 裡，直到啟動之後，RAM 才開始忙碌起來。</div>
</div>

<div class="cozy-line-steps">
<div class="cl-step bear">
<div class="cl-num">01</div>
<div class="cl-body"><span class="cl-title">遊戲原本存在 SSD</span><span class="cl-connector"></span><span class="cl-desc">程式、圖片、音效、地圖資料都安靜地存放在硬碟裡，還沒被使用</span></div>
</div>
<div class="cl-step moss">
<div class="cl-num">02</div>
<div class="cl-body"><span class="cl-title">啟動遊戲</span><span class="cl-connector"></span><span class="cl-desc">作業系統把目前需要的程式與資料，從 SSD 載入 RAM</span></div>
</div>
<div class="cl-step bear">
<div class="cl-num">03</div>
<div class="cl-body"><span class="cl-title">CPU 從記憶體取得資料</span><span class="cl-connector"></span><span class="cl-desc">CPU 讀取 RAM 裡的內容，才能真正執行遊戲</span></div>
</div>
<div class="cl-step moss">
<div class="cl-num">04</div>
<div class="cl-body"><span class="cl-title">開越多程式，RAM 用越多</span><span class="cl-connector"></span><span class="cl-desc">每個程式都要佔用一部分 RAM 空間，同時開的程式越多，剩餘空間越少</span></div>
</div>
<div class="cl-step bear">
<div class="cl-num">05</div>
<div class="cl-body"><span class="cl-title">關機後，RAM 內容通常會消失</span><span class="cl-connector"></span><span class="cl-desc">RAM 屬於揮發性記憶體，需要持續供電才能維持資料</span></div>
</div>
</div>

第一步，遊戲的所有素材都還躺在 SSD 裡：


```bash
└── Game
    ├── 程式
    ├── 圖片
    ├── 音效
    └── 地圖資料
```

第二、三步，啟動遊戲後，資料先載入 RAM，再由 CPU 讀取出來執行：


```bash
SSD
 │
 │ 載入資料
 ▼
RAM
 │
 │ CPU 讀取
 ▼
CPU
 │
 ▼
執行遊戲
```


第四步，`16 GB` 的 RAM 被拆給不同程式使用，這也是為什麼工作管理員裡的用量常常逼近上限：

```bash
16 GB RAM

Chrome      3 GB
VS Code     2 GB
遊戲        6 GB
Discord     1 GB
系統與其他  3 GB
----------------
剩餘        1 GB
```

所以會在工作管理員看到 <code>Memory 13.8 / 16 GB</code>，代表目前有大量 RAM 正被系統與程式使用。

第五步，也是最容易被忽略的一點：因為 RAM 是揮發性記憶體，一旦斷電，內容通常就會不見。假設正在編輯一份還沒儲存的文件，流程是這樣的：

```bash
正在編輯的內容
      ↓
     RAM
      ↓
突然斷電
      ↓
資料可能消失
```

按下「儲存」之後，資料才會真正寫入 SSD 等持久儲存裝置，這也是為什麼「存檔」這個動作這麼重要。

<!-- endtab -->

<!-- tab RAM-->

RAM 的本質可以想成幾十億個極小的電子狀態儲存格，硬體把這些儲存格組織起來，再讓 CPU 用地址找到某一段資料。

<div class="cozy-hero">
<span class="ch-dot d1">🧩</span><span class="ch-dot d2">🌿</span><span class="ch-dot d3">🌼</span><span class="ch-bear">🐻</span>
<div class="ch-tag">觀念拆解</div>
<div class="ch-title">RAM 的兩種樣貌：抽象模型與物理實體</div>
</div>

<div class="cozy-feature-row">
<div class="cf-item">
<div class="cf-icon">📦</div>
<div class="cf-title">抽象模型</div>
<div class="cf-desc">寫程式時最好用的想像，一排連續編號的格子，每格都有自己的地址</div>
</div>
<div class="cf-item">
<div class="cf-icon">🔩</div>
<div class="cf-title">物理實體</div>
<div class="cf-desc">實際硬體是 PCB 電路板搭配 DRAM 晶片，裡面才是真正的記憶體 Cell</div>
</div>
</div>

作為程式設計師的抽象模型，RAM 看起來像這樣：

```bash
RAM
┌────┬────┬────┬────┬────┐
│0x00│0x01│0x02│0x03│0x04│
└────┴────┴────┴────┴────┘
```

但物理世界會更接近這個層級結構：

```bash
RAM 模組
│
├── PCB 電路板
│
├── DRAM 晶片
│    │
│    ├── 大量記憶體 Cell
│    ├── 大量記憶體 Cell
│    ├── 大量記憶體 Cell
│    └── ...
│
└── 控制、訊號與供電線路
```

假設程式執行 <code>char x = 65;</code>，CPU 最後需要操作某個記憶體位置。從軟體角度可以想成：

```bash
Address       Data

0x1000   →    01000001
0x1001   →    00110101
0x1002   →    10101010
0x1003   →    00000000
```

其中 <code>0x1000</code> 就是地址，它比較像門牌號碼。例如「台北市 XX 路 100 號」這串地址本身不是房子，它只是標示出要找的地方。

CPU 給出地址之後，硬體才會去找對應的資料，用高度簡化的流程來看：

<div class="cozy-line-steps">
<div class="cl-step bear">
<div class="cl-num">01</div>
<div class="cl-body"><span class="cl-title">CPU 提出要求</span><span class="cl-connector"></span><span class="cl-desc">我要 <code>Address 0x1000</code> 的資料</span></div>
</div>
<div class="cl-step moss">
<div class="cl-num">02</div>
<div class="cl-body"><span class="cl-title">記憶體系統找到位置</span><span class="cl-connector"></span><span class="cl-desc">透過控制電路，把要求對應到實際的 DRAM 位置</span></div>
</div>
<div class="cl-step bear">
<div class="cl-num">03</div>
<div class="cl-body"><span class="cl-title">DRAM 回傳資料</span><span class="cl-connector"></span><span class="cl-desc">取得 <code>01000001</code> 之後送回給 CPU</span></div>
</div>
</div>

所以程式裡看到 <code>int x = 10;</code>，底層牽涉到的概念就是某段記憶體位置儲存了 <code>x</code> 的資料，內容是 <code>00000000 00000000 00000000 00001010</code>。假設 <code>int</code> 是 4 bytes，它通常會佔用連續的數個 byte 位址。

<!-- endtab -->

<!-- tab Pointer-->

Pointer（指標）就是一個存放記憶體位址的變數。用 C 舉例：

```c
int x = 10;
int *p = &x;
```

<div class="cozy-hero">
<span class="ch-dot d1">📍</span><span class="ch-dot d2">🌿</span><span class="ch-dot d3">🌼</span><span class="ch-bear">🐻</span>
<div class="ch-tag">核心觀念</div>
<div class="ch-title">Pointer 就是存位址的變數</div>
<div class="ch-desc">x 存的是實際的值，p 存的是 x 住在哪個地址。</div>
</div>

先把它想成 RAM 裡的一張對照表：

```bash
Address       Data
────────────────────────
0x1000        10        ← x
...
0x5000        0x1000    ← p
```

`x` 裡面放的是 `10`。`p` 自己也是一個變數，只是它存的資料是 `x` 的位址 `0x1000`。

再看一次完整過程，先有 `int x = 10;`：

<div class="cozy-card-grid">
<div class="cozy-card bear">
<div class="cc-badge">x</div>
<div class="cc-title">變數 x</div>
<div class="cc-desc">地址是 <code>0x1000</code>，值是 <code>10</code></div>
</div>
<div class="cozy-card moss">
<div class="cc-badge">p</div>
<div class="cc-title">指標 p</div>
<div class="cc-desc">地址是 <code>0x5000</code>，值是 <code>0x1000</code>（也就是 x 的地址）</div>
</div>
</div>

接著 `int *p = &x;`，`&x` 的意思就是「給我 x 的記憶體位址」。因此兩者的關係是：

```bash
        p                       x
┌──────────────┐          ┌──────────┐
│    0x1000    │ ───────→ │    10    │
└──────────────┘          └──────────┘
   Address                  Address
   0x5000                   0x1000
```


所以我們常常畫成 `p → x`，但這個箭頭實際表達的意思是，`p` 裡面存著 `x` 的位址，並不是 `p` 跟 `x` 是同一個東西。

<div class="cozy-bear-divider"><span class="bd-icon">🐻</span></div>

<!-- endtab -->

<!-- tab C# ref vs C Pointer-->

看一個經典的交換數值範例，分別用 C# 的 `ref` 與 C 的 `Pointer` 實作。

C#：

```csharp
void Swap(ref int a, ref int b)
{
    int temp = a;
    a = b;
    b = temp;
}

int x = 10;
int y = 20;

Swap(ref x, ref y);
```

結果是 `x = 20`、`y = 10`。

C：

```c
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int x = 10;
int y = 20;

swap(&x, &y);
```

結果一樣是 `x = 20`、`y = 10`。

<div class="cozy-feature-row">
<div class="cf-item">
<div class="cf-icon">C#</div>
<div class="cf-title">ref x</div>
<div class="cf-desc">讓 function 直接操作原本的 <code>x</code></div>
</div>
<div class="cf-item">
<div class="cf-icon">C</div>
<div class="cf-title">&x</div>
<div class="cf-desc">取得 <code>x</code> 地址，傳給 pointer，再用 <code>*x</code> 操作原本的 <code>x</code></div>
</div>
</div>

`ref` 可以當成 `Pointer` 某種用途的高階語言版本，但 `Pointer` 本身還能拿來建立資料結構、走訪陣列、操作動態記憶體、與硬體或 OS API 溝通。

如果直接記成「C Pointer 等於 C# ref」，之後會遇到問題，因為 C 的 pointer 用途廣得多。舉例來說，pointer 可以先宣告成普通變數再指定指向誰：

```c
int a = 10;
int *p;

p = &a;
p = &b;
p = &c;
```

甚至還有 `int **pp = &p;` 這種指標的指標，也就是 Pointer to Pointer。

<div class="cozy-bullet-card">
<div class="bc-title">C Pointer 能做到、但 C# ref 做不到的事</div>
<ul>
<li>修改外部變數（這部分跟 <code>ref</code> 很像）</li>
<li>指向其他資料，之後可以隨時改指向別的目標</li>
<li>進行 Pointer 運算，例如走訪陣列位址</li>
<li>操作動態記憶體，配合 <code>malloc</code>／<code>free</code></li>
<li>建立 Linked List、Tree 等需要「自我指向」的資料結構</li>
<li>用於系統程式設計，直接與硬體或 OS API 溝通</li>
</ul>
</div>

一句話總結，Pointer 讓程式把「記憶體位置」本身當成一個值來保存、傳遞，並透過它存取那個位置上的資料。Pointer 最強的地方，就是「資料在哪裡」這件事情，也能變成程式可以保存和操作的資訊。

<div class="cozy-bear-divider"><span class="bd-icon">🐻</span></div>

<!-- endtab -->

{% endtabs %}