n = 3

a = 0
b = 1
for _ in range(n-1):
	c = a + b
	a = int(b)
	b = int(c)
	print(a,b,c)
print(b%1234567)