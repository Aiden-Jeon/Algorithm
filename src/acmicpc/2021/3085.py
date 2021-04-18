"""
title: 사탕 게임
date: 2021-04-13
- problem number: 3085
- link: https://www.acmicpc.net/problem/3085  

---

## Define input, output
- Input: 캔디의 종류가 써 있는 matrix
- Output: 가장 긴 캔디의 길이

## 설명
swap후 가장 긴 캔디의 길이를 구하고 다시 swap한다.
-> 메모리를 줄일 수 있음.

"""
import sys


def get_max_candy(candies):
    max_cnt = 1
    for i in range(N):
        max_row = 1
        max_col = 1
        for j in range(1, N):
            # row candy
            if candies[i][j - 1] == candies[i][j]:
                max_row += 1
            else:
                max_row = 1

            # col candy
            if candies[j - 1][i] == candies[j][i]:
                max_col += 1
            else:
                max_col = 1
            max_cnt = max(max_cnt, max_row, max_col)
    return max_cnt


N = int(sys.stdin.readline())
candies = []
for _ in range(N):
    candies.append(list(sys.stdin.readline().strip()))

max_candy = 1
for i in range(N):
    for j in range(1, N):
        if candies[i][j - 1] != candies[i][j]:
            candies[i][j - 1], candies[i][j] = candies[i][j], candies[i][j - 1]
            max_candy = max(max_candy, get_max_candy(candies))
            candies[i][j], candies[i][j - 1] = candies[i][j - 1], candies[i][j]

        if candies[j - 1][i] != candies[j][i]:
            candies[j - 1][i], candies[j][i] = candies[j][i], candies[j - 1][i]
            max_candy = max(max_candy, get_max_candy(candies))
            candies[j][i], candies[j - 1][i] = candies[j - 1][i], candies[j][i]

    if max_candy == N:
        break

print(max_candy)
