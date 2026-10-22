const fs=require('fs'),cheerio=require('cheerio');
const model=JSON.parse(fs.readFileSync('.codex-tmp/resource-adjust/content.json','utf8'));
const visual=cheerio.load(fs.readFileSync('public/2026/10/01/K8S-resource-adjust/index.html','utf8'));
const pure=cheerio.load(fs.readFileSync('public/2026/10/01/K8S-resource-adjust-pure/index.html','utf8'));
const norm=s=>s.replace(/\s/g,'').replace(/`/g,'');
const plain=s=>s.replace(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g,'$1');
const a=norm(visual('.kubernetes-helm').text()),b=norm(pure('#article-container').text()),missing=[];
for(const t of model)for(const block of t.blocks){const texts=block.kind==='table'?[...block.headers,...block.rows.flat()]:[block.title,block.kind==='diagram'?null:block.text,block.caption].filter(Boolean);for(const s of texts){const n=norm(plain(s));if(!a.includes(n)||!b.includes(n))missing.push({kind:block.kind,text:s,visual:a.includes(n),pure:b.includes(n)});}}
const report={missing,visualPanels:visual('.tabs > .tab-contents > .tab-item-content').length,diagramSources:visual('.kh-diagram .mermaid-src').length,hasMermaidRuntime:visual.html().includes('loadMermaid'),frontmatterSame:fs.readFileSync('source/_posts/K8S/resource-adjust.md','utf8').split('---')[1]===fs.readFileSync('source/_posts/K8S/resource-adjust-pure.md','utf8').split('---')[1]};
fs.writeFileSync('.codex-tmp/resource-adjust/content-check.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));if(missing.length)process.exitCode=1;
