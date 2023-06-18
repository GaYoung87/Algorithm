# start ~ 레버, 레버 ~ end 두번 bfs돌기

from collections import deque

def bfs(start, end, maps):
    near = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]
    q = deque([])

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:
                q.append([i, j, 0])
                visit[i][j] = 1

                while q:
                    nx, ny, cnt = q.popleft()

                    if maps[nx][ny] == end:
                        return cnt

                    for dx, dy in near:
                        if 0 <= nx + dx < len(maps) and 0 <= ny + dy < len(maps[0]) and maps[nx + dx][ny + dy] != 'X' and visit[nx + dx][ny + dy] == 0:
                            q.append((nx + dx, ny + dy, cnt+1))
                            visit[nx + dx][ny + dy] = 1

    return -1


def solution(maps):
    answer = 0

    s_bfs = bfs('S', 'L', maps)
    l_bfs = bfs('L', 'E', maps)

    if s_bfs != -1 and l_bfs != -1:
        return s_bfs + l_bfs

    return -1
