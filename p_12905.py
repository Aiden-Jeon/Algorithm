import sys

q = lambda :sys.stdin.readline().strip().split(',')
board = []
for i in range(2):
	board.append(list(map(int,q())))


def solution(board):
	maximum = 0
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] != 0 and i-1>=0 and j-1>=0 :
				if board[i - 1][j]*board[i][j - 1]*board[i - 1][j - 1] != 0:
					board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
			if board[i][j]>maximum:
				maximum = board[i][j]
	return maximum**2
print(solution(board))
