import sys

n = int(sys.stdin.readline())

i = 0
while n > (i*(i+1))/2:
	i+=1
n -= int((i*(i-1))/2)
if (i+1)%2 == 1:
	print('/'.join([str(n),str(i+1-n)]))
else:
	print('/'.join([str(i+1-n),str(n)]))

