import sys
a = int(sys.stdin.readline().strip())
x = int(sys.stdin.readline().strip())


bin_x = bin(x)[2:]

a_pow = a
result = 1
for i in reversed(bin_x):
	if i == '1':
		result = (a_pow*result) % 1000000007
	a_pow = (a_pow*a_pow)%1000000007
	
print(result%1000000007)