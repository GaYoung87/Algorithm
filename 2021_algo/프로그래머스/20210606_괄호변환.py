def balance(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    
    if cnt == 0:
        return True
    return False

def correct(p):
    left = 0
    right = 0

    for i in p:
        if i == '(':
            left += 1
        else:
            right += 1

        if left < right:
            return False
    return True

def divide(p):
    for i in range(1, len(p) + 1):
        if balance(p[:i]):
            u, v = p[:i], p[i:]
            return u, v

def solution(p):

    if p == '':  # 1번
        return ''

    u, v = divide(p)  # 2번

    if correct(u):
        return u + solution(v)


#   4-4. u의 첫 번째와 마지막 문자를 제거하고,
#  나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:len(u)-1]
        for word in u:
            if word == '(':
                answer += ')'
            else:
                answer += '('

    return answer



# p = "(()())()"  # "(()())()"
# p = ")("  # "()"
p = "()))((()"  # "()(())()"

print(solution(p))