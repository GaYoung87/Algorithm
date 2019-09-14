for t in range(int(input())):
    V, E = map(int, input().split())
    path = []
    for e in range(E):
        data = list(map(int, input().split()))
        path.append(data)
    start, end = map(int, input().split())
    visit = [False] * (V + 1)
    adj = [[] for _ in range(V + 1)]

    for p in path:
        adj[p[0]].append(p[1])  # [[], [4, 3], [3, 5], [], [6], [], []]

    result = 0
    stack = [start]
    visit[start] = True
    while stack:
        node = stack.pop()
        if visit[node] == False:
            visit[node] = True
            if visit[end]:
                result = 1
                break
        stack.extend(adj[node])
    print('#{} {}'.format(t + 1, result))