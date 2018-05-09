import sys
j_n = int(sys.stdin.readline().strip())
obj = list(map(int,sys.stdin.readline().strip().split(' ')))
n = int(sys.stdin.readline().strip())

fam = {}
for i in range(n):
	a,b = list(map(int,sys.stdin.readline().strip().split(' ')))
	if a in list(fam.keys()):
		fam[a] = set(list(fam[a])+[b])
	else:
		fam[a] = set([b])
	if b in list(fam.keys()):
		fam[b] = set(list(fam[b])+[a])
	else:
		fam[b] = set([a])

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []
    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path + [m]))
    return result

path = dfs_paths(fam,obj[0],obj[1]) 
l = []
if len(path) > 0:
	for i in range(len(path)):
		l.append(len(path[i]))
	print(min(l)-1)
else:
	print(-1)