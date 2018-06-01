import sys
q = lambda: int(sys.stdin.readline())
n = q()
k = q()

left = 1
right = k
ans = 0
while left <= right:
	cnt = 0
	mid = (left + right) //2
	for i in range(1,n+1):
		cnt += min(mid//i,n)
	if cnt < k:
		left = mid + 1
	else:
		ans = mid
		right = mid - 1
print(ans)