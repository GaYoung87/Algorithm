def is_p(arr):
    for i in range(len(arr) // 2):
        if arr[i] != arr[-1 -i]:
            return False
    return len(arr)


for t in range(1):
    N = int(input())
    board = [list(input()) for _ in range(100)]
    board_re = list(map(list, zip(*board)))
    # 가로
    mymax = 0
    for b in board:  # board에서 한 줄씩 뽑기
        for i in range(100, 1, -1):  # 회문길이
            for j in range(101 - i):
                result = b[j:j + i]
                if mymax < is_p(result):
                    mymax = is_p(result)

    # 세로
    for b in board_re:
        for i in range(mymax, 100):
            for j in range(101 - i):
                result = b[j:j + i]
                if mymax < is_p(result):
                    mymax = is_p(result)

    print('#{} {}'.format(t + 1, mymax))