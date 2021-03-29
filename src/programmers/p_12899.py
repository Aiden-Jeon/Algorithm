import sys
#n = int(sys.stdin.readline().strip())

	def solution(n):
		arr = ['1','2','4']
		answer = ''
		while n>0:
			answer = arr[int((n-1)%3)] + answer
			n = (n-1)//3
			#print(n,answer)
		return answer
for n in range(1,10):
	print(solution(n))

