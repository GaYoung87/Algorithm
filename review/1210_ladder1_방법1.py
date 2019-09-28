def ladder(x, y):
    if x == 0:
        return y

    else:
        if y == 0:
            if board[x][y + 1] == 1:
                board[x][y] = -1
                y += 1
            elif board[x - 1][y] == 1:
                board[x][y] = -1
                x -= 1
            a = ladder(x, y)
            if a:
                return a
       # return을 해야하는 이유!
       # return을 하지 않으면, 전에 값이 저장되지 않고, None으로 받아진다.
       # ladder(x, y)는 그 전의 y를 받아온다. 저장하지 않고, 그 다음 단계를 나아가면 None!  -> 개념에 정리!
        elif y == 99:
            if board[x][y - 1] == 1:
                board[x][y] = -1
                y -= 1
            elif board[x - 1][y] == 1:
                board[x][y] = -1
                x -= 1
            a = ladder(x, y)
            if a:
                return a

        elif y != 0 and y != 99:
            if board[x][y - 1] == 1:
                board[x][y] = -1
                y -= 1
            elif board[x][y + 1] == 1:
                board[x][y] = -1
                y += 1
            elif board[x - 1][y] == 1:
                board[x][y] = -1
                x -= 1
            a = ladder(x, y)
            if a:
                return a

for t in range(1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    a = 99
    b = board[-1].index(2)  # 9

    print('#{} {}'.format(t + 1, ladder(a, b)))

'''
[ for문 사용 불가! ]
    for i in range(10):
        for j in range(10):
            if board[i][j] == 2:
                result = ladder(i, j)
    why? for문 돌리면 result 값이 나와도 계속 돌림!!
'''
