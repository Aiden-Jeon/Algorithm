import sys
import re
n = sys.stdin.readline().strip()
n = re.sub('\+',' +',n)
n = re.sub('\-',' -',n)
n = list(map(int,n.split()))

for i in range(len(n)-1):
	if n[i] < 0:
		if n[i+1] > 0:
			n[i+1] = n[i+1]*-1
print(sum(n))
