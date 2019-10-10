# 개념
# 1 << 3이면 1000이다. (print시에는 )
# i&(1<<j) : i의 j번째 비트가 1인지 아닌지 리턴

# 1. 부분집합
'''
부분집합 생성하기
'''
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)
for i in range(1<<n):
    for j in range(n+1):
        if i & (1<<j):
            print(arr[j], end=',')
        print()






#
# '''
# 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.
# '''
# arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# sum = 0
# cnt = 0
# for i in range(1, 1 << len(arr)): # i = 1~2^10-1
#     sum = 0
#     for j in range(len(arr)):
#         if i & (1 << j):
#             sum += arr[j]
#
#     if sum == 0:
#         cnt += 1
#         print("%d : " %cnt, end= " ")
#         for j in range(len(arr)):
#             if i & (1 << j):
#                 print(arr[j], end= " ")
#         print()