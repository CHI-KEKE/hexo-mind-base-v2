---
title: Ring Buffer
date: 2026-09-10 15:05:03
categories: CS
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/cs/ring-buffer.png
cover: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/cs/ring-buffer.png
tags:
toc:
toc_number:
comments:
---

{% tabs Ring Buffer %}

<!-- tab 有限的資源 -->
<style>
.cozy{background:transparent;color:var(--cozy-ink);border-radius:0;padding:0;line-height:1.95;font-family:'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif}.hero{position:relative;overflow:hidden;background:radial-gradient(ellipse at 5% 10%,#88a86955,transparent 65%),linear-gradient(150deg,#6f9250,#547a3d 55%,#3f5f2e);color:#fbf8ef;border-radius:22px;padding:32px 30px 66px;margin:0 0 28px;box-shadow:0 8px 22px #3f5f2e22}.hero h1{color:#fff9eb;font-size:1.65rem;line-height:1.55;margin:0 0 12px}.hero p{color:#f4f4e7;font-size:1rem;line-height:1.9;max-width:95%}.hero small{color:#f4f4e7;letter-spacing:2px}.grid{display:flex;flex-wrap:wrap;gap:14px;margin:18px 0 26px}.card{flex:1 1 210px;padding:18px 20px;border:1px solid var(--cozy-line);border-radius:20px;background:var(--cozy-surface);box-shadow:0 4px 12px #785a320a}.card h3{color:var(--cozy-bear);margin:0 0 6px}.card p{color:var(--cozy-muted);margin:0;font-size:.9rem}.bear{background:#f3e3d4;color:var(--cozy-ink)}.cream{background:var(--cozy-surface);color:var(--cozy-ink)}.moss{background:#edf2e2;color:var(--cozy-ink)}.pre{background:var(--cozy-surface);color:var(--cozy-ink);border:1px solid var(--cozy-line);border-radius:14px;padding:18px;overflow-x:auto;white-space:pre;font-family:Consolas,monospace}.callout{background:#fff8e9;border:1px solid #e5c98d;border-radius:14px;padding:15px;margin:18px 0;color:var(--cozy-muted)}.arch{background:var(--cozy-surface);border:1px solid var(--cozy-line);border-radius:18px;padding:20px;color:var(--cozy-ink);box-shadow:0 4px 14px #785a3208}.arch h2{color:var(--cozy-ink);font-size:1.3rem;border-bottom:2px dashed var(--cozy-line);padding-bottom:12px}.arch-row{display:flex;gap:14px;flex-wrap:wrap;margin:14px 0}.node{flex:1 1 180px;padding:16px;border:1px solid var(--cozy-line);border-radius:12px;text-align:center;background:var(--cozy-node);color:var(--cozy-ink)}.arch .red{background:#f3e3d4;color:var(--cozy-bear);border-color:#c99d7b}.arch .blue{background:var(--cozy-node);color:var(--cozy-green);border-color:var(--cozy-green)}.arch .green{background:#edf2e2;color:var(--cozy-green);border-color:#9eb77d}.arrow{text-align:center;color:var(--cozy-edge);font-size:1.5rem}.table{width:auto;max-width:100%;border-collapse:separate;border-spacing:0;border:1px solid var(--cozy-line);border-radius:14px;overflow:hidden;background:var(--cozy-surface);font-size:.9rem}.table th,.table td{padding:11px 14px;border:0;border-bottom:1px solid var(--cozy-line);text-align:left}.table th{background:var(--cozy-node);color:var(--cozy-ink)}.table tr:last-child td{border-bottom:0}.table tr:nth-child(even){background:var(--cozy-paper)}.cozy ol{list-style:none;counter-reset:cozy-step;padding-left:46px;position:relative}.cozy ol:before{content:'';position:absolute;left:16px;top:10px;bottom:12px;width:2px;background:var(--cozy-line)}.cozy ol>li{position:relative;counter-increment:cozy-step;margin:0 0 18px;padding-left:5px}.cozy ol>li:before{content:counter(cozy-step);position:absolute;left:-45px;top:0;width:31px;height:31px;line-height:29px;text-align:center;border:1px solid var(--cozy-bear);border-radius:50%;background:var(--cozy-surface);color:var(--cozy-bear);font-weight:700}#article-container{--cozy-paper:#fbf7ef;--cozy-surface:#fffdf8;--cozy-ink:#4a3a28;--cozy-muted:#6b5c46;--cozy-line:#e5d8c0;--cozy-green:#547a3d;--cozy-bear:#95613d;--cozy-node:#edf2e2;--cozy-edge:#6b7653;color:var(--cozy-ink)}#article-container .tabs{border:1px solid var(--cozy-line);border-radius:22px;background:var(--cozy-paper);box-shadow:0 8px 28px rgba(90,70,40,.08)}#article-container .tabs>.nav-tabs{padding:12px;gap:7px;background:var(--cozy-paper);border-bottom:1px dashed var(--cozy-line)}#article-container .tabs>.nav-tabs>.tab{border:1px solid var(--cozy-line);border-radius:18px;background:var(--cozy-surface);color:var(--cozy-muted);font-size:13px;padding:7px 13px;line-height:1.65}#article-container .tabs>.nav-tabs>.tab.active{background:var(--cozy-green);border-color:var(--cozy-green);color:#fffdf3}#article-container .tabs>.nav-tabs>.tab:hover{border-color:var(--cozy-bear)}#article-container h2{color:var(--cozy-ink);font-size:1.3rem;margin:34px 0 20px;padding:0 0 12px;border-bottom:2px dashed var(--cozy-line)}#article-container h2:before{content:'🌿';font-size:1rem;margin-right:10px}#article-container h3{color:var(--cozy-bear);font-size:1.08rem;margin:26px 0 14px}#article-container :not(pre)>code{color:var(--cozy-bear);background:#efe5d3;border-radius:6px;padding:2px 5px;overflow-wrap:anywhere}[data-theme='dark'] #article-container{--cozy-paper:#252a22;--cozy-surface:#30372b;--cozy-ink:#f0e8d8;--cozy-muted:#d0c5b2;--cozy-line:#535b46;--cozy-green:#adc38b;--cozy-bear:#e1b48b;--cozy-node:#414c35;--cozy-edge:#c6d4ae}[data-theme='dark'] #article-container .tabs>.nav-tabs>.tab.active{background:#547a3d;border-color:#adc38b}@media(max-width:600px){ #article-container .tabs>.nav-tabs{padding:9px;gap:6px}#article-container .tabs>.nav-tabs>.tab{font-size:12px;padding:7px 10px}.hero{padding:24px 20px 64px}.hero h1{font-size:1.35rem}.hero p{max-width:100%}.table{font-size:.84rem}.table th,.table td{padding:9px 10px}.cozy{padding:0}.arch-row{flex-direction:column}}
#article-container .highlight{border-radius:14px;border:1px solid #4c6650;background:#1f2a22;overflow:hidden;margin:18px 0;box-shadow:0 4px 14px rgba(38,53,42,.18)}#article-container .highlight table{border:0;border-radius:0;background:transparent;width:100%;margin:0}#article-container .highlight td{border:0;padding:0}#article-container .highlight .highlight-tools{background:#314734;color:#d6e5d0}#article-container .highlight .code{background:#1f2a22;color:#eef1e2}#article-container .highlight .gutter{background:#26352a;color:#91a88b}#article-container .highlight pre{background:transparent;color:#eef1e2}#article-container .highlight .keyword{color:#b7d88f}#article-container .highlight .title,#article-container .highlight .function{color:#f2c879}#article-container .highlight .string{color:#d8e99f}#article-container .highlight .number{color:#f2b38d}#article-container .highlight .comment{color:#91a88b}#article-container .highlight .built_in,#article-container .highlight .literal{color:#8fc9d6}.pre{background:#26352a!important;color:#eef1e2!important;border-color:#4c6650!important}
</style>
<div class="cozy"><div class="hero"><small>DATA STRUCTURE NOTE</small><h1>資料會一直增加，空間卻不會變大</h1><p>只要資料會持續流入，就要先決定容量上限，以及空間用完之後要保留什麼、捨棄什麼。<code>Ring Buffer</code> 用固定大小的記憶體循環使用。</p></div><div class="grid"><div class="card cream"><h3>固定容量</h3><p>資料不會讓記憶體無限成長。</p></div><div class="card bear"><h3>循環索引</h3><p>走到最後一格後回到索引 0。</p></div><div class="card moss"><h3>滿載策略</h3><p>空間用完後要定義資料保留規則。</p></div></div></div>
<!-- endtab -->

<!-- tab Ring Buffer -->
<div class="cozy"><div class="hero"><small>CORE IDEA</small><h1>一排格子，繞一圈繼續使用</h1><p><code>Ring Buffer</code> 是固定數量的格子。資料寫到最後一格後回到第一格。</p></div><ol><li>配置容量為 5 的陣列：<code>[_, _, _, _, _]</code>。</li><li><code>writeIndex</code> 指向下一筆資料要寫入的位置。</li><li>使用 <code>(index + 1) % capacity</code> 計算下一個索引。</li></ol><pre class="pre">buffer = [_, _, _, _, _]
          0  1  2  3  4

寫入 A：
[A] [_] [_] [_] [_]
     ↑
   write</pre><div class="callout"><strong>關鍵觀念：</strong>「Ring」描述的是索引如何循環，記憶體本身仍然是一段連續的陣列。</div><h2>為什麼不需要搬動資料</h2><p>只要把 <code>readIndex</code> 往前移，就能表示資料已經被讀取，原本的值不必立刻搬走。</p></div>
<!-- endtab -->

<!-- tab 移動視角 -->
<div class="cozy"><div class="hero"><small>READING WINDOW</small><h1>資料沒有搬家，閱讀起點改變了</h1><p>目前的 <code>readIndex</code> 決定邏輯上的第一筆資料。</p></div><pre class="pre">index
  0  1  2  3  4
[F][G][C][D][E]
       ↑
      read

readIndex = 2
讀取順序：C → D → E → F → G</pre><div class="grid"><div class="card bear"><h3>實際記憶體</h3><p>陣列位置依然是 0 到 4。</p></div><div class="card cream"><h3>邏輯順序</h3><p>從 <code>readIndex</code> 開始循環讀取。</p></div><div class="card moss"><h3>操作成本</h3><p>讀寫主要是更新索引。</p></div></div></div>
<!-- endtab -->

<!-- tab % 只是實現循環的工具 -->
<div class="cozy"><div class="hero"><small>INDEX WRAPAROUND</small><h1><code>%</code> 把索引帶回循環範圍</h1><p>取餘數只是把「走到底後回到起點」寫成索引計算。</p></div><pre class="pre">index = (index + 1) % size;

index++;
if (index == size)
{
    index = 0;
}</pre><table class="table"><thead><tr><th>目前索引</th><th>下一個索引</th></tr></thead><tbody><tr><td><code>0</code></td><td><code>1</code></td></tr><tr><td><code>4</code></td><td><code>0</code></td></tr></tbody></table></div>
<!-- endtab -->

<!-- tab Producer 與 Consumer -->
<div class="cozy"><div class="hero"><small>SYSTEM VIEW</small><h1>Ring Buffer 是兩種速度之間的暫存區</h1><p>它可以吸收短時間的速度差，但不能消除長期的產能落差。</p></div><div class="arch"><h2>Producer → Ring Buffer → Consumer</h2><div class="arch-row"><div class="node red"><strong>Producer</strong><br><small>持續產生資料</small></div></div><div class="arrow">↓</div><div class="arch-row"><div class="node blue"><strong>Ring Buffer</strong><br><small>固定容量暫存區</small></div></div><div class="arrow">↓</div><div class="arch-row"><div class="node green"><strong>Consumer</strong><br><small>逐筆處理資料</small></div></div><p class="callout"><strong>閱讀方式：</strong>紅色代表資料入口，藍色代表緩衝核心，綠色代表資料處理端。箭頭表示資料流向。</p></div><div class="grid"><div class="card bear"><h3>網路封包</h3><p>封包持續進入，處理程式逐筆取出。</p></div><div class="card cream"><h3>音訊與 UART</h3><p>短時間的處理延遲可以先放在緩衝區。</p></div><div class="card moss"><h3>Sensor</h3><p>固定容量能控制記憶體使用量。</p></div></div></div>
<!-- endtab -->

<!-- tab C# 實作 -->


<div class="cozy"><div class="hero"><small>C# IMPLEMENTATION</small><h1>完整的 Ring Buffer 實作</h1><p>這個版本保留原本的 <code>Main()</code>、泛型類別、讀寫索引與輸出紀錄，完整展示資料如何進入與離開環形緩衝區。</p></div><div class="callout"><strong>程式碼預設收合：</strong>點擊下方標題即可展開完整 C# 程式碼。</div>{% hideToggle 展開完整 C# 程式碼 %}

```csharp
void Main()
{
    var ringBuffer = new RingBuffer<string>(5);
    ringBuffer.Write("Abby");
    ringBuffer.Write("Alex");
    ringBuffer.Read().Dump();
    ringBuffer.Read().Dump();
    ringBuffer.Read().Dump();
    ringBuffer.Read().Dump();
    ringBuffer.Read().Dump();
    ringBuffer.Read().Dump();
}

public class RingBuffer<T>
{
    private readonly T[] buffer;
    private int readIndex;
    private int writeIndex;
    private int count;

    public int Capacity => buffer.Length;

    public RingBuffer(int capacity)
    {
        if (capacity <= 0)
        {
            /// throw
        }

        writeIndex = 0;
        readIndex = 0;
        count = 0;
        buffer = new T[capacity];
    }

    public void Write(T item)
    {
        $"writeIndex:{writeIndex}".Dump();
        buffer[writeIndex] = item;
        writeIndex = (writeIndex + 1) % Capacity;
        $"NewwriteIndex:{writeIndex}".Dump();
        count++;
    }

    public T Read()
    {
        $"readIndex:{readIndex}".Dump();
        T item = buffer[readIndex];
        buffer[readIndex] = default;
        readIndex = (readIndex + 1) % Capacity;
        $"NewreadIndex:{readIndex}".Dump();
        count--;
        return item;
    }
}
```

{% endhideToggle %}<ol><li><code>Write</code> 使用 <code>writeIndex</code> 寫入資料，再以 <code>% Capacity</code> 移動到下一格。</li><li><code>Read</code> 使用 <code>readIndex</code> 取出資料，再把已讀位置清成預設值。</li><li>原始版本保留了完整執行流程，空與滿的安全檢查可在後續版本另外補上。</li></ol></div>


<!-- endtab -->

<!-- tab Ring Buffer 如果來不及 Read，新資料一直進來怎麼辦？ -->
<div class="cozy"><div class="hero"><small>WHEN THE BUFFER IS FULL</small><h1>容量只能延後問題，不能消除速度差</h1><p>假設 <code>Producer</code> 每秒產生 100 筆，<code>Consumer</code> 每秒只能處理 50 筆，緩衝區最終仍然會滿。</p></div><pre class="pre">Producer：每秒產生 100 筆
        ↓
Ring Buffer：容量有限
        ↓
Consumer：每秒處理 50 筆</pre><div class="grid"><div class="card bear"><h3>覆蓋舊資料</h3><p>保留最新資料，捨棄較早資料。</p></div><div class="card cream"><h3>丟掉新資料</h3><p>保留緩衝區內的資料，新進資料寫入失敗。</p></div><div class="card moss"><h3>等待處理端</h3><p>讓寫入端暫停或降低速度。</p></div></div><div class="callout"><strong>另一種選擇：</strong>把壓力轉移到 Disk、Queue 或 Broker，也要另外定義容量、失敗與恢復策略。</div><h2>設計時需要先回答的問題</h2><ul><li>資料過期後是否還有價值？</li><li>滿載時能不能遺失最新資料？</li><li>寫入端能不能暫停或降速？</li><li>資料是否需要跨程序或跨機器保存？</li></ul><div class="callout"><strong>結論：</strong><code>Ring Buffer</code> 解決固定空間內的循環讀寫，以及短時間的速度差。長期速度落差仍需要資料保留、背壓或外部佇列策略。</div></div>
<!-- endtab -->

{% endtabs %}

