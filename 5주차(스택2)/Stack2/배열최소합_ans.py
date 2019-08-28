TC = int(input())

def find_min(row):  # 단계 별로 값을 누적하여 누적한 값이 최소값 보다 같거나 크면 다음단계로 내려가지 않음

    global submin, my_min

    if submin > my_min:  # 맨 우측까지 왔으면
        return   # 누적중인 값이 최소보다 크면 하위 검색 중단
    if row == n:  # 맨 아래까지 니려왔으면
        if submin < my_min:  # 누적값이 최소값보다 작으면 최소값 갱신
            my_min = submin
        return   # 더 이상 내려가지 않음


    for x in range(n):
        if visited[x] == 0:
            visited[x] = 1
            submin += my_min[row][x]  # 최소값 누적변수에 누적
            find_min(row + 1)
            visited[x] = 0
            submin -= mymap[row][x]


for tc in range(1,TC + 1):
    n = int(input())
    mymap = [list(map(int, input().split())) for i in range(n)]
    visited = [0] * n
    my_min = 9 * N
    submin = 0
    find_min(0):