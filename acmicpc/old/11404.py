import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

inf = float('inf')
dist = [[] for _ in range(n)]
for i in range(n):
	for j in range(n):
		if i!=j:
			dist[i].append(inf)
		else:
			dist[i].append(0)

for _ in range(m):
	a,b,k = list(map(int,sys.stdin.readline().split()))
	dist[a-1][b-1] = min(dist[a-1][b-1],k)
	
for k in range(n):
	for i in range(n):
		for j in range(n):
			dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for i in range(n):
	for j in range(n):
		if dist[i][j] == inf:
			dist[i][j] = 0
for d in dist:
	print(' '.join(list(map(str,d))))
