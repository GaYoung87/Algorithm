from collections import deque

def solution(numbers, target):

    answer = 0
    # 1 -> 0 -> -1 ->..
    #        ->  1
    #   -> 2
    q = deque([numbers[0], 0], (-1)*[numbers[0], 0])  # [첫번째 숫자, number갯수]
    n = len(numbers)

    while q:
        num, time = q.popleft()
        time += 1

        if time < n:
            q.append([num + numbers[time], time])
            q.append([num - numbers[time], time])

        else:
            if num == target:
                answer += 1
    print(q)
    return answer