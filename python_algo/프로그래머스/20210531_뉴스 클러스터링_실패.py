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

    # 1) 실패: set를 이용해 교집합, 합집합을 선택하면 중복되는 것은 제거됨
    # gyo = set(first_ls) & set(second_ls)
    # hap = set(first_ls) | set(second_ls)
    # print(gyo)

    # 2) 실패: 직접 합집합 만들기
    gyo = []
    
    if len(first_ls) > len(second_ls):
        for i in second_ls:
            gyo.append(i)
            first_ls.remove(i)
    else:
        for i in first_ls:
            gyo.append(i)
            second_ls.remove(i)
    print('gyo')
    print(gyo)
    hap = first_ls + second_ls
    print('hap')
    print(hap)
    # 합집합이 0이면 65536 출력 
    if len(hap) == 0:
        return 65536

    return int(len(gyo) / len(hap) * 65536)


# str1 = 'FRANCE'
# str2 = 'french'  # 16384
# str1 = 'handshake'
# str2 = 'shake hands'  # 65536
# str1 = 'aa1+aa2'
# str2 = 'AAAA12'  # 43690
str1 = 'E=M*C^2'
str2 = 'e=m*c^2'  # 65536

print(solution(str1, str2))