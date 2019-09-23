# 인덱스([])  : 0 1 2 3 4 5 6 7
# 전체 string : a b b c a a c b
# 부분 string : a b b a

# <비교방법>
# 1. [0]에서 비교 시작 : [3]에서 오류 
# 2. [1]에서 비교 시작
# 전체 string : a b b c a a c b
# 부분 string :   a b b a         비교 시작 -> [0]에서 오류
# 3. [2]에서 비교 시작
# 4. 반복,, => 하나하나 완전탐색하는 것

# <시간복잡도>
# O(n**2)



## 방법 1 ##

part = 'is'
text = 'What is this?'

def compare(text, part):
    t = 0  # total의 인덱스
    p = 0  # part의 인덱스
    while t < len(text) and p < len(part):
        if text[t] != part[p]:
            p = 0
            t += 1
        t += 1
        p += 1
    
    if p == len(part):
        return t - len(part)
    else:
        return -1  # 검색 실패

print(compare(text, part))

## 방법 2 ##

p = 'is'
t = 'What is this?'

M = len(p)
N = len(t)

def B(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i -= j   # 이때 i의 의미는?
            j = -1  # 밑에서 +1을 해주기때문에 다시 [0]으로 돌아감
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return -1

print(B(p, t))