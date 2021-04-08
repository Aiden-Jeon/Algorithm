"""
title: 문자열 분석
date: 2021-04-08
- problem number: 10820
- link: https://www.acmicpc.net/problem/10820  

---

## Define input, output
- Input: 소문자, 대문자, 숫자, 공백으로 이루어진 어떤 문자열
- Output: 소문자, 대문자, 숫자, 공백의 개수

## 설명
주어진 문자열 시작과 끝에 공백이 있음으로 strip 하면 안 된다.
"""
import sys
from collections import Counter


for i in range(100):
    lower = 0
    upper = 0
    number = 0
    blank = 0
    line = sys.stdin.readline()
    if not line:
        break
    counts = Counter(line)
    for key in counts:
        if key == " ":
            blank += counts[key]
        elif ord("0") <= ord(key) <= ord("9"):
            number += counts[key]
        elif ord("a") <= ord(key) <= ord("z"):
            lower += counts[key]
        elif ord("A") <= ord(key) <= ord("Z"):
            upper += counts[key]
    print(lower, upper, number, blank)    
