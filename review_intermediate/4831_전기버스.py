for t in range(int(input())):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))  # 충전기있는 곳
    station = 0
    cnt = 0  # 최종적으로 몇번 충전이 될 것인지
    back = 0  # station += K를 했을 때 충전소가 없다면 뒤로갈 것
    for i in range(N + 1):
        if station == N:
            break
        elif station == 0:
            station += K
        elif station != 0 and station != N:
            if station in data:
                cnt += 1
                station += K
                back = 0
            else:
                station -= 1
                back += 1  # back이 K번만큼 뒤로갔는데도 없다면 도착불가 -> 0
                if back == K:
                    cnt = 0
                    break
    print('#{} {}'.format(t + 1, cnt))
