import sys
a = list(map(int,sys.stdin.readline().split(',')))
b = list(map(int,sys.stdin.readline().split(',')))
a.sort()
b.sort(reverse=True)
print(a,b)
c = list(map(lambda x,y: x*y,a,b))
print(sum(c))