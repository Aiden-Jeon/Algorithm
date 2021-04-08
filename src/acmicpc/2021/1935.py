"""
title: 후위 표기식2
date: 2021-04-08
- problem number: 1935
- link: https://www.acmicpc.net/problem/1935  

---

## Define input, output
- Input: 후위표기식으로 표시된 식
- Output: 값

## 설명

후위 표기식과 다르게 정방향으로 접근한다.  
후휘 표기식 자체가 컴퓨터에서 식을 간단하게 계산하기 위해서 만들어진 것을 생각하자.
"""
import sys


def calculator(after, before, cur):
    if cur == "+":
        return before + after
    elif cur == "-":
        return before - after
    elif cur == "*":
        return before * after
    elif cur == "/":
        return before / after


N = int(sys.stdin.readline())
math = sys.stdin.readline().strip()

alphabet = ord("A")
replace = {}
for _ in range(N):
    n = int(sys.stdin.readline())
    replace[chr(alphabet)] = n
    alphabet += 1

stacks = []
for cur in math:
    if ord("A") <= ord(cur) <= ord("Z"):
        stacks.append(replace[cur])
    else:
        after = stacks.pop()
        before = stacks.pop()
        stacks.append(calculator(after, before, cur))

print("{:.2f}".format(stacks[0]))
