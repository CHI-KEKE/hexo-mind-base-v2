const {chromium}=require('../compression-review/node_modules/playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve('public');
const out=path.resolve('.codex-tmp/compression-cozy');
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.woff2':'font/woff2'};
const server=http.createServer((req,res)=>{let pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\/Mind\//,'/');let file=path.join(root,pathname);if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');if(!file.startsWith(root)||!fs.existsSync(file)){res.writeHead(404);return res.end();}res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');fs.createReadStream(file).pipe(res);});
(async()=>{await new Promise(r=>server.listen(4179,'127.0.0.1',r));const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});const page=await browser.newPage({viewport:{width:1440,height:1000}});const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto('http://127.0.0.1:4179/Mind/2026/09/06/CS-compression/',{waitUntil:'networkidle'});console.log('title',await page.title());if(await page.locator('.cozy-hero').count()!==1)throw Error('Cozy version missing');await page.waitForSelector('.mermaid-wrap svg',{timeout:60000,state:'attached'});const result=[];
for(const mode of ['desktop','mobile','dark']){
await page.setViewportSize(mode==='mobile'?{width:390,height:844}:{width:1440,height:1000});
if(mode==='dark'){await page.evaluate(()=>scrollTo(0,1000));await page.waitForTimeout(500);const toggle=page.locator('#darkmode');if(!await page.locator('#rightside-config-hide').evaluate(e=>e.classList.contains('show')))await page.locator('#rightside-config').click();await toggle.click();await page.waitForFunction(()=>document.documentElement.dataset.theme==='dark');await page.waitForTimeout(1500);}
const buttons=page.locator('#article-container .nav-tabs .tab');
for(let i=0;i<1;i++){
await buttons.nth(i).click();await page.waitForTimeout(180);const panel=page.locator('#article-container .tab-item-content.active');if(i===0)await page.locator('#article-container .tabs').screenshot({path:path.join(out,`${mode}-overview.png`)});await panel.screenshot({path:path.join(out,`${mode}-${i+1}.png`)});
if(mode==='mobile'){const wide=panel.locator('.compression-wide-diagram');for(let w=0;w<await wide.count();w++){await wide.nth(w).evaluate(e=>e.scrollLeft=e.scrollWidth);await wide.nth(w).screenshot({path:path.join(out,`mobile-${i+1}-right-${w}.png`)});}}
const info=await panel.evaluate(el=>({svg:el.querySelectorAll('.mermaid-wrap svg').length,errors:el.innerText.includes('Syntax error'),width:document.documentElement.scrollWidth,viewport:innerWidth,markers:[...el.querySelectorAll('path[marker-end]')].every(p=>{let m=p.getAttribute('marker-end').match(/#([^)'\"]+)/);return !m||!!document.getElementById(m[1])})}));result.push({mode,tab:i+1,...info});
}
}
const sheet=await browser.newPage({viewport:{width:1240,height:1000}});
for(const mode of ['desktop','mobile','dark']){await sheet.setContent(`<html><body style="margin:0;background:#ddd;font-family:sans-serif"><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:12px">${Array.from({length:10},(_,i)=>`<div><h3>${mode} / ${i+1}</h3><img style="width:100%" src="data:image/png;base64,${fs.readFileSync(path.join(out,`${mode}-${i+1}.png`)).toString('base64')}"></div>`).join('')}</div></body></html>`);await sheet.screenshot({path:path.join(out,`${mode}-contact.png`),fullPage:true});}
await page.goto('http://127.0.0.1:4179/Mind/2026/09/06/CS-compression-pure/',{waitUntil:'networkidle'});await page.locator('#article-container').screenshot({path:path.join(out,'pure.png')});console.log('pure',await page.locator('#article-container').innerText().then(t=>({byte23:t.includes('23 bytes'),hasRawTags:t.includes('{%')})));
fs.writeFileSync(path.join(out,'final-overview-results.json'),JSON.stringify({errors,result},null,2));console.log(JSON.stringify({errors,result}));await browser.close();server.close();})().catch(e=>{console.error(e);server.close();process.exit(1)});


