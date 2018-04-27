import sys
q = lambda: sys.stdin.readline().strip()
n,k = list(map(int,q().split(' ')))
coins = []
for i in range(n):
	coins.append(int(q()))

dp = [-1] *(k+1)
for x in coins:
	if x <= k:
		dp[x] = 1

for price in range(1, k+1):
	for coin in coins:
		if price - coin > 0 and dp[price - coin] != -1:
			if dp[price] == -1:
				dp[price] = dp[price - coin]+1
			else:
				dp[price] = min(dp[price - coin]+1, dp[price])
print(dp[k])
