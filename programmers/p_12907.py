n=6
money=[2,3]

answer = [0] * (n+1)
answer[0] = 1

temp = 0
for i in range(1,n+1):
	if i == 1:
		temp = 0
	else:
		temp = answer[i-1]
	for m in money:
		if i % m == 0:
			answer[i] = temp +1
	print(answer)