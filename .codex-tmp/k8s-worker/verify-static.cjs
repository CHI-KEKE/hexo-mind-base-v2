const {chromium}=require('../compression-review/node_modules/playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve('public'),out=path.resolve(process.env.VERIFY_OUT||'.codex-tmp/k8s-worker/static');fs.mkdirSync(out,{recursive:true});const base=process.env.VERIFY_BASE||'http://127.0.0.1:4183';
const server=http.createServer((req,res)=>{
let f=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\/Mind\//,'/'));
if(!f.startsWith(root+path.sep)){res.writeHead(403);return res.end();}
if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
if(!fs.existsSync(f)){res.writeHead(404);return res.end();}
res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);
});
(async()=>{
await new Promise(r=>server.listen(4183,'127.0.0.1',r));
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage({viewport:{width:1440,height:1000}});const errors=[],results=[];
page.on('pageerror',e=>errors.push(e.message));
await page.goto(base+'/Mind/2026/09/19/K8S-worker-pod-cpu-memory/',{waitUntil:'networkidle'});
await page.waitForSelector('.kh-diagram-image',{state:'attached'});
await page.waitForFunction(()=>document.querySelectorAll('.kh-diagram-image').length===5&&[...document.querySelectorAll('.kh-diagram-image')].every(e=>e.complete&&e.naturalWidth>0));
const tabs=page.locator('.tabs > .nav-tabs > .tab');
if(await tabs.count()!==4)throw Error('Expected 4 tabs');
for(const mode of ['desktop','mobile','dark','mobile-dark']){
await page.setViewportSize(mode.includes('mobile')?{width:390,height:844}:{width:1440,height:1000});
if(mode==='dark'){
await page.evaluate(()=>scrollTo(0,1000));await page.waitForTimeout(400);
if(!await page.locator('#rightside-config-hide').evaluate(e=>e.classList.contains('show')))await page.locator('#rightside-config').click();
await page.locator('#darkmode').click();await page.waitForFunction(()=>document.documentElement.dataset.theme==='dark');
await page.waitForFunction(()=>document.querySelectorAll('.kh-diagram-image').length===5&&[...document.querySelectorAll('.kh-diagram-image')].every(e=>e.complete&&e.naturalWidth>0));
}
for(let i=0;i<4;i++){
await tabs.nth(i).click();
const panel=page.locator('.tabs > .tab-contents > .tab-item-content.active');
await panel.screenshot({path:path.join(out,`${mode}-tab-${i+1}.png`),style:'#nav,#rightside{visibility:hidden!important}'});
const blocks=panel.locator('.kh-code');
if(i===2&&await panel.getByRole('region',{name:'HPA 容忍範圍模擬',exact:true}).count())await panel.getByRole('region',{name:'HPA 容忍範圍模擬',exact:true}).screenshot({path:path.join(out,`${mode}-tolerance-table.png`),style:'#nav,#rightside{visibility:hidden!important}'});
for(let j=0;j<await blocks.count();j++)await blocks.nth(j).screenshot({path:path.join(out,`${mode}-code-${i+1}-${j}.png`),style:'#nav,#rightside{visibility:hidden!important}'});
const diagrams=panel.locator('.kh-diagram');
for(let j=0;j<await diagrams.count();j++){
await diagrams.nth(j).screenshot({path:path.join(out,`${mode}-diagram-${i+1}-${j}.png`),style:'#nav,#rightside{visibility:hidden!important}'});
if(mode.includes('mobile')){
await diagrams.nth(j).evaluate(e=>e.scrollLeft=e.scrollWidth);
await diagrams.nth(j).screenshot({path:path.join(out,`${mode}-diagram-${i+1}-${j}-right.png`),style:'#nav,#rightside{visibility:hidden!important}'});
await diagrams.nth(j).evaluate(e=>e.scrollLeft=0);
}
}
results.push({mode,tab:i+1,...await panel.evaluate(el=>({visiblePanels:document.querySelectorAll('.tab-item-content.active').length,width:document.documentElement.scrollWidth,viewport:innerWidth,svg:el.querySelectorAll('.kh-diagram-image').length,diagramsLoaded:[...el.querySelectorAll('.kh-diagram-image')].every(e=>e.complete&&e.naturalWidth>0),raw:/\{%|<div class=|Syntax error|Lexical error/.test(el.innerText),logo:[...el.querySelectorAll('img.kh-logo')].every(e=>e.complete&&e.naturalWidth>0),code:[...el.querySelectorAll('.kh-code')].map(e=>({frame:getComputedStyle(e).backgroundColor,pre:getComputedStyle(e.querySelector('pre')).backgroundColor})),arrows:[...el.querySelectorAll('.kh-diagram [marker-end]')].every(e=>{const m=e.getAttribute('marker-end').match(/#([^)'\"]+)/);return m&&document.getElementById(m[1]);})}))});
}
console.log(mode,'checked');
}
await page.goto(base+'/Mind/2026/09/19/K8S-worker-pod-cpu-memory-pure/',{waitUntil:'networkidle'});
const pure=await page.locator('#article-container').innerText();
const findings={errors,results,pure:{noTags:!(/\{%|<div class=/.test(pure)),hasFormula:pure.includes('desiredReplicas = ceil'),hasWorker:pure.includes('Max Processes')}};
fs.writeFileSync(path.join(out,'results.json'),JSON.stringify(findings,null,2));console.log(JSON.stringify(findings));
await browser.close();server.close();
if(errors.length||results.some(r=>r.width>r.viewport||r.visiblePanels!==1||r.raw||!r.logo||!r.diagramsLoaded||!r.arrows||r.code.some(c=>c.frame!==c.pre)))process.exitCode=1;
})().catch(e=>{console.error(e);server.close();process.exit(1)});
