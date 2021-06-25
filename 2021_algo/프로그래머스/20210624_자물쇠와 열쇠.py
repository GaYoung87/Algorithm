key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]  # true


def rotation(arr):
    n = len(arr)
    bd = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            bd[j][n-1-i] = arr[i][j]
    return bd


# def solution(key, lock):
#     len_key = len(key)
#     len_lock = len(lock)
#     n = len_key + len_lock + 1
#     board = [[0] * (n) for _ in range(n)]

#     for i in range(len_lock):
#         for j in range(len_lock):
#             board[i+len_key-1][j+len_key-1] = lock[i][j]

#     start = len_key
#     end = len_key + len_lock - 1

#     for _ in range(4):
#         for i in range(end):
#             for j in range(end):
#                 if check(i, j, start, end, board, key, lock):
#                     return True

#         rotated_key = rotation(key)

#     return False

len_key = len(key)
len_lock = len(lock)
n = len_key + len_lock + 1
board = [[0] * (n) for _ in range(n)]

for i in range(len_lock):
    for j in range(len_lock):
        board[i+len_key-1][j+len_key-1] = lock[i][j]

start = len_key
end = len_key + len_lock - 1

for _ in range(4):
    for i in range(end):
        for j in range(end):
            if check(i, j, start, end, board, key, lock):
                return True

    rotated_key = rotation(key)
