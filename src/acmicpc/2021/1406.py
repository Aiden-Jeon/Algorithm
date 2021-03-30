"""
title: 에디터
problem: 1406  
link: https://www.acmicpc.net/problem/1406  

Input: 문자열, 명령어
Output: 명령어에 의해 수정된 문자열

입력으로 들어오는 크기의 최대값이 50000임
1. indexing 으로 할 경우 P 를 받을 때 O(n) 이 발생
2. insert, pop 의 경우 값을 추가하거나 뺄 때 해당 index의 오른쪽 값들을 한 칸씩 미루어야 해서 시간 복잡도가 O(n) 이 발생함
"""
import sys

string = sys.stdin.readline().strip()
N = int(sys.stdin.readline())

left = list(string)
right = []
for _ in range(N):
    command = sys.stdin.readline().strip()
    if command[0] == "P":
        left.append(command[-1])
    elif command[0] == "L" and left:
        right.append(left.pop())
    elif command[0] == "D" and right:
        left.append(right.pop())
    elif command[0] == "B" and left:
        left.pop()

print("".join(left + right[::-1]))
