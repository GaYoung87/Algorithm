from collections import deque


def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(q1), sum(q2)
    cnt = 0
    # while q1 and q2:  # q1, q2 <= 300,000이니까 while문 말고 for문으로 변경
    for i in range(300000):
        if q1_sum == q2_sum:
            return cnt
        elif q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
            cnt += 1
        else:
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num
            cnt += 1

    return -1