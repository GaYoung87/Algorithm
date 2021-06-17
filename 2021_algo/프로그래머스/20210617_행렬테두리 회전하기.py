def solution(rows, columns, queries):
    answer = []
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4]]# [[2,2,5,4],[3,3,6,6],[5,1,6,3]]  # [8, 10, 25]
# rows = 3
# columns = 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]  # [1, 1, 5, 3]
# rows = 100
# columns = 97
# queries = [[1,1,100,97]]  # [1]

board = [[] for _ in range(rows)]

for i in range(rows):
    for j in range(columns):
        board[i].append(i * columns + (j+1))

for x1, y1, x2, y2 in queries:
    temp = board[x1-1][y2-1]
    min_value = temp
    
    # 북쪽 테두리
    min_value = min(min(board[x1-1][y1-1:y2-1]), min_value)
    board[x1-1][y1:y2] = board[x1-1][y1-1:y2-1]
    print(board)

[[ 1,  2,  3,  4,  5,  6], 
 [ 7,  8,  8,  9, 11, 12], 
 [13, 14, 15, 16, 17, 18],
 [19, 20, 21, 22, 23, 24], 
 [25, 26, 27, 28, 29, 30], 
 [31, 32, 33, 34, 35, 36]]