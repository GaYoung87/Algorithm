# 효율성 통과 방법 : O(N) 혹은 O(1)로 줄이기!
# 누적합 이용!

def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]  # 누적합을 위한 판

    # 누적합을 위한 세팅
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            temp[r1][c1] += -degree
            temp[r1][c2 + 1] += degree
            temp[r2 + 1][c1] += degree
            temp[r2 + 1][c2 + 1] += -degree
        else:
            temp[r1][c1] += degree
            temp[r1][c2 + 1] += -degree
            temp[r2 + 1][c1] += -degree
            temp[r2 + 1][c2 + 1] += degree

    # 행 누적합
    for x in range(len(temp) - 1):
        for y in range(len(temp[0]) - 1):
            temp[x][y + 1] += temp[x][y]

    # 열 누적합
    for x in range(len(temp) - 1):
        for y in range(len(temp[0]) - 1):
            temp[x + 1][y] += temp[x][y]

    # 값 확인
    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] += temp[x][y]
            if board[x][y] > 0:
                answer += 1

    return answer