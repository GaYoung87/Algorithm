near = [(0, 1), (-1, 0), (0, -1)]
for t in range(1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(10)]

    start = board[9].index(2)  # 9

    for i in range(10):
        for j in range(10):
            if board[i][j] == 2:
                queue = [(i, j)]
                board[i][j] = 0
                while queue:
                    x, y = queue.pop(0)
                    for a, b in near:
                        xi, yi = (x + a, y + b)
                        if 0 <= xi < 10 and 0 <= yi < 10:
                            if board[xi][yi] == 1:
                                queue.append((xi, yi))
                                board[xi][yi] = 0


