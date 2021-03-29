import sys 
q = lambda: sys.stdin.readline().split(',')
land = []
for _ in range(3):
	land.append(list(map(int,q())))

for i in range(1,len(land)):
	for j in range(4):
		temp = list(map(lambda x: x + land[i][j],land[i-1]))
		temp[j] = 0
		land[i][j] = max(temp)
print(max(land[-1]))
