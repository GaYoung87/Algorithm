from collections import deque

def solution(maps):
    answer = []

    near = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visit[i][j] == 0:
                q = deque([i, j])
                visit[i][j] = 1

                cnt = 0
                while q:
                    nx, ny = q.popleft()
                    cnt += int(maps[nx][ny])

                    for dx, dy in near:
                        if 0 <= nx+dx < len(maps) and 0 <= ny+dy < len(maps[0]) and  maps[nx+dx][ny+dy] != 'X' and visit[nx+dx][ny+dy] == 0:
                            q.append((nx+dx, ny+dy))
                            visit[nx+dx][ny+dy] = 1

                if cnt > 0:
                    answer.append(cnt)

    if answer:
        answer.sort()
    else:
        answer = [-1]

    return answer