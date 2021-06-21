from collections import deque

def solution(N, road, K):
    nodes = {}
    dist = { i:float('inf') if i != 1 else 0 for i in range(1, N+1) }
    for v1, v2, d in road:
        if v1 in nodes:
            nodes[v1].append((v2, d))
        else:
            nodes[v1] = [(v2, d)]
        if v2 in nodes:
            nodes[v2].append((v1, d))
        else:
            nodes[v2] = [(v1, d)]

    q = deque([1])
    while q:
        now_node = q.popleft()
        for next_node, d in nodes[now_node]:
            if dist[next_node] > dist[now_node] + d:
                dist[next_node] = dist[now_node] + d
                q.append(next_node)

    cnt = 0
    for key, d in dist.items():
        if d <= K:
            cnt += 1
    # print(cnt)

    return cnt

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3  # 4
# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4  # 4


# {1: [(2, 1), (4, 2)], 2: [(1, 1), (3, 3), (5, 2)],
#  3: [(2, 3), (5, 1)], 5: [(2, 2), (3, 1), (4, 2)], 
#  4: [(1, 2), (5, 2)]}

