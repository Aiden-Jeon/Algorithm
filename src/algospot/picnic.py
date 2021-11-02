# https://www.algospot.com/judge/problem/read/PICNIC
from copy import deepcopy
import sys


def find_no_pair(pairs):
    for i, j in enumerate(pairs):
        if j == 0:
            return i
    return -1


def pair_friends(pairs, cnt):
    cur = find_no_pair(pairs)
    if cur == -1:
        return cnt + 1

    for friend in pair_dict[cur]:
        if pairs[friend] == 0:
            next_pairs = deepcopy(pairs)
            next_pairs[cur] = next_pairs[friend] = 1
            cnt = pair_friends(next_pairs, cnt)
    return cnt


###
read = sys.stdin.readline
C = int(read().strip())
for c in range(C):
    n, m = map(int, read().strip().split(" "))
    f_pair = list(map(int, read().strip().split(" ")))
    pair_dict = {i: [] for i in range(n)}
    for i in range(0, m * 2, 2):
        a, b = f_pair[i : i + 2]
        pair_dict[a] += [b]
        pair_dict[b] += [a]
    cnt = pair_friends([0 for i in range(n)], 0)
    print(cnt)
