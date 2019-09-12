# def color_bd():

for t in range(int(input())):
    N = int(input())
    board = [[0] * 10 for _ in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += color

    cnt = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] >= 3:
                cnt += 1

    print(cnt)
