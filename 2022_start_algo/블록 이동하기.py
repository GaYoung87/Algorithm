board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
result = 7

"""
1. BFS
2. 

"""
from collections import deque

n = len(board)
# 현재 좌표 위치 큐 삽입, 확인용 set
q = deque([])
robot = {(1, 1), (1, 2)}
visited = []
q.append((robot, 0))
visited.append(robot)
while q:
    position, time = q.popleft()

    if (n, n) in position:  # 종점 도착
        print(time)
        break

    print(next_position(robot))
    break

def next_position(robot):
    temp = []
    near = [(0,1), (0,-1), (1,0), (-1,0)]
    (x1, y1), (x2, y2) = robot

    # 1. 상하좌우 이동
    
    # 2. 가로 -> 세로 회전
    
    # 3. 세로 -> 가로 회전














    return temp