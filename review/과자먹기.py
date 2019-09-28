'''
[ 문제 분석 시 ]
1. 무조건 상하좌우로 이동한다고 near 사용 X
  -> 상하좌우로 이동한다는 것은 대각선으로 갈 수 없다는 것!!
2. 반복해서 로봇을 이동시킨다 -> 반복하면 for, while문 사용!
3. 이동거리의 합 중 최솟값 -> 최소합(백트래킹)
'''


'''
이 문제는 치킨배달과 동일!!!!
'''

'''
func함수 생성할 때, for문해서 반복적으로 도는 재귀함수를 먼저 짜고, 그 후에 재귀를 빠져나오는 조건 작성!
'''
def func(x, sum=0):
    global mymin

    if x == 6:
        if mymin > sum:
            mymin = sum
            return

    if mymin < sum:
        return

    for i in range(6):
        if not visit[i]:
            visit[i] = True
            func(x + 1, sum + ls_t[x][i])
            visit[i] = False


for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(10)]

# 상하좌우로 이동한다고 무조건 near 쓸 필요가 없다!
# 1. 로봇 6개, 과자 6개가 있을 때, 로1-과1~로1-과6, ~, 로6-과1~로6과6까지 모든 경우의 수를 구한다.
# 2. 로봇1~6의 각각 과자먹는 경우에서 최소합을 구하면 ok

    robot = []
    snack = []
    for i in range(10):
        for j in range(10):
            if board[i][j] == 9:
                robot.append((i, j))
            elif board[i][j] != 0:
            # 이때, elif board[i][j] != 0 and board[i][j] != 9:라고 안써도 된다.
            # 이미 if문에서 9가 아니기 때문에 elif문으로 내려온 것이기 때문이다.
                snack.append((i, j))

    ls_t = []
    for r in robot:
        ls = []
        for s in snack:
            a = abs(r[0] - s[0]) + abs(r[1] - s[1])  # 로봇과 과자의 거리
            ls.append(a)
        ls_t.append(ls)

    # 최소합 구하기 -> func함수
    visit = [False] * 6
    mymin = 99999999999
    func(0)
    print(mymin)