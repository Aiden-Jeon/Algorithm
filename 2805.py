import sys
n,m = list(map(int,sys.stdin.readline().split()))
tree = list(map(int,sys.stdin.readline().split()))

right = max(tree)
left = 0
result = 0
def cut_tree(tree,mid):
	cut = 0
	for t in tree:
		if t > mid:
			cut += t-mid
	return cut

while left <= right:
	mid = (left+right)//2
	cut = cut_tree(tree,mid)
	if cut >= m:
		result = max(mid,result)
		left = mid + 1
	else:
		right = mid -1

print(result)

