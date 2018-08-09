n = 6
answer = [0,1,2]
answer.extend([0]*(n-2))
for i in range(3,n+1):
	answer[i] = answer[i-1]+answer[i-2]
	print(answer)