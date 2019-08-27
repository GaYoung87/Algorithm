for t in range(1, int(input()) + 1):
    N = int(input())
    board = []
    stack = []
    visit = []
    for n in range(N):
        board.append(list(map(int, input().split())))
        visit += [[False] * N]
    print(visit)