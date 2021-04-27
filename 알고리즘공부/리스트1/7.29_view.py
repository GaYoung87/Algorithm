def my_min(x):  # 마지막에5, 9, 6에서 가장 적게 차이나는 값을 뽑기 위해 my_min이라는 함수 생성
    my_value = x[0]
    for num in x:
        if my_value > num:
            my_value = num
    return my_value

for t in range(10):
    n = int(input())
    data = list(map(int, input().split()))
    result = []  # 특정 건물에서 조망을 확인하기 위한 리스트!
    for i in range(2, n-2):
        if data[i] - data[i-2] > 0 and data[i] - data[i-1] > 0 and data[i] - data[i+1] > 0 and data[i] - data[i+2] > 0:
            result += [[data[i] - data[i-2], data[i] - data[i-1], data[i] - data[i+1], data[i] - data[i+2]]]  # 건물 별로 리스트를 만들어 그곳에서 조망건물수 확인
    # print(result)   # [[5, 2, 3, 1], [7, 5, 9, 3], [2, 6, 6, 6]]

    total = 0
    for r in result:  # 최소갯수 더하기
        total += my_min(r)
    print('#{0} {1}'.format(t+1, total))
