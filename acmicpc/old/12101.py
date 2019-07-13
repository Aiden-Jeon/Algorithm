import sys
import itertools
n,k = list(map(int,sys.stdin.readline().strip().split()))

arr = {1:['1'],
	2:['11','2'],
	3:['111','12','21','3']}
for i in range(4,n+1):
	temp = []
	for j in arr[i-1]:
		temp.append(j+'1')
	for j in arr[i-2]:
		temp.append(j+'2')
	for j in arr[i-3]:
		temp.append(j+'3')
	temp.sort()
	arr[i] = temp

if len(arr[n])<k:
	print(-1)
else:
	print('+'.join(arr[n][k-1]))