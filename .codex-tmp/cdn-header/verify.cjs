const {chromium}=require('../compression-review/node_modules/playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const base=process.env.VERIFY_BASE||'http://127.0.0.1:4187';
const root=path.resolve('public'),out=path.resolve(process.env.VERIFY_OUT||'.codex-tmp/cdn-header/screens');fs.mkdirSync(out,{recursive:true});
const mime={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.svg':'image/svg+xml'};
const server=http.createServer((req,res)=>{let f=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\/Mind\//,'/'));if(!f.startsWith(root+path.sep)){res.writeHead(403);return res.end();}if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');if(!fs.existsSync(f)){res.writeHead(404);return res.end();}res.setHeader('Content-Type',mime[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);});
(async()=>{
await new Promise(r=>server.listen(4187,'127.0.0.1',r));
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage({viewport:{width:1500,height:1000}}),errors=[],results=[];
page.on('pageerror',e=>errors.push(e.message));
const response=await page.goto(base+'/Mind/2026/09/28/K8S-CDN-Header-Lost/',{waitUntil:'networkidle'});
if(response.status()!==200)throw Error('Article HTTP '+response.status());
const onlineArticle=await response.text();
fs.writeFileSync(path.join(out,'served.html'),onlineArticle);
if(base.startsWith('https:')&&onlineArticle!==fs.readFileSync('public/2026/09/28/K8S-CDN-Header-Lost/index.html','utf8'))throw Error('Published HTML differs from built article');
await page.waitForSelector('.kh-diagram svg',{state:'attached',timeout:60000});
const tabs=page.locator('.tabs > .nav-tabs > .tab');if(await tabs.count()!==6)throw Error('six tabs required');
for(const mode of ['desktop','mobile','dark']){
await page.setViewportSize(mode==='mobile'?{width:390,height:844}:{width:1500,height:1000});
if(mode==='dark'){await page.evaluate(()=>scrollTo(0,1000));await page.waitForTimeout(400);if(!await page.locator('#rightside-config-hide').evaluate(e=>e.classList.contains('show')))await page.locator('#rightside-config').click();await page.locator('#darkmode').click();await page.waitForFunction(()=>document.documentElement.dataset.theme==='dark');await page.waitForTimeout(1000);}
for(let i=0;i<6;i++){
await tabs.nth(i).click();await page.waitForTimeout(400);
const panel=page.locator('.tabs > .tab-contents > .tab-item-content.active');
const style='#nav,#rightside{visibility:hidden!important;}';
await panel.screenshot({path:path.join(out,`${mode}-tab-${i+1}.png`),style});
for(const [sel,label] of [['.kh-code','code'],['.kh-diagram','diagram']]){const els=panel.locator(sel);for(let j=0;j<await els.count();j++)await els.nth(j).screenshot({path:path.join(out,`${mode}-${label}-${i+1}-${j}.png`),style});}
results.push(await panel.evaluate((el)=>({tab:el.id,mode:document.documentElement.dataset.theme,viewport:innerWidth,width:document.documentElement.scrollWidth,visible:document.querySelectorAll('.tabs > .tab-contents > .active').length,diagrams:el.querySelectorAll('.kh-diagram svg').length,rawTags:/\{%|<div class=|Syntax error|Lexical error/.test(el.innerText),arrows:[...el.querySelectorAll('.kh-diagram [marker-end]')].every(e=>{let m=e.getAttribute('marker-end').match(/#([^)'\"]+)/);return m&&!!document.getElementById(m[1]);}),codes:[...el.querySelectorAll('.kh-code')].map(e=>({frame:getComputedStyle(e).backgroundColor,code:getComputedStyle(e.querySelector('pre')).backgroundColor}))})));
}console.log(mode,'complete');
}
await page.goto(base+'/Mind/2026/09/28/K8S-CDN-Header-Lost-pure/',{waitUntil:'networkidle'});
const pure=await page.locator('#article-container').innerText();
fs.writeFileSync(path.join(out,'results.json'),JSON.stringify({errors,results,pureOK:pure.includes('edge-check-001')&&!pure.includes('{%')},null,2));
console.log(JSON.stringify({errors,checks:results.length,failures:results.filter(r=>r.width>r.viewport||r.visible!==1||r.rawTags||!r.arrows||r.codes.some(c=>c.frame!==c.code)),pureOK:pure.includes('edge-check-001')}));
await browser.close();server.close();
})().catch(e=>{console.error(e);process.exit(1)});
