for t in range(1, int(input()) + 1):
    N = int(input())
    board = []
    stack = []
    visit = []
    for n in range(N):
        board.append(list(map(int, input().split())))
        visit += [[False] * N]
    
    # for i in range(N):
    #     for j in range(N):
    stack.append(0)
    stack.append(0)
# print(stack)
    # while stack:
    for x in range(N):
        for y in range(N):
            if x == 0:
                visit[x][y] = True
            if y == 0:
                visit[x][y] = True

    print(stack)
    print(visit)
