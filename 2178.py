import sys
import re
m,n = list(map(int,sys.stdin.readline().strip().split()))
mat = {}
for i in range(m):
	tmp = sys.stdin.readline().strip()
	tmp = re.sub('1','1 ',tmp)
	tmp = re.sub('0','0 ',tmp)
	tmp = list(map(int,tmp.strip().split()))
	mat[i] = tmp

queue = [([0,0],[[0,0]])]
result = []
i_move = [1,0,-1,0]
j_move = [0,1,0,-1]

while queue:
	wh,path = queue.pop(0)
	if wh == [m-1,n-1]:
		result.append(path)
	else:
		for z in range(4):
			tmp_path = path.copy()
			ni = wh[0] + i_move[z]
			nj = wh[1] + j_move[z]
			if ni >=0 and ni<m and nj>=0 and nj<n and [ni,nj] not in path and mat[ni][nj] == 1:
				tmp_path.append([ni,nj])
				mat[ni][nj] = 0
				queue.append(([ni,nj],tmp_path))

l = []
for i in range(len(result)):
	l.append(len(result[i]))
print(min(l))