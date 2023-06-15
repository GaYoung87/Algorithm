def solution(name, yearning, photo):
    name_dict = {}
    for i in range(len(name)):
        name_dict[name[i]] = yearning[i]

    # print(name_dict)

    answer = []
    for i in range(len(photo)):
        score = 0
        for n in photo[i]:
            if n in name_dict:
                score += name_dict[n]

        answer.append(score)

    return answer