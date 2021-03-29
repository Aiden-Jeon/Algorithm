# input: sentence with words
# - 단어의 기준은 space
# - 대문자는 유지
# output: 문장에서 단어들의 위치는 보존하고 각 단어들의 역순으로 이루어진 문장
import sys


N = int(sys.stdin.readline())

for _ in range(N):
    words = sys.stdin.readline().split(" ")
    words = list(map(lambda x :x[::-1], words))
    sentence = " ".join(words)
    print(sentence)
