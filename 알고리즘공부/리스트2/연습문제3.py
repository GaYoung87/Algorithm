# # arr = 9 20 2 18 11 19 1 25 3 21 8 24 10 17 7 15 4 16 5 6 12 13 22 23 14

# # arr 정렬

# data = list(map(int, input().split()))

# for k in range(len(data)-1):
#     for i in range(len(data)-k-1):
#         if data[i] > data[i+1]:
#             data[i], data[i+1] = data[i+1], data[i]

# board = [[0 for j in range(5)] for l in range(5)]
# print(board)

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# row = 1
# while board == []:
#     if row == 1:
#         for x in range(5):
#         for i in range(4):
#             testX = x + d[i]



# 선생님 코드
ary = [ [ 9, 20, 2, 18, 11 ],
	[ 19, 1, 25, 3, 21 ],
	[ 8, 24, 10, 17, 7 ],
	[ 15, 4, 16, 5, 6 ],
	[ 12, 13, 22, 23, 14 ] ]

sorted_ary = [[0  for _ in range(5)] for _ in range(5)]

def sel_min():
    minX, minY= 0, 0
    for i in range(5):
        for j in range(5):
            if ary[minX][minY] > ary[i][j]:
                minX, minY = i, j

    min = ary[minX][minY]
    ary[minX][minY] = 99
    return min

def isWall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5: return True
    if sorted_ary[x][y] != 0: return True
    return False


X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_stat = 0  # 0:오른쪽, 1:아래, 2:왼쪽, 3:위

for i in range(25):
    cur_min = sel_min()
    sorted_ary[X][Y] = cur_min
    X += dx[dir_stat]
    Y += dy[dir_stat]

    if isWall(X, Y):
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = (dir_stat + 1) % 4
        X = X + dx[dir_stat]
        Y = Y + dy[dir_stat]


for i in range(5):
    for j in range(5):
        print(sorted_ary[i][j], end=" ")
    print()

