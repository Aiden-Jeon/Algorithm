#!/usr/bin/env python3
import sys
from datetime import datetime


number = sys.argv[1]
difficult = sys.argv[2]
title = sys.argv[3].replace(" ", "-").lower()
today = datetime.now().strftime("%Y-%m-%d")
FILE_FORMAT = \
f"""\"\"\"
title: {title}
date: {today}
- problem number: {number}
- difficult: {difficult}  
- https://leetcode.com/problems/{title}/  

---

## Define input, output
- Input:
- Output: 

## 설명

\"\"\"

"""

with open(f"src/leetcode/{number}.py", "w") as f:
    f.write(FILE_FORMAT)
