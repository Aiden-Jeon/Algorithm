import sys
q = sys.stdin.readline().strip()
for i in range(int(q)):
	b = ' '*(int(q)-1-i)
	for _ in range(i+1):
		b += '* '
	print(b)