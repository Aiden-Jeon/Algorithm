"""
title: 리모컨
date: 2021-04-13
- problem number: 1107
- link: https://www.acmicpc.net/problem/1107  

---

## Define input, output
- Input: target 채널, 고장난 스위치 개수, 고장난 스위치 목록
- Output: 최소한의 클릭으로 target 채널에 도달하기

## 설명
- 신경써야 할 부분
    1. 고장난 스위치 개수가 0이면 3번째 줄은 주어지지 않는다.
    -> 확인 안할 경우 ValueError
    2. 스위치가 전부 고장날 수 있다.
    -> 방법에 따라 NameError

- 반례 모음
    - https://www.acmicpc.net/board/view/46120

"""
import sys
from itertools import product


target = sys.stdin.readline().strip()
f = int(sys.stdin.readline())

if 0 < f < 10:
    fault = sys.stdin.readline().strip().split(" ")
    remote = []
    for i in range(10):
        if str(i) in fault:
            pass
        else:
            remote.append(str(i))

    start_idx = 0
    for start_idx, t in enumerate(target):
        if t not in remote:
            if start_idx > 0:
                start_idx -= 1
            break

    def cal(c, target, start_idx):
        cnt = len(c) + start_idx
        c = target[:start_idx] + "".join(c)
        cnt += abs(int(c) - int(target))
        return cnt

    min_cnt = abs(int(target) - 100)
    for i in range(1, len(target) - start_idx + 2):
        comb = product(remote, repeat=i)
        m = min(map(lambda x: cal(x, target, start_idx), comb))
        min_cnt = min(min_cnt, m)
    print(min_cnt)
elif f == 0 :
    min_cnt = min(len(target), abs(int(target) - 100))
    print(min_cnt)
else:
    print(abs(int(target) - 100))
