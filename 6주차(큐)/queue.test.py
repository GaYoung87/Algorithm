# myque = []  # 리스트
#
# def enQueue(item):     # global 안써도 괜찮 -> why? myque라는 리스트의 주소를 읽어옴
#     myque.append(100)  # -> myque자체에 100을 append한 것이아니라, 주소에다가 가지고옴.
#                        # myque list자체에다가 넣는 것은 아님!
#
#
# print("myque", myque)
# enQueue(100)
# print("myque", myque)
# print("ok")

def IsSafe(y,x):
    return 0 <= y < N and 0<= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)

def BFS(start_y, start_x):
    global D_result
    Q.append((start_y, start_x))
    visited.append((start_y, start_x))

    while Q:
        start_y, start_x = Q.pop(0)
        for dir in range(4):
            NewY = start_y + dy[dir]
            NewX = start_x + dx[dir]
            if IsSafe(NewY, NewX) and (NewY, NewX) not in visited:
                Q.append((NewY, NewX))
                visited.append((NewY, NewX))
                Distance[NewY][NewX] = Distance[start_y][start_x] +1
                if Maze[NewY][NewX] == 3:
                    D_result = Distance[NewY][NewX] -1
                    return


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    D_result = 0
    Q = []
    Distance = [[0]*N for _ in range(N)]
    BFS(start_y, start_x)
    print('#{} {}'.format(tc, D_result))