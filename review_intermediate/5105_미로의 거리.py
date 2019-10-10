# def bfs():
#     while queue:
#         x, y, result = queue.pop(0)
#         for a, b in near:
#             xi, yi = (x + a, y + b)
#             if 0 <= xi < N and 0 <= yi < N:
#                 if board[xi][yi] == 0:
#                     queue.append((xi, yi, result + 1))
#                     board[xi][yi] = 1
#                 elif board[xi][yi] == 3:
#                     return result
#     # 어차피 아무리 미로탈출을 못해도 queue가 빈리스트가 되니까, append가 안됨.
#     # result값이 출력이 안되면 flag로 제어
#     return 0  # 완전 다 돌았을 때, 값이 없으면 0을 리턴해라.




near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
# 1. queue를 사용할지, stack을 사용할지 결정해야함. how?
    flag = 0
    stop = 0
    queue = []
    for i in range(N):
        if stop == 1:
            break
        for j in range(N):
    # 2. 값이 2일때 시작 -> queue에 집어넣으면서 cnt도 집어넣음
            if board[i][j] == 2:
                queue.append((i, j, 0))
                stop = 1
                break
                # path_list.append(path)
    rs = bfs()
    print(rs)
#     while queue:
#         x, y, result = queue.pop(0)
#         for a, b in near:
#             xi, yi = (x + a, y + b)
#             if 0 <= xi < N and 0 <= yi < N:
# # 3. 0을 지나면서 cnt += 1 해주지만, 3에 도달하면 그 cnt print한다.
#                 if board[xi][yi] == 0:
#                     queue.append((xi, yi, result + 1))
#                     board[xi][yi] = 1
#                 elif board[xi][yi] == 3:
# # 3-1 도달하면 break -> 이것을 flag로 제어
#                     flag = 1
#                     break  # 이 break는 for a, b in near을 빠져나가기 위해 사용!
#             if flag == 1:  # while문 나가게 하기위해서 break 사용!
#                 answer = result  # 3에 닿았을 때 0의 갯수를 샌다
#                 break
#
#                 # 한칸 더 앞에서 적으면 answer이 모두 0 why? while문 돌기 전에는 전부다 flag = 0이므로!!
#                 if flag == 0:  # while문을 다 돌고 queue가 빈칸이 되어 while문을 나와을 때에도
#                     answer = 0  # flag가 0이면 answer = 0이다
#                     break
#     print('#{} {}'.format(t + 1, answer))