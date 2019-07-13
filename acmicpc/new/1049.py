import sys

n,m = list(map(int, sys.stdin.readline().strip().split(' ')))

min_p = min_s = 1001
for _ in range(m):
	p,s = list(map(int, sys.stdin.readline().strip().split(' ')))
	min_p = min(min_p, p)
	min_s = min(min_s, s)

if n<=6:
	print(min(min_p, min_s*n))
else:
	print(min(min_p*(n//6+1),min_p*(n//6) + min_s*(n%6), min_s*n))