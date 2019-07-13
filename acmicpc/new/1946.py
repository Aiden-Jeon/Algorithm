import sys

T = int(sys.stdin.readline())

for t in range(T):
	n = int(sys.stdin.readline())
	scores = [0]*(n+1)
	for _ in range(n):
		a,b = sys.stdin.readline().strip().split(' ')
		scores[int(a)] = int(b)
	cnt = 1
	top = scores[1]
	for i in range(2,n+1):
		if top == 1:
			break
		else:
			if scores[i] < top:
				top = scores[i]
				cnt += 1
	print(cnt)
