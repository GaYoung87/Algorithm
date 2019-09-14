word = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]

def find(num):
    for i in range(10):
        if num[0] == word[i][0] and num[1] == word[i][1] and num[2] == word[i][2]:
            return i


for t in range(int(input())):
    N = input()
    number = input().split()
    cnt = [0] * 10

    for num in number:
        cnt[find(num)] += 1

    result = ''
    for i in range(10):
        result += word[i] * cnt[i]

    print('#{} {}'.format(t + 1, result))


