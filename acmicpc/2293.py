n,k = list(map(int,input().split()))
coins = [int(input()) for _ in range(n)]
ans = [0] *(k+1)
ans[0] = 1
for c in coins:
	for i in range(k+1):
		if c<=i:
			ans[i] += ans[i-c]
print(ans[-1])