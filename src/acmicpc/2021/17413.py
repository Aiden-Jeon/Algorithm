
"""
title: 단어 뒤집기2
- problem number: 17413
- link: https://www.acmicpc.net/problem/17413  

---

## Define input, output
- Input: Strings, special token "<", ">" "<...>" is tag, and don't reverse the tag
- Output: reversed string with tags

"""
import sys


string = sys.stdin.readline().strip()
stack = []
reverse = ""

is_tag = False
for s in string:
    if s == " ":
        while stack:
            reverse += stack.pop()
        reverse += s
    elif s == "<":
        while stack:
            reverse += stack.pop()
        is_tag = True
        reverse += s
    elif s == ">":
        is_tag = False
        reverse += s
    elif is_tag:
        reverse += s
    else:
        stack.append(s)

while stack:
    reverse += stack.pop()
print(reverse)
