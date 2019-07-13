import sys
import queue

n,m = list(map(int,input().split()))
q = queue.Queue()
ans = []
for i in range(1,n+1):
	q.put(i)

while len(ans)!=n:
	cnt = 1
	while cnt!=m:
		cnt+=1
		q.put(q.get())
	ans.append(q.get())

print('<'+', '.join(list(map(str,ans)))+'>')