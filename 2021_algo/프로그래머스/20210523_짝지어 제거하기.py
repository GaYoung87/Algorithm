def solution(s):
    check = []
    for i in s:
        if check:
            if check[-1] == i:
                check.pop()
            else:
                check.append(i)
        
        else:
            check.append(i)

    if check:
        return 0
    return 1