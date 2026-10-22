const {chromium}=require('../compression-review/node_modules/playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve('public'),out=path.resolve('.codex-tmp/grafana-1');
const server=http.createServer((req,res)=>{
let f=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\/Mind\//,'/'));
if(!f.startsWith(root+path.sep)){res.writeHead(403);return res.end();}
if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
if(!fs.existsSync(f)){res.writeHead(404);return res.end();}
res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);
});
(async()=>{
await new Promise(r=>server.listen(4187,'127.0.0.1',r));
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage({viewport:{width:1440,height:1000}});const errors=[],results=[];
page.on('pageerror',e=>errors.push(e.message));
await page.goto('http://127.0.0.1:4187/Mind/2026/09/22/Metrix-grafana-1/',{waitUntil:'networkidle'});
await page.waitForFunction(()=>document.querySelectorAll('.gd-diagram svg').length===7,{},{timeout:60000});

const svgs=await page.locator('.gd-diagram svg').evaluateAll(es=>es.map(e=>e.outerHTML));
const assets=path.resolve('source/images/grafana-1');fs.mkdirSync(assets,{recursive:true});
for(const [i,name] of [[4,'loki-query'],[5,'memory-panel']]){
let svg=svgs[i];
// External SVG documents isolate marker IDs from other tabs.
if(!svg.includes('xmlns='))svg=svg.replace('<svg','<svg xmlns="http://www.w3.org/2000/svg"');
fs.writeFileSync(path.join(assets,name+'.svg'),svg);
}
console.log('Exported two sequence SVGs');await browser.close();server.close();
})().catch(e=>{console.error(e);server.close();process.exit(1)});
