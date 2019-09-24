def game(x, sum):
    global mymin

    if x == N:
        # x == N-1이 아닌 이유: 밑에서 game(x+1, sum+board[x][n])를 해주기때문에
        # N=3이면 원래 x는 0~2까지이지만 x+1을 해주기때문에
        # x=3일 때, 더이상 visit 작업을 하지 않고, stop 한다
        if mymin > sum:
            mymin = sum
            return

    if mymin < sum:  # 이것이 backtracking! sum이 기존 최저보다 작으면 가다가 말고 stop!
        return

    for i in range(N):
        if visit[i] == False:
            visit[i] = True
            game(x + 1, sum + board[x][i])
            visit[i] = False


for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    visit = [False] * N
    mymin = 999999999

    game(0, 0)

    print('#{} {}'.format(t+1, mymin))