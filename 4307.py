import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
	l,n = list(map(int,sys.stdin.readline().strip().split()))
	
	sh = [0]*n
	ln = [0]*n

	for j in range(n):
		ant = int(sys.stdin.readline().strip())
		if ant > l-ant:
			sh[j] = l-ant
			ln[j] = ant
		else:
			sh[j] = ant
			ln[j] = l-ant
	print(max(sh),max(ln))
