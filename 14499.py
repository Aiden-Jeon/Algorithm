import sys
q = lambda: list(map(int,sys.stdin.readline().strip().split()))
n,m,x,y,k = q()
mat = {}
for i in range(n):
	mat[i] = q()
move = q()

def dice_move(dice,l):
	result = []
	if l==1:
		for i in [4,2,1,6,5,3]:
			result += [dice[i-1]]
	if l==2:
		for i in [3,2,6,1,5,4]:
			result += [dice[i-1]]
	if l==3:
		for i in [5,1,3,4,6,2]:
			result += [dice[i-1]]
	if l==4:
		for i in [2,6,3,4,1,5]:
			result += [dice[i-1]]
	return result
dice = [0] * 6
x_move = [0,0,-1,1]
y_move = [1,-1,0,0]
answer = []
while move:
	l = move.pop(0)
	if (l==1 and y>m-2) or (l==2 and y<1) or (l==3 and x<1) or (l==4 and x>n-2):
		pass
	else:
		dice = dice_move(dice,l)
		upper = dice[0]
		x += x_move[l-1]
		y += y_move[l-1]
		if mat[x][y] == 0:
			mat[x][y] = dice[-1]
		else:
			dice[-1] = mat[x][y]
			mat[x][y] = 0
		answer.append(str(upper))

print("\n".join(answer))
		