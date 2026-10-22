from pathlib import Path
for name in ['verify.cjs','content-check.cjs','gallery.cjs']:
 s=(Path('.codex-tmp/cdn-header')/name).read_text(encoding='utf-8')
 s=s.replace('cdn-header','resource-adjust').replace('2026/09/28/K8S-CDN-Header-Lost','2026/10/01/K8S-resource-adjust').replace('CDN-Header-Lost','resource-adjust').replace('edge-check-001','readiness')
 if name=='verify.cjs':
  s=s.replace('!==6','!==7').replace('six tabs','seven tabs').replace('i<6','i<7')
  s=s.replace("console.log(JSON.stringify({errors,checks:","console.log(JSON.stringify({errors,checks:")
 if name=='gallery.cjs':
  s=s.replace("dir='.codex-tmp/resource-adjust/screens'","dir=process.env.VERIFY_OUT||'.codex-tmp/resource-adjust/screens'")
  s=s.replace("n.startsWith(mode+'-'+type+'-')","n.startsWith(mode+'-'+type+'-')&&!n.includes('gallery')")
 (Path('.codex-tmp/resource-adjust')/name).write_text(s,encoding='utf-8')
