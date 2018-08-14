import sys

n = int(sys.stdin.readline().strip())

answer = list(map(int,sys.stdin.readline().strip().split()))
for _ in range(n-1):
	cost = list(map(int,sys.stdin.readline().strip().split()))
	temp = []
	for i in range(len(cost)):
		if i == 0:
			temp.append(cost[i]+answer[0])
		elif i == len(cost)-1:
			temp.append(cost[i]+answer[-1])
		else:
			temp.append(cost[i]+max(answer[i-1],answer[i]))
	answer = temp.copy()
print(max(answer))
