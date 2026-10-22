---
title: 撤回最後一次 Commit：git reset 與 git commit --amend
date: 2026-10-11 19:32:00
categories: Git
description: 剛 Commit 完才發現內容有錯時，分清楚 git reset 與 git commit --amend 會改動哪些位置，以及已經 Push 後要注意什麼。
top_img: https://pub-d7e550ef212547d888a6e01348459946.r2.dev/style/git.png
cover : https://pub-d7e550ef212547d888a6e01348459946.r2.dev/style/git.png
tags:
toc:
toc_number:
comments :
---

{% tabs back-to-commit %}

<!-- tab 先看情境-->

<style>
:root{--gg-orange:#f05133;--gg-paper:#fff8f4;--gg-white:#fff;--gg-ink:#2d2928;--gg-muted:#746761;--gg-line:#e8d8d1;--gg-code:#2d2928;--gg-code-ink:#fff8f4;--gg-danger:#b42318;--gg-danger-bg:#fff1ef}
.gg-hero,.gg-commit-flow,.gg-three-zone,.gg-before-after,.gg-case-grid,.gg-steps,.gg-table-scroll,.gg-note{box-sizing:border-box;font-family:'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif}
.gg-hero *,.gg-commit-flow *,.gg-three-zone *,.gg-before-after *,.gg-case-grid *,.gg-steps *,.gg-table-scroll *,.gg-note *{box-sizing:border-box}
.gg-hero{position:relative;overflow:hidden;margin:0 0 28px;padding:42px 38px;background:var(--gg-orange);color:#fff;border-radius:12px;isolation:isolate}
.gg-hero::before,.gg-hero::after{content:'';position:absolute;border-radius:50%;background:rgba(255,255,255,.08);z-index:-1}
.gg-hero::before{width:360px;height:360px;left:-170px;bottom:-240px}.gg-hero::after{width:310px;height:310px;right:-150px;top:-200px}
.gg-hero h2{margin:0 0 12px!important;color:#fff!important;font-size:clamp(1.8rem,5vw,3.2rem);font-weight:850;line-height:1.15}
.gg-hero p{max-width:46em;margin:0;color:#fff;line-height:1.8}.gg-hero code{background:rgba(255,255,255,.14)!important;color:#fff!important;border:1px solid rgba(255,255,255,.22)}
.gg-graph-mark{position:absolute;right:30px;bottom:24px;width:150px;height:84px;opacity:.72}.gg-graph-mark line{stroke:#fff;stroke-width:2}.gg-graph-mark circle{fill:#fff}
.gg-section{margin:30px 0 14px;padding-left:14px;border-left:5px solid var(--gg-orange);color:var(--gg-ink);font-weight:800;line-height:1.4}
.gg-commit-flow{margin:22px 0;padding:22px;background:var(--gg-paper);border:1px solid var(--gg-line);border-radius:10px;color:var(--gg-ink);overflow-x:auto}
.gg-commit-track{display:flex;align-items:flex-start;justify-content:center;min-width:520px}.gg-commit-node{width:130px;text-align:center}
.gg-commit-dot{display:flex;width:46px;height:46px;margin:0 auto 10px;align-items:center;justify-content:center;background:var(--gg-orange);color:#fff;border:5px solid var(--gg-white);border-radius:50%;box-shadow:0 0 0 2px var(--gg-orange);font-weight:850}
.gg-commit-node strong{display:block;font-size:.92rem;line-height:1.45;overflow-wrap:anywhere}.gg-commit-link{width:64px;margin-top:22px;border-top:3px solid var(--gg-orange)}
.gg-commit-ref{width:max-content;margin:18px auto 0;padding:6px 12px;background:var(--gg-white);border:1px solid var(--gg-line);border-radius:999px;color:var(--gg-muted);font-size:.9rem;font-weight:700}
.gg-three-zone{display:grid;grid-template-columns:minmax(0,1fr) 52px minmax(0,1fr) 52px minmax(0,1fr);gap:10px;margin:22px 0;align-items:stretch}
.gg-zone,.gg-snapshot,.gg-case,.gg-step{padding:18px;background:var(--gg-white);border:1px solid var(--gg-line);border-radius:8px;color:var(--gg-ink)}
.gg-zone{border-top:5px solid var(--gg-orange)}.gg-zone strong,.gg-note strong,.gg-step strong{display:block;margin-bottom:6px}.gg-zone p,.gg-snapshot p,.gg-case p,.gg-step p,.gg-note p{margin:0;color:var(--gg-muted);line-height:1.7}
.gg-arrow{display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--gg-orange);font-weight:800;text-align:center}.gg-arrow span{font-size:1.5rem}.gg-arrow small{color:var(--gg-muted)}
.gg-before-after{display:grid;grid-template-columns:minmax(0,1fr) 92px minmax(0,1fr);gap:16px;margin:24px 0;align-items:center}.gg-snapshot h4,.gg-case h4{margin:0 0 10px!important;color:var(--gg-ink)!important}
.gg-command{text-align:center;color:var(--gg-orange);font:700 .9rem/1.5 Consolas,monospace;overflow-wrap:anywhere}.gg-case-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin:22px 0}.gg-case{border-top:5px solid var(--gg-orange)}
.gg-steps{position:relative;margin:24px 0;padding-left:30px}.gg-steps::before{content:'';position:absolute;left:10px;top:12px;bottom:12px;border-left:2px solid var(--gg-orange)}
.gg-step{position:relative;margin-bottom:18px}.gg-step::before{content:'';position:absolute;left:-26px;top:20px;width:12px;height:12px;background:var(--gg-orange);border:3px solid var(--gg-paper);border-radius:50%}
.gg-note{margin:22px 0;padding:17px 20px;background:var(--gg-paper);border-left:5px solid var(--gg-orange);border-radius:4px;color:var(--gg-ink)}.gg-note.danger{background:var(--gg-danger-bg);border-left-color:var(--gg-danger)}.gg-note.danger strong{color:var(--gg-danger)}
.gg-table-scroll{display:inline-block;max-width:100%;margin:22px 0;overflow-x:auto;border:1px solid var(--gg-line);border-radius:8px}
#article-container table.gg-table,.gg-table{width:auto;max-width:100%;margin:0;border-collapse:collapse;background:var(--gg-white);color:var(--gg-ink)}.gg-table th,.gg-table td{padding:12px 15px;border:1px solid var(--gg-line);text-align:left;vertical-align:top;background:var(--gg-white)}.gg-table th{background:var(--gg-paper);font-weight:750}
#article-container .highlight,#article-container .highlight .code{background:var(--gg-code)!important;color:var(--gg-code-ink)!important}#article-container .highlight table,#article-container .highlight pre{width:100%!important;background:transparent!important}#article-container .highlight .gutter{background:#3b3533!important;color:#d8c8c1!important}
[data-theme='dark']{--gg-paper:#211d1b;--gg-white:#2b2624;--gg-ink:#fff7f2;--gg-muted:#d4c3bb;--gg-line:#594740;--gg-orange:#ff6b4a;--gg-code:#171412;--gg-code-ink:#fff8f4;--gg-danger:#ff8f82;--gg-danger-bg:#351d1b}
@media(max-width:720px){.gg-hero{padding:30px 22px 86px}.gg-graph-mark{left:22px;right:auto;bottom:12px;width:120px}.gg-three-zone,.gg-before-after,.gg-case-grid{grid-template-columns:1fr}.gg-arrow span{transform:rotate(90deg)}.gg-table th,.gg-table td{min-width:9em}.gg-commit-flow{padding:18px 8px}.gg-commit-track{min-width:0;justify-content:center}.gg-commit-node{width:86px}.gg-commit-link{width:14px}.gg-commit-dot{width:38px;height:38px;border-width:4px}.gg-commit-node strong{font-size:.72rem}.gg-commit-ref{font-size:.78rem}}
</style>

<div class="gg-hero">
<h2>剛 Commit 完，才發現內容有錯</h2>
<p>程式已經提交，但 <code>database.yml</code> 的設定不對，Commit Message 也寫得不夠清楚。這時不用把整段工作重做，只要先決定要「拆回來修改」，還是「直接重做最後一次 Commit」。</p>
<svg class="gg-graph-mark" viewBox="0 0 150 84" role="img" aria-label="Git 分支節點裝飾"><line x1="12" y1="70" x2="62" y2="42"></line><line x1="62" y1="42" x2="108" y2="12"></line><line x1="62" y1="42" x2="126" y2="70"></line><circle cx="12" cy="70" r="5"></circle><circle cx="62" cy="42" r="6"></circle><circle cx="108" cy="12" r="5"></circle><circle cx="126" cy="70" r="5"></circle></svg>
</div>

假設正在開發一個 `ASP.NET Core API`，目前已有三個 Commit：

<div class="gg-commit-flow" role="img" aria-label="A、B、C 三個 Commit，master 與 HEAD 指向 C">
<div class="gg-commit-track">
<div class="gg-commit-node"><span class="gg-commit-dot">A</span><strong><code>init project</code></strong></div>
<div class="gg-commit-link"></div>
<div class="gg-commit-node"><span class="gg-commit-dot">B</span><strong><code>add user API</code></strong></div>
<div class="gg-commit-link"></div>
<div class="gg-commit-node"><span class="gg-commit-dot">C</span><strong><code>add database config</code></strong></div>
</div>
<div class="gg-commit-ref"><code>master</code> 與 <code>HEAD</code> 指向 C</div>
</div>

剛完成 C 時執行了：

```bash
git add .
git commit -m "add database config"
```

接著才發現兩件事：

1. `database.yml` 的設定有錯。
2. Commit Message 不夠精確。

目標是撤回 C，修好內容後再提交。接下來分別看 `git reset` 與 `git commit --amend` 會怎麼處理。

<!-- endtab -->

<!-- tab git reset-->

`git reset` 可以把目前分支移到另一個 Commit。選擇的模式不同，Index 與 Working Tree 會跟著出現不同結果。

它常用來處理三種情況：

1. 已經執行 `git add`，但想取消暫存。
2. 已經執行 `git commit`，但想撤回 Commit 並保留程式碼。
3. 已經執行 `git commit`，而且確定連程式碼變更都不要了。

這次希望撤回 C，但保留程式碼繼續修改，因此執行：

```bash
git reset HEAD^
```

沒有指定模式時，`git reset` 預設使用 `--mixed`。`HEAD^` 表示目前 Commit 的上一個 Commit，所以目前分支會從 C 回到 B。

<div class="gg-before-after">
<div class="gg-snapshot"><h4>Reset 前</h4><p><code>master</code> 與 <code>HEAD</code> 指向 C，<code>database.yml</code> 已經放進 C。</p></div>
<div class="gg-command">git reset<br>HEAD^</div>
<div class="gg-snapshot"><h4>Reset 後</h4><p><code>master</code> 與 <code>HEAD</code> 回到 B，C 的檔案變更仍留在 Working Tree。</p></div>
</div>

<h2 class="gg-section">三個位置發生什麼變化</h2>

<div class="gg-three-zone">
<div class="gg-zone"><strong>Local Repository</strong><p>目前分支從 C 回到 B。C 不再是這個分支的最新 Commit。</p></div>
<div class="gg-arrow"><span>→</span><small>同步到 B</small></div>
<div class="gg-zone"><strong>Index</strong><p>內容回到 B 的狀態，所以 C 的變更不再是 Staged。</p></div>
<div class="gg-arrow"><span>↔</span><small>保留差異</small></div>
<div class="gg-zone"><strong>Working Tree</strong><p>保留 C 的檔案變更，可以接著修改，不必重新寫一次。</p></div>
</div>

如果 `database.yml` 是 C 才新增的檔案，B 與 Index 都沒有它。Reset 後，這個檔案仍留在 Working Tree，因此會顯示為 `Untracked`。

修改完 `database.yml` 後，再重新加入暫存區並建立 Commit：

```bash
git add config/database.yml
git commit -m "configure database connection"
```

最後的歷史會從 C 改成 D：

<div class="gg-commit-flow" role="img" aria-label="A、B、D 三個 Commit，master 與 HEAD 指向 D">
<div class="gg-commit-track">
<div class="gg-commit-node"><span class="gg-commit-dot">A</span><strong><code>init project</code></strong></div>
<div class="gg-commit-link"></div>
<div class="gg-commit-node"><span class="gg-commit-dot">B</span><strong><code>add user API</code></strong></div>
<div class="gg-commit-link"></div>
<div class="gg-commit-node"><span class="gg-commit-dot">D</span><strong><code>configure database connection</code></strong></div>
</div>
<div class="gg-commit-ref"><code>master</code> 與 <code>HEAD</code> 指向 D</div>
</div>

D 就是修改後重新建立的新 Commit。

<h2 class="gg-section">三種模式的差別</h2>

<div class="gg-table-scroll" role="region" aria-label="git reset 三種模式比較" tabindex="0">
<table class="gg-table">
<thead><tr><th scope="col">模式</th><th scope="col">目前分支</th><th scope="col">Index</th><th scope="col">Working Tree</th><th scope="col">適合情況</th></tr></thead>
<tbody>
<tr><th scope="row"><code>--soft</code></th><td>移到指定 Commit</td><td>保留原本內容</td><td>保留原本內容</td><td>撤回 Commit，但讓變更維持 Staged</td></tr>
<tr><th scope="row"><code>--mixed</code></th><td>移到指定 Commit</td><td>重設成指定 Commit</td><td>保留原本內容</td><td>撤回 Commit，讓變更回到 Unstaged。這是預設模式</td></tr>
<tr><th scope="row"><code>--hard</code></th><td>移到指定 Commit</td><td>重設成指定 Commit</td><td>重設成指定 Commit</td><td>連檔案變更都確定不要了</td></tr>
</tbody>
</table>
</div>

<div class="gg-note danger">
<strong><code>--hard</code> 會直接改寫 Working Tree</strong>
<p>尚未保存的檔案變更可能被覆蓋或刪除。只有確定這些內容不再需要時才使用。</p>
</div>

<!-- endtab -->

<!-- tab git commit --amend-->

如果只是想修正最後一個 Commit，`git commit --amend` 通常更直接。它會用新的 Commit 取代目前分支最後一個 Commit，不需要先把 Commit 拆回來。

<div class="gg-case-grid">
<div class="gg-case"><h4>Commit Message 寫錯</h4><p>檔案內容沒問題，只想把最後一次 Commit 的訊息改正。</p></div>
<div class="gg-case"><h4>Commit 漏掉檔案</h4><p>先把漏掉的檔案放進 Index，再把它補進最後一次 Commit。</p></div>
</div>

<h2 class="gg-section">Commit Message 寫錯</h2>

假設剛才執行：

```bash
git add .
git commit -m "add usr api"
```

發現 `usr` 拼錯了，想改成 `user`，可以直接執行：

```bash
git commit --amend -m "add user api"
```

<div class="gg-before-after">
<div class="gg-snapshot"><h4>原本</h4><p>A → B → C<br><code>add usr api</code></p></div>
<div class="gg-command">git commit<br>--amend</div>
<div class="gg-snapshot"><h4>修改後</h4><p>A → B → C'<br><code>add user api</code></p></div>
</div>

C' 是新的 Commit，所以 Commit Hash 也會改變。

<h2 class="gg-section">Commit 後發現漏掉檔案</h2>

假設剛提交：

```bash
git add UserService.cs
git commit -m "add user api"
```

接著發現 `UserController.cs` 沒有一起提交。先把漏掉的檔案放進 Index，再重做最後一次 Commit：

```bash
git add UserController.cs
git commit --amend --no-edit
```

這兩行指令分別做了以下事情：

1. `git add` 把漏掉的檔案加入 Index。
2. `--amend` 重新建立最後一次 Commit，內容使用目前的 Index。
3. `--no-edit` 保留原本的 Commit Message。

<div class="gg-before-after">
<div class="gg-snapshot"><h4>原本的 C</h4><p><code>UserService.cs</code></p></div>
<div class="gg-command">git add<br>git commit --amend</div>
<div class="gg-snapshot"><h4>新的 C'</h4><p><code>UserService.cs</code><br><code>UserController.cs</code></p></div>
</div>

Git 歷史看起來仍然只有一次功能提交，但最後那個 Commit 已經換成新的物件。

<h2 class="gg-section">為什麼 Hash 會改</h2>

Git 的 Commit 是不可變的。`git commit --amend` 並不是打開原本的 Commit 直接修改，而是照下面的順序重做一次：

<div class="gg-steps">
<div class="gg-step"><strong>1. 找到目前 Commit 的 Parent</strong><p>新的 Commit 會接回相同的上一個 Commit。</p></div>
<div class="gg-step"><strong>2. 讀取目前的 Index</strong><p>Index 裡有哪些內容，新的 Commit 就會收進哪些內容。</p></div>
<div class="gg-step"><strong>3. 決定 Commit Message</strong><p>可以換成新訊息，也可以用 <code>--no-edit</code> 保留原訊息。</p></div>
<div class="gg-step"><strong>4. 建立新 Commit</strong><p>目前分支改指向新 Commit，原本的 Commit 不再是分支頂端。</p></div>
</div>

<!-- endtab -->

<!-- tab reset 與 amend 怎麼選-->

兩個指令都會改寫目前分支的歷史，但使用時機不太一樣。

<div class="gg-table-scroll" role="region" aria-label="git reset 與 git commit amend 比較" tabindex="0">
<table class="gg-table">
<thead><tr><th scope="col">比較</th><th scope="col"><code>git reset HEAD^</code></th><th scope="col"><code>git commit --amend</code></th></tr></thead>
<tbody>
<tr><th scope="row">適合情況</th><td>想先撤回最後一次 Commit，再繼續修改或重新安排暫存內容</td><td>只想直接修正最後一次 Commit 的內容或訊息</td></tr>
<tr><th scope="row">會改變目前分支歷史</th><td>會</td><td>會</td></tr>
<tr><th scope="row">會立即建立新 Commit</th><td>不會</td><td>會</td></tr>
<tr><th scope="row">會移動分支指標</th><td>會，先移到指定 Commit</td><td>會，改指向新 Commit</td></tr>
<tr><th scope="row">原本 Commit 立即消失</th><td>不會，只是不再由目前分支指向</td><td>不會，只是不再由目前分支指向</td></tr>
<tr><th scope="row">可以透過 <code>reflog</code> 找回</th><td>通常可以</td><td>通常可以</td></tr>
</tbody>
</table>
</div>

<div class="gg-note">
<strong>選擇方式</strong>
<p>想把最後一次 Commit 拆回來，再慢慢整理，使用 <code>git reset</code>。只想把最後一次 Commit 直接換成修正版，使用 <code>git commit --amend</code>。</p>
</div>

`reflog` 會記錄本機分支與 `HEAD` 曾經指向的位置，所以原本的 Commit 通常還找得到。不過這不是永久備份，過期或清理後仍可能失去紀錄。

<!-- endtab -->

<!-- tab 已經 Push 怎麼辦-->

已經 Push 的 Commit 經過 `reset` 或 `amend` 後，本機歷史會跟遠端不同。一般的 `git push` 通常會拒絕這種 `non-fast-forward` 更新，因為遠端無法只靠往前新增 Commit 走到新的歷史。

<div class="gg-note danger">
<strong>改寫已公開的歷史會影響其他開發者</strong>
<p>強制 Push 可能讓其他人的本機分支與遠端歷史分岔。共享分支在改寫前要先確認團隊流程，不能只看本機結果正確就直接覆蓋遠端。</p>
</div>

如果團隊允許改寫該分支，可以使用：

```bash
git push --force-with-lease
```

`--force-with-lease` 會先檢查遠端分支是否仍是本機預期的版本。若遠端已經出現其他人推上去的新 Commit，Push 會被拒絕，避免直接把那些內容蓋掉。

它仍然是強制更新，不代表任何情況都安全。若 Commit 已經公開，而且不應改寫歷史，通常改用 `git revert` 建立一個新的反向 Commit，讓遠端歷史繼續往前走。

<!-- endtab -->

<!-- tab 撤回到特定 Commit-->

前面的例子都使用 `HEAD^` 回到上一個 Commit。若要回到更早的位置，可以先查看紀錄：

```bash
git log --oneline

e12d8ef (HEAD -> master) add database.yml in config folder
85e7e30 add hello
657fce7 add container
abb4f43 update index page
cef6e40 create index page
cc797cd init commit
```

<h2 class="gg-section">使用 Commit Hash 的相對位置</h2>

`e12d8ef^` 表示 `e12d8ef` 的上一個 Commit：

```bash
git reset e12d8ef^
```

<h2 class="gg-section">使用目前分支或 HEAD</h2>

此時 `HEAD` 與 `master` 都指向 `e12d8ef`，所以也可以寫成：

```bash
git reset master^
git reset HEAD^
```

這兩行在目前狀態下都會回到 `85e7e30`。`HEAD^` 也可以寫成 `HEAD~1`，兩者在「回到第一個 Parent」這個情況下代表相同位置。

<h2 class="gg-section">直接指定目標 Commit</h2>

如果已經知道要回到 `85e7e30`，可以直接指定：

```bash
git reset 85e7e30
```

以上指令都沒有另外寫模式，因此預設使用 `--mixed`。目前分支與 Index 會回到指定 Commit，Working Tree 則保留原本的檔案內容。

<!-- endtab -->

{% endtabs %}
