
"""
title: 쇠막대기
- problem number: 10799
- link: https://www.acmicpc.net/problem/10799  

---

## Define input, output
- Input: 쇠 막대기의 시작, 끝, 레이저 포인트에 대한 array
- Output: 레이저로 잘린 쇠막대기의 총 개수

"""
import sys


points = list(sys.stdin.readline().strip())

total = 0
remain = []
for i, point in enumerate(points):
    if point == ")":
        j = remain.pop()
        if i - j == 1:
            total += len(remain)
        else:
            total += 1
    else:
        remain.append(i)

print(total)