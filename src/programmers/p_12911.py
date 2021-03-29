n = 12
bn = bin(n)

for i in range(n+1,1000001):
	if bin(i).count('1') == bn.count('1'):
		print(i)
		break
		