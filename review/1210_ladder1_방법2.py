for t in range(10):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    j = board[99].index(2)

    for i in range(99, 0 , -1):
        if j != 0 and board[i][j-1]:
            while j > 0 and board[i][j-1]:
                j -= 1
