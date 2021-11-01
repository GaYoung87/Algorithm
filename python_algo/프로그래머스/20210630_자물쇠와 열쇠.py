import pprint
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate(arr):
    n = len(arr)
    bd = [[0]*n for _ in range(n)]

    for i in range(len(arr)):
        for j in range(len(arr)):
            bd[j][n-i-1] = arr[i][j]
    
    return bd

def check(board, len_lock, len_key):
    for r in range(len_lock):
        for c in range(len_lock):
            if board[len_key+r][len_key+c] != 1:
                return False
    return True


def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)

    n = 2 * len_key + len_lock
    board = [[0]*n for _ in range(n)]

    for i in range(len_lock):
        for j in range(len_lock):
            board[len_key+i][len_key+j] += lock[i][j]

    for time in range(4):
        for i in range(1, len_key + len_lock):
            for j in range(1, len_key + len_lock):
                for x in range(len_key):
                    for y in range(len_key):
                        board[i+x][j+y] += key[x][y]  # board판에 key 넣기

                if check(board, len_lock, len_key):
                    return True
                
                for x in range(len_key):
                    for y in range(len_key):
                        board[i+x][j+y] -= key[x][y]  # board판에 key 빼기

        key = rotate(key)
    return False

print(solution(key, lock))





