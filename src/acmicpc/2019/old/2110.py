import sys
n,c = list(map(int,sys.stdin.readline().split()))
house = [0]*n
for i in range(n):
	house[i] = int(sys.stdin.readline())
house.sort()

left = 0
right = house[-1] - house[0]
ans = 0
while left <= right:
	gap = (left+right) //2
	cnt = 1
	now = house[0]

	for i in range(1,n):
		if house[i]-now >= gap:
			cnt += 1
			now = house[i]

	if cnt >= c:
		ans = gap
		left = gap +1
	else:
		right = gap - 1
print(ans)