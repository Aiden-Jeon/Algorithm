import sys

q = lambda: int(sys.stdin.readline())
n = q()
arr = [0] * 8001
r_min = 9999
r_max = -9999
r_sum = 0 
for _ in range(n):
	t = q()
	r_min = min(r_min,t)
	r_max = max(r_max,t)
	r_sum += t
	arr[t+4000] += 1

def median(arr,n):
	n = n//2 +1
	for i in range(len(arr)):
		if arr[i]!=0:
			if n > arr[i]:
				n -= arr[i]
			else:
				return i - 4000
				break
def mode(arr):
	arr_max = max(arr)
	ans = []
	cnt = 0
	for i in range(len(arr)):
		if arr[i]==arr_max and cnt<2:
			ans = i - 4000
			cnt += 1
		if cnt == 2:
			ans = i-4000
			break
	return ans

#mean
print(round(r_sum/n))
#median
print(median(arr,n))
#mode
print(mode(arr))
#range
print(r_max-r_min)
