import sys
n,m = list(map(int,sys.stdin.readline().split()))

inf = float('inf')
dist = [[] for _ in range(n)]
for i in range(n):
	for j in range(n):
		if i!=j:
			dist[i].append(inf)
		else:
			dist[i].append(0)

for _ in range(m):
	a,b = list(map(int,sys.stdin.readline().split()))
	dist[a-1][b-1] = 1
	dist[b-1][a-1] = 1


for k in range(n):
	for i in range(n):
		for j in range(n):
			dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ans = list(map(sum,dist))
print(ans.index(min(ans))+1)
