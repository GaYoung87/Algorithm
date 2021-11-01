
# str1 = 'FRANCE'
# str2 = 'french'  # 16384
# str1 = 'handshake'
# str2 = 'shake hands'  # 65536
# str1 = 'aa1+aa2'
# str2 = 'AAAA12'  # 43690
str1 = 'E=M*C^2'
str2 = 'e=m*c^2'  # 65536

def solution(str1, str2):
    # 대문자, 소문자 구분 안함
    str1 = str1.lower()
    str2 = str2.lower()

    first_ls = []
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            first_ls.append(str1[i:i+2])

    second_ls = []
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            second_ls.append(str2[i:i+2])

    if len(first_ls) == 0 and len(second_ls) == 0:
        return 65536

    else:
        gyo = []
        if len(first_ls) > len(second_ls):
            for i in second_ls:
                if i in first_ls:  # 중복이 된다면, 교집합 리스트에 넣고, 한번 제거해준다.
                    gyo.append(i)
                    first_ls.remove(i)
        else:
            for i in first_ls:
                if i in second_ls:
                    gyo.append(i)
                    second_ls.remove(i)

        hap = first_ls + second_ls

        # 합집합이 0이면 65536 출력 
        if len(hap) == 0:
            return 65536

        return int(len(gyo) / len(hap) * 65536)

print(solution(str1, str2))