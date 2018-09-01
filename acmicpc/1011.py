import sys

def solution(n):
	i=1;cnt=0;
	while n-2*i>=0:
		n -= 2*i
		i += 1
		cnt += 2
		# print(n,i,cnt)
	for j in reversed(range(1,i+1)):
		# print(n,j,cnt)
		if n>=j:
			n -= j
			cnt += 1
		elif n == 0:
			break
	return cnt

n = int(sys.stdin.readline())
for _ in range(n):
	a,b = list(map(int,sys.stdin.readline().split()))
	print(solution(b-a))