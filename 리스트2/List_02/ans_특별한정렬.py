# 1 2 3 4 5 6 7 8 9 10 (i)
# 홀수번째 : maxI -> 10과 1 자리바꿈 (10 2 3 4 5 6 7 8 9 1) 10은 정렬 완성!
# 짝수번째면 : minI -> 맨 앞에 값을 두고 맨 뒤의 값과 두번째 자리 값을 바꿈 (10 1 3 4 5 6 7 8 9 2)


for t in range(int(input())):
    result = []
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(10):
        minI = maxI = i
        if i % 2 == 0:  # 홀수번째!!(index 기준) index 1, 3, 5, ,,
            for j in range(i+1, N):
                if nums[maxI] < nums[j]:
                    maxI = j
            nums[i], nums[maxI] =nums[maxI], nums[i]
        else:
            for j in range(i+1, N):
                if nums[minI] > nums[j]:
                    minI = j
            nums[i], nums[minI] =nums[minI], nums[i]
    
    print('#%d' % t, end=' ')
    for i in range(10): print(nums[i], end=' ')
    print()