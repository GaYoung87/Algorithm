from pprint import pprint

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]  # true

def rotation(bd):
    n = len(bd)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-1-i] = bd[i][j]
    return result

def check(board, len_lock, len_key):
    for i in range(len_lock):
        for j in range(len_lock):
            if board[len_key + i][len_key + j] != 1:
                return False
    return True

def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)

    n = 2 * len_key + len_lock
    board = [[0] * n for _ in range(n)]

    for i in range(len_lock):
        for j in range(len_lock):
            board[len_key + i][len_key + j] += lock[i][j]
    pprint(board)

    for time in range(4):  # 1번 key로 처음부터끝까지 돌리고, 2번key로 처음부터끝까지 돌리고..
        # board에 key 하나씩 넣어보기
        for i in range(1, len_key+len_lock):  # i, j는 board에 key 들어가는 시작점
            for j in range(1, len_key+len_lock):
                for x in range(len_key):  # x, y는 key안에서의 자리
                    for y in range(len_key):
                        board[i+x][j+y] += key[x][y]  # board판에 key 넣기

                # 채워지는 여부 확인
                if check(board, len_lock, len_key):
                    return True

                # key가 완벽하게 채워지지 않으면 board판에 key 빼기
                for x in range(len_key):
                    for y in range(len_key):
                        board[i + x][j + y] -= key[x][y]

        key = rotation(key)

    return False

print(solution(key, lock))