for t in range(1, T+1):
    N = int(input())
    m = [[0]*10 for i in range(10)]
    cnt = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):  # 같은 색인 영역은 겹치지 않는다.
            for j in range(c1, c2 + 1):
                m[i][j] += color

    for i in range(10):
        for j in range(10):
            if m[i][j] == 3:
                cnt += 1