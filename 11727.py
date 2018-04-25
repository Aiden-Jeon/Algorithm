import sys
n = int(sys.stdin.readline().strip())

b = [0,1,3]

for i in range(3,n+1):
	b.append(b[i-1]+2*b[i-2])

print(b[n]%10007)