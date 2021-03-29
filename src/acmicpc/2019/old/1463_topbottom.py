import sys
q = sys.stdin.readline().strip()

d = [0] * (int(q)+1)
def go(n):
	if n==1: return 0
	if d[n]>0: return d[n]
	
	d[n] = go(n-1) + 1
	if n%2 == 0:
		temp = go(n//2) + 1
		if d[n]>temp:
			d[n] = temp
	if n%3 == 0:
		temp = go(n//3) + 1
		if d[n]>temp:
			d[n] = temp
	return d[n]
print(go(int(q)))
print(d)