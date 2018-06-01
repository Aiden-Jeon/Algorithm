import sys
n = int(sys.stdin.readline())
request = list(map(int,sys.stdin.readline().split()))
total = int(sys.stdin.readline())

def give(request,mid):
	money = 0
	for r in request:
		if r <= mid:
			money += r
		else:
			money += mid
	return money

left = 1
right = total
ans = 0 
if sum(request) <= total:
	print(max(request))
else:
	while left <= right:
		mid = (left+right) // 2
		money = give(request,mid)

		if money > total:
			right = mid - 1
		else:
			ans = mid
			left = mid + 1
		
	print(ans)


