for t in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1, 1<<12): 
    # 공집합은 없음!! / 12자리만 관심이 있음 (1<<0부터 1<<11까지 해서 1000~과 &시키면 
        bitCnt = sum = 0
        for i in range(12):
            if i & (1<<j):
                sum += j + 1
                bitCnt += 1
        if sum == K and bitCnt == N:
            cnt += 1
    print('#%d %d' % (t, cnt))