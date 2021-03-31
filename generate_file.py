#!/usr/bin/env python3
import sys

number = sys.argv[1]
title = sys.argv[2]

FILE_FORMAT = \
f"""\"\"\"
title: {title}
- problem number: {number}
- link: https://www.acmicpc.net/problem/{number}  

---

## Define input, output
- Input:
- Output: 

## 설명

\"\"\"
import sys


N = int(sys.stdin.readline())
"""

with open(f"src/acmicpc/2021/{number}.py", "w") as f:
    f.write(FILE_FORMAT)
