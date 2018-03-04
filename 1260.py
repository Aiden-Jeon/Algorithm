import sys
q = lambda: sys.stdin.readline().strip()
l = list(map(int,q().split(' ')))

adj = [[0] for i in range(l[0]+1)]
for i in range(l[1]):
	r1,r2 = list(map(int,q().split(' ')))
	for j in range(1,l[0]+1):
		if j == r1:
			adj[j].append(r2)
		if j == r2 and j!=r1:
			adj[j].append(r1)


##DFS
visit = []; stack = []
cur = l[2]
visit.append(cur)
stack.extend(sorted(adj[cur][1:],reverse=True))

while len(stack)>0:
	cur = stack[-1]
	visit.append(cur)
	stack = stack[:-1]
	for i in stack:
		if i in adj[cur]:
			stack.pop(stack.index(i))
	for i in sorted(adj[cur],reverse=True):
		if i not in visit and i not in stack and i !=0:
			stack.append(i)

##
visit2 = []; que = []
cur = l[2]
visit2.append(cur)
que.extend(adj[cur][1:])

while len(que)>0:
	cur = que[0]
	visit2.append(cur)
	que = que[1:]
	for i in adj[cur]:
		if i not in visit2 and i not in que and i !=0:
			que.append(i)
print (' '.join(map(str,visit)))
print (' '.join(map(str,visit2)))
