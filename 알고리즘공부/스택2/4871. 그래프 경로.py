import sys
sys.stdin = open("4871input.txt", "r")

def search_map(start):  # 행 번호
    visited[start] = 1  # 방문한 곳은 1
    for next in range(1, mynode + 1):
        if mymap[start][next] == 1 and visited[next] == 0:
            if next == end_node:
                result = 1  # 갈 수 있는 곳
                return  # 검색 중단
            search_map(next)  # 다음 노드로 가서 검색


TC =int(input())
for tc in range(1, TC + 1):
    mynode, myline = map(int, input().split())
    mymap = [[0] * (mynode + 1) for _i in range(mynode + 1)]  # 2차원 배열 맵

    for i in range(myline):
        start_node, end_node = map(int, input().split())
        mymap[start_node][end_node] = 1

    start_node, end_node = map(int, input().split())
    visited = [0] * (mynode + 1)  # 방문 했던 곳 표시용
    result = 0

    search_map(start_node)  # 재귀함수
    print('#{} {}'.format(tc, result))


