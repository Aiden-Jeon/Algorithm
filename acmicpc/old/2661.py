import sys
n = int(sys.stdin.readline().strip())

stack = ['1']

while stack:
	s = stack.pop()
	if len(s) == n:
		print(s)
		break
	else:
		for i in ['3','2','1']:
			t = s+i
			no = 1
			for i in range(1,len(t)//2+1):
				if t[-i:] == t[-i*2:-i]:
					no = 0
					break
			if no:
				stack.append(t)
