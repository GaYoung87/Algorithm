# def solution(s):
s = 'baabaa'

def solution(s):
    i = 0
    while i < len(s) - 1:
        if s[i] != s[i + 1]:
            i += 1
            
        else:
            s = s[:i] + s[i + 2:]
            i = 0
    
    if len(s) == 0:
        return 1
    return 0

print(solution(s))