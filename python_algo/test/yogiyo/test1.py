def check(word2):
    word2.lower()
    answer = ''
    for i in word2:
        if i != '-':
            answer += i

    if len(answer) <= 8:
        return answer
    else:
        return answer[:8]

def solution(S, C):
    back = '@' + C.lower() + '.com; '
    answer = ''
    people = S.split(";")
    check_num = {}
    for i in people:
        first, last = '', ''
        if len(i.split()) == 2:
            first, last = i.split()
            last = check(last)
        else:
            first, middle, last = i.split()
            last = check(last)

        first, last = first.lower(), last.lower()

        if (first, last) not in check_num:
            check_num[(first, last)] = 1
            answer += first+'.'+last+back
        else:
            check_num[(first, last)] += 1
            answer += first+'.'+last+str(check_num[(first, last)])+back
    return answer[:len(answer)-2]

