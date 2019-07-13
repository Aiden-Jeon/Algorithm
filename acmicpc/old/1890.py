import sys
q = lambda: sys.stdin.readline().strip().split(' ')
N = int(q()[0])
mat = []
w_mat = []
for i in range(N):
	tmp = list(map(int,q()))
	mat.append(tmp)
	w_mat.append(list(map(lambda x:0*x,tmp)))
w_mat[0][0]=1

for i in range(N):
	for j in range(N):
		if w_mat[i][j] != 0 and mat[i][j] >0:
			if i + mat[i][j] <N:
				w_mat[i+mat[i][j]][j] += w_mat[i][j]
			if j + mat[i][j] <N:
				w_mat[i][j+mat[i][j]] += w_mat[i][j]
print(w_mat[-1][-1]) 