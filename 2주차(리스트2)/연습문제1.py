# arr = [[1, 1, 1, 1, 1], 
#        [1, 0, 0, 0, 1], 
#        [1, 0, 0, 0, 1], 
#        [1, 0, 0, 0, 1], 
#        [1, 1, 1, 1, 1]]

def my_abs(x, y):
    if x - y > 0:
        result = x - y
    else:
        result = y - x
    return result

# distance = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# for x in range(len(arr)):
#     for y in range(len(arr)):
#         for i, j in distance:
#             if 


# 선생님 답
arr = [[1, 1, 1, 1, 1], 
       [1, 0, 0, 0, 1], 
       [1, 0, 0, 0, 1], 
       [1, 0, 0, 0, 1], 
       [1, 1, 1, 1, 1]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += my_abs(arr[x][y], arr[testX][testY])
                print(my_abs(arr[x][y], arr[testX][testY]))

# print('sum = %d' % sum) 
