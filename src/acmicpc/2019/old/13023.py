import sys
q = lambda: sys.stdin.readline().strip()
m,n = q().split(' ')

g = []
for _ in range(int(n)):
	r = list(map(int,q().split(' ')))
	g.append(r)

result = 0
for j in range(int(n)):
	for i in range(j+1,int(n)):
		if g[i][0] not in g[j] and g[i][1] not in g[j]:
			for z in range(j+1,i):
				a1 = g[z][0] in g[i] or g[z][1] in g[i]
				a2 = g[z][0] in g[j] or g[z][1] in g[j]
				if a1 and a2:
					result = 1
print(result)

