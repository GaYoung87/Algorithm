def solution(rows, columns, queries):
    board = [[] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            board[i].append(i * columns + (j+1))

    answer = []
    for x1, y1, x2, y2 in queries:
        temp = board[x1-1][y1-1]
        mymin = temp
        
        # 위
        for y in range(y1, y2):
            next_val = board[x1-1][y]
            board[x1-1][y] = temp
            temp = next_val

            if mymin > temp:
                mymin = temp

        # 오른쪽
        for x in range(x1, x2):
            next_val = board[x][y2-1]
            board[x][y2-1] = temp
            temp = next_val

            if mymin > temp:
                mymin = temp

        # 아래
        for y in range(y2-1, y1-1, -1):
            next_val = board[x2-1][y-1]
            board[x2-1][y-1] = temp
            temp = next_val

            if mymin > temp:
                mymin = temp
        
        # 왼쪽
        for x in range(x2-1, x1-1, -1):
            next_val = board[x-1][y1-1]
            board[x-1][y1-1] = temp
            temp = next_val

            if mymin > temp:
                mymin = temp
        answer.append(mymin)
    # print(answer)
    return answer

# rows = 6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]  # [8, 10, 25]
# rows = 3
# columns = 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]  # [1, 1, 5, 3]
rows = 100
columns = 97
queries = [[1,1,100,97]]  # [1]


