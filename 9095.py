import sys
q = lambda: int(sys.stdin.readline().strip())
n = []
for _ in range(q()):
	n.append(q())
n_s = list(reversed(sorted(n)))

n_list = [0] * (n_s[0]+1)
for i in range(1,n_s[0]+1):
	if i in [1,2,3]:
		n_list[i] = 2**(i-1)	
	else:
		for j in [1,2,3]:
			n_list[i] += n_list[i-j]
for i in n:
	print(n_list[i])
