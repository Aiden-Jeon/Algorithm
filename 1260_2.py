import sys
q = lambda: sys.stdin.readline().strip()
l = list(map(int,q().split(' ')))


check = [False] * (l[0]+1)


cur = l[2]
visit = [l[2]]
stack = [l[2]]
check[l[2]] = True
