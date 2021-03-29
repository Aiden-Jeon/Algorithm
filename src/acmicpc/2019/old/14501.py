import sys
q = lambda: sys.stdin.readline().strip()
n = int(q())

tp = [0] * 25
for i in range(n):
	t,p = list(map(int,q().split()))

	if tp[i] > tp[i+1]:
		tp[i+1] = tp[i]
	if tp[i+t] < tp[i] + p:
		tp[i+t] = tp[i] + p
	
print(tp[n])

