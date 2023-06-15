def solution(park, routes):
    # 1. 'S'의 위치찾기
    # 2. 이동하기
    #   2-1. 근데 이때, 원래 움직이기 시작한 점을 저장하고, 움직이는 지점은 새로표시
    #   2-2. 그래야 X를 만나면 해당명령 무시하고 다음명령 실행 가능

    answer = []
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j
                break

    print('x, y')
    print(x, y)
    print('===========================================================')
    for route in routes:
        new_x, new_y = x, y

        for n in range(int(route[2])):
            if route[0] == 'E' and new_y != len(park[0])-1 and park[new_x][new_y+1] != 'X':
                new_y += 1
                #  끝까지 간게 맞으면 값을 바꾸고, 끝까지 간게 아니면 값 냅두기(pass하고 다음 route진행)
                if n == int(route[2])-1:
                    y = new_y

            elif route[0] == 'W' and new_y != 0 and park[new_x][new_y-1] != 'X':
                new_y -= 1
                if n == int(route[2])-1:
                    y = new_y

            elif route[0] == 'N' and new_x != 0 and park[new_x-1][new_y] != 'X':
                new_x -= 1
                if n == int(route[2]) - 1:
                    x = new_x

            elif route[0] == 'S' and new_x != len(park)-1 and park[new_x+1][new_y] != 'X':
                new_x += 1
                if n == int(route[2]) - 1:
                    x = new_x

            print('new_x, new_y')
            print(new_x, new_y)
            print('===========================================================')
    return [x, y]
