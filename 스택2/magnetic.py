for tc in range(1, 11):
    n = int(input())
    mymap = []
    for i in range(100):
        mymap.append(list(map(int, input().split())))

    mycount = 0  # 교착 횟수 저장용

    # 세로방향 검색
    for col in range(n):
        # 1을 만난 표식 생성
        meet1 = False
        for row in range(n):
            if mymap[row][col] == 1:
                meet1 = True
            if mymap[row][col] == 2 and meet1 == True:
                mycount += 1  # 교착횟수 증가
                meet1 = False  # 1과의 만남을 없앰
    
    print('#{} {}'.format(tc, mycount))