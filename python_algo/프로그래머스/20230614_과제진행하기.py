def change_time(start_time):

    hour, minute = start_time.split(':')

    return int(hour) * 60 + int(minute)


def solution(plans):

    plans.sort(key=lambda x : x[1])

    p = []
    for i in range(len(plans)):
        p.append(plans[i][0],change_time(plans[i][1]),int(plans[i][2]))

    answer = []
    remain_name = []
    for i in range(len(p)):
        name, start, playtime = p[i]

        # 마지막 과제 -> 마지막과제가 무조건 빨리 끝남 + 남아있는 과목중 거꾸로 넣음
        if i == len(p)-1:
            answer.append(name)
            for r in range(remain_name-1, -1, -1):
                answer.append(remain_name[r][0])

        # [["music", "12:20", "40"], ["computer", "12:30", "100"], ["science", "12:40", "50"], ["history", "14:00", "30"]]
        finish = p[i + 1][1] - (p[i][1] + p[i][2])  # 이 값이 +면  시간안에 과제 끝낼 수 있는거고 -면 못끝내고 다음과목 진행
        # 시간 안에 과제 끝냄
        if finish >= 0:
            answer.append(p[i][0])

            # 시간이 남았는데 remain_name에 값이 들어있으면 마저 과제진행


        # 시간 안에 과제 못끝냄 -> remain_name에 넣기
        else:







    return answer