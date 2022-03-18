def solution(lottos, win_nums):
    answer = []
    return answer



lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]  # [3, 5]
# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]  # [1, 6]
# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]  # [1, 1]

def solution(lottos, win_nums):
    result = [6, 6, 5, 4, 3, 2, 1]
    lottos.sort()
    win_nums.sort()

    cnt = 0
    cnt_zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        if lotto == 0:
            cnt_zero += 1

    answer = [result[cnt+cnt_zero], result[cnt]]

    return answer
