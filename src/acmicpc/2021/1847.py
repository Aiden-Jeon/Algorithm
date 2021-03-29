# input: empty stack 1 // n
# output: array <a1, a2, ...> ai = (push, pop) if cannot return NO

# stack = [] /  / 4
# stack = [1] /  / 4
# stack = [1, 2] /  / 4
# stack = [1, 2, 3] /  / 4
# stack = [1, 2, 3, 4] /  / 4
# stack = [1, 2, 3] / 4 / 3
# stack = [1, 2] / 4 3
# stack = [1, 2, 5] / 4 3
# stack = [1, 2, 5, 6] / 4 3
# stack = [1, 2, 5] / 4 3 6
# stack = [1, 2, 5, 7] / 4 3 6
# stack = [1, 2, 5, 7, 8] / 4 3 6
# stack = [1, 2, 5, 7] / 4 3 6 8
# stack = [1, 2, 5] / 4 3 6 8 7
# stack = [1, 2] / 4 3 6 8 7 5
# stack = [1] / 4 3 6 8 7 5 2
# stack = [] / 4 3 6 8 7 5 2 1
import sys


N = int(sys.stdin.readline())
stack = []
result = []
s = 1
for _ in range(N):
    j = int(sys.stdin.readline())
    while True:
        if s <= j:
            stack.append(s)
            result.append("+")
            s += 1
        else:
            p = stack.pop()
            if j == p:
                result.append("-")
            else:
                result.append("NO")
            break
    if result[-1] == "NO":
        break

if result[-1] == "NO":
    print("NO")
else:
    for r in result:
        print(r)
