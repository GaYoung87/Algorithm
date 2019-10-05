for t in range(int(input())):
    N, M, K = map(int, input().split())

    data = list(map(int, input().split()))
    start = data[0]
    plus = 0

    for k in range(K):
        plus += M
        if plus <= len(data) - 1:
            data[plus:0] = [data[plus-1] + data[plus]]
        elif plus == len(data):
            data[plus:0] = [data[plus-1] + start]
        elif plus > len(data):
            plus -= len(data)
            data[plus:0] = [data[plus-1] + data[plus]]

    data = data[::-1]
    print('#{}'.format(t+1), end=' ')
    if len(data) > 10:
        for i in range(10):
            print(data[i], end=' ')
        print()
    else:
        for i in range(len(data)):
            print(data[i], end=' ')
        print()
