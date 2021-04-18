"""
title: 날짜 계산
date: 2021-04-10
- problem number: 1476
- link: https://www.acmicpc.net/problem/1476  

---

## Define input, output
- Input: 
    - 1년이 지날 때마다 E, S, M 이 1씩 증가
    - 단 각각은 아래의 범위 만큼만 가질 수 있음
    - 넘을 경우에는 1로 초기화
        - 1 <= E <= 15 / 1 <= S <= 28 / 1 <= M <= 19
- Output: 
    - e, s, m 이 주어졌을 때 몇 년이 흘렀는지

"""
import sys


E, S, M = map(int, sys.stdin.readline().rstrip().split(" "))
e = s = m = 1
cnt = 1
while True:
    if E == e and S == s and M == m:
        break
    e += 1
    if e == 16:
        e = 1
    s += 1
    if s == 29:
        s = 1
    m += 1
    if m == 20:
        m = 1
    cnt += 1

print(cnt)
