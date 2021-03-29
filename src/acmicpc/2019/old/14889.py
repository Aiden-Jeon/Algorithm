import sys
import itertools
q = lambda: sys.stdin.readline().strip()
n = int(q())
stat = {}
player = []
for i in range(n):
	stat[i] = list(map(int,q().split()))
	player.append(i)


def score(t1,t2):
	t1_s = 0
	t2_s = 0
	for a1 in t1:
		for a2 in t1:
			t1_s += stat[a1][a2]
	for b1 in t2:
		for b2 in t2:
			t2_s += stat[b1][b2]
	return abs(t1_s - t2_s)

comb = list(itertools.combinations(player,int(n//2)))
min_s = float('inf')
for i in range(int(len(comb)//2)):
	t1 = comb[i]
	t2 = comb[-(i+1)]
	if min_s > score(t1,t2):
		min_s = score(t1,t2)
print(min_s)
	
