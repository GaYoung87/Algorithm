# 버블 sort : O(n^2)
# 퀵 sort : O(nlogn)
# 카운팅 sort : O(n+k), 자료형이 discrete
# == 은 단어를 하나하나 맞는지 확인 ex. ZRO -> 'Z','R','O' 가 'Z','R','O'와 일치하는지
# 최종 값을 내고 print()를 찍어라! ex. print(max(result)) 하지말아라! why? print 사긴 많이 걸림

# index구조 : 인덱스는 전체 확인하는 것이 아니라 특정 지점으로 바로 감 -> 속도 빠름#
numidx = [[0] * 100 for _ in range(100)]
numidx[ord('Z')][ord('R')] = 0
# if 0~99면 100개를 numidx로 해줘야함

p = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

def getind(num):
    for i in range(10):
        if num[0] == p[i][0] and num[1] == p[i][1] amd num[2] == p[i][2]:
            return i

for t in range(1, t+1):
    temp = input()
    nums = input().split()

    cnt = [0] * 10

    for num in nums:
        cnt[numidx[ord(num[0])][ord(num[1])]] += 1

    ans = ''
    for i in range(10):
        ans += p[i] * cnt[i]
    
        print()

