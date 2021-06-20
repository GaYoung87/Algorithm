def solution(N, road, K):
    answer = 0

    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3  # 4
# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4  # 4

from collections import deque


nodes = {}
dist = { i:float('inf') for i in range(1, N+1) }
for v1, v2, d in road:
    nodes[v1] = nodes.get(v1, []) + [(v2, d)]
    nodes[v2] = nodes.get(v2, []) + [(v1, d)]
que = deque([1])
print(nodes)                                                                                                                                               