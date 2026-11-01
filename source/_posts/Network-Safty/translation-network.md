---
title: Translation API 網路與授權排查
date: 2026-10-22 08:37:00
categories: network-safety
description: 
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Devops/k8s/k8s2.png
tags:
toc:
toc_number:
comments :
---

{% tabs translation-network %}

<!-- tab 案件-->

<style>
.kubernetes-helm{--kh-blue:#326de6;--kh-link:#2455b5;--kh-bg:#fff;--kh-ink:#333;--kh-soft:#eef4ff;--kh-line:#d5deed;--kh-code:#182235;--kh-code-ink:#f3f6fc;--kh-danger:#b42318;--kh-danger-soft:#fff1f0;--kh-warn:#9a6700;--kh-warn-soft:#fff8df;background:var(--kh-bg);color:var(--kh-ink);padding:24px;font-family:'Segoe UI','PingFang TC','Microsoft JhengHei',sans-serif;line-height:1.85;overflow-wrap:anywhere;}
.kubernetes-helm *{box-sizing:border-box;}
#article-container .kubernetes-helm h2,#article-container .kubernetes-helm h3,#article-container .kubernetes-helm h4,.kubernetes-helm h2,.kubernetes-helm h3,.kubernetes-helm h4{color:var(--kh-ink);line-height:1.4;font-weight:800;margin:0 0 16px;}
.kubernetes-helm p{margin:12px 0;}
.kubernetes-helm a{color:var(--kh-link);text-decoration:underline;text-underline-offset:3px;}
.kubernetes-helm :focus-visible{outline:3px solid var(--kh-link);outline-offset:4px;}
.kubernetes-helm code{font-family:Consolas,monospace;background:var(--kh-soft);color:inherit;padding:2px 5px;border-radius:3px;overflow-wrap:anywhere;}
.kubernetes-helm .kh-hero{padding:28px 0 32px;margin-bottom:28px;border-bottom:3px solid var(--kh-blue);}
.kubernetes-helm .kh-emblem{display:block;width:58px;height:58px;margin-bottom:20px;background:var(--kh-blue);clip-path:polygon(50% 0,89% 19%,99% 61%,72% 96%,28% 96%,1% 61%,11% 19%);}
.kubernetes-helm .kh-hero h2{font-size:clamp(1.6rem,4vw,2.6rem);letter-spacing:-.02em;}
.kubernetes-helm .kh-hero p{max-width:46em;}
.kubernetes-helm .kh-section{padding-left:14px;border-left:5px solid var(--kh-blue);margin-top:32px!important;}
.kubernetes-helm .kh-note{padding:16px 20px;margin:22px 0;background:var(--kh-soft);border-left:4px solid var(--kh-blue);border-radius:4px;}
.kubernetes-helm .kh-note.warn{background:var(--kh-warn-soft);border-left-color:var(--kh-warn);}
.kubernetes-helm .kh-note.danger{background:var(--kh-danger-soft);border-left-color:var(--kh-danger);}
.kubernetes-helm .kh-note strong{display:block;margin-bottom:4px;}
.kubernetes-helm .kh-table-scroll{max-width:100%;overflow-x:auto;margin:22px 0;}
#article-container .kubernetes-helm table.kh-table,.kubernetes-helm table.kh-table{width:auto;max-width:100%;margin:0;border-collapse:collapse;table-layout:auto;background:var(--kh-bg);color:var(--kh-ink);}
.kubernetes-helm .kh-table.wide{width:100%;}
.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{padding:12px 16px;border:1px solid var(--kh-line);text-align:left;vertical-align:top;background:var(--kh-bg);color:var(--kh-ink);}
.kubernetes-helm .kh-table th{background:var(--kh-soft);font-weight:700;}
.kubernetes-helm .kh-code{margin:24px 0;background:var(--kh-code);color:var(--kh-code-ink);border-radius:4px;overflow:hidden;}
.kubernetes-helm .kh-code-label{padding:8px 16px;border-bottom:1px solid #43516a;font-size:.85rem;}
#article-container .kubernetes-helm pre.kh-pre,.kubernetes-helm pre.kh-pre{margin:0!important;padding:18px!important;background:var(--kh-code)!important;color:var(--kh-code-ink)!important;border:0!important;border-radius:0!important;box-shadow:none!important;text-shadow:none!important;white-space:pre!important;overflow-x:auto!important;font:14px/1.8 Consolas,monospace!important;tab-size:4;}
.kubernetes-helm .kh-diagram{overflow-x:auto;border:1px solid var(--kh-line);border-radius:4px;margin:22px 0;padding:16px;background:var(--kh-bg);}
.kubernetes-helm .kh-diagram svg{display:block;min-width:0;height:auto!important;margin:0 auto;background:var(--kh-bg)!important;}
.kubernetes-helm .kh-caption{font-size:.92em;margin:10px 0 0;color:var(--kh-ink);}
.kubernetes-helm .kh-checklist{list-style:none;margin:14px 0;padding:0;}
.kubernetes-helm .kh-checklist li{position:relative;padding:8px 0 8px 30px;}
.kubernetes-helm .kh-checklist li::before{content:'✓';position:absolute;left:0;top:9px;width:20px;height:20px;line-height:20px;text-align:center;border:1px solid var(--kh-blue);border-radius:50%;color:var(--kh-blue);font-weight:800;}
[data-theme='dark'] .kubernetes-helm{--kh-blue:#7fa9ff;--kh-link:#a4c2ff;--kh-bg:#17202e;--kh-ink:#eef2f8;--kh-soft:#23334e;--kh-line:#52647f;--kh-danger:#ff8f87;--kh-danger-soft:#3a2428;--kh-warn:#f0c36a;--kh-warn-soft:#3b3323;}
@media(max-width:600px){.kubernetes-helm{padding:12px;}.kubernetes-helm .kh-hero{padding:16px 0 24px;}.kubernetes-helm .kh-note{padding:14px;}.kubernetes-helm .kh-table th,.kubernetes-helm .kh-table td{padding:10px;min-width:7em;}.kubernetes-helm .kh-diagram{padding:8px;}}
</style>

<div class="kubernetes-helm">
<div class="kh-hero"><span class="kh-emblem" aria-hidden="true"></span><h2>503 到底卡在哪？代理找不到後面的服務</h2><p>畫面已經收到 503，代表請求至少走到某個代理。這個代理接著要把請求交給 Translation API 時，還沒等到 API 回話，連線就失敗了。</p></div>

<div class="kh-note danger"><strong>一句話先講完</strong><p>把代理想成櫃台：Claude 已經把需求交到櫃台，但櫃台聯絡不到後面的 Translation API。問題發生在「代理 → API」這一段，不是 API 裡面的登入或權限檢查。</p><p>目前只知道斷在代理後面，還不知道是 Service 沒找到可用 Pod、Pod 還沒 Ready、Port 對不上，還是中間網路斷掉。</p></div>

<h3 class="kh-section">503 卡點圖</h3>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Caller["Claude 工具"] -->|請求已送到這裡| Proxy["回傳 503 的代理，像櫃台"]
Proxy -->|轉交給後面的服務| Failed["沒接通 Translation API<br/>也沒等到 API 回話"]
Failed -.-> Unknown["還要找出哪一環斷了"]
Unknown -.-> Checks["檢查 Endpoint、Pod Ready、<br/>Port 與網路"]
style Failed fill:#fff1f0,stroke:#b42318,stroke-width:3px,color:#333
style Unknown fill:#fff8df,stroke:#9a6700,stroke-width:2px,color:#333
{% endmermaid %}

<p class="kh-caption">紅色是已經知道的斷點，黃色是接下來要查的範圍。圖沒有連進 Translation API，因為目前沒有證據顯示 API 收到這次請求。</p>
</div>

<div class="kh-table-scroll" role="region" aria-label="503 已確認與尚未確認事項" tabindex="0">
<table class="kh-table wide">
<thead><tr><th scope="col">判讀層次</th><th scope="col">目前結論</th></tr></thead>
<tbody>
<tr><td>現在知道的</td><td>某個代理回了 503。它想連後面的服務，但還沒收到任何 HTTP 回應就斷線。</td></tr>
<tr><td>現在還不知道的</td><td>是哪個代理回 503，以及 Service、Endpoint、Pod、Port 或網路中的哪一項出問題。</td></tr>
<tr><td>這次不用先查的</td><td><code>[Authorize]</code>、Firebase Token 與內部 IP Middleware。這些程式要等請求進入 Translation API 後才會執行。</td></tr>
</tbody>
</table>
</div>

<div class="kh-note"><strong>接下來先查兩件事就好</strong><p>先從完整回應標頭和存取日誌找出「是哪個代理回了 503」，再到那個環境檢查 Endpoint、Pod Ready、代理要連的 Port，以及程式真正監聽的 Port。找到這兩項，才有辦法指出是哪個元件壞掉。</p></div>

</div>

<!-- endtab -->

<!-- tab InternalIpAuthorizationMiddleware-->

<div class="kubernetes-helm">

<h3 class="kh-section">內部請求要同時帶對 IP 和 Token</h3>

<p>Translation API 收到請求後，會看來源 IP 是否在白名單，也會比對 <code>Authorization</code> 裡的內部固定 Token。兩個都正確，這次請求才會取得內部使用者身分。</p>

<p>只要有一項不符，程式就不建立內部身分，但請求仍會往後走。這段 Middleware 不會自己擋掉外部 IP，也不會跳過後面的驗證流程。</p>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Request["請求進入 Translation API"] --> Ip{"來源 IP 在白名單嗎？"}
Ip -->|否| Continue["不建立內部身分"]
Ip -->|是| Token{"Authorization 是正確的內部固定 Token 嗎？"}
Token -->|否| Continue
Token -->|是| Identity["建立 InternalUser 身分與 Admin claim"]
Identity --> Authentication["執行 UseAuthentication"]
Continue --> Authentication
Authentication --> Authorization["路由階段執行 UseAuthorization"]
Authorization --> Endpoint["依 endpoint 與業務規則決定結果"]
{% endmermaid %}

<p class="kh-caption">兩條失敗分支會匯入一般後續流程，不代表請求已獲准，也不代表請求立刻被拒絕。</p>
</div>

<h3 class="kh-section">請求進入 API 後，檢查順序是什麼</h3>

<p>順序是內部 IP Middleware、身分驗證、授權檢查。即使前面已經拿到內部身分，後面的驗證與授權仍然會繼續執行。</p>

<p>一般使用者登入後會拿到 Firebase Token。API 會檢查 Token 是誰簽發、給誰使用、是否過期；至於某支 API 一定要不要登入，仍要看該 endpoint 的設定。</p>

<h3 class="kh-section">程式看到的來源 IP 從哪裡來</h3>

<p>程式先看連線上的 <code>RemoteIpAddress</code>。如果請求有 <code>X-Forwarded-For</code>，就改拿其中第一個 IP，因為直接連到 API 的可能是代理，不一定是原始呼叫方。</p>

<p>白名單來自 <code>InternalAuth:AllowedIps</code>。目前 <code>appsettings.json</code> 與 <code>appsettings.Development.json</code> 都列出三個 IP，部署環境仍可能覆寫這些設定。</p>

<div class="kh-note warn"><strong>這裡要小心</strong><p>程式沒有確認 <code>X-Forwarded-For</code> 一定由可信任代理寫入。因此，入口代理怎麼處理這個標頭，會直接影響白名單判斷是否可靠。</p></div>

<h3 class="kh-section">內部固定 Token 與 Firebase Token</h3>

<div class="kh-table-scroll" role="region" aria-label="內部固定 Token 與 Firebase Token 比較" tabindex="0">
<table class="kh-table wide">
<thead><tr><th scope="col">憑證</th><th scope="col">來源</th><th scope="col">驗證方式</th><th scope="col">用途</th></tr></thead>
<tbody>
<tr><td>內部固定 Token</td><td><code>InternalAuth:PermanentToken</code></td><td>Middleware 完整比對 <code>Authorization: Bearer &lt;Token&gt;</code> 與來源 IP</td><td>符合條件時建立內部身分</td></tr>
<tr><td>Firebase Token</td><td>一般使用者登入流程</td><td>JWT 驗證簽發者、使用對象與有效期限</td><td>確認一般使用者身分</td></tr>
</tbody>
</table>
</div>

<p>內部固定 Token 不會在每次請求時產生。<code>appsettings.Development.json</code> 有自己的設定值，其他環境使用哪個值，須以實際載入的設定為準。固定 Token 必須保密，公開文件不應列出實際內容。</p>

<h3 class="kh-section">建立的身分與 <code>Admin</code> claim</h3>

<p>兩個條件都符合時，Middleware 會建立已驗證的 <code>ClaimsIdentity</code>，放入名稱 <code>InternalUser</code>、代表內部使用者的 Email，以及值為 <code>Admin</code> 的角色 claim。Claim 是附在使用者身分上的資料，後續授權程式可以讀取。</p>

<div class="kh-note"><strong><code>Admin</code> claim 不等於所有管理員權限</strong><p><code>UserRepo</code> 會另外從 Email 與角色名單計算業務角色。請求最後能執行哪些功能，仍要看 endpoint 與業務邏輯如何檢查身分及角色。</p></div>


</div>

<!-- endtab -->

<!-- tab [Authorize]-->

<div class="kubernetes-helm">

<h3 class="kh-section"><code>[Authorize]</code> 只先問：有沒有可用的登入身分</h3>

<p>Controller 或 Action 標了 <code>[Authorize]</code> 後，請求要先有一個已通過驗證的使用者身分，才能進入那段程式。</p>

<p>這個身分可能來自 Firebase Token，也可能由內部 IP Middleware 建立。只有 <code>[Authorize]</code> 時，它只確認「已登入」，不代表一定是 <code>Admin</code> 或 <code>Translator</code>。</p>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Request["請求進入 API"] --> Mark{"目標 Action 標有 [Authorize] 嗎？"}
Mark -->|否| Action["進入 Action"]
Mark -->|是| Identity{"目前有已驗證的身分嗎？"}
Identity -->|否| Reject["框架拒絕進入 Action"]
Identity -->|是| Action
Action --> Role{"Action 或 Service 另有角色檢查嗎？"}
Role -->|否| Logic["執行後續程式邏輯"]
Role -->|是| Business{"業務角色符合要求嗎？"}
Business -->|否| Deny["業務授權拒絕操作"]
Business -->|是| Logic
{% endmermaid %}

<p class="kh-caption">沒有標示 <code>[Authorize]</code>，只代表進入 Action 前沒有強制要求驗證身分，不保證 Action 一定成功。</p>
</div>

<p>進入 Action 後，程式還可能再查角色，也可能因資料或外部服務失敗。連不連得到 API、是否已登入、是否有操作權限，是三件不同的事。</p>

<h3 class="kh-section">Token、Email 與業務角色的鏈路</h3>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Firebase["Firebase Token"] --> Auth["UseAuthentication 驗證 Token"]
Internal["白名單 IP 加內部固定 Token"] --> Middleware["InternalIpAuthorizationMiddleware 建立身分"]
Auth --> Email["身分中的 Email claim"]
Middleware --> Email
Email --> Repo["UserRepo.getRoles"]
Repo --> User["先加入 User"]
Repo --> Lists["比對 Admin 與 Translator 名單"]
Lists --> Roles["產生 RoleType"]
{% endmermaid %}

<p class="kh-caption">兩種 Token 負責建立或驗證身分，<code>UserRepo</code> 再用 Email 計算自己的業務角色。</p>
</div>

<ol>
<li><code>UserRepo</code> 從目前身分的 Email claim 取得 <code>CurrentUserId</code>。</li>
<li><code>getRoles()</code> 先加入基本的 <code>User</code> 角色。</li>
<li>如果有 Email，就用它對照 <code>_N1CONFIG:Roles:Admin</code> 與 <code>_N1CONFIG:Roles:Translator</code>，加入符合的 <code>RoleType</code>。</li>
<li><code>GET /api/translations/roles</code> 的 <code>AdminController.GetRoles()</code> 只把 <code>UserRepo.Roles</code> 轉成文字回傳，不負責驗證 Token，也不會賦予角色。</li>
</ol>

<p><code>GET /api/translations/roles</code> 本身沒有標示 <code>[Authorize]</code>。若請求沒有 Email claim，依目前算法會回傳 <code>User</code>。</p>

<p>例如 <code>RollbackTranslation</code> 同時標有 <code>[Authorize]</code>，並在 Action 內呼叫 <code>CheckAuthRole(RoleType.Admin)</code>。只取得已驗證身分，仍不足以執行這項操作。</p>


</div>

<!-- endtab -->

<!-- tab HTTP 503-->

<div class="kubernetes-helm">

<h3 class="kh-section">先講答案：代理要轉給 Translation API 時沒接通</h3>

<div class="kh-note danger"><strong>先別查 API 授權</strong><p>目前的錯誤是在代理往後連線時發生，Translation API 很可能還沒看到這次請求。因此，<code>[Authorize]</code>、Firebase Token 與內部 IP 白名單不是第一個要查的地方。</p></div>

<h3 class="kh-section">錯誤訊息其實說了什麼</h3>

<div class="kh-code">
<div class="kh-code-label">原始錯誤訊息</div>
<pre class="kh-pre">upstream connect error or disconnect/reset before headers.
retried and the latest reset reason: remote connection failure</pre>
</div>

<p><code>before headers</code> 的意思是：代理還沒收到後方服務的 HTTP 回應，連線就斷了，所以只好回 503。這不能證明 Translation API 收到請求，也不能直接說一定是 Port 設錯。</p>

<p>Envoy 常會回這種文字，但目前還不能只靠一句訊息就認定一定是 Envoy。要知道是哪個代理回的，仍要看完整回應標頭與同一時間的代理日誌。</p>

<h3 class="kh-section">先確認：真正送出請求的是本機，還是雲端</h3>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Claude["Claude Desktop 發起工具呼叫"] --> Type{"Translation 請求由哪種工具送出？"}
Type -->|本機 MCP 或桌面擴充| Local["使用電腦送出 HTTP 請求"]
Type -->|遠端 MCP Connector| Cloud["Anthropic 雲端送出 HTTP 請求"]
Local --> LocalNet["使用當下的路由、DNS 與代理設定"]
Cloud --> CloudNet["使用雲端環境的路由與 DNS"]
LocalNet --> Domain["translation.qa.91dev.tw"]
CloudNet --> Domain
{% endmermaid %}

<p class="kh-caption">Claude 會使用雲端服務處理對話，但真正發送 Translation HTTP 請求的位置，取決於實際使用的工具。</p>
</div>

<p>本機 MCP 會使用這台電腦當下的網路與 DNS；遠端 Connector 則從雲端送出。電腦連上 VPN，不代表雲端工具也跟著進入公司網路。Chrome Extension 也要看實際是哪個功能在送請求。</p>

<p>兩種 Connector 的執行位置可參考 <a href="https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors">Claude 的本機與遠端 Connector 說明</a>。</p>

<p>當時一般 Wi-Fi 對該網域解析到公開 IP <code>35.201.120.17</code>。即使請求從雲端送出，也不能只憑「公司內網位址無法從雲端連接」這項推測，就斷定該次請求連到私有 IP 或已找出 503 根因。</p>

<h3 class="kh-section">VPN、TLS、DNS、防火牆目前都只是候選</h3>

<div class="kh-table-scroll" role="region" aria-label="503 排查假設與確認方式" tabindex="0">
<table class="kh-table wide">
<thead><tr><th scope="col">排查假設</th><th scope="col">目前能確認的事</th><th scope="col">下一步證據</th></tr></thead>
<tbody>
<tr><td>VPN 或路由</td><td>一般本機子程序使用同一台電腦的路由，不能直接認定 MCP 沒有繼承路由，也不宜先套用 <code>HTTP_PROXY</code> 或 <code>HTTPS_PROXY</code>。</td><td>比較終端機與工具的 DNS、環境變數、代理設定及執行位置。雲端工具則檢查雲端可到達的入口。</td></tr>
<tr><td>mTLS 或 SSL 憑證</td><td><code>remote connection failure</code> 沒有指出是否在 TLS 握手失敗，也無法證明是私有 CA。</td><td>查看實際端點、TLS 錯誤與代理日誌。不要把 <code>NODE_TLS_REJECT_UNAUTHORIZED=0</code> 當成解法，CA 問題應正確設定信任鏈。</td></tr>
<tr><td>DNS 解析</td><td>公司內網與一般 Wi-Fi 的 DNS 答案不同，但不知道事故請求的工具解析到哪個位址。</td><td>在工具實際執行環境查 DNS；固定測試某個 IP 時用 <code>curl --resolve</code> 保留原網域的 HTTPS 條件。</td></tr>
<tr><td>防火牆或 IP 白名單</td><td>基礎設施限制可能存在，但缺少防火牆或入口日誌。<code>Origin</code> 與 CORS 不代表網路可達，內部 IP Middleware 也沒有封鎖所有外部 IP。</td><td>檢查入口、防火牆與負載平衡器日誌，並核對實際網路政策。</td></tr>
</tbody>
</table>
</div>

<div class="kh-note warn"><strong>先不要猜根因</strong><p>要還原當時發生什麼事，至少要知道請求從哪裡送出、發生時間、完整回應標頭，以及同一時間的代理日誌。</p></div>

<h3 class="kh-section">進到 Kubernetes 後，請求會經過這幾站</h3>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Client["呼叫方"] -->|HTTPS| Proxy["入口代理"]
Proxy -->|轉送上游| Service["Kubernetes Service"]
Service -->|選擇可用 Endpoint| Pod["Translation Pod"]
Pod -->|容器監聽 Port| App["Translation API"]
{% endmermaid %}

<p class="kh-caption">此圖只表示需要逐層核對的上游路徑，不代表每一層都已證實存在或已確認故障。</p>
</div>

<p>先找出是哪一站回了 503，再往它的下一站查。程式庫裡有兩套部署資料，不代表它們同時生效，所以不能把兩套 Port 放在一起就判定衝突。</p>

<div class="kh-table-scroll" role="region" aria-label="兩套部署資料比較" tabindex="0">
<table class="kh-table wide">
<thead><tr><th scope="col">部署資料</th><th scope="col">程式庫中的設定</th><th scope="col">尚需確認</th></tr></thead>
<tbody>
<tr><td>Helm 部署</td><td><code>charts/translation-web-api/values-tw-qa.yaml</code> 與 <code>values-tw-prod.yaml</code> 的 <code>api.servicePort</code> 都是 <code>50350</code>。根目錄 <code>Dockerfile</code> 以建置參數 <code>NYS_PORT</code> 設定 <code>EXPOSE</code>，並用 <code>--urls http://*:${NYS_PORT}</code> 啟動。<code>pipeline/build-config.sh</code> 匯出的 Port 是 <code>50350</code>。</td><td>共用 pipeline 如何傳入 <code>NYS_PORT</code>、Helm 模板產出的 Service <code>targetPort</code>，以及實際 Pod 監聽 Port。</td></tr>
<tr><td><code>k8s/template</code> 部署</td><td><code>deploy.yaml</code> 的 <code>containerPort</code> 與 probe Port 是 <code>80</code>；<code>svc.yaml</code> 的 Service Port 與 <code>targetPort</code> 也都是 <code>80</code>。</td><td>這套模板是否仍用於發生錯誤的環境。</td></tr>
</tbody>
</table>
</div>



<h3 class="kh-section">Pod 不 Ready 或重啟，也可能讓代理找不到服務</h3>

<p><code>k8s/template/deploy.yaml</code> 的 readiness probe 呼叫 <code>/api/translations/health?readness</code>。這個路徑對應的 <code>AdminController.Health()</code> 直接回傳 <code>OK</code>，沒有檢查 MongoDB 或 Firebase。</p>

<p>如果 probe 失敗，先看 Pod 有沒有啟動、程式監聽哪個 Port、probe 連線結果和 Pod 事件，不要先猜是 MongoDB 或 Firebase。</p>

<p>Helm values 設定的記憶體上限為 <code>1000Mi</code>，另有 <code>COMPlus_GCHeapHardLimit</code>。Pod OOM 或反覆重啟也是排查方向，但只有 Pod 狀態、事件或前一次容器日誌出現對應證據時，才能列為原因。</p>

<h3 class="kh-section">建議的排查順序</h3>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Headers["保存完整回應標頭、時間、Host 與路徑"] --> Source["對照入口存取日誌，確認 503 回應來源"]
Source --> Route["核對 Ingress、Service、EndpointSlice 與 Deployment"]
Route --> Ready{"Service 有可用 Endpoint 嗎？"}
Ready -->|否| Probe["追查 readiness、selector、Pod 事件與重啟"]
Ready -->|是| Connect["追查監聽 Port、網路連通性與代理設定"]
Probe --> Evidence["用同一時間的日誌確認原因"]
Connect --> Evidence
{% endmermaid %}

<p class="kh-caption">流程用觀察結果縮小範圍，不把 503 文字本身當成根因證據。</p>
</div>

<div class="kh-code">
<div class="kh-code-label">Kubernetes 檢查指令</div>
<pre class="kh-pre">kubectl get ingress,svc,deploy,pods -n &lt;namespace&gt;
kubectl get endpointslices -n &lt;namespace&gt; -l kubernetes.io/service-name=&lt;service-name&gt;
kubectl describe svc &lt;service-name&gt; -n &lt;namespace&gt;
kubectl describe pod &lt;pod-name&gt; -n &lt;namespace&gt;
kubectl logs &lt;pod-name&gt; -n &lt;namespace&gt; --previous</pre>
</div>

<h3 class="kh-section">Envoy 可以想成轉送請求的櫃台</h3>

<p>Envoy 站在呼叫方與 Translation API 中間，先收請求，再決定要轉給哪個服務。它也負責重試和記錄連線狀態。Istio 常用 Envoy 來實際轉送服務之間的流量。</p>

<p>套到這次情況，就是「Claude → 代理 → Translation API」。代理有收到前面的請求，卻聯絡不到後面的 API，所以由代理回 503，Translation API 不一定看過這次請求。</p>

<p>要確認是否為 Envoy，以及它位於哪一段連線，需要對照 HTTP 回應標頭和代理日誌。可參考 <a href="https://www.envoyproxy.io/docs/envoy/v1.36.0/configuration/observability/access_log/usage">Envoy 存取日誌文件</a>中的 response flags 與 response code details，區分上游連線失敗、連線被重設及其他 503 情境。</p>
</div>

<!-- endtab -->

<!-- tab TLS 錯誤-->

<div class="kubernetes-helm">

<h3 class="kh-section">TLS 錯誤代表連 HTTPS 入口都還沒成功</h3>

<div class="kh-code">
<div class="kh-code-label">原始錯誤訊息</div>
<pre class="kh-pre">Client network socket disconnected before secure TLS connection was established</pre>
</div>

<p>這行錯誤表示 HTTPS 安全連線還沒建立完成就斷了，所以連 HTTP 回應都沒拿到，也不會有 401、403 或 503 這類狀態碼。</p>

<p>但只看這一行，還不知道是誰把連線關掉，也不能直接說是憑證、網路或代理設定造成。</p>

<h3 class="kh-section">TLS 錯誤和 503，斷在不同位置</h3>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Caller["呼叫端送出 HTTPS 請求"] --> TLS{"與 HTTPS 入口完成 TLS 握手嗎？"}
TLS -->|否| Error["呼叫端回報 TLS 連線錯誤，沒有 HTTP 狀態碼"]
TLS -->|是| Gateway["HTTPS 入口處理 HTTP 請求"]
Gateway --> Upstream{"入口連往上游成功嗎？"}
Upstream -->|否| Status["入口代理可能回傳 HTTP 503"]
Upstream -->|是| API["請求交由 Translation API 處理"]
{% endmermaid %}

<p class="kh-caption">前半段是呼叫端到 HTTPS 入口，後半段是入口到 Translation 上游。兩段連線可能各自失敗。</p>
</div>

<div class="kh-table-scroll" role="region" aria-label="HTTP 503 與 TLS socket error 比較" tabindex="0">
<table class="kh-table wide">
<thead><tr><th scope="col">比較</th><th scope="col">HTTP 503 upstream error</th><th scope="col">TLS socket error</th></tr></thead>
<tbody>
<tr><th scope="row">呼叫端收到什麼</th><td>一個 HTTP 503 回應</td><td>連線錯誤，沒有 HTTP 回應</td></tr>
<tr><th scope="row">已能確定的階段</th><td>呼叫端已收到某個 HTTP 服務或代理的回應，失敗可能發生在它往上游的連線。</td><td>呼叫端與其連接的 HTTPS 端點尚未完成 TLS 握手。</td></tr>
<tr><th scope="row">不能直接推論</th><td>一定是特定代理、Pod 或 Port 的問題。</td><td>一定是憑證、防火牆或 Translation API 的問題。</td></tr>
</tbody>
</table>
</div>

<p>如果 Claude 使用的工具在連上 HTTPS 入口前就中斷，呼叫端會看到 TLS 錯誤。如果工具已連上入口，而入口往 Translation 上游的連線失敗，呼叫端才可能收到代理回傳的 503。兩種訊息可能出現在不同次請求，同一次呼叫的不同網路區段也可能各自有不同失敗原因。</p>
</div>

<!-- endtab -->

<!-- tab 外網 DNS 與連線分析-->

<div class="kubernetes-helm">

<h3 class="kh-section">同一個網域，內網與一般 Wi-Fi 會走不同入口</h3>

<p>電腦連公司內網時，DNS 會指向私有入口；連一般 Wi-Fi 時，DNS 會指向公開入口。下面是兩個不同網路環境的結果。</p>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Domain["translation.qa.91dev.tw"] --> Network{"查詢時連接哪種網路？"}
Network -->|公司內網| PrivateDns["private-ingress-alb.eks.91dev.tw"]
PrivateDns --> AwsAlb["internal-private-eks-ingress-alb-1654285349.ap-northeast-1.elb.amazonaws.com"]
AwsAlb --> PrivateIp["10.50.45.132 或 10.50.40.7"]
Network -->|一般 Wi-Fi| PublicIp["35.201.120.17"]
{% endmermaid %}

<p class="kh-caption">這是分流 DNS 的觀察結果。它只能證明查詢結果不同，不能單靠 DNS 推定兩個入口後方的完整轉送路徑。</p>
</div>

<div class="kh-table-scroll" role="region" aria-label="內外網 DNS 結果比較" tabindex="0">
<table class="kh-table wide">
<thead><tr><th scope="col">測試網路</th><th scope="col">當時的解析結果</th></tr></thead>
<tbody>
<tr><td>公司內網</td><td><code>translation.qa.91dev.tw</code> → <code>private-ingress-alb.eks.91dev.tw</code> → <code>internal-private-eks-ingress-alb-1654285349.ap-northeast-1.elb.amazonaws.com</code> → <code>10.50.45.132</code> 或 <code>10.50.40.7</code></td></tr>
<tr><td>一般 Wi-Fi</td><td><code>translation.qa.91dev.tw</code> → <code>35.201.120.17</code></td></tr>
</tbody>
</table>
</div>

<p>公司內網的結果是私有 IP，一般 Wi-Fi 的結果是公開 IP。這能確認當時兩個網路環境走向不同入口，但不能證明入口後方如何轉送，也不能單憑公開 IP 判定由哪個負載平衡器回應。</p>

<p>要分析 Claude 的呼叫，仍須先確定替 Claude 發送 HTTP 請求的工具在哪裡執行，以及它當時解析到哪個位址。</p>

<h3 class="kh-section">直接打公開 IP，不等於用原網域測試</h3>

<div class="kh-code">
<div class="kh-code-label">一般 Wi-Fi 的測試紀錄</div>
<pre class="kh-pre">curl -v https://35.201.120.17/api/v3/projects
# curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to 35.201.120.17:443</pre>
</div>

<p>把 IP 直接放進 HTTPS 網址後，SNI、憑證名稱驗證與 HTTP <code>Host</code> 都會跟著改變，所以測試條件已經不是原本的網域。</p>

<p>這不代表請求「沒有 Host header」。如果 HTTP 請求成功送出，Host 會是該 IP。上述 <code>curl: (35)</code> 只說明 TLS 連線失敗，無法直接推定為憑證名稱不符，也沒有取得 HTTP 503。</p>

<h3 class="kh-section">指定 IP，同時保留原網域條件</h3>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Curl["curl --resolve"] --> Dns["只覆寫本次 DNS 結果為 35.201.120.17"]
Dns --> Tls["URL 與 TLS SNI 保留 translation.qa.91dev.tw"]
Tls --> Http["HTTP Host 保留 translation.qa.91dev.tw"]
Http --> Result["觀察指定入口的 TLS 與 HTTP 結果"]
{% endmermaid %}

<p class="kh-caption"><code>--resolve</code> 只控制本次連線目的 IP，不會讓一般 Wi-Fi 取得公司內網的存取能力。</p>
</div>

<div class="kh-code">
<div class="kh-code-label">保留網域條件的指定 IP 測試</div>
<pre class="kh-pre">curl -v --resolve translation.qa.91dev.tw:443:35.201.120.17 \
  https://translation.qa.91dev.tw/api/v3/projects</pre>
</div>

<p>比較公司內網、一般 Wi-Fi 與 Claude 工具的結果時，應記錄每次執行位置、DNS 答案、完整回應或錯誤，以及發生時間。</p>

<p>參考資料：<a href="https://everything.curl.dev/usingcurl/connections/name.html">curl 的名稱解析說明</a>、<a href="https://curl.se/libcurl/c/libcurl-errors.html">curl 錯誤碼</a>。</p>
</div>

<!-- endtab -->

<!-- tab 外網存取方式-->

<div class="kubernetes-helm">

<h3 class="kh-section">一般使用者要先登入，再拿 Firebase Token 呼叫 API</h3>

<p>先透過 VPN 開啟 QA 網站並登入，再從瀏覽器 Network 面板找到 Firebase Token，最後把它放進 API 請求的 <code>Authorization</code> 標頭。</p>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Vpn["連上可存取 QA 的公司網路或 VPN"] --> Site["開啟 translation.qa.91dev.tw 並登入"]
Site --> DevTools["在瀏覽器 Network 面板選擇任一 API request"]
DevTools --> Token["讀取 Authorization: Bearer eyJ..."]
Token --> Call["帶 Firebase Token 呼叫 Translation API"]
Call --> Valid{"Token 仍在有效期內嗎？"}
Valid -->|是| Auth["API 驗證 Token 與 endpoint 授權"]
Valid -->|否| Expired["回傳 401，重新登入取得 Token"]
{% endmermaid %}

<p class="kh-caption">這條流程描述 Firebase Token 的取得與使用，不等同於內部固定 Token 的驗證路徑。</p>
</div>

<h3 class="kh-section">操作步驟</h3>

<ol>
<li>開啟 <code>translation.qa.91dev.tw</code>。QA 需要公司內網或 VPN。</li>
<li>完成登入後開啟瀏覽器開發者工具。</li>
<li>在 Network 面板選擇任一 API request。</li>
<li>從 request headers 找到 <code>Authorization: Bearer eyJ...</code>。</li>
<li>將 Token 放入 API 呼叫的 <code>Authorization</code> 標頭。</li>
</ol>

<div class="kh-code">
<div class="kh-code-label">帶 Firebase Token 呼叫</div>
<pre class="kh-pre">curl https://translation.qa.91dev.tw/api/v3/projects \
  -H "Authorization: Bearer eyJhbGci......"</pre>
</div>

<div class="kh-table-scroll" role="region" aria-label="外網存取注意事項" tabindex="0">
<table class="kh-table wide">
<thead><tr><th scope="col">項目</th><th scope="col">說明</th></tr></thead>
<tbody>
<tr><td>Firebase Token 有效期</td><td><strong>1 小時</strong>，過期會回傳 <code>401</code>。</td></tr>
<tr><td>QA 環境</td><td>只能從內網存取，需要 VPN。</td></tr>
<tr><td>Production 環境</td><td><code>translation.91app.io</code> 或 <code>translation.io.91app.com</code>。</td></tr>
</tbody>
</table>
</div>

<div class="kh-note danger"><strong>Token 屬於敏感憑證</strong><p>文章與截圖不應保留完整 Token。分享排查紀錄時只保留足以辨識憑證類型的開頭，並遮蔽其餘內容。</p></div>
</div>

<!-- endtab -->

<!-- tab 環境資訊-->

<div class="kubernetes-helm">

<h3 class="kh-section">QA 與 Production 走不同入口</h3>

<p>QA 走內網 ALB，需要公司網路或 VPN；兩個 Production 網域走 GCP CLB。這裡只整理已知入口，不代表已經知道入口後面的完整路徑。</p>

<div class="kh-diagram">

{% mermaid %}
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "14px"}}}%%
flowchart TB
Caller["呼叫方"] --> Env{"目標環境？"}
Env -->|QA| QaDomain["translation.qa.91dev.tw"]
QaDomain --> QaEntry["內網 ALB，需要 VPN"]
Env -->|Production 主要網域| ProdDomain["translation.91app.io"]
ProdDomain --> ProdEntry["GCP CLB"]
Env -->|Production 備用網域| BackupDomain["translation.io.91app.com"]
BackupDomain --> BackupEntry["GCP CLB"]
{% endmermaid %}

<p class="kh-caption">三條分支代表環境入口選擇，不表示請求會依序經過三個網域。</p>
</div>

<div class="kh-table-scroll" role="region" aria-label="Translation API 環境資訊" tabindex="0">
<table class="kh-table wide">
<thead><tr><th scope="col">環境</th><th scope="col">Domain</th><th scope="col">備註</th></tr></thead>
<tbody>
<tr><td>QA</td><td><code>translation.qa.91dev.tw</code></td><td>內網 ALB，需要 VPN</td></tr>
<tr><td>Production</td><td><code>translation.91app.io</code></td><td>GCP CLB</td></tr>
<tr><td>Production 備用入口</td><td><code>translation.io.91app.com</code></td><td>GCP CLB</td></tr>
</tbody>
</table>
</div>

<div class="kh-note"><strong>排查時先固定環境</strong><p>記錄網域、網路位置、DNS 結果與發生時間，再比對該環境的入口日誌與 Kubernetes 狀態。不同環境的 Port 或模板不能直接混在一起判定衝突。</p></div>
</div>

<!-- endtab -->

{% endtabs %}
