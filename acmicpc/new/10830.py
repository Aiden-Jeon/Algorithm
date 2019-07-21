import sys

def matmul(A, B):
	n = len(A)
	result = []
	for a in A:
		row = []
		for i in range(n):
			temp = 0
			for j in range(n):
				temp = (temp + a[j]*B[j][i]) % 1000
			row += [temp]
		result.append(row)
	return result

N, B = map(int, sys.stdin.readline().strip().split())

mat = []
for i in range(N):
	temp = list(map(int, sys.stdin.readline().strip().split()))
	mat.append(temp)

result = mat.copy()
first = True
for i in reversed(bin(B)[2:]):
	if i == '1':
		if first:
			result = mat.copy()
			first = False
		else:
			result = matmul(result, mat)
	mat = matmul(mat, mat)

for r in result:
	print(' '.join(map(lambda x: str(x%1000),r)))