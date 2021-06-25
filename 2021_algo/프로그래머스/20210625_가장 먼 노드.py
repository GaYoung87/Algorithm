from collections import deque

def solution(n, edge):
    check = [[] for _ in range(n+1)]
    for start, end in edge:
        check[start].append(end)
        check[end].append(start)

    q = deque([[1, 0]])
    visit = [-1] * (n+1)
    while q:
        node, cnt = q.popleft()
        if visit[node] == -1:
            visit[node] = cnt

            for i in check[node]:
                q.append([i, cnt+1])

    mymax = max(visit)
    answer = 0
    for v in visit:
        if v == mymax:
            answer += 1
    # print(answer)
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]




