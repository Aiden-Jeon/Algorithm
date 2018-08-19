import sys
q = lambda: int(sys.stdin.readline().strip())
n = q()

for i in range(n):
	t = q()
	if i == 0:
		arr = [0] * (t+1)
		arr[1] = 1; arr[2] = 2; arr[3] =4
		for i in range(4,t+1):
			arr[i] += (arr[i-1] + arr[i-2] + arr[i-3]) % 1000000009
		if t <=3 :
			print(arr[t])
		else:
			print(arr[-1]% 1000000009)
	else:
		if t<len(arr):
			print(arr[t])
		else:
			l = len(arr)
			arr.extend([0]* (t-l+1))
			for i in range(l,t+1):
				arr[i] += (arr[i-1] + arr[i-2] + arr[i-3]) % 1000000009
			print(arr[-1]% 1000000009)