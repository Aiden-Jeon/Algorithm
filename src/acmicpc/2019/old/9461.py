t = int(input())
arr = [int(input()) for _ in range(t)]
n = max(arr)
ans = [1,1,1,2,2] 
ans.extend([0]*(n-5))
for i in range(5,n):
	ans[i] = ans[i-1]+ans[i-5]
for a in arr:
	print(ans[a-1])
