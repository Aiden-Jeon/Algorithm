import sys
r = lambda: sys.stdin.readline().strip()
m,n = r().split(' ')
ml = [i for i in range(1,int(m)+1)]

print('<')
while len(ml) > 0:
	for i in range(1,int(n)+1):
		if i%int(n) ==0:
			print('%d, '%ml.pop(0))
		else:
			ml.append(ml.pop(0))
print('>')