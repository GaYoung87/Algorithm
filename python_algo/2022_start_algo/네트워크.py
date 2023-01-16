# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]  # 2
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]  # 1

from collections import deque

def solution(n, computers):
    visit = [0 for _ in range(n)]
    answer = 0
    for i in range(n):
        if visit[i] == 0:
            answer += 1
            visit[i] = 1
            q = deque([])
            q.append(i)

            while q:
                computer = q.popleft()
                for j in range(n):
                    if j != computer and computers[computer][j] == 1 and visit[j] == 0:
                        q.append(j)
                        visit[j] = 1

    return answer

