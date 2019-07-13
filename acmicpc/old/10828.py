import sys
q = lambda: sys.stdin.readline().strip()
n = int(q())
stack = []

for _ in range(n):
	command = q()
	if command[:4] == 'push':
		stack.append(int(command[4:]))
	elif command == 'top':
		if len(stack)>0:
			print(stack[-1])
		else:
			print(-1)
	elif command == 'size':
		print(len(stack))
	elif command =='empty':
		if len(stack)==0:
			print(1)
		else:
			print(0)
	elif command == 'pop':
		if len(stack) >0:
			print(stack.pop())
		else:
			print(-1)
