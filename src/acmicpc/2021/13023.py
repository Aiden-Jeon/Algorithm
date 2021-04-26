"""
title: ABCDE
date: 2021-04-18
- problem number: 13023
- link: https://www.acmicpc.net/problem/13023  

---

## Define input, output
- Input: 사람 N과 M개의 친구 관계가 들어온다
- Output: 5명이 연속해서 친구 관계가 있는지 확인한다.

## 설명
재귀 DFS로 풀어야 시간 초과 하지 않음!
재귀로 visit 을 1로 바꿔주고 해결되지 않고 재귀에서 나올 경우 다시 0 으로 돌려주어야 함.

"""
import sys


N, M = map(int, sys.stdin.readline().strip().split(" "))

relation = {}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    relation.setdefault(a, [])
    relation.setdefault(b, [])
    relation[a] += [b]
    relation[b] += [a]

stack = [[i] for i in relation.keys()]
visit = [False] * N


def dfs(cur, depth):
    visit[cur] = True
    if depth == 5:
        return 1
    for friend in relation.get(cur, []):
        if not visit[friend]:
            result = dfs(friend, depth + 1)
            if result:
                return result
            visit[friend] = False


for i in range(N):
    result = dfs(i, 1)
    visit[i] = False
    if result:
        break

print(result if result else 0)
