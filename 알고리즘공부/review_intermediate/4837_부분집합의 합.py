result = []
def comb(arr, k):
    if len(arr) == N:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(data)):
            comb(arr + [data[idx]], idx)


for t in range(int(input())):
    N, K = map(int, input().split())
    data = [n for n in range(1, 13)]
    result = []
    comb([], -1)
    # print(result)
    cnt = 0
    for i in result:
        sum_r = 0
        for j in i:
            sum_r += j
        if sum_r == K:
            cnt = 1
            # break
    print('#{} {}'.format(t + 1, cnt))