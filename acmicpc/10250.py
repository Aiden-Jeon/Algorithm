def solution(h,w,n):
	i = 1
	while n-h>0:
		n -= h
		i += 1
	if len(str(i)) == 1:
		i = '0' + str(i)
	return ''.join([str(n),str(i)])

for _ in range(int(input())):
	h,w,n = list(map(int,input().split()))
	print(solution(h,w,n))