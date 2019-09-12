def count(k, start, end):
    middle = (start + end) // 2
    cnt = 0
    while middle != k:
        if k > middle:
            start = middle
            cnt += 1
        elif k < middle:
            end = middle
            cnt += 1
        middle = (start + end) // 2
    return cnt

for t in range(int(input())):
    P, A, B = map(int, input().split())
    start = 1

    if count(A, start, P) < count(B, start, P):
        result = 'A'
    elif count(A, start, P) > count(B, start, P):
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(t + 1, result))
