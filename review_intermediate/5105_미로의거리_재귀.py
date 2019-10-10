def dfs(x, y, cnt=0):
    global rs
    if rs != 0:
        return

    for a, b in near:
        xi, yi = (x+a, y+b)
        if 0 <= xi < N and 0 <= yi < N:
            if board[xi][yi] == 0:
                board[xi][yi] = 1
                dfs(xi, yi, cnt+1)
                board[xi][yi] = 0  # 최소합에 있는 것처럼 복구작업!
                                   # 찾았던 길이었지만, 다른길                                                                                                                                                                                                                                                                                과 겹칠 수 있으므로!
                                   # 꼭!!!!해야함!! visit과 마찬가지
            elif board[xi][yi] == 3:
                rs = cnt
                return  # 값은 안나옴 None출력


near = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    rs = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                dfs(i, j)

    print(rs)

'''
<찾았던 길이지만, 다른 길과 겹칠 수 있기때문에 하는 복구작업!> ex. 최소합에있던 것
방법1. ㅜ9ㅑ
'''