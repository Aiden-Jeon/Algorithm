import sys
n =  int(sys.stdin.readline().strip())

e = 1
l = 2

for i in range(1,n):

	e_tmp= e + l
	l_tmp= (e*2) + l
	e = e_tmp
	l = l_tmp

print(sum([e,l])%9901)