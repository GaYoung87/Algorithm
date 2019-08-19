def isPalinH(x, y):
    for i in range(M // 2):
        if s[x][y + i] != s[x][y + (M - 1) - i]
        return False
    print(s[x][y:y + M])

def isPalinV(x, y):
    for i in range(M // 2):
        if s[x + i][y] != s[x + (M - 1) - i][y]
        return False

    for _ in range(x, x + M):
        print(s[_][y], end=' ')

for t in range(int(input())):
    N, M = map(int, input().split())
    s = [input() for i in range(N)]

    print('#{}'.format(t), end=' ')

    # for i in range(N):
    #     for j in range(N - M + 1):
    #         isPalinH(i, j)
    #         isPalinV(j, i)


    found = False
    for i in range(N):
        if found:
            break
        for j in range(N - M + 1):
            if isPalinH(i, j):
                found = True
                break
            if isPalinV(i, j):
                found = True
                break
