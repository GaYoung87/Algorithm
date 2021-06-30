def solution(people, limit):
    people.sort()

    # 정렬 후, 몸무게가 가장 큰 사람과 
    # 가장 작은 사람의 값을 더해 limit과 비교
    start = 0
    end = len(people) - 1
    cnt = 0
    while start <= end:
        # 구명보트 최대2명만 탈 수 있기때문에 
        # start, end만 더하면 됨
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        cnt += 1

    # print(cnt)

    return cnt

# people = [70, 50, 80, 50]
# limit = 100  # 3
people = [70, 80, 50]
limit = 100  # 3

