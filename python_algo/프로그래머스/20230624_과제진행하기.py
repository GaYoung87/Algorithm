def change_time(start_time):
    hour, minute = start_time.split(':')
    return int(hour) * 60 + int(minute)


def solution(plans):
    p = []
    for i in range(len(plans)):
        p.append([plans[i][0], change_time(plans[i][1]), int(plans[i][2])])

    p.sort(key=lambda x: x[1])
    # [["korean", 700, 30], ["english", 730, 20], ["math", 750, 40]]
    # [["music", 740, 40], ["computer", 750, 100], ["science", 760, 50], ["history", 840, 30]]
    # [["aaa", 720, 20], ["bbb", 730, 30], ["ccc", 760, 10]]
    answer = []
    remain_ls = []
    for i in range(len(p)):
        name, start, playtime = p[i]

        # 마지막일 때 일단 name을 answer에 넣고, remain_name에 남아있는 값들을 거꾸로 넣기
        if i == len(p) - 1:
            answer.append(name)
            for r in range(len(remain_ls) - 1, -1, -1):
                answer.append(remain_ls[r][0])
            break

        else:
            # 시간 안에 과제 끝남
            if p[i + 1][1] >= start + playtime:
                answer.append(name)
                temp_time = p[i + 1][1] - (start + playtime)

                # 시간 안에 과제끝나고 remain_name안에 값이 있으면 확인
                while temp_time != 0 and remain_ls:
                    r_name, r_playtime = remain_ls.pop()
                    if temp_time >= r_playtime:
                        answer.append(r_name)
                    else:
                        remain_ls.append([r_name, r_playtime-temp_time])
                        temp_time = 0

            # 시간 안에 과제 못끝내면 remain_name에 넣기
            else:
                remain_ls.append([name, playtime - (p[i + 1][1] - start)])

    print(answer)
    print(remain_ls)
    return answer