import sys

n,k = list(map(int, sys.stdin.readline().strip().split(' ')))

coins = [int(sys.stdin.readline()) for _ in range(n)]
total = 0

while k!=0 :
	coin = coins.pop()
	total += k//coin
	k %= coin

print(total)