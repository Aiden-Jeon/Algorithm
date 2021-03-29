import sys
import re
n = int(sys.stdin.readline())

mat = []
for i in range(n):
	tmp = sys.stdin.readline().strip()
	tmp = re.sub('0','0 ',tmp)
	tmp = re.sub('1','1 ',tmp)
	mat.append(list(map(int,tmp.split(' ')[:-1])))

queue = []
i_move = [1,0,-1,0]
j_move = [0,1,0,-1]

danji = 0
l = []
for a in range(n):
	for b in range(n):
		if mat[a][b]!=0:
			queue = [[a,b]]
			visited = []
			while queue:
				i,j = queue.pop(0)
				for m in range(4):
					ni = i + i_move[m]
					nj = j + j_move[m]
					if ni>=0 and ni<=n-1 and nj>=0 and nj<=n-1 and mat[ni][nj]==1 and [ni,nj] not in visited:
						queue.append([ni,nj])
				if [i,j] not in visited:
					visited.append([i,j])
				mat[i][j] = 0
			danji+=1
			l.append(len(visited))

print(danji)
l = sorted(l)
for i in range(len(l)):
	print(l[i])