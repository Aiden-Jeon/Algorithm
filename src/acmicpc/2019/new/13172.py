import sys

def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return a

M = int(sys.stdin.readline())
X = 1000000007

bunmo, bunja = list(map(int, sys.stdin.readline().strip().split()))

for _ in range(M-1):
	t_bunmo, t_bunja = list(map(int, sys.stdin.readline().strip().split()))
	bunja = bunmo*t_bunja + bunja*t_bunmo
	bunmo *= t_bunmo
	bunja %= X
	bunmo %= X
	
g = gcd(bunmo, bunja)
bunmo //= g
bunja //= g

print((bunja%X * (pow(bunmo,X-2, X))%X))
