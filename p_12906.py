import sys
arr = list(map(int,sys.stdin.readline().strip().split(',')))
answer = [arr[0]]
for a in arr[1:]:
	if a != answer[-1]:
		answer.append(a)
print(answer)