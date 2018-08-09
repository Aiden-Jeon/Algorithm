n = 15

answer = 1
for i in range(1,n):
	s = i
	for j in range(i+1,n):
		s += j 
		if s == n:
			answer +=1
		if s>n:
			break

print(answer)