import sys

sys.stdin = open("4869input.txt", "r")

def paper(w):
    if w == r:  # 목표 너비가 되면
        return 1
    if w > n:
        return 0

TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())  # 목표 너비
    r = paper(0)