import sys
T = int(sys.stdin.readline())

for t in range(T):
	l,n = list(map(int, sys.stdin.readline().strip().split(' ')))
	max_time = 0
	min_time = 0
	for _ in range(n):
		ant = int(sys.stdin.readline())
		if l-ant >= ant:
			ant_max = l-ant
			ant_min = ant
		else:
			ant_max = ant
			ant_min = l-ant
		max_time = max(max_time, ant_max)
		min_time = max(min_time, ant_min)
	print(min_time, max_time)