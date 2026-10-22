const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve('public'),out=path.resolve('.codex-tmp/grafana-1');
const server=http.createServer((req,res)=>{
let f=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\/Mind\//,'/'));
if(!f.startsWith(root+path.sep)){res.writeHead(403);return res.end();}
if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
if(!fs.existsSync(f)){res.writeHead(404);return res.end();}
res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);
});
server.listen(4188,'127.0.0.1',()=>console.log('Preview: http://127.0.0.1:4188/Mind/2026/09/22/Metrix-grafana-1/'));
