##시간초과##
import sys
import collections

n,m = list(map(int,sys.stdin.readline().split()))

mat = [[] for _ in range(n+1)]
for _ in range(m):
	a,b = list(map(int,sys.stdin.readline().split()))
	mat[b].append(a)


hack = []
for i in range(1,n+1):
	queue = collections.deque(mat[i])
	visited = [i]
	cnt = 1
	while queue:
		std = queue.popleft()
		cnt += 1
		for s in mat[std]:
			if s not in visited:
				queue.append(s)
				visited.append(s)
	hack.append([cnt,i])

hack.sort(reverse=True)
num, com = hack.pop(0)
ans = [str(com)]

for h in hack:
	if h[0] == num:
		ans.append(str(h[1]))
ans.sort()
print(' '.join(ans))