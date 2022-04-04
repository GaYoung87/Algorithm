board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
# result = 7


from collections import deque

def next_position(robot, board):
    temp = []  # 다음번에 갈 수 있는 곳 모두 넣기
    near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    (x1, y1), (x2, y2) = robot

    # 1. 상하좌우 이동
    for i in range(4):
        if board[x1 + near[i][0]][y1 + near[i][1]] == 0 and board[x2 + near[i][0]][y2 + near[i][1]] == 0:
            temp.append({(x1 + near[i][0], y1 + near[i][1]), (x2 + near[i][0], y2 + near[i][1])})

    # 2. 가로 -> 세로 회전
    if x1 == x2:
        for a in [1, -1]:  # 만약 (1,2)에서 -1이 된다면 에러남 -> 4방면 가쪽에 벽하나 세우기
            if board[x1 + a][y1] == 0 and board[x2 + a][y2] == 0:
                temp.append({(x1, y1), (x1 + a, y1)})
                temp.append({(x2, y2), (x2 + a, y2)})

    # 3. 세로 -> 가로 회전
    if y1 == y2:
        for b in [1, -1]:
            if board[x1][y1 + b] == 0 and board[x2][y2 + b] == 0:
                temp.append({(x1, y1), (x1, y1 + b)})
                temp.append({(x2, y2), (x2, y2 + b)})

    return temp

def solution(board):
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # 현재 좌표 위치 큐 삽입, 확인용 set
    q = deque([])
    robot = {(1, 1), (1, 2)}
    visited = []
    q.append((robot, 0))
    visited.append(robot)

    while q:
        robot, time = q.popleft()

        if (n, n) in robot:  # 종점 도착
            return time

        # bfs 진행
        for location in next_position(robot, new_board):
            if location not in visited:
                visited.append(location)
                q.append((location, time+1))
