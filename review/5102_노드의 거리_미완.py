for t in range(int(input())):
    V, E = map(int, input().split())
    data = []
    for e in range(E):
        data.append(list(map(int, input().split())))
        # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    start, end = map(int, input().split())
    visit = []
    adj = [[] for _ in range(V + 1)]
    print(adj)
    for i in range(E):
        adj[data[i][0]].append(data[i][1])
        adj[data[i][1]].append(data[i][0])

    cnt = 0
    queue = [start]  # 1
    while queue:
        node = queue.pop(0)  # 1
        if node not in visit: # visit에 1이 없다면
            visit.append(node)  # visit = [1]
            queue.append(adj[node])

