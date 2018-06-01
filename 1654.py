import sys
k,n = list(map(int,sys.stdin.readline().strip().split()))
line = [0]*k
for i in range(k):
	line[i] = int(sys.stdin.readline().strip())

def cutting(line,mid):
	cut = 0
	for l in line:
		cut += l//mid
	return cut

left = 1
right = max(line)
ans = 0

while left<=right:
	mid = (left+right)//2
	cut = cutting(line,mid)
	if cut >= n:
		ans = mid
		left = mid + 1
	else:
		right = mid - 1
print(ans)

