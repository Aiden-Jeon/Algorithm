import sys
q = sys.stdin.readline().strip()
q = int(q)
for i in range(1,q+1):
	if i == 1:
		print(" "*(q-i)+'*')	
	else:
		if i == q:
			print('*'*(2*i-1))
		else:
   			print(" "*(q-i)+'*'+" "*(2*i-3)+'*')