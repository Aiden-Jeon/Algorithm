#시간초과 
import sys
n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
tree = [0] * (n+1)
queue = []
for _ in range(n-1):
	x,y = list(map(int,sys.stdin.readline().split()))
	graph[x].append(y)
	graph[y].append(x)
	if x == 1:
		queue.append((y,[x,y]))
		tree[y] = x
	if y == 1:
		queue.append((x,[y,x]))
		tree[x] = y


while queue:
	t,path = queue.pop(0)
	for s in graph[t]:
		if s not in path:
			queue.append((s,path+[s]))
			tree[s] = t

tree = list(map(str,tree))
print('\n'.join(tree[2:]))


