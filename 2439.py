import sys
q = sys.stdin.readline().strip()

for i in range(1,int(q)+1):
	print(' '*(int(q)-i)+'*'*i)
	