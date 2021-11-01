def solution(record):
    answer = []
    # 한번에 이름변경하고, print하는거 동시에 못한다
    # 1. 이름 확인 dictionary 만들기
    check = {}
    for i in record:
        if i.split()[0] == 'Enter' or i.split()[0] == 'Change':
            check[i.split()[1]] = i.split()[2]

    # 2. print하기
    for i in record:
        if i.split()[0] == 'Enter':
            answer.append(check[i.split()[1]]+'님이 들어왔습니다.')
        elif i.split()[0] == 'Leave':
            answer.append(check[i.split()[1]]+'님이 나갔습니다.')
    
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
          "Enter uid1234 Prodo","Change uid4567 Ryan"]

