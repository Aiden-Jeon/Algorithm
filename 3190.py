import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

mat = {}
for i in range(n):
	mat[i] = [0]*n

for _ in range(k):
	r,c = list(map(int,sys.stdin.readline().strip().split()))
	mat[r-1][c-1] = 1

l = int(sys.stdin.readline().strip())
def info(l):
	time = []
	move = []
	for _ in range(l):
		t,c = list(sys.stdin.readline().strip().split())
		time.append(int(t)+1)
		move.append(c)
	return time,move
time,move = info(l)

def direction(c,d):
	if c == 'L':
		d -=1
		if d == 0: d = 4
	if c == 'D':
		d += 1
		if d == 5: d = 1
	return d

r_move = [0,1,0,-1]
c_move = [1,0,-1,0]
r,c,d,t = [0,0,1,0]
snake = [[0,0]]
mat[r][c] = -1
while True:
	t += 1
	if t in time:
		time.pop(0)
		where = move.pop(0)
		d = direction(where,d)
	r += r_move[d-1]
	c += c_move[d-1]
	if r<0 or c<0 or r>n-1 or c>n-1:
		break
	else:
		if mat[r][c] == -1:
			break
		else:
			if mat[r][c] == 1:
				mat[r][c] = -1
				snake.append([r,c])
			else:
				mat[r][c] = -1
				t1,t2 = snake.pop(0)
				mat[t1][t2] = 0
				snake.append([r,c])
print(t)
