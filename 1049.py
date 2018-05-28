import sys
q = lambda: list(map(int,sys.stdin.readline().strip().split()))
n,m = q()
p = []
s = []
for i in range(m):
	t1,t2 = q()
	p.append(t1)
	s.append(t2)
if min(s)*6 > min(p):
	price = min(p) * (n//6)
	if min(s)*(n%6) < min(p):
		price += min(s)*(n%6)
	else:
		price += min(p)
else:
	price = min(s) * n
print(price)