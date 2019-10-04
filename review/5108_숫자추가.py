for t in range(int(input())):
    N, M, L = map(int, input().split()) # N:수열길이,M:추가횟수,L:출력할 인덱스 번호
    data = list(map(int, input().split()))

    for m in range(M):
        idx, num = map(int, input().split())
        left = data[:idx]
        right = data[idx:]
        data = left + [num] + right

    print('#{} {}'.format(t+1, data[L]))
