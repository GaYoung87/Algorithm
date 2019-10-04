for t in range(int(input())):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for m in range(M - 1):
        plus_data = list(map(int, input().split()))
        # print(plus_data)
        for n in range(N):
            if plus_data[0] < data[n]:
                data[n:0] = plus_data
                # why? data = data[0:n] + plus_data + data[n+1:N]을 하면 4 2 -> 2 3 4 5/4 8 7 6인 경우는 ok
                # 4 4 -> 2 3 4 5/4 8 7 6/9 10 15 16/1 2 6 5인 경우는 이상하게 나옴,,
                break

            if n == N - 1:
                data += plus_data
    print('#{}'.format(t+1), end=' ')
    data.reverse()
    for k in range(10):
        print(data[k], end=' ')
