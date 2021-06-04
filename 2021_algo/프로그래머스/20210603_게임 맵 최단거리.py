from collections import deque

def solution(maps):
    r = len(maps)
    c = len(maps[0])
    visit = [[-1 for _ in range(c)] for _ in range(r)]

    near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([[0, 0]])
    visit[0][0] = 1
    while q:
        y, x = q.popleft()

        for a, b in near:
            yi, xi = y + a, x + b

            if 0 <= yi < r  and 0 <= xi < c and maps[yi][xi] == 1:
                if visit[yi][xi] == -1:
                    visit[yi][xi] = visit[y][x] + 1
                    q.append([yi, xi])

    return visit[-1][-1]



maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]  # 11
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]  # -1
