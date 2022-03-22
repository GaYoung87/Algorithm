# 효율성 통과 못함
def solution(board, skill):
    answer = 0

    for type, r1, c1, r2, c2, degree in skill:
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if type == 1:
                    board[x][y] -= degree
                else:
                    board[x][y] += degree

    # 2차원 배열의 원소를 일일이 참조하기 때문에 시간 복잡도가 O(N*M)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]  # 10
# board = [[1,2,3],[4,5,6],[7,8,9]]
# skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]  # 6

# 효율성 통과 방법 : O(N) 혹은 O(1)로 줄이기!
# 누적합 이용!
