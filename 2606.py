import sys

n_c = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

net = {}
for i in range(n):
	a,b = list(map(int,sys.stdin.readline().strip().split()))
	if a in list(net.keys()):
		net[a] = set(list(net[a])+[b])
	else:
		net[a] = set([b])
	if b in list(net.keys()):
		net[b] = set(list(net[b])+[a])
	else:
		net[b] = set([a])

queue = [1]
visited = []
while queue:
	v = queue.pop(0)
	if v not in visited:
		queue += net[v]
		visited.append(v)

print(len(visited)-1)