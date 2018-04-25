import sys
n = int(sys.stdin.readline().strip())

a = [0] * 10
b = [1,2,2,2,2,2,2,2,2,1]
for i in range(n-2):
	if i != n-3:
		for j in range(10):
			if j==0:
				a[j] = b[j+1]
			else:
				if j==9:
					a[j] = b[j-1]
				else:
					a[j] = b[j-1]+b[j+1]
		b = a.copy()
	else:
		for j in range(1,10):
			if j != 9:
				a[j] = b[j-1] + b[j+1]
			else:
				a[j] = b[j-1]
		a[0] = 0

if n ==1:
	print(9)
else:
	if n==2:
		print(sum(b[1:]))
	else:
		print(sum(a)%1000000000)

