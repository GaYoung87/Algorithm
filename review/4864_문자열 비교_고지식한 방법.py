for t in range(int(input())):
    str1 = input()  # ['X', 'Y', 'P', 'V']
    str2 = input()
    N = len(str1)
    M = len(str2)

    rs = 0
    for m in range(M - N + 1):
        result = ''
        result += str2[m:m+len(str1)]

        if result == str1:
            rs = 1

    print('#{} {}'.format(t+1, rs))