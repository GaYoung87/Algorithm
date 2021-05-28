s = "aabbaccc"  # 7
s = "ababcdcdababcdcd"  # 9
s = "abcabcdede"  # 8
s = "abcabcabcabcdededededede"  # 14
s = "xababcdcdababcdcd"  # 17

def solution(s):
    mymin = 999999999999999999
    
    answer = ''
    
    if len(s) == 1:  # s = 'a'인 경우는 그냥 바로 결과 낼 수 있음
        return 1
    
    for i in range(1, len(s) // 2 + 1):  # 압축문자갯수는 전체문자의 반까지만 봐도 됨
        cnt = 1  # 압축되는 문자갯수 세기
        front = s[:i]
        
        for j in range(i, len(s), i):  # 압축문자 갯수만큼 띄어진 다음칸을 봐야함
            back = s[j:j+i]
            if back == front:  # 압축 가능하면
                cnt += 1
            else:  # 압축 불가능하면
                if cnt == 1:
                    cnt = ''  # cnt에 상관없게 answr에 더해줄 수 있도록 진행
                answer += str(cnt) + front
                front = back  # 새로 시작할 수 있게 판깔기(1)
                cnt = 1  # 새로 시작할 수 있게 판깔기(2)
        
        # 마지막 부분의 값을 answer에 포함시키기 위해 진행
        if cnt == 1:
            cnt = ''  # cnt에 상관없게 answr에 더해줄 수 있도록 진행
        answer += str(cnt) + front  # for문 돌때마다
    
        if mymin > len(answer):
            mymin = len(answer)
        
        answer = ''  # for문을 돌 때마다 answer가 새로시작할 수 있도록 판깔기
        
    return mymin
