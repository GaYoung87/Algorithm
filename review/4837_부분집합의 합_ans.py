for t in range(int(input())):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1, 1 << 12):
        # print(i)
        bitCnt = sum = 0
        for j in range(12):
            if i & (i << j):  # i의 j번째 비트가 1인지 아닌지 리턴
                sum += (j + 1)
                bitCnt += 1
        if sum == K and bitCnt == N:
            cnt += 1

