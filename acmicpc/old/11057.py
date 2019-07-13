import sys
q = int(sys.stdin.readline().strip())
a = [1]*10
for i in range(q-1):
	tmp = [0]*10
	for j in range(10):
		tmp[j] = sum(a[j:])
	a = tmp.copy()

print(sum(a)%10007)
