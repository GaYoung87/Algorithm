# min, max (동시 갱신)
def find(a, n):
    max_value = a[0]
    min_value = a[0]

    for i in range(1, n):
        if a[i] > max_value:
            max_value = a[i]
        if a[i] < min_value:
            min_value = a[i]

    return max_value - min_value


# 전기버스
# 1, 3, 5, 7, 9에 충전소에 있으므로 -> 0 1 0 1 0 1 0 1 0 1로 표현 
for t in ramge(1, int(input()) + 1):
    N = int(input())
    cards = input()
    cnt = [0] * 10

    for i in range(N):
        cnt[int(cards[i])] += 1

    max1 = 0
    for i in range(10):
    if cnt[max1] <= cnt[i]:
        max1 = i

    while(True):
        pre = cur
        cur += K
        if cur >= N:
            break
            if stations[cur] == 1:
                cnt += 1
            else:
                for i in range(1, K+1):
                    if stations[cur - i] == 1:
                        cur -= i
                        cnt += 1
                        break
                if cur == pre

# 숫자카드 
N, M = map(int, input().split())
v = list(map(int, input().split()))

sum = 0
for i in range(M):
    sum += v[i]

    minv = maxv = sum

    for i in range(N-M+1):
        sum = 0
        for j in range(i, i + M):
            sum += v[j]
        if maxv < sum:
            maxv = sum
        if minv > sum:
            minv = sum
    print('#%d %d' % (t, maxv - minv))
