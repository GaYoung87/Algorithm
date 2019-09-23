text = 'a pattern matching algorithm'
pattern = 'rithm'
s = pattern[::-1]  # mhtir 으로 나온다
skip = list(range((len(pattern))))  # m = 0, h = 1, t = 2, i = 3, r = 4 => [0, 1, 2, 3, 4]

i = len(pattern)-1  # 4 -> 인덱스
result = 0

while i < len(text):  # i가 len(text)보다 작아야지 찾으러갈 수 있음
    nxt = len(s)  # 5
    j = 0
    if s[j] == text[i]:  # ex. m == m
        while j < len(s):  # len(s) = 5 -> mhtir이 돌아감
            if s[j] != text[i-j]:
                nxt = nxt - j
                break  # s[j] != text[i-j] 이면 while문 끝
            j += 1  # 새로시작해야하니까 j += 1 해주기
        if j == len(s):
            result = 1        #### 큰 if문에 조건문 추가하고 맨 밑에 i += nxt 바꾸기
    else:
        while j < len(s):  #ex. m == t
            if s[j] == text[i]:
                nxt = min(j, nxt)
                break
            j += 1
    if result:
        break
    i += nxt

print(result)