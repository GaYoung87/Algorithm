for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        found = False
        for j in range(N):
            if arr[i * 2] == arr[j * 2 + 1]:
                found = True
                break

        if found == False:
            start_position = i
            break

    arr[0], arr[start_position * 2] = arr[start_position * 2], arr[0]
    arr[1], arr[start_position * 2 + 1] = arr[start_position * 2 + 1], arr[1]

    for i in range(1, N - 1):
        for j in range(i, N):
            if arr[i * 2 - 1] == arr[j * 2]:
                arr[i * 2], arr[j * 2] = arr[j * 2], arr[i * 2]
                arr[i * 2 + 1], arr[j * 2 + 1] = arr[j * 2 + 1], arr[i * 2 + 1]
                break

    print('#{}'.format(t + 1), end=' ')
    for i in range(N * 2):
        print('{}'.format(arr[i]), end=' ')
    print()