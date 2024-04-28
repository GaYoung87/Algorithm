def solution(s):
    num = 0
    for i in s:
        if i == '(':
            num += 1
        if i == ')':
            num -= 1
        if num < 0:
            return False

    if num == 0:
        return True
    elif num > 0:
        return False
