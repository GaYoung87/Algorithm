def solution(n, computers):
    cnt = 0
    visit = [0 for i in range(n)]
    def dfs(computers, visit, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visit[j] == 0:
                visit[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visit[i] == 0:
                    stack.append(i)
    start=0
    while 0 in visit:
        if visit[start] ==0:
            dfs(computers, visit, start)
            cnt += 1
        start += 1
    # print(cnt)
    return cnt

# n = 3  # 2
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n = 3  # 1
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
