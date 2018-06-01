import sys
import queue

m,n = list(map(int,sys.stdin.readline().split()))
mat = {}
queue = []
for i in range(n):
	mat[i] = list(map(int,sys.stdin.readline().split()))
	for j in range(m):
		if mat[i][j] == 1:
			queue.append((i,j))

for i,j in queue:
	if i>0 and not mat[i-1][j]:
		mat[i-1][j] = mat[i][j]+1
		queue.append((i-1,j))
	if i + 1 < n and not mat[i + 1][j]:
		mat[i + 1][j] = mat[i][j] + 1
		queue.append((i + 1, j))
	if j > 0 and not mat[i][j - 1]:
		mat[i][j - 1] = mat[i][j] + 1
		queue.append((i, j - 1))
	if j + 1 < m and not mat[i][j + 1]:
		mat[i][j + 1] = mat[i][j] + 1
		queue.append((i, j + 1))

if sum(map(lambda x: x.count(0),mat.values())):
	print(-1)
else:
	print(max(map(max,mat.values()))-1)
	