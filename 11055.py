import sys
a = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip().split(' ')
b = list(map(int,b))
c = [None]* a
for i in range(a):
	c[i] = b[i]	
	for j in range(i):
		if b[j] < b[i] and c[i] < c[j] + b[i]:
			c[i] = c[j] + b[i]
print(max(c))

