n = 3
s = 12

answer=[]
if n<s:
	print([-1])
while n>1:
	answer.append(int(s/n))
	s -= answer[-1]
	n-=1
	
answer.append(s)
print(answer)