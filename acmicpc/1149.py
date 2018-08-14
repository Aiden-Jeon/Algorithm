import sys
n = int(sys.stdin.readline().strip())

temp2 = [0,0,0]
for i in range(n):
	rgb = list(map(int,sys.stdin.readline().strip().split()))
	if i == 0:
		answer = rgb.copy()
	else:
		for j in range(3):
			temp = list(map(lambda x:x+rgb[j],answer))
			del temp[j]
			temp2[j] = min(temp)
		answer = temp2.copy()
print(min(answer))