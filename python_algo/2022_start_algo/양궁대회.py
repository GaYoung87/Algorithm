# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]  # [0,2,2,0,1,0,0,0,0,0,0]
n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]  # [-1]
# n = 9
# info = [0,0,1,2,0,1,1,1,1,1,1]  # [1,1,2,0,1,2,2,0,0,0,0]
# n = 10
# info = [0,0,0,0,0,0,0,0,3,4,3]  # [1,1,1,1,1,1,1,1,0,0,2]

from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    mymax = 0
    for temp in list(combinations_with_replacement(range(0, 11), n)):
        lion_now = [0 for _ in range(11)]
        for t in temp:
            lion_now[10 - t] += 1

        lion = 0
        apeach = 0
        for i in range(11):
            l, a = lion_now[i], info[i]

            if l == a == 0:
                continue
            if l > a:
                lion += (10 - i)
            else:
                apeach += (10 - i)

        if lion > apeach:
            if mymax < (lion - apeach):
                mymax = lion - apeach
                answer = lion_now

    if answer == []:
        return [-1]
    return answer
