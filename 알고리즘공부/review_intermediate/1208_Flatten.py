def my_min(arr):
    mymin = arr[0]
    for i in range(1, len(arr)):
        if mymin > arr[i]:
            mymin = arr[i]
    return mymin

def my_max(arr):
    mymax = arr[0]
    for i in range(1, len(arr)):
        if mymax < arr[i]:
            mymax = arr[i]
    return mymax

def find_index(x, arr):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


for t in range(1):
    N = int(input())
    data = list(map(int, input().split()))

    for n in range(N):
        max_data = my_max(data)
        min_data = my_min(data)
        max_index = find_index(max_data, data)
        min_index = find_index(min_data, data)

        data[max_index] -= 1
        data[min_index] += 1

    result = my_max(data) - my_min(data)

    print('#{} {}'.format(t, result))

