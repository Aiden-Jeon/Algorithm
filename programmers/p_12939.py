import sys
s = sys.stdin.readline().strip()

s = list(map(int,s.split()))
s.sort()
answer = str(s[0])+' '+str(s[-1])
print(answer)