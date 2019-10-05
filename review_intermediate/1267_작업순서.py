for t in range(10):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[] for i in range(V + 1)]
    visit = [None] + [0] * V

    for i in range(0, len(data), 2):
        adj[data[i]].append(data[i + 1])
        visit[data[i + 1]] += 1

    stack = []
    result = ''
    for i in range(1, V + 1):
        stack.append(i)
        while stack:
            node = stack.pop()
            if visit[node] > 0:
                visit[node] -= 1
            elif visit[node] == 0:
                visit[node] = 'X'
                result += str(node) + ' '
                stack.extend(adj[node])

    print('#{} {}'.format(t + 1, result))

