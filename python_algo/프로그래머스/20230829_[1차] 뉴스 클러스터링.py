def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1_ls = []
    str2_ls = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_ls.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_ls.append(str2[i:i + 2])

    str1_l = str1_ls.copy()
    str2_l = str2_ls.copy()

    common_ls = []
    # common, total = 0, 0
    for word in str1_ls:
        if word in str2_l:
            common_ls.append(word)
            str1_l.remove(word)
            str2_l.remove(word)
    print(common_ls)
    print(str1_l)
    print(str2_l)
    # 교집합, 합집합 구하기
    common = len(common_ls)
    total = len(common_ls) + len(str1_l) + len(str2_l)

    if len(str1_l) == 0 and len(str2_l) == 0:
        return 65536
    else:
        return int(common / total * 65536)