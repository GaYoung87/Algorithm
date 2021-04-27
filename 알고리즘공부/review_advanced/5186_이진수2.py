for t in range(int(input())):
    num = float(input())

    result = []

    c = -1
    while num > 0 and c > -14:
        if num >= 2 ** c:
            result += ['1']
            num -= 2 ** c

        else:
            result += ['0']
        c -= 1


    if len(result) >= 13:
        result = ['overflow']

    print('#{} {}'.format(t+1, ''.join(result)))
