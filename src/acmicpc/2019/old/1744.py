import sys
b = int(sys.stdin.readline().strip())
pos =[]
neg = []
for i in range(b):
	q = int(sys.stdin.readline().strip())
	if q >0:
		pos.append(q)
	else:
		neg.append(q)
pos = sorted(pos,reverse=True)
neg = sorted(neg)

for i in range(0,len(pos),2):
	if i != len(pos)-1:
		if pos[i]*pos[i+1] > pos[i]:
			pos[i] = pos[i]*pos[i+1]
			pos[i+1] = 0

for i in range(0,len(neg),2):
	if i != len(neg)-1:
		if neg[i]*neg[i+1] >= neg[i]*(-1):
			neg[i] = neg[i]*neg[i+1]
			neg[i+1] = 0

for i in range(len(neg)):
	if neg[i] == 0:
		for j in range(i):
			if neg[j] <0:
				neg[j] = 0
				break
print(sum(neg)+sum(pos))


