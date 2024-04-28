from collections import deque


def solution(maps):
    near = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    answer = []

    q = deque()

    for i in range(len(maps)):
        maps[i] = list(maps[i])

    lenx, leny = len(maps), len(maps[0])
    visit = [[0] * leny for _ in range(lenx)]

    for x in range(lenx):
        for y in range(leny):
            if maps[x][y] != 'X' and visit[x][y] == 0:
                q.append([x, y])
                visit[x][y] = 1
                # print(maps[x][y])

                val = 0
                while q:
                    i, j = q.popleft()
                    val += int(maps[i][j])
                    # print(val)

                    for dx, dy in near:
                        if 0 <= i + dx < lenx and 0 <= j + dy < leny and maps[i + dx][j + dy] != 'X' and visit[i + dx][
                            j + dy] == 0:
                            # print('9')
                            visit[i + dx][j + dy] = 1
                            # print([i+dx,j+dy])
                            q.append([i + dx, j + dy])

                answer.append(val)
                # print(val)
                # print(q)
                # print('--------------------------------')
    if answer:
        return sorted(answer)
    else:
        return [-1]
