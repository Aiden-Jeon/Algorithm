#!/usr/bin/env python3
import sys
from datetime import datetime


sitename = sys.argv[1]
number = sys.argv[2]
title = sys.argv[3]
today = datetime.now().strftime("%Y-%m-%d")
FILE_FORMAT = \
f"""\"\"\"
title: {title}
date: {today}
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

with open(f"src/acmipc/2021/{number}.py", "w") as f:
    f.write(FILE_FORMAT)
