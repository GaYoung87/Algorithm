s = "[](){}"  # 3
# s = "}]()[{"  # 2
# s = "[)(]"  # 0
# s = "}}}"  # 0

def check(s):
    temp = []
    for word in s:
        if word in ['[', '(', '{']:
            temp.append(word)
        else:
            if not temp:  # temp에 값이 없으면
                return False
            # temp에 값이 들어있으면
            x = temp.pop()
            if word == ']' and x != '[':
                return False
            elif word == ')' and x != '(':
                return False
            elif word == '}' and x != '{':
                return False
    if temp:  # temp에 값이 들어있으면
        return False

    return True

def solution(s):
    cnt = 0
    for i in range(len(s)):
        s = s[1:] + s[0]

        if check(s):
            cnt += 1

    return cnt
