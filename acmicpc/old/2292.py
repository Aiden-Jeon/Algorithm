import sys

n = int(sys.stdin.readline())

if n == 1:
	print(1)
else:
	i = 0
	while n - i*6>0:
		if i == 0:
			n -= 1
		else:
			n -= i*6
		i+=1

	print(i+1)