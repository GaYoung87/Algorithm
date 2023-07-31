def solution(survey, choices):
    answer = ''
    mbti = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}

    for i in range(len(survey)):
        if survey[i] in mbti:
            mbti[survey[i]] += choices[i] - 4
        else:
            survey[i] = survey[i][::-1]
            mbti[survey[i]] -= choices[i] - 4

    for m in mbti:
        if mbti[m] > 0:
            answer += m[1]
        else:
            answer += m[0]

    return answer