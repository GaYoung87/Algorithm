for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split()))]
    visit = [True] + [False] * (N - 1)

    mymin = 9999
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                result = board[i][j]

                visit[j] = True
                if j == i:


