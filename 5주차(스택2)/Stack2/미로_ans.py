def is_ok()


def find_map(startY, startX):   # 재귀함수

    global result

    # 1. 종료조건
    if mymap[startY][startX] == 3:
        result = 1
        return  # 검색 종료

    # 2. 반복검색
    # 4방향 검색 / 테두리 벗어나지 않고 가보지 않은 곳!
    if is_ok(startY, startX + 1):
        find_map(startY, startX + 1)   # 우측
    elif is_ok(startY + 1, startX):
        find_map(startY + 1, startX)   # 아래
    elif is_ok(startY, startX - 1):
        find_map(startY, startX - 1)   # 좌측
    elif is_ok(startY - 1, startX):
        find_map(startY - 1, startX)   # 위

for t i range(1, int(input())):
    n = int(input())
    mymap = []
    for i in range(n):
        row_list = list(map(int, list(input())))