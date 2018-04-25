import sys 
q = lambda: sys.stdin.readline().strip().split(' ')
m,n = list(map(int,q()))
tmp_mat = [[0]*(n+1)]
for i in range(m):
	tmp = [0]+list(map(int,q()))
	tmp_mat.append(tmp)

for i in range(1,m+1):
	for j in range(1,n+1):
		tmp_mat[i][j] += max(tmp_mat[i][j-1],tmp_mat[i-1][j],tmp_mat[i-1][j-1])
print(tmp_mat[m][n])