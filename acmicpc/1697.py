import sys
n,k = list(map(int,sys.stdin.readline().split()))

visited = [0]*100001
queue = [n]
if n>=k:
	print(n-k)	
else:
	while queue:
		x = queue.pop(0)
		if x!=k:
			if x>0 and not visited[x-1]:
				queue.append(x-1)
				visited[x-1] = visited[x] + 1
			if x+1<=100000 and not visited[x+1]:
				queue.append(x+1)
				visited[x+1] = visited[x] + 1
			if 2*x<=100000 and not visited[2*x]:
				queue.append(2*x)
				visited[2*x] = visited[x] + 1
		else:
			print(visited[k])
			break