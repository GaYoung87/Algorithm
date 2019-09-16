def game(a, b):
    if a == 1:
        if b == 1 or b == 3:
            return a
        else:
            return b
    elif a == 2:
        if b == 1 or b == 2:
            return b
        else:
            return a
    elif a == 3:
        if b == 2 or b == 3:
            return a
        else:
            return b

for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(1, len(data) + 1):