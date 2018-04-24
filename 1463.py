import sys
a = int(sys.stdin.readline().strip())+1

log = [0]*a


for i in range(1,a):
	log[i] = log[i-1] +1
	if i%2 == 0:
		if log[i] > log[int(i/2)]+1:
			log[i] = log[int(i/2)]+1

	if i%3 == 0:
		if log[i] > log[int(i/3)]+1:
			log[i] = log[int(i/3)]+1
	print(log,i)
