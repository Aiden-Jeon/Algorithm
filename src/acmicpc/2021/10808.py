"""
title: 알파벳 개수
date: 2021-04-08
- problem number: 10808
- link: https://www.acmicpc.net/problem/10808  

---

## Define input, output
- Input: 소문자로 이루어진 단어 S
- Output: 각 소문자별 count

## 설명

"""
import sys
from collections import Counter


S = sys.stdin.readline()
S = Counter(S)
answer = [str(S.get(chr(c), 0)) for c in range(ord("a"), ord("z") + 1)]
print(" ".join(answer))
