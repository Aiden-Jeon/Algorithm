import sys
a,b = list(map(int,sys.stdin.readline().split()))

month = [0,31,29,31,30,31,30,31,31,30,31,30]
week = ['THU','FRI','SAT','SUN','MON','TUE','WED']

def solution(a,b):
	day = sum(month[:a]) + b
	return week[day%7]

print(solution(a,b))
