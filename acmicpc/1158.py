import sys
r = lambda: sys.stdin.readline().strip()
m,n = r().split(' ')
ml = [i for i in range(1,int(m)+1)]
stack = ''
while len(ml) > 0:
	for i in range(int(n)-1):
		ml.append(ml.pop(0))
	stack = stack + str(ml.pop(0)) +', '
print('<'+stack[:-2]+'>')
## 시간초과 