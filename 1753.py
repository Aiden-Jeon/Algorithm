import sys
import heapq

def dijkstra(mat,s,v):
	d = [float('inf')] * (v+1)
	d[s] = 0
	queue = []
	heapq.heappush(queue,(0,s))
	
	while queue:
		j,i = heapq.heappop(queue)
		for a,b in mat[i]:	
			if j+b < d[a]:
				d[a] = b+j
				heapq.heappush(queue,(b+j,a))
	answer = []
	for i in range(1,len(d)):
		if d[i] == float('inf'):
			answer.append('INF')
		else:
			answer.append(str(d[i]))
	return answer

def run():
	v,e = list(map(int,sys.stdin.readline().strip().split()))
	s = int(sys.stdin.readline().strip())
	mat = [[] for _ in range(v+1)]

	for _ in range(e):
		a,b,w = list(map(int,sys.stdin.readline().strip().split()))
		mat[a].append((b,w))

	print('\n'.join(dijkstra(mat,s,v)))

run()