"""
title: 요세푸스 문제  
- problem number: 1158  
- link: https://www.acmicpc.net/problem/1158   

---

## Define input, output
- Input: <a1, a2, .. an>, order k  
- Output: <a^1, a^2, .. a^n>  


## 설명
list를 이용할 경우 append or pop 에서 O(N)이 소모된다.    
시간복잡도를 줄이기 위해서는 아래의 과정이 각각 O(1) 이어야 한다.  

- left pop, right append  
- left append, right pop  

이를 위해서 deque를 사용했다.  
"""
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split(" "))
deq = deque()
for i in range(1, n + 1):
    deq.append(i)

answer = []
while deq:
    for _ in range(k - 1):
        deq.append(deq.popleft())
    answer += [deq.popleft()]
answer = ", ".join(map(str, answer))
print(f"<{answer}>")
