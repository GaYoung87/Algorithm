def solution(today, terms, privacies):
    answer = []

    terms_dict = {}
    for term in terms:
        a, b = term.split(" ")
        terms_dict[a] = int(b)

    t_yyyy, t_mm, t_dd = today.split(".")

    for i in range(len(privacies)):
        day, types = privacies[i].split(" ")
        yyyy, mm, dd = map(int, day.split("."))
        mm += terms_dict[types]

        if mm % 12 == 0:
            yyyy += (mm // 12) - 1
            mm = 12
        else:
            yyyy += (mm // 12)
            mm = mm % 12

        # 05.02 이런식으로 바꿔야함
        yyyy, mm, dd = str(yyyy), str(mm), str(dd)
        if len(mm) == 1:
            mm = '0' + mm
        if len(dd) == 1:
            dd = '0' + dd

        if int(t_yyyy + t_mm + t_dd) >= int(yyyy + mm + dd):
            answer.append(i + 1)

    return answer