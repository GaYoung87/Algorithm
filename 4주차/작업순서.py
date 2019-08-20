for t in range(1):
    v, e = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[] for i in range(v + 1)]
    visit = [None] + [0] * v

    for k in range(0, len(data), 2):
        adj[data[k]].append(data[k + 1]) 
        visit[data[k + 1]] += 1
    # print(adj)    # [[], [2, 5], [3], [], [1], []]
    # print(visit)  # [None, 1, 1, 1, 0, 1]

    for i in 