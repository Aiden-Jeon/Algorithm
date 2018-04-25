import sys 
n = int(sys.stdin.readline().strip())
p = sys.stdin.readline().strip().split(' ')
p = list(map(int,p)) #세트별 판매 가격

s = [0]*n
s[0] = p[0]
for i in range(1,n+1):
	s_tmp = [p[i-1]]
	#print(i,i//2)
	for j in range(1,i//2+1):
		s_tmp.append(s[i-j-1]+s[j-1])
	
	s[i-1] = max(s_tmp)
print(max(s))

