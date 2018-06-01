import sys
import copy
q = lambda: sys.stdin.readline().strip()
n = int(q())
mat = {}
for i in range(n):
	mat[i] = list(map(int,q().split()))

min_h = 0
max_h = max(map(max,mat.values()))
max_c = 0
for h in range(min_h,max_h):
	t_mat = copy.deepcopy(mat)
	for t in range(n):
		t_mat[t] = list(map(lambda x:0 if x<=h else x, t_mat[t]))
	cnt = 0
	for i in range(n):
		for j in range(n):
			if t_mat[i][j] != 0:
				queue = []
				cnt+=1
				t_mat[i][j] = cnt
				queue.append((i,j))
				for x,y in queue:
					if x > 0 and t_mat[x-1][y]!=0:
						t_mat[x-1][y] = 0
						queue.append((x-1,y))
					if x < n-1 and t_mat[x+1][y]!=0:
						t_mat[x+1][y] = 0
						queue.append((x+1,y))
					if y > 0 and t_mat[x][y-1]!=0:
						t_mat[x][y-1] = 0
						queue.append((x,y-1))
					if y < n-1 and t_mat[x][y+1]!=0:
						t_mat[x][y+1] = 0
						queue.append((x,y+1))
	max_c = max(cnt,max_c)
print(max_c)