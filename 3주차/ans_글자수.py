for t in range(int(input())):
    str1 = input()
    str2 = input()

    maxcnt = 0
    for ch1 in str1:
        cnt = 0
        for ch2 in str2:
            if ch1 == ch2:
                cnt += 1
        if maxcnt < cnt:
            maxcnt = cnt
    
    print('#{} {}'.format(t+1, maxcnt))
        