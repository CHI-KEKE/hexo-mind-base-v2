const {chromium}=require('../compression-review/node_modules/playwright');
const fs=require('fs'),path=require('path');
(async()=>{
const base=__dirname,b=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const p=await b.newPage({viewport:{width:1500,height:1000}});
for(const mode of ['desktop','mobile','dark','mobile-dark']){
const files=fs.readdirSync(base).filter(f=>f.startsWith(mode+'-code-'));
const content=files.map(f=>`<figure><figcaption>${f}</figcaption><img src="data:image/png;base64,${fs.readFileSync(path.join(base,f)).toString('base64')}"></figure>`).join('');
await p.setContent(`<html><head><style>body{margin:18px;background:#ddd;font:14px sans-serif}main{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}figure{margin:0;overflow:hidden}img{max-width:100%;display:block}figcaption{margin:5px}</style></head><body><main>${content}</main></body></html>`);
await p.screenshot({path:path.join(base,mode+'-code-gallery.png'),fullPage:true});
}
await b.close();
})();
