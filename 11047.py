import sys
q = lambda: sys.stdin.readline().strip()
n,k = list(map(int,q().split(' ')))
coins = []
for i in range(n):
	coins.append(int(q()))
coins = list(reversed(coins))

coin = 0
for i in coins:
	if k // i != 0:
		coin += k//i
		k = k%i
print(coin)