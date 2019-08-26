for t in range(10):
    n = int(input())
    board = []
    result = []
    sum_num_l = 0
    sum_num_r = 0

    for i in range(100):   # board와 board_re 만들기
        board.append(list(map(int, input().split())))
    # print(board)
        board_re = list(zip(*board))
    # print(board_re)
    for k in board:  # 가로에서 합 구하기
        result += [sum(k)]
    for j in board_re:  # 세로에서 합 구하기
        result += [sum(j)]
    for l in range(len(board)):  # 대각선 합 구하기
        sum_num_l += board[l][l]  # 왼쪽부터 시작
        sum_num_r += board[-1-l][l]  # 오른쪽부터 시작
    result += [sum_num_l, sum_num_r]

    print('#{0} {1}'.format(n, max(result)))


# 값을 저장하지 말고, 이미 저장되어있던 max값과 비교해서 갈아엎기!!
# import sys
# sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    max = sum = 0
    for i in range(100):
        for j in range(100):
            sum += array[i][j]
        if max < sum : max = sum
        sum = 0

    for i in range(100):
        for j in range(100):
            sum += array[j][i]
        if max < sum : max = sum
        sum = 0

    for i in range(100):
        sum += array[i][i]
        if max < sum: max = sum
        sum = 0

    for i in range(100):
        sum += array[i][99 - i]
        if max < sum: max = sum

    print("#%d %d" %(tc, max))