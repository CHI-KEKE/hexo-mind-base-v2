from pathlib import Path
import re,html
root=Path('C:/Dev/Hexo-mind')
formal=root/'source/_posts/K8S/worker-pod-cpu-memory.md'
plain=root/'source/_posts/K8S/worker-pod-cpu-memory-pure.md'
s=formal.read_text(encoding='utf-8');p=plain.read_text(encoding='utf-8')
(root/'.codex-tmp/k8s-worker/before-tolerance.md').write_text(s,encoding='utf-8')
(root/'.codex-tmp/k8s-worker/before-tolerance-pure.md').write_text(p,encoding='utf-8')
title='目標 70%，為什麼到 71% 還不擴容？'
assert title not in s
parts=[];pure=[]
def text(t):
 t=re.sub(r'<a href="([^"]+)">(.*?)</a>',r'[\2](\1)',t)
 t=t.replace('<code>','`').replace('</code>','`').replace('<strong>','**').replace('</strong>','**')
 return html.unescape(re.sub(r'<[^>]*>','',t))
def paragraph(t):parts.append('<p>'+t+'</p>');pure.append(text(t))
def heading(t):parts.append('<h4>'+t+'</h4>');pure.append('#### '+t)
def note(t):parts.append('<div class="kh-note info"><p>'+t+'</p></div>');pure.append('> '+text(t))
def table(headers,rows):
 parts.append('<div class="kh-table-scroll" role="region" aria-label="HPA 容忍範圍模擬" tabindex="0"><table class="kh-table"><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>')
 pure.append('\n'.join(['| '+' | '.join(map(text,headers))+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(text,row))+' |' for row in rows]))
parts.append('<h3 class="kh-section">'+title+'</h3>');pure.append('### '+title)
paragraph('70% 是希望維持的平均負載。實際用量會上下浮動，HPA 允許它在目標附近小幅變動，避免為了短暫升高一點點，就啟動額外的 Pod。這段緩衝範圍由 <code>tolerance</code> 決定，預設值是 <code>0.1</code>，也就是相對目標值的 10%。實際環境可能另有設定。')
paragraph('以目標 70% 計算，下界是 <code>70% × 0.9 = 63%</code>，上界是 <code>70% × 1.1 = 77%</code>。也就是約 63%～77% 的範圍，並非將 70% 直接加減 10 個百分點得到 60%～80%。在這個範圍內，HPA 不會因該指標的小幅偏差而改變副本數。')
heading('先看一個容易被向上取整放大的變化')
paragraph('假設目前有 2 個 Pod，平均利用率從 70% 變成 71%。若只使用簡化公式，會得到 <code>ceil(2 × 71 / 70) = ceil(2.0286) = 3</code>。利用率只增加 1 個百分點，副本建議卻從 2 個變成 3 個，數量增加了 50%。')
paragraph('加入容忍範圍後，<code>71 / 70 ≈ 1.0143</code>，相對目標只偏高約 1.43%，仍小於 10%。HPA 便維持 2 個 Pod，讓小幅波動留在緩衝範圍內。只有偏差夠大時，才繼續評估是否需要調整。')
heading('模擬：負載逐步升高，再慢慢下降')
paragraph('以下以 Memory 目標 70%、容忍值 10%、副本上下限 2～4 為例。假設各 Pod 的 request 相同、都已就緒且指標完整，CPU 沒有提出更大的副本建議。每列是後續取得的一次假設量測，不代表固定秒數，也不是正式環境的監控紀錄。')
table(['觀察順序','目前 Pod／平均利用率','判斷與結果'],[
 ['第 1 次','2 個／70%','正好在目標，維持 2 個。'],
 ['第 2 次','2 個／71%','落在容忍範圍內，維持 2 個；不因向上取整而增加到 3 個。'],
 ['第 3 次','2 個／76%','<code>76 / 70 ≈ 1.086</code>，仍在容忍範圍內，維持 2 個。'],
 ['第 4 次','2 個／80%','<code>80 / 70 ≈ 1.143</code>，超出容忍範圍。<code>ceil(2 × 80 / 70) = 3</code>，其他條件允許時可擴到 3 個。'],
 ['第 5 次','3 個／55%','假設新增 Pod 已就緒後，後續量測降到 55%。雖低於 63%，但 <code>ceil(3 × 55 / 70) = 3</code>，副本建議仍是 3 個。'],
 ['第 6 次','3 個／40%','<code>ceil(3 × 40 / 70) = 2</code>，得到 2 個的縮容建議；還須檢查穩定視窗與縮容政策，未必立即減少。']
])
paragraph('第 5 次的 55% 是假設觀察到的數值，不是新增一個 Pod 後一定會出現的結果。尤其 Memory 可能包含快取、常駐資料與正在處理的任務，新增 Pod 不會自動搬走舊 Pod 已使用的記憶體；必須以後續量測確認負載是否真的下降。')
heading('換成本文的記憶體設定，看得更具體')
paragraph('每個 Container 的 Memory request 是 <code>2000Mi</code>，因此 70% 目標對應平均 <code>1400Mi</code>，容忍範圍約為平均 <code>1260Mi～1540Mi</code>。平均用到 <code>1500Mi</code> 時是 75%，仍在範圍內；平均用到 <code>1600Mi</code> 時是 80%，才會超出範圍並進一步評估擴容。這些數字都是 HPA 的平均指標，不能拿來當成單一 Container 的安全上限。')
note('<strong>容忍值看偏差大小，穩定視窗看一段時間內的建議。</strong> 即使利用率已超出容忍範圍，副本取整也可能讓數量不變。若已得到較少副本的建議，預設縮容穩定視窗還會參考最近 5 分鐘內較高的建議，避免短暫下降就急著縮容；這不等於每次固定等待 5 分鐘後必定縮容。')
paragraph('容忍範圍與演算法依據見 <a href="https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#algorithm-details">Kubernetes HPA 演算法說明</a>。')
marker='<h3 class="kh-section">從多個指標得到一個副本建議</h3>'
assert s.count(marker)==1
s=s.replace(marker,'\n\n'.join(parts)+'\n\n'+marker,1)
pm='### 從多個指標得到一個副本建議'
assert p.count(pm)==1
p=p.replace(pm,'\n\n'.join(pure)+'\n\n'+pm,1)
# Synchronize the user's existing prose removals without restoring them.
old=(root/'.codex-tmp/k8s-worker/before-svg-fix.md').read_text(encoding='utf-8')
oldparagraphs=re.findall(r'<p>(.*?)</p>',old,re.S)
currentparagraphs=set(re.findall(r'<p>(.*?)</p>',s,re.S))
removed=[]
for para in oldparagraphs:
 if para in currentparagraphs:continue
 md=text(para)
 if md in p:
  replacement=''
  if para.startswith('本例假設 HPA 使用資源利用率指標。'):
   replacement=text(para.removeprefix('本例假設 HPA 使用資源利用率指標。'))
  if '> '+md in p:p=p.replace('> '+md,replacement,1)
  else:p=p.replace(md,replacement,1)
  removed.append(md[:30])
p=re.sub(r'\n{3,}','\n\n',p)
formal.write_text(s,encoding='utf-8');plain.write_text(p,encoding='utf-8')
print('Inserted tolerance section; synchronized existing paragraph edits:',len(removed))
