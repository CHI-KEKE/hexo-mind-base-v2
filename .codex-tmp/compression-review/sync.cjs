const fs = require('fs');
const file = 'source/_posts/CS/compression.md';
let text = fs.readFileSync(file, 'utf8').replace('僅凭', '僅憑').replace('資料比较', '資料比較');
fs.writeFileSync(file, text);
const pure = text.replace(/<style>[\s\S]*?<\/style>/g, '').replace(/<div class="compression-wide-diagram">|<\/div>/g, '').replace(/{% tabs .*?%}\s*/g, '').replace(/<!-- tab (.*?)-->/g, '## $1').replace(/<!-- endtab -->/g, '').replace(/{% endtabs %}/g, '').replace(/{% mermaid %}/g, '```mermaid').replace(/{% endmermaid %}/g, '```').replace(/\n{3,}/g, '\n\n');
fs.writeFileSync('source/_posts/CS/compression-pure.md', pure);
console.log(JSON.stringify({tabs:(text.match(/<!-- tab /g)||[]).length,diagrams:(text.match(/{% mermaid %}/g)||[]).length,pureWritten:true}));
