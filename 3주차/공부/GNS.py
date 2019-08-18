import sys
sys.stdin = open('input.txt', 'r')

p = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]

def getidx(num):   # dict에서 key값을 가지고 value값 찾기
    for i in range(10):
        if num[0] == p[i][0] and num[1] == p[i][1] and num[2] == p[i][2]:
            return i

for t in range(int(input())):
    temp = input()
    nums = input().split()

    cnt = [0] * 10

    for num in nums:
        cnt[getidx(num)] += 1

    ans = ''
    for i in range(10):
        ans += p[i] * cnt[i]
    print('#%d ' % (t, ans))
