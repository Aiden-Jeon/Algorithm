import sys
arr = list(map(int,sys.stdin.readline().strip().split(',')))
divisor = int(sys.stdin.readline().strip())

answer = [i for i in arr if i%divisor==0]
answer.sort()
if len(answer) == 0:
	answer = [-1]	
print(answer)