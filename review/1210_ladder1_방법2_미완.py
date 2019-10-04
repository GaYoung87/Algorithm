9iifor t in range(1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(10)]

    j = board[9].index(2)  # y값

    for i in range(9, 0, -1):  # x값
        if j != 0 and board[i][j-1] == 1:
            while j > 0 and board[i][j-1] == 1:
                j -= 1

        elif j != 9 and board[i][j+1] == 1:
            while j < 9 and board[i][j+1] == 1:
                j += 1

    print(j)
