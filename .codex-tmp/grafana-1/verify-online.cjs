const {chromium}=require('../compression-review/node_modules/playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve('public'),out=path.resolve('.codex-tmp/grafana-1/online');fs.mkdirSync(out,{recursive:true});
const server=http.createServer((req,res)=>{
let f=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\/Mind\//,'/'));
if(!f.startsWith(root+path.sep)){res.writeHead(403);return res.end();}
if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
if(!fs.existsSync(f)){res.writeHead(404);return res.end();}
res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);
});
(async()=>{

const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage({viewport:{width:1440,height:1000}});const errors=[],results=[];
page.on('pageerror',e=>errors.push(e.message));
await page.goto('https://chi-keke.github.io/Mind/2026/09/22/Metrix-grafana-1/',{waitUntil:'networkidle'});
await page.waitForFunction(()=>document.querySelectorAll('.gd-diagram svg').length===5 && [...document.querySelectorAll('.gd-sequence')].filter(e=>e.complete&&e.naturalWidth>0).length===2,{},{timeout:60000});
const tabs=page.locator('.tabs > .nav-tabs > .tab');
if(await tabs.count()!==5)throw Error('Expected five tabs');
const captureStyle='#nav,#rightside{visibility:hidden!important}';
for(const mode of ['desktop','mobile','dark','mobile-dark']){
await page.setViewportSize(mode.includes('mobile')?{width:390,height:844}:{width:1440,height:1000});
if(mode==='dark'){
await page.evaluate(()=>scrollTo(0,1000));await page.waitForTimeout(400);
if(!await page.locator('#rightside-config-hide').evaluate(e=>e.classList.contains('show')))await page.locator('#rightside-config').click();
await page.locator('#darkmode').click();await page.waitForFunction(()=>document.documentElement.dataset.theme==='dark');
await page.waitForFunction(()=>document.querySelectorAll('.gd-diagram svg').length===5 && [...document.querySelectorAll('.gd-sequence')].filter(e=>e.complete&&e.naturalWidth>0).length===2);
}
for(let i=0;i<5;i++){
await tabs.nth(i).click(); await page.waitForTimeout(200); console.log('Tab',mode,i+1,await page.locator('.tab-contents').evaluate(e=>[...e.children].map(x=>x.tagName+':'+x.className)));
if(await page.locator('.tabs > .tab-contents > .tab-item-content.active').count()!==1){fs.writeFileSync(path.join(out,'failed-dom.html'),await page.content());throw Error('Missing active panel');}
const panel=page.locator('.tabs > .tab-contents > .tab-item-content.active');
await panel.screenshot({path:path.join(out,`${mode}-tab-${i+1}.png`),style:captureStyle});
const blocks=panel.locator('.gd-code');
for(let j=0;j<await blocks.count();j++)await blocks.nth(j).screenshot({path:path.join(out,`${mode}-code-${i+1}-${j}.png`),style:captureStyle});
const diagrams=panel.locator('.gd-diagram,.gd-plot');
for(let j=0;j<await diagrams.count();j++){
await diagrams.nth(j).screenshot({path:path.join(out,`${mode}-diagram-${i+1}-${j}.png`),style:captureStyle});
if(mode.includes('mobile')){
await diagrams.nth(j).evaluate(e=>e.scrollLeft=e.scrollWidth);
await diagrams.nth(j).screenshot({path:path.join(out,`${mode}-diagram-${i+1}-${j}-right.png`),style:captureStyle});
await diagrams.nth(j).evaluate(e=>e.scrollLeft=0);
}
}
results.push({mode,tab:i+1,...await panel.evaluate(el=>({visiblePanels:document.querySelectorAll('.tabs .tab-item-content.active').length,width:document.documentElement.scrollWidth,viewport:innerWidth,svg:el.querySelectorAll('.gd-diagram svg,.gd-sequence').length,raw:/\{%|<div class=|Syntax error|Lexical error/.test(el.innerText),code:[...el.querySelectorAll('.gd-code')].map(e=>({frame:getComputedStyle(e).backgroundColor,pre:getComputedStyle(e.querySelector('pre')).backgroundColor})),arrows:[...el.querySelectorAll('.gd-diagram [marker-end]')].every(e=>{const m=e.getAttribute('marker-end').match(/#([^)'\"]+)/);return m&&e.closest('svg').querySelector('[id="'+m[1]+'"]');}),diagrams:[...el.querySelectorAll('.gd-diagram svg')].map(e=>({width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height,viewBox:e.getAttribute('viewBox')}))}))});
}
console.log(mode,'five tabs checked');
}
await page.goto('https://chi-keke.github.io/Mind/2026/09/22/Metrix-grafana-1-pure/',{waitUntil:'networkidle'});
const pure=await page.locator('#article-container').innerText();
const findings={errors,results,pure:{noTags:!(/\{%|<div class=/.test(pure)),hasMetric:pure.includes('http_requests_total'),hasError:pure.includes('OutOfMemoryException'),hasAlert:pure.includes('Dify Error')}};
fs.writeFileSync(path.join(out,'results.json'),JSON.stringify(findings,null,2));console.log(JSON.stringify(findings));
await browser.close();server.close();
if(errors.length||!findings.pure.noTags||results.some(r=>r.width>r.viewport||r.visiblePanels!==1||r.raw||!r.arrows||r.code.some(c=>c.frame!==c.pre)))process.exitCode=1;
})().catch(e=>{console.error(e);server.close();process.exit(1)});
