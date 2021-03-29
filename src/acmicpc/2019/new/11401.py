import sys
N, K = map(int, sys.stdin.readline().strip().split())

mod = 1000000007
 
bunja = 1
bunmo = 1
 
for i in range(1, N+1):
    bunja = bunja * i % mod
 
for i in range(1, K+1):
    bunmo = bunmo * i % mod
 
for i in range(1, N-K+1):
    bunmo = bunmo * i % mod

result = 1
for i in reversed(bin(mod-2)[2:]):
	if i == '1':
		result = result * bunmo % mod
	bunmo = bunmo * bunmo % mod
print(bunja * result % mod)