for t in range(int(input())):
    V, E = map(int, input().split())
    data = []
    for e in range(E):
        data.append(list(map(int, input().split())))
        # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    start, end = map(int, input().split())
    visit = []
    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        adj[data[i][0]].append(data[i][1])
        adj[data[i][1]].append(data[i][0])

''' 방법1 '''
    cnt = 0
    queue = [start, -1]  # 연관 없는 숫자(-1)를 넣어서 -1이 나올 때마다 cnt += 1

    while queue:
        node = queue.pop(0)
        if node == end:
            break

        if node not in visit and node != -1:
            visit.append(node)
            queue.extend(adj[node])

        elif node == -1:
            queue.append(node)
            cnt += 1
            if queue[0] == -1:  # 이걸 하는 이유는?
                cnt = 0
                break

    print('#{} {}'.format(t + 1, cnt))

''' 방법2 '''
    queue = [(start, 0)]  # 이때, 0은 cnt

    while queue:
        node = queue.pop(0)
        rs = node[1]  # cnt를 print 하기위해
        if node[0] == end:
            result = rs
            break

        for r in adj[node[0]]:  # 1 -> 4, 3
            if r not in visit:
                visit.append(r)
            queue.append((r, rs + 1))

    print('#{} {}'.format(t + 1, result))
