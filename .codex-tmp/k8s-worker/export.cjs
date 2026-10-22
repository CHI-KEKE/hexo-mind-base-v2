const {chromium}=require('../compression-review/node_modules/playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve('public'),out=path.resolve('.codex-tmp/k8s-worker');
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
await page.goto('http://127.0.0.1:4183/Mind/2026/09/19/K8S-worker-pod-cpu-memory/',{waitUntil:'networkidle'});
await page.waitForSelector('.kh-diagram svg',{state:'attached'});
await page.waitForFunction(()=>document.querySelectorAll('.kh-diagram svg').length===5);

const diagrams=await page.evaluate(async()=>{
const result=[];
for(const [i,el] of [...document.querySelectorAll('.kh-diagram .mermaid-src')].entries()){
const config=JSON.parse(el.dataset.config);config.htmlLabels=false;config.flowchart.htmlLabels=false;
const source=el.textContent;
const rendered=await mermaid.render('export-kh-'+i,'%%{init: '+JSON.stringify(config)+'}%%\n'+source);
result.push({svg:rendered.svg,source});
}
return result;
});
fs.writeFileSync(path.join(out,'diagram-exports.json'),JSON.stringify(diagrams,null,2));
console.log('Exported',diagrams.length,'SVG diagrams');
await browser.close();server.close();
})().catch(e=>{console.error(e);server.close();process.exit(1)});
