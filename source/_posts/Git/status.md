---
title: status
date: 2026-10-09 08:40:00
categories: Git
description: 從修改檔案、git add 到 commit，理解 git status 顯示的檔案狀態。
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/style/git.png
cover : https://pub-d7e550ef212547d888a6e01348459946.r2.dev/style/git.png
tags:
toc:
toc_number:
comments :
---

{% tabs status%}

<!-- tab Git 區分狀態的底層邏輯-->

<style>
:root{--gg-orange:#f05133;--gg-coral:#f25d3b;--gg-light:#f46640;--gg-paper:#fff8f4;--gg-white:#fff;--gg-ink:#2d2928;--gg-muted:#746761;--gg-line:#e8d8d1;--gg-code:#2d2928;--gg-code-ink:#fff8f4;}
.gg-hero,.gg-three-zone,.gg-decision,.gg-steps,.gg-before-after,.gg-status-grid,.gg-table-scroll,.gg-note{box-sizing:border-box;font-family:'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif;}
.gg-hero *,.gg-three-zone *,.gg-decision *,.gg-steps *,.gg-before-after *,.gg-status-grid *,.gg-table-scroll *,.gg-note *{box-sizing:border-box;}
.gg-hero{position:relative;overflow:hidden;padding:42px 38px;margin:0 0 28px;background:var(--gg-orange);color:var(--gg-white);border-radius:12px;isolation:isolate;}
.gg-hero::before,.gg-hero::after{content:'';position:absolute;border-radius:50%;background:rgba(255,255,255,.08);z-index:-1;}
.gg-hero::before{width:360px;height:360px;left:-170px;bottom:-240px;}
.gg-hero::after{width:310px;height:310px;right:-150px;top:-200px;}
.gg-hero h2{margin:0 0 12px!important;color:var(--gg-white)!important;font-size:clamp(1.8rem,5vw,3.2rem);font-weight:850;letter-spacing:-.03em;line-height:1.15;}
.gg-hero p{max-width:44em;margin:0;color:var(--gg-white);font-size:1.02rem;line-height:1.8;}
.gg-hero code{background:rgba(255,255,255,.14)!important;color:var(--gg-white)!important;border:1px solid rgba(255,255,255,.22);}
.gg-graph-mark{position:absolute;right:30px;bottom:24px;width:150px;height:84px;opacity:.72;}
.gg-graph-mark line{stroke:var(--gg-white);stroke-width:2;}
.gg-graph-mark circle{fill:var(--gg-white);}
.gg-section{margin:30px 0 14px;padding-left:14px;border-left:5px solid var(--gg-orange);color:var(--gg-ink);font-weight:800;line-height:1.4;}
.gg-three-zone{display:grid;grid-template-columns:minmax(0,1fr) 62px minmax(0,1fr) 62px minmax(0,1fr);align-items:stretch;gap:10px;margin:22px 0;}
.gg-zone{padding:20px;background:var(--gg-white);border:1px solid var(--gg-line);border-top:5px solid var(--gg-orange);border-radius:8px;color:var(--gg-ink);box-shadow:0 8px 22px rgba(79,45,34,.07);}
.gg-zone strong{display:block;margin-bottom:7px;font-size:1.08rem;}
.gg-zone p{margin:0;color:var(--gg-muted);line-height:1.7;}
.gg-arrow{display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--gg-orange);font-weight:800;text-align:center;line-height:1.35;}
.gg-arrow span:first-child{font-size:1.65rem;line-height:1;}
.gg-arrow small{margin-top:7px;color:var(--gg-muted);font-weight:650;}
.gg-arrow small code{display:inline-block;white-space:nowrap;}
.gg-decision{margin:22px 0;padding:24px;background:var(--gg-paper);border:1px solid var(--gg-line);border-radius:10px;color:var(--gg-ink);}
.gg-node{padding:13px 16px;background:var(--gg-white);border:2px solid var(--gg-orange);border-radius:8px;text-align:center;font-weight:750;line-height:1.5;}
.gg-node.question{max-width:360px;margin:0 auto;background:var(--gg-orange);color:var(--gg-white);}
.gg-branches{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:32px;}
.gg-branches::before{content:'';position:absolute;top:-18px;left:25%;right:25%;border-top:2px solid var(--gg-orange);}
.gg-branch{position:relative;min-width:0;}
.gg-branch::before{content:'';position:absolute;top:-18px;left:50%;height:18px;border-left:2px solid var(--gg-orange);}
.gg-branch-label{display:block;width:max-content;margin:-31px auto 10px;padding:2px 9px;background:var(--gg-paper);color:var(--gg-orange);font-weight:800;}
.gg-branch p{margin:10px 0 0;color:var(--gg-muted);line-height:1.7;}
.gg-mini-branches{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px;}
.gg-result{padding:12px;background:var(--gg-white);border:1px solid var(--gg-line);border-radius:7px;text-align:center;}
.gg-result strong{display:block;color:var(--gg-orange);}
.gg-steps{position:relative;margin:24px 0;padding-left:30px;}
.gg-steps::before{content:'';position:absolute;left:10px;top:12px;bottom:12px;border-left:2px solid var(--gg-orange);}
.gg-step{position:relative;margin:0 0 18px;padding:17px 18px;background:var(--gg-white);border:1px solid var(--gg-line);border-radius:8px;color:var(--gg-ink);}
.gg-step::before{content:'';position:absolute;left:-26px;top:20px;width:12px;height:12px;background:var(--gg-orange);border:3px solid var(--gg-paper);border-radius:50%;}
.gg-step strong{display:block;margin-bottom:5px;}
.gg-step p{margin:0;color:var(--gg-muted);line-height:1.7;}
.gg-before-after{display:grid;grid-template-columns:minmax(0,1fr) 100px minmax(0,1fr);align-items:center;gap:16px;margin:24px 0;}
.gg-snapshot{padding:20px;background:var(--gg-white);border:1px solid var(--gg-line);border-radius:8px;color:var(--gg-ink);}
.gg-snapshot h4{margin:0 0 12px!important;color:var(--gg-ink)!important;}
.gg-snapshot ul{margin:0;padding-left:20px;}
.gg-command{text-align:center;color:var(--gg-orange);font:700 .9rem/1.5 Consolas,monospace;overflow-wrap:anywhere;}
.gg-status-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin:22px 0;}
.gg-status-card{padding:18px;background:var(--gg-white);border:1px solid var(--gg-line);border-top:5px solid var(--gg-orange);border-radius:8px;color:var(--gg-ink);}
.gg-status-card h4{margin:0 0 8px!important;color:var(--gg-ink)!important;}
.gg-status-card p{margin:0;color:var(--gg-muted);line-height:1.7;}
.gg-note{margin:22px 0;padding:17px 20px;background:var(--gg-paper);border-left:5px solid var(--gg-orange);border-radius:4px;color:var(--gg-ink);line-height:1.75;}
.gg-note strong{display:block;margin-bottom:4px;}
.gg-note p{margin:0;}
.gg-table-scroll{max-width:100%;margin:22px 0;overflow-x:auto;}
#article-container table.gg-table,.gg-table{width:auto;max-width:100%;margin:0;border-collapse:collapse;background:var(--gg-white);color:var(--gg-ink);}
.gg-table th,.gg-table td{padding:12px 15px;border:1px solid var(--gg-line);text-align:left;vertical-align:top;background:var(--gg-white);}
.gg-table th{background:var(--gg-paper);font-weight:750;}
#article-container .highlight,#article-container .highlight .code{background:var(--gg-code)!important;color:var(--gg-code-ink)!important;}
#article-container .highlight table{width:100%!important;background:transparent!important;}
#article-container .highlight pre{background:transparent!important;color:var(--gg-code-ink)!important;}
#article-container .highlight .gutter{background:#3b3533!important;color:#d8c8c1!important;}
[data-theme='dark']{--gg-paper:#211d1b;--gg-white:#2b2624;--gg-ink:#fff7f2;--gg-muted:#d4c3bb;--gg-line:#594740;--gg-orange:#ff6b4a;--gg-coral:#d94b30;--gg-light:#ed6040;--gg-code:#171412;--gg-code-ink:#fff8f4;}
@media(max-width:720px){.gg-hero{padding:30px 22px 86px;}.gg-graph-mark{left:22px;right:auto;bottom:12px;width:120px;}.gg-three-zone,.gg-before-after,.gg-status-grid{grid-template-columns:1fr;}.gg-arrow{padding:2px 0;}.gg-arrow span:first-child{transform:rotate(90deg);}.gg-branches{grid-template-columns:1fr;}.gg-branches::before,.gg-branch::before{display:none;}.gg-branch-label{margin:0 auto 8px;}.gg-mini-branches{grid-template-columns:1fr;}.gg-table th,.gg-table td{min-width:9em;}}
</style>

<div class="gg-hero">
<h2>Git 怎麼看檔案狀態</h2>
<p><code>git status</code> 主要回答兩個問題：哪些檔案改過，以及哪些內容已經準備放進下一次 Commit。Git 會比較「已經提交的上一版」、「準備提交的版本」和「目前正在修改的版本」。</p>
<svg class="gg-graph-mark" viewBox="0 0 150 84" role="img" aria-label="Git 分支節點裝飾"><line x1="12" y1="70" x2="62" y2="42"></line><line x1="62" y1="42" x2="108" y2="12"></line><line x1="62" y1="42" x2="126" y2="70"></line><circle cx="12" cy="70" r="5"></circle><circle cx="62" cy="42" r="6"></circle><circle cx="108" cy="12" r="5"></circle><circle cx="126" cy="70" r="5"></circle></svg>
</div>

<h2 class="gg-section">先認識三個位置</h2>

<div class="gg-three-zone">
<div class="gg-zone"><strong>HEAD</strong><p>已經提交的上一版。若倉庫還沒有 Commit，可以把它想成空的起點。</p></div>
<div class="gg-arrow"><span>↔</span><small>是否已準備提交</small></div>
<div class="gg-zone"><strong>Index，也叫暫存區</strong><p>已經執行 <code>git add</code>，準備放進下一次 Commit 的檔案版本。</p></div>
<div class="gg-arrow"><span>↔</span><small>是否又有新修改</small></div>
<div class="gg-zone"><strong>Working Tree</strong><p>硬碟上目前看得到、正在修改的實體檔案。</p></div>
</div>

可以把整個過程記成：在 Working Tree 修改檔案，執行 `git add` 把當下的版本放進 Index，最後執行 `git commit` 建立新的 Commit。

`git status` 主要整理三類資訊：

1. 比較 `HEAD` 和 Index，找出已經執行 `git add`、準備提交的內容。
2. 比較 Index 和 Working Tree，找出修改後還沒有執行 `git add` 的內容。
3. 檢查 Working Tree，找出尚未交給 Git 管理，而且沒有被 ignore 規則排除的新檔案。

剛建立的 `test.txt` 只存在於 Working Tree。它還沒有執行 `git add`，也沒有出現在先前的 Commit，因此狀態是 `Untracked`。

<div class="gg-note">
<strong><code>git add</code> 就是把內容加入暫存區</strong>
<p>執行 <code>git add test.txt</code> 時，Git 會把 <code>test.txt</code> 當下的內容放進 Index。這個動作就叫「暫存」。檔案仍留在 Working Tree，也還沒有建立 Commit。底層會同時更新 Index 中的路徑、檔案模式與內容識別值。</p>
</div>

<h2 class="gg-section">Tracked、Untracked 與 Ignored</h2>

`Tracked` 表示檔案已經交給 Git 管理。它可能早已存在於某個 Commit，也可能是剛執行 `git add`、第一次放進 Index 的新檔案。

`Untracked` 表示這是尚未執行 `git add` 的新檔案。檔案存在於 Working Tree，但上一個 Commit 與 Index 都沒有它。

只有 Git 尚未追蹤的路徑，才會繼續套用 `.gitignore` 等 ignore 規則。已追蹤的檔案不會因為後來加入 `.gitignore` 就自動停止追蹤。

<div class="gg-decision">
<div class="gg-node question">這個路徑已被 Git 追蹤？</div>
<div class="gg-branches">
<div class="gg-branch"><span class="gg-branch-label">是</span><div class="gg-node">Tracked</div><p>再比較三個位置，判斷最新修改是否已經執行 <code>git add</code>。</p></div>
<div class="gg-branch"><span class="gg-branch-label">否</span><div class="gg-node">符合 ignore 規則？</div><div class="gg-mini-branches"><div class="gg-result"><strong>是</strong>Ignored，一般的 <code>git status</code> 不列出</div><div class="gg-result"><strong>否</strong>Untracked，列在未追蹤檔案中</div></div></div>
</div>
</div>

<!-- endtab -->

<!-- tab ignore 實驗觀察-->

這個實驗先建立 `test.txt`，再把它寫進 `.gitignore`。因為 `test.txt` 從未執行 `git add`，Git 還沒有開始追蹤它，所以 ignore 規則可以把它隱藏起來。

<div class="gg-steps">
<div class="gg-step"><strong>1. 建立倉庫</strong><p><code>git init</code> 建立空倉庫，此時還沒有 Commit，也沒有被追蹤的檔案。</p></div>
<div class="gg-step"><strong>2. 建立 test.txt</strong><p>檔案只存在於 Working Tree，所以 <code>git ls-files</code> 沒有輸出。</p></div>
<div class="gg-step"><strong>3. 加入 ignore 規則</strong><p><code>.gitignore</code> 符合 <code>test.txt</code>，一般的 <code>git status</code> 不再列出它。</p></div>
<div class="gg-step"><strong>4. 顯示 ignored 檔案</strong><p><code>git status --ignored</code> 會把 <code>test.txt</code> 顯示在 Ignored files 區段。</p></div>
</div>

```bash
# 建立實驗資料夾
mkdir testgit
cd testgit
git init

# 確認 Git 狀態
git status

#### On branch master
#### No commits yet
#### nothing to commit (create/copy files and use "git add" to track)

# 現在位置
pwd

#### /mnt/c/Users/Allen/Desktop/testgit

# 列出所有檔案
ls -a

# 建立檔案
# > 是輸出重新導向，會把 echo 的內容寫進 test.txt
echo "Hello Git" > test.txt
ls -a

#### .  ..  .git  test.txt

# 查看 Index 目前記錄的路徑
git ls-files

#### 沒有輸出

# 建立 ignore 規則
echo "test.txt" > .gitignore
cat .gitignore
git status
git status --ignored

#### On branch master
#### No commits yet
####
#### Untracked files:
####   (use "git add <file>..." to include in what will be committed)
####         .gitignore
####
#### Ignored files:
####   (use "git add -f <file>..." to include in what will be committed)
####         test.txt
####
#### nothing added to commit but untracked files present (use "git add" to track)
```

<div class="gg-note">
<strong>建立順序不是關鍵</strong>
<p>先建立 <code>.gitignore</code> 再建立 <code>test.txt</code>，結果也相同。判斷重點是 <code>test.txt</code> 尚未執行 <code>git add</code>，也沒有出現在先前的 Commit。</p>
</div>

<!-- endtab -->

<!-- tab 狀態-->

Git 判斷狀態時，可以分成兩個問題。第一個問題是「Git 是否已經知道這個路徑」，第二個問題是「三個位置之間是否有差異」。

<h2 class="gg-section">第一個問題：Git 是否管理這個路徑</h2>

<div class="gg-status-grid">
<div class="gg-status-card"><h4>Tracked</h4><p>Git 已經在管理這個檔案。它曾經被 Commit，或已透過 <code>git add</code> 放進 Index。</p></div>
<div class="gg-status-card"><h4>Untracked</h4><p>尚未執行 <code>git add</code> 的新檔案，Git 還沒有開始管理它。</p></div>
<div class="gg-status-card"><h4>Ignored</h4><p>路徑尚未被追蹤，而且符合 ignore 規則。一般的 <code>git status</code> 不會列出它。</p></div>
</div>

<h2 class="gg-section">第二個問題：三個位置是否有差異</h2>

<div class="gg-table-scroll" role="region" aria-label="Git 檔案狀態比較" tabindex="0">
<table class="gg-table">
<thead><tr><th scope="col">狀態</th><th scope="col">Git 看到的差異</th><th scope="col">代表意思</th></tr></thead>
<tbody><tr><th scope="row">Unmodified</th><td>三個位置的內容一致</td><td>Git 正在管理檔案，目前沒有變更</td></tr><tr><th scope="row">Modified</th><td>Working Tree 與 Index 不同</td><td>檔案已修改，但最新內容尚未執行 <code>git add</code></td></tr><tr><th scope="row">Staged</th><td>Index 與 HEAD 不同</td><td>已執行 <code>git add</code>，這個版本會進入下一次 Commit</td></tr></tbody>
</table>
</div>

<div class="gg-note">
<strong>Staged 與 Modified 可以同時存在</strong>
<p>假設檔案的 A 版本先執行 <code>git add</code>，接著又改成 B 版本。Index 裡仍是準備提交的 A 版本，Working Tree 則是最新的 B 版本。若沒有再次執行 <code>git add</code>，下一次 Commit 只會收錄 A 版本。</p>
</div>

<!-- endtab -->

<!-- tab 已經被 tracked 才加入 ignore file 實驗-->

這個實驗先對 `tracked.txt` 執行 `git add`。這時檔案已放進 Index，Git 也開始追蹤它。之後才把相同路徑加入 `.gitignore`，無法取消已經開始的追蹤。

<div class="gg-steps">
<div class="gg-step"><strong>1. 建立 tracked.txt</strong><p>檔案剛建立時仍是 Untracked。</p></div>
<div class="gg-step"><strong>2. 執行 git add</strong><p><code>tracked.txt</code> 的當下版本放進 Index，成為 Tracked 與 Staged。</p></div>
<div class="gg-step"><strong>3. 寫入 .gitignore</strong><p>ignore 規則只影響尚未追蹤的路徑，不會刪除 Index 裡既有的項目。</p></div>
<div class="gg-step"><strong>4. 再次執行 git status</strong><p><code>tracked.txt</code> 仍出現在 Changes to be committed。</p></div>
</div>

```bash
echo "I will be tracked" > tracked.txt
git status

#### On branch master
####
#### No commits yet
####
#### Untracked files:
####   (use "git add <file>..." to include in what will be committed)
####         .gitignore
####         tracked.txt
####
#### nothing added to commit but untracked files present (use "git add" to track)

git add tracked.txt
git status

#### On branch master
####
#### No commits yet
####
#### Changes to be committed:
####   (use "git rm --cached <file>..." to unstage)
####         new file:   tracked.txt
####
#### Untracked files:
####   (use "git add <file>..." to include in what will be committed)
####         .gitignore

echo "tracked.txt" >> .gitignore
git status

#### On branch master
####
#### No commits yet
####
#### Changes to be committed:
####   (use "git rm --cached <file>..." to unstage)
####         new file:   tracked.txt
####
#### Untracked files:
####   (use "git add <file>..." to include in what will be committed)
####         .gitignore
```

<div class="gg-note">
<strong><code>.gitignore</code> 不會解除追蹤</strong>
<p><code>tracked.txt</code> 已經透過 <code>git add</code> 放進 Index，因此 Git 仍準備把它放進下一次 Commit。若要保留本機檔案，但不再讓 Git 追蹤，需要使用 <code>git rm --cached</code>。</p>
</div>

<!-- endtab -->

<!-- tab git rm --cached-->


例如平常會有 `git rm -r --cached bin obj .vs TestResults`


`git rm --cached tracked.txt` 會把 `tracked.txt` 從 Index，也就是 Git 準備提交與追蹤的清單中移除，但不會刪除硬碟上的實體檔案。

<div class="gg-before-after">
<div class="gg-snapshot"><h4>執行前</h4><ul><li>Index 有 <code>tracked.txt</code></li><li>Working Tree 有 <code>tracked.txt</code></li></ul></div>
<div class="gg-command">git rm<br>--cached<br>tracked.txt</div>
<div class="gg-snapshot"><h4>執行後</h4><ul><li>Index 移除 <code>tracked.txt</code></li><li>Working Tree 保留 <code>tracked.txt</code></li></ul></div>
</div>

<h2 class="gg-section">與一般 git rm 的差別</h2>

<div class="gg-table-scroll" role="region" aria-label="git rm 指令比較" tabindex="0">
<table class="gg-table">
<thead><tr><th scope="col">指令</th><th scope="col">從 Index 移除</th><th scope="col">刪除硬碟檔案</th><th scope="col">適用情境</th></tr></thead>
<tbody><tr><th scope="row"><code>git rm --cached &lt;檔名&gt;</code></th><td>是</td><td>否</td><td>停止追蹤，但保留本機檔案</td></tr><tr><th scope="row"><code>git rm &lt;檔名&gt;</code></th><td>是</td><td>是</td><td>從版本控制與工作目錄一起移除檔案</td></tr></tbody>
</table>
</div>

## 實驗

```bash
# 從 Index 移除，但保留本機檔案
git rm --cached tracked.txt
git status

#### On branch master
####
#### No commits yet
####
#### Untracked files:
####   (use "git add <file>..." to include in what will be committed)
####         .gitignore
####
#### nothing added to commit but untracked files present (use "git add" to track)

# 確認檔案仍在 Working Tree
ls

#### test.txt  tracked.txt
```

<div class="gg-note">
<strong>為什麼這次沒有出現 deleted</strong>
<p>這個實驗還沒有建立任何 Commit，所以 <code>HEAD</code> 是空的。把 <code>tracked.txt</code> 從 Index 移除後，準備提交的內容也變回空白，因此沒有顯示刪除。若檔案早已存在於先前的 Commit，執行 <code>git rm --cached</code> 會把「下一次 Commit 要停止追蹤這個檔案」列為已暫存的變更。</p>
</div>

<!-- endtab -->

<!-- tab 為甚麼會有 Staged 階段-->

Working Tree 裡可能同時存在已完成、做到一半與只供測試的修改。若 `git commit` 每次都收錄全部修改，不相關的內容就會混進同一個版本存檔點。Staged 階段讓 Git 多一個「先挑選，再存檔」的步驟。

<div class="gg-three-zone">
<div class="gg-zone"><strong>Working Tree</strong><p>目前所有修改，包含完成與尚未完成的內容。</p></div>
<div class="gg-arrow"><span>→</span><small><code>git add</code> 挑選</small></div>
<div class="gg-zone"><strong>Index，也叫暫存區</strong><p>這次準備提交的內容，可以把它看成下一個 Commit 的草稿。</p></div>
<div class="gg-arrow"><span>→</span><small><code>git commit</code> 存檔</small></div>
<div class="gg-zone"><strong>Commit</strong><p>把 Index 的內容正式保存成一個版本存檔點。</p></div>
</div>

<h2 class="gg-section">同時修改三個檔案的例子</h2>

目前有三個檔案發生異動，但這次只想提交已完成的登入修正：

<div class="gg-table-scroll" role="region" aria-label="Staged 檔案挑選範例" tabindex="0">
<table class="gg-table">
<thead><tr><th scope="col">檔案</th><th scope="col">目前情況</th><th scope="col">這次是否執行 <code>git add</code></th><th scope="col">是否進入下一個 Commit</th></tr></thead>
<tbody><tr><th scope="row"><code>login.cs</code></th><td>登入修正已完成</td><td>是</td><td>是</td></tr><tr><th scope="row"><code>payment.cs</code></th><td>付款功能做到一半</td><td>否</td><td>否，繼續留在 Working Tree</td></tr><tr><th scope="row"><code>notes.txt</code></th><td>本機測試紀錄</td><td>否</td><td>否，繼續留在 Working Tree</td></tr></tbody>
</table>
</div>

```bash
git add login.cs
git commit -m "修正登入錯誤"
```

這次 Commit 只收錄 `login.cs`。另外兩個檔案不會消失，也不會被提交，仍然留在 Working Tree。

<div class="gg-note">
<strong>同一個檔案也能只挑部分修改</strong>
<p><code>git add -p login.cs</code> 會把修改拆成數個區塊，再逐一決定是否放進 Index。因此 Staged 挑選的不只是檔名，也可以是檔案裡的部分修改。</p>
</div>

Staged 階段的目的，是讓每個 Commit 只保存一組彼此相關、已經準備好的修改。這樣比較容易閱讀歷史、進行 Code Review，也比較容易只還原某一次修改。

<!-- endtab -->

<!-- tab commit 的意義-->

Commit 可以理解成 Git 裡的一個「版本存檔點」。它會保存 Index 當下準備好的內容，並接在前一個 Commit 後面，形成可以回頭查看的版本歷史。

<div class="gg-steps">
<div class="gg-step"><strong>Commit A</strong><p>建立專案的最初版本。</p></div>
<div class="gg-step"><strong>Commit B</strong><p>在 Commit A 後面加入登入功能。</p></div>
<div class="gg-step"><strong>Commit C</strong><p>在 Commit B 後面修正登入錯誤。</p></div>
</div>

每個 Commit 都是獨立的版本存檔點，因此可以查看某個版本、比較兩個版本，或把檔案恢復成某個版本的內容。

<h2 class="gg-section">一個 Commit 記錄哪些資料</h2>

<div class="gg-table-scroll" role="region" aria-label="Commit 記錄內容" tabindex="0">
<table class="gg-table">
<thead><tr><th scope="col">資料</th><th scope="col">代表意思</th></tr></thead>
<tbody><tr><th scope="row">專案快照</th><td>這次 Commit 保存的檔案與目錄內容</td></tr><tr><th scope="row">上一個 Commit</th><td>這個版本是接在哪個版本後面</td></tr><tr><th scope="row">作者與時間</th><td>誰在什麼時間建立這個版本</td></tr><tr><th scope="row">Commit Message</th><td>這次修改的說明，例如「修正登入錯誤」</td></tr><tr><th scope="row">Hash</th><td>辨識這個 Commit 的編號，例如 <code>a1b2c3d</code></td></tr></tbody>
</table>
</div>

<h2 class="gg-section">Commit 同時是動作與結果</h2>

<div class="gg-status-grid">
<div class="gg-status-card"><h4>作為動作</h4><p>執行 <code>git commit</code>，把 Index 的內容保存成一個新版本。</p></div>
<div class="gg-status-card"><h4>作為結果</h4><p>指已經建立好的版本紀錄，例如「查看上一個 Commit」。</p></div>
</div>

<h2 class="gg-section">Commit 不等於上傳</h2>

<div class="gg-three-zone">
<div class="gg-zone"><strong><code>git add</code></strong><p>挑選內容，放進 Index。</p></div>
<div class="gg-arrow"><span>→</span><small>準備完成</small></div>
<div class="gg-zone"><strong><code>git commit</code></strong><p>在本機建立版本存檔點。</p></div>
<div class="gg-arrow"><span>→</span><small>需要分享時</small></div>
<div class="gg-zone"><strong><code>git push</code></strong><p>把本機 Commit 上傳到遠端倉庫。</p></div>
</div>

<div class="gg-note">
<strong>Commit 建立後，內容就固定了</strong>
<p>Commit 會依專案快照、上一個 Commit、作者、時間與說明等資料產生自己的 Hash。即使使用 <code>git commit --amend</code> 修改上一個 Commit，Git 實際上也是建立另一個新 Commit，並產生新的 Hash。</p>
</div>

所以 `git commit -m "修正登入錯誤"` 的完整意思是：把 Index 裡準備好的內容，在本機建立成一個新的版本存檔點，並用「修正登入錯誤」說明這次修改。

<!-- endtab -->

{% endtabs %}
