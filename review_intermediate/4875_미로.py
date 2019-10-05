for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input())))

    stack = []
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                stack.append((i, j))
                while stack:
                    x, y = stack.pop()
                    for a, b in near:
                        xi, yi = (x + a, y + b)
                        if 0 <= xi < N and 0 <= yi < N:
                            if board[xi][yi] == 0:
                                stack.append((xi, yi))
                                board[xi][yi] = 1
                            if board[xi][yi] == 3:
                                result = 1
                                break
    print('#{} {}'.format(t+1, result))
