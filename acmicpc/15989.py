n = int(input())
arr = [int(input()) for _ in range(n)]
k = max(arr)
ans = [0] * (k+1)
ans[0] = 1
for c in range(1,4):
	for i in range(k+1):
		if c<=i:
			ans[i] += ans[i-c]
for a in arr:	
	print(ans[a])