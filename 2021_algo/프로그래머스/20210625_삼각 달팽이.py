def solution(n):
    board = [[0] * (i+1) for i in range(n)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            # down
            if i % 3 == 0:
                x += 1
            # right
            elif i % 3 == 1:
                y += 1
            # up
            else:
                x -= 1
                y -= 1
            board[x][y] += num
            num += 1

    answer = []
    for i in board:
        for j in i:
            if j != 0:
                answer.append(j)
    # print(answer)
    return answer

    
n = 5



