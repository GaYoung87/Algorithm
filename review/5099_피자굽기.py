for t in range(int(input())):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    pizza_ls = []
    for i in range(len(pizza)):
        pizza_ls.append([i + 1, pizza[i]])

    queue = []
    for n in range(N):
        queue.append(pizza_ls.pop(0))


    while queue:
        if queue[0][1] // 2 != 0:
            if len(queue) == 1:  # queue[0][1] // 2 != 0인 queue가 하나들어있을 때, 그것이 마지막 피자가 된다.
                a = queue.pop(0)
                break  # 그래서 while문을 빠져나감 (queue가 하나 남아있지만, while문을 빠져나가야하니깐! why? len(queue)가 0이 되려면 계속 돌기때문!)
            else:
                queue[0][1] = queue[0][1] // 2
                queue.append(queue.pop(0))
        else:
            if len(pizza_ls) == 0:
                a = queue.pop(0)  # 마지막에 [[5, 1][4, 1]] 인 경우에 [[4, 1]]로 된 후, 이는 [4, 0]이 되니까 그냥 pop되어서 사라진다. 이를 막기 위해 a = queue.pop(0)이라고 설정
            elif len(pizza_ls) != 0:
                queue.pop(0)
                queue.append(pizza_ls.pop(0))
    print('#{} {}'.format(t+1, a[0]))