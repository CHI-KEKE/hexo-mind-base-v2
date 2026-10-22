const {chromium}=require('./compression-review/node_modules/playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const captureStyle='#nav,#rightside{visibility:hidden!important;}';
const base=process.env.VERIFY_BASE||'http://127.0.0.1:4179';
const root=path.resolve('public'),out=path.resolve(process.env.VERIFY_OUT||'.codex-tmp/taiwan-id');
fs.mkdirSync(out,{recursive:true});
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.woff2':'font/woff2'};
const server=http.createServer((req,res)=>{
let file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\/Mind\//,'/'));
if(!file.startsWith(root+path.sep)){res.writeHead(403);return res.end();}
if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');
if(!fs.existsSync(file)){res.writeHead(404);return res.end();}
res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');fs.createReadStream(file).pipe(res);
});
(async()=>{
await new Promise(r=>server.listen(4179,'127.0.0.1',r));
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage({viewport:{width:1500,height:1000}});const errors=[],results=[];
page.on('pageerror',e=>errors.push(e.message));
await page.goto(base+'/Mind/2026/09/17/Encode-taiwan-id/',{waitUntil:'networkidle'});
await page.waitForSelector('.bc-mindmap',{state:'attached'});
await page.waitForSelector('.bc-mermaid svg',{state:'attached',timeout:30000});
console.log('diagrams loaded');
const tabs=page.locator('.tabs > .nav-tabs > .tab');
if(await tabs.count()!==6)throw Error('Expected six tabs');
for(const mode of ['desktop','mobile','dark']){
await page.setViewportSize(mode==='mobile'?{width:390,height:844}:{width:1500,height:1000});
if(mode==='dark'){
await page.evaluate(()=>scrollTo(0,1000));await page.waitForTimeout(400);
if(!await page.locator('#rightside-config-hide').evaluate(e=>e.classList.contains('show')))await page.locator('#rightside-config').click();
await page.locator('#darkmode').click();await page.waitForFunction(()=>document.documentElement.dataset.theme==='dark');
await page.waitForTimeout(800);await page.waitForSelector('.bc-mermaid svg',{state:'attached'});
}
for(let i=0;i<6;i++){
await tabs.nth(i).click();await page.waitForTimeout(180);
const panel=page.locator('.tabs > .tab-contents > .tab-item-content.active');
await panel.screenshot({style:captureStyle,path:path.join(out,`${mode}-tab-${i+1}.png`)});
const detail=panel.locator('details');
if(await detail.count()){
await detail.locator('summary').click();await detail.screenshot({style:captureStyle,path:path.join(out,`${mode}-case-details.png`)});await detail.locator('summary').click();
}
const blocks=panel.locator('.bc-code');
for(let j=0;j<await blocks.count();j++)await blocks.nth(j).screenshot({style:captureStyle,path:path.join(out,`${mode}-tab-${i+1}-code-${j+1}.png`)});
if(i===5){
await panel.locator('.bc-map-scroll').screenshot({style:captureStyle,path:path.join(out,`${mode}-mindmap.png`)});
if(mode==='mobile'){
await panel.locator('.bc-map-scroll').evaluate(e=>e.scrollLeft=(e.scrollWidth-e.clientWidth)/2);await panel.locator('.bc-map-scroll').screenshot({style:captureStyle,path:path.join(out,'mobile-mindmap-center.png')});
await panel.locator('.bc-map-scroll').evaluate(e=>e.scrollLeft=e.scrollWidth);await panel.locator('.bc-map-scroll').screenshot({style:captureStyle,path:path.join(out,'mobile-mindmap-right.png')});
}
await panel.locator('.bc-mermaid').screenshot({style:captureStyle,path:path.join(out,`${mode}-flow.png`)});
}
const info=await panel.evaluate(el=>({mode:document.documentElement.dataset.theme,visiblePanels:document.querySelectorAll('.tabs > .tab-contents > .active').length,width:document.documentElement.scrollWidth,viewport:innerWidth,svg:el.querySelectorAll('svg').length,rawTags:/\{%|&lt;div|<span class=/.test(el.innerText),syntaxError:/Syntax error|Lexical error/.test(el.innerText),codeBackgrounds:[...el.querySelectorAll('.bc-code')].map(e=>({frame:getComputedStyle(e).backgroundColor,code:getComputedStyle(e.querySelector('pre')).backgroundColor})),arrows:[...el.querySelectorAll('.bc-mermaid [marker-end]')].every(e=>{const m=e.getAttribute('marker-end').match(/#([^)'\"]+)/);return m&&document.getElementById(m[1]);})}));
results.push({view:mode,tab:i+1,...info});
}
console.log(mode,'six tabs checked');
}
await page.goto(base+'/Mind/2026/09/17/Encode-taiwan-id-pure/',{waitUntil:'networkidle'});
const pureText=await page.locator('#article-container').innerText();
if(pureText.includes('{%')||pureText.includes('<div class='))throw Error('Raw tags in pure version');
await page.locator('#article-container').screenshot({style:captureStyle,path:path.join(out,'pure.png')});
const findings={errors,results,pure:{hasCode:pureText.includes('IsValidTaiwanId'),hasMindmap:pureText.includes('程式腦：身分證驗證思考心智圖')}};
fs.writeFileSync(path.join(out,'results.json'),JSON.stringify(findings,null,2));
console.log(JSON.stringify(findings));
await browser.close();server.close();
if(errors.length||results.some(r=>r.width>r.viewport||r.visiblePanels!==1||r.rawTags||r.syntaxError||!r.arrows||r.codeBackgrounds.some(c=>c.frame!==c.code)))process.exitCode=1;
})().catch(e=>{console.error(e);server.close();process.exit(1)});
