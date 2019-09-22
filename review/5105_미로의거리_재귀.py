near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(a, b, cnt = 0):
    global answer
    while queue:
        x, y, result = queue.pop(0)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < N:
                # 3. 0을 지나면서 cnt += 1 해주지만, 3에 도달하면 그 cnt print한다.
                if board[xi][yi] == 0:
                    board[xi][yi] = 1
                    bfs(xi, yi, result + 1)
                elif board[xi][yi] == 3:
                    # 3-1 도달하면 break -> 이것을 flag로 제어
                    return result
        return 0


for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    flag = 0
    answer = 0
    queue = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                rs = bfs(i, j)

    print(rs)
