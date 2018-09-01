n = int(input())
arr = [int(input()) for _ in range(n)]
ans = [0] * len(arr)
for i in range(n):
	if i == 0:
		ans[0] = arr[0]
	elif i == 1:
		ans[1] = arr[0] + arr[1]
	elif i == 2:
		ans[2] = max(arr[0]+arr[2],arr[1]+arr[2])
	else:
		ans[i] = max(arr[i]+arr[i-1]+max(ans[:i-2]),arr[i]+max(ans[:i-1]))
	# print(ans)
print(max(ans))