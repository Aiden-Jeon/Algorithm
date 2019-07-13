import sys
q = lambda: int(sys.stdin.readline().strip())
n = q()

stair = [0]
for _ in range(n):
	stair.append(q())

answer = [0] * (n+1)
answer[1] = stair[1]
if n>2:
	for i in range(2,n+1):
		answer[i] = stair[i] + max(stair[i-1]+answer[i-3],answer[i-2])
	print(answer[-1])
else:
	print(sum(stair))
