for t in range(int(input())):
    N = int(input())
    data = list(map(int, input()))  # [4, 9, 6, 7, 9]

    # 1. [0, 0, 0, 0, ,,, 0]을 만든 후
    cnt = [0] * 10

    # 2. 해당 숫자가 나오면 해당 숫자인덱스에 추가한후
    for i in data:
        cnt[i] += 1  # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # 3. max
    mymax = cnt[0]
    for i in range(1, len(cnt)):
        if cnt[i] >= mymax:
            mymax = cnt[i]

    for i in range(len(cnt) - 1, -1, -1):
        if mymax == cnt[i]:
            result = i
            break

    print('#{} {} {}'.format(t+1, result, mymax))