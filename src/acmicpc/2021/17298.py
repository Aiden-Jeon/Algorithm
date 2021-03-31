"""
title: 오큰수
- problem number: 17298
- link: https://www.acmicpc.net/problem/17298  

---

## Define input, output
- Input: Array <$a_{1}$, $a_{2}$,...,$a_{n}$>
- Output: 
  - Array <$a'_{1}$, $a'_{2}$,...,$a'_{n}$> 
  - $b_{i} = max(a'_{i+1}, a'_{i+2}, ..., a'_{n})$
  - $a'_{i} = \text{if } b_{i} > a_{i} \text{ then } b_{i} \text{ else }-1$

"""
import sys


N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split(" ")))
stack = []
answer = [-1] * N
for i, val in enumerate(array):
    while stack and array[stack[-1]] < val:
        answer[stack.pop()] = val
    stack.append(i)

print(*answer)
