import sys
q = lambda: int(sys.stdin.readline())
n = q()
arr = [0]*10001
for _ in range(n):
	arr[q()] += 1

for i in range(10001):
	if arr[i] != 0:
		for _ in range(arr[i]):
			print(i)