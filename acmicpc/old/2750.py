import sys
q = lambda: int(sys.stdin.readline())
n = q()

arr = []
for _ in range(n):
	arr.append(q())
arr.sort()
for i in arr:
	print(i)
	