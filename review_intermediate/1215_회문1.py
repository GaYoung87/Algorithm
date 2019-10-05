def is_p(arr):
    for i in range(N // 2):
        if arr[i] != arr[-1 - i]:
            return False
    return arr

for t in range(10):
    N = int(input())
    board = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8 - N + 1):
            result = board[i][j:j + N]
            if is_p(result):
                cnt += 1

    board_re = list(map(list, zip(*board)))
    for i in range(8):
        for j in range(8 - N + 1):
            result = board_re[i][j:j + N]
            if is_p(result):
                cnt += 1
    print('#{} {}'.format(t+1, cnt))