for t in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    for i in range(N):
        found = False  # 수나사를 찾았는지 안찾았는지. 못찾았으면 
        for j in range(N):
            if arr[i * 2] == arr[j * 2 + 1]:
                found = True
                break
        if found == False:
            start_position = i
            break
    
    arr[0], arr[start_position * 2] = arr[start_position * 2], arr[0]  # max, min 값 구하는 것과 비슷함.
    arr[1], arr[start_position * 2 + 1] = arr[start_position * 2 + 1], arr[1]

    for i in range(1, N - 1):
        for j in range(i, N)
:
if arr