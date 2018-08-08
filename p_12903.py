import sys
s = sys.stdin.readline().strip()

def solution(s):
	l = len(s)
	if l%2==1:
		return s[int(l/2)]
	else:
		return s[int(l/2)-1:int(l/2)+1]

print(solution(s))