def edit(plus):
    if plus[0] == 'I':
        data[int(plus[1]):0] = [int(plus[2])]

    elif plus[0] == 'D':
        data.pop(int(plus[1]))

    elif plus[0] == 'C':
        data[int(plus[1])] = int(plus[2])

for t in range(int(input())):
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))

    for m in range(M):
        plus = list(input().split())
        edit(plus)

    if len(data) <= L - 1:
        result = -1
    else:
        result = data[L]
    print('#{} {}'.format(t+1, result))