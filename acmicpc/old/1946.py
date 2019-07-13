import sys

T = int(sys.stdin.readline())

for i in range(T):
	n = int(sys.stdin.readline())
	score = []
	ni = 0
	while ni < n:
		score.append(list(map(int,sys.stdin.readline().split())))
		ni +=1
	score.sort()
	cnt = 1
	top = score[0]
	for j in range(1,n):
		if top[1] > score[j][1]:
			cnt += 1
			top = score[j]
	print(cnt)
	