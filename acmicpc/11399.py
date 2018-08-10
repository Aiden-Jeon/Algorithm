import sys
n = int(sys.stdin.readline().strip())
p = sorted(list(map(int,sys.stdin.readline().strip().split(' '))))

time = 0
for i in range(1,n+1):
	time += p[i-1] * (n+1-i)
print(time)