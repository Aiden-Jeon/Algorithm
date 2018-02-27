import sys
a = int(sys.stdin.readline().strip())
b1 = sys.stdin.readline().strip().split(' ')
b1 = list(map(int,b1))
c1 = [None]* a
c2 = [None]* a
for i in range(a):
	c1[i] = 1
	for j in range(i):
		if b1[j] < b1[i] and c1[i] < c1[j]+1:
			c1[i] = c1[j] +1
for i in reversed(range(a)):
	c2[i] = 1
	for j in reversed(range(i,a)):
		if b1[j] < b1[i] and c2[i] < c2[j]+1:
			c2[i] = c2[j] +1

d = list(map(lambda x,y:x+y-1,c1,c2))
print(max(d))