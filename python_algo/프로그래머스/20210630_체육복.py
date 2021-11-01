def solution(n, lost, reserve):
    reserve_n = set(reserve) - set(lost)
    lost_n = set(lost) - set(reserve)

    answer = n - len(lost_n)
    for i in lost_n:
        # 작은거(i-1)부터 채우면 i+1이 있으면 채울 수 있음
        if i - 1 in reserve_n:
            answer += 1
            reserve_n.remove(i-1)
        elif i + 1 in reserve_n:
            answer += 1
            reserve_n.remove(i+1)
    # print(answer)
    return answer


n = 8
lost = [2, 4, 6]
reserve = [3, 5]  # 5
# n = 5
# lost = [2, 4]
# reserve = [3]  # 4
# n = 3
# lost = [3]
# reserve = [1]  # 2
