# reverse함수
def my_reverse(data):
    result = ''
    for i in data:
        result = i + result
    return result

print(my_reverse('hello ssafy'))


# 선생님 코드
s = 'Reverse this string'
sr = ''
for i in range(len(s)-1, -1, -1):
    sr = sr + s[i]

print(sr)