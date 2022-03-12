rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]  # result = [8, 10, 25]

def solution(rows, columns, queries):
    board = [[0 for col in range(columns)] for row in range(rows)]
    val = 1
    for row in range(rows):
        for col in range(columns):
            board[row][col] = val
            val += 1

    # 방법1: 오른아래왼위
    # 방법2: 위왼아래오른
    # 방법2가 더 간단
    answer = []
    for x1, y1, x2, y2 in queries:
        temp = board[x1-1][y1-1]
        mymin = temp

        # 왼쪽라인에서 위로올라옴
        for i in range(x1 - 1, x2 - 1):
            new = board[i + 1][y1 - 1]
            board[i][y1 - 1] = new
            mymin = min(new, mymin)

        # 위쪽라인에서 오른쪽으로 이동
        for i in range(y1 - 1, y2 - 1):
            new = board[x2 - 1][i + 1]
            board[x2 - 1][i] = new
            mymin = min(new, mymin)

        # 오른쪽라인에서 아래로 이동
        for i in range(x2- 1, x1 - 1, -1):
            new = board[i - 1][y2 - 1]
            board[i][y2 - 1] = new
            mymin = min(new, mymin)

        # 아래쪽라인에서 왼쪽으로 이동
        for i in range(y2- 1, y1 - 1, -1):
            new = board[x1 - 1][i - 1]
            board[x1 - 1][i] = new
            mymin = min(new, mymin)

        board[x1 - 1][y1] = temp
        answer.append(mymin)

    return answer

# rows = 3
# columns = 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]  # result = [1, 1, 5, 3]
# rows = 100
# columns = 97
# queries = [[1,1,100,97]]  # result = [1]
