import sys 
q = lambda: sys.stdin.readline().strip().split(' ')
m,n = list(map(int,q()))
tmp_mat = []
for i in range(m):
	tmp = list(map(int,q()))
	tmp_mat.append(tmp)

def right(mat,row,col):
	return mat[row][col] + mat[row][col-1]
def down(mat,row,col):
	return mat[row][col] + mat[row-1][col]
def diag(mat,row,col):
	return mat[row][col] + mat[row-1][col-1]

for i in range(0,m):
	for j in range(0,n):
		if i == 0:
			if j!=0:
				tmp_mat[i][j] = right(tmp_mat,i,j)
		else:
			if j == 0 :
				tmp_mat[i][j] = down(tmp_mat,i,j)
			else:
				tmp_mat[i][j] = max([right(tmp_mat,i,j),down(tmp_mat,i,j),diag(tmp_mat,i,j)])
print(tmp_mat[m-1][n-1])