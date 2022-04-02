s = "aabbaccc"  # 7
# s = "ababcdcdababcdcd"  # 9
# s = "abcabcdede"  # 8
# s = "abcabcabcabcdededededede"  # 14
# s = "xababcdcdababcdcd"  # 17

def solution(s):
    mymin = 99999999999999999999999999
    answer = ''

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        front = s[:i]

        for j in range(i, len(s), i):  # 압축문자 갯수만큼 띄어진 다음칸을 봐야함
            back = s[j:j+i]
            if front == back:
                cnt += 1
            else:
                if cnt == 1:
                    answer += front
                else:
                    answer += str(cnt) + front

                front = back
                cnt = 1  # 새로 시작하기

        # 마지막 값 넣어야함
        if cnt == 1:
            answer += front
        else:
            answer += str(cnt) + front

        if mymin > len(answer):
            mymin = len(answer)

        answer = ''

    return mymin