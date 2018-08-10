import sys
N = int(sys.stdin.readline().strip())
zero = [0]
one  = [1]
for i in range(N-1):
	zero_tmp = 0
	one_tmp = 0
	zero_tmp += one[i] + zero[i]
	one_tmp += zero[i]

	one.append(one_tmp)
	zero.append(zero_tmp)
print(zero[-1]+one[-1])