import sys
q = lambda: sys.stdin.readline().strip().split(' ')
M,N = list(map(int,q()))
mat = []
w_mat = []
for i in range(M):
	tmp = list(map(int,q()))
	mat.append(tmp)
	w_mat.append(list(map(lambda x:0*x,tmp)))
w_mat[0][0]=1

print(mat,w_mat)
for i in range(M):
	for j in range(N):
		if i+1<M:
			if mat[i][j] > mat[i+1][j]:
				w_mat[i+1][j] += w_mat[i][j]
		if i-1>0:
			if mat[i-1][j] > mat[i][j]:
				w_mat[i][j] += w_mat[i-1][j]
		if j+1<N:
			if mat[i][j] > mat[i][j+1]:
				w_mat[i][j+1] += w_mat[i][j]
		if j-1>0:
			if mat[i][j-1] > mat[i][j]:
				w_mat[i][j] += w_mat[i][j-1]
print(w_mat)