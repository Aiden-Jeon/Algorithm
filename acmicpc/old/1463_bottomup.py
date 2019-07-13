import sys
q = sys.stdin.readline().strip()

d = [None] * (int(q)+1)
d[1] = 0
for i in range(2,(int(q)+1)):
	d[i] = d[i-1]+1
	if i%2 == 0:
		if d[i] > d[int(i/2)] + 1:
			d[i] = d[int(i/2)] + 1
	if i%3 == 0:
		if d[i] > d[int(i/3)] + 1:
			d[i] = d[int(i/3)] + 1
print(d[int(q)])
