import sys 
N = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip().split(' ')
s = list(map(int,s)) 

max_sum = s[0]


for i in range(1,N):
	if s[i-1] >0 and s[i] + s[i-1] >0:
		s[i] += s[i-1]
		print(s)
	if max_sum < s[i]:
		max_sum = s[i]
print(max_sum)