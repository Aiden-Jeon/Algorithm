import sys
q = sys.stdin.readline().strip()

d = [None]* (int(q)+1)
d[1:3] = [1,2]
for n in range(3,int(q)+1):
	d[n] = (d[n-1] + d[n-2])%10007
print(d[int(q)])
		