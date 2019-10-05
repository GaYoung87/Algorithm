for t in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))
    result = []
    for i in range(2, N - 2):
        if data[i] - data[i-2] > 0 and data[i] - data[i-1] > 0 and data[i] - data[i+1] > 0 and data[i] - data[i+2] > 0:
            result += [[data[i] - data[i-2], data[i] - data[i-1], data[i] - data[i+1], data[i] - data[i+2]]]

    cnt = 0
    for r in result:
        cnt += min(r)
    print('#{} {}'.format(t + 1, cnt))
