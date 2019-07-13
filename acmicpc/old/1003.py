import sys
q = lambda: int(sys.stdin.readline().strip())
T = q()

for t in range(T):
	n = q()
	zero_a = 1; one_a = 0
	zero_b = 0; one_b = 1
	if n == 0:
		print(' '.join([str(zero_a),str(one_a)]))
	elif n == 1:
		print(' '.join([str(zero_b),str(one_b)]))
	else:
		for i in range(n-1):
			zero_c = zero_a + zero_b; one_c = one_a + one_b
			zero_a = zero_b; one_a = one_b
			zero_b = zero_c; one_b = one_c
		print(' '.join([str(zero_b),str(one_b)]))


