import sys
q = lambda: sys.stdin.readline().strip()
n = int(q())

for i in range(n):
	stack = []
	r = q()
	for j in range(len(r)):
		if r[j] == '(':
			stack.append(r[j])
		if r[j] == ')':
			if len(stack) == 0:
				stack.append(r[j])
			elif stack[-1] == '(':
				stack.pop()
	if len(stack) == 0:
		print('YES')
	else:
		print('NO')
