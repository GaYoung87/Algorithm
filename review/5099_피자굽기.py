for t in range(int(input())):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    pizza_ls = []
    for i in range(len(pizza)):
        pizza_ls.append([i + 1, pizza[i]])

    queue = []
    for n in range(N):
        queue.append(pizza_ls.pop(0))

    i = 0
    while queue:
        if queue[i][1] // 2 != 0:
            if len(queue) == 1:
                a = queue.pop(0)
                # why? a = queue.pop(0)만 하면 되는거 아닌가???? but 이것만 a = 이라고하면 a를 알수없다고함...ㅠㅠㅠㅠ
                # queue가 하나들어있을 때, 그것이 마지막 피자가 된다.
                break  # 그래서 while문을 빠져나감
            else:
                queue[i][1] = queue[i][1] // 2
                queue.append(queue.pop(0))
        else:
            if len(pizza_ls) == 0:
                a = queue.pop(0)
                # 이것만 a = queue.pop(0)하면 10개 중 8개 맞음 why?
                # why? 여기에도 a = 이라고 붙여야하는가? a = queue.pop(0)인가
            elif len(pizza_ls) != 0:
                queue.pop(0)
                queue.append(pizza_ls.pop(0))
    print('#{} {}'.format(t+1, a[0]))