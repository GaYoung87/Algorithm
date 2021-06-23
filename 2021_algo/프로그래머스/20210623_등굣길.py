def solution(m, n, puddles):
    # puddles = 0
        # 더해나갈 때 그대로 더하고, paddles인 경우 pass
    # puddles = -1 (웅덩이 표현)
        # 더해나갈 때 0으로 간주하고 진행해야함
    near = [(0, 1), (1, 0)]
    board = [[0] * (m+1) for _ in range(n+1)]
    board[1][1], board[n][m] = 1, 1

    # n, m으로 시작하면 문제점: x=0, y=0인 경우 더할 수 없음
    # x ~ 1, n+1, y ~ 1, m+1로 두면 다 0으로 들어가므로 괜찮아짐
    for x in range(1, n+1):
        for y in range(1, m+1):
            if [y, x] in puddles:
                continue
            if y == 1 and x == 1:  # 시작점 제외
                continue
            board[x][y] = board[x][y-1] + board[x-1][y]
    #print(board[n][m] % 1000000007)
    
    return board[n][m] % 1000000007

m = 4
n = 3
puddles = [[2, 2]]  # 4

