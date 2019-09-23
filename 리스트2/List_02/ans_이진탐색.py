def binarySearch(n, key):
    l = 1
    r = n
    cnt = 0

    while 1:  # True라고 해도 괜찮지만 알아서 True나 False로 해석
        mid = int((l + r) / 2)
        cnt += 1

        if mid == key:
            break   # while문을 빠져나가는 방법! break -> while True: 해도 상관 없음!
        elif mid < key:
            l = mid
        else:
            r = mid

        return cnt

        
for t in range(int(input())):
    pages, key1, key2 = map(int, input().split())
    cnta = binarySearch(pages, key1)
    cntb = binarySearch(pages, key2)

    result =  '0'
    if cnta < cntb:
        result = 'A'
    elif cnta > cntb:
        result = 'B'

    print('#%d %c' % (t, result))