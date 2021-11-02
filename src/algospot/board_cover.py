# https://www.algospot.com/judge/problem/read/PICNIC
import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 9)

yx_fill = [
    [(0, 0), (0, 1), (1, 0)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)],
]


def next_xy(x, y, w):
    if x + 1 >= w:
        new_x = 0
        new_y = y + 1
    else:
        new_x = x + 1
        new_y = y
    return new_x, new_y


def fill_board(x, y, board, cnt):
    # 끝에 도달하면 전부다 채워져 있기 때문에 1을 추가해서 반환한다.
    if x == w - 1 and y == h - 1:
        return cnt + 1
    if board[y][x] == "#":
        x, y = next_xy(x, y, w)
        cnt = fill_board(x, y, board, cnt)
    else:
        for p in yx_fill:
            skip = False
            new_board = deepcopy(board)
            for (i, j) in p:
                new_y = y + i
                new_x = x + j
                # 채울 수 있는 범위를 벗어나거나 이미 채워져 있는 경우 다음 패턴으로 넘어간다
                if new_y >= h or new_x >= w or new_board[y + i][x + j] == "#":
                    skip = True
                    break
                new_board[new_y][new_x] = "#"
            if skip:
                continue
            new_x, new_y = next_xy(x, y, w)
            cnt = fill_board(new_x, new_y, new_board, cnt)
    return cnt


###
read = sys.stdin.readline
C = int(read().strip())
for c in range(C):
    h, w = map(int, read().strip().split(" "))
    board = []
    for _ in range(h):
        b = read().strip()
        b = [i for i in b]
        board.append(b)
    cnt = fill_board(0, 0, board, 0)
    print(cnt)
