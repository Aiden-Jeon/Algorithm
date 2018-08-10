import sys
import copy

m,n = list(map(int,sys.stdin.readline().strip().split()))
mat = {}
for i in range(m):
	tmp = list(map(int,sys.stdin.readline().strip().split()))
	mat[i] = tmp

i_move = [1,0,-1,0]
j_move = [0,1,0,-1]

def Virus(t_mat):
	queue = []
	visited = []
	for i in range(m):
		for j in range(n):
			if t_mat[i][j] == 2:
				queue.append([i,j])
	while queue:
		a,b = queue.pop(0)
		for z in range(4):
			ni = a + i_move[z]
			nj = b + j_move[z]
			if ni >= 0 and nj >=0 and ni<m and nj<n and t_mat[ni][nj]==0 and [ni,nj] not in visited:
				queue.append([ni,nj])
				t_mat[ni][nj] = 2
				visited.append([ni,nj])	

	cnt = 0
	for c in range(len(t_mat)):
		cnt += t_mat[c].count(0)
	return cnt

arr = []
for i in range(m):
	for j in range(n):
		if mat[i][j] == 0:
			arr.append([i,j])

v_max = 0
for a in range(len(arr)):
	for b in range(a,len(arr)):
		if a == b: continue
		for c in range(b,len(arr)):
			if b == c or a == c: continue
			t_mat = copy.deepcopy(mat)
			t_mat[arr[a][0]][arr[a][1]] = 1
			t_mat[arr[b][0]][arr[b][1]] = 1
			t_mat[arr[c][0]][arr[c][1]] = 1
			v = Virus(t_mat)
			if v > v_max :
				v_max = v
print(v_max)
