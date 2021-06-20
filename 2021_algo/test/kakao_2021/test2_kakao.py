# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#           ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#           ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
#           ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
#           ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
 # [1, 0, 1, 1, 1]
 
# def solution(places):

#     answer = []
#     return answer



places = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
# places = ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
# places = ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"]
# places = ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]
# places = ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]


answer = []
# board = []
# for i in places:
#     bd = []
#     for j in i:
#         bd.append(j)
#     board.append(bd)
# print(board)

board = [['P', 'O', 'O', 'O', 'P'],
 ['O', 'X', 'X', 'O', 'X'],
 ['O', 'P', 'X', 'P', 'X'],
 ['O', 'O', 'X', 'O', 'X'],
 ['P', 'O', 'X', 'X', 'P']]


near = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# person = []
# for i in range(5):
#     for j in range(5):
#         if board[i][j] == "P":
#             person.append([i, j])

person = [[0, 0]]
visit = [[0] * 5 for _ in range(5)]
while person:
    x, y = person.pop(0)
    print(x,y)

    for a, b in near:
        xi, yi = (x + a, y + b)
        if 0 <= xi < 5 and 0 <= yi < 5 and board[xi][yi] == "O":
            visit[xi][yi] = visit[x][y] + 1.
            person.append([xi, yi])
        elif 0 <= xi < 5 and 0 <= yi < 5 and visit[xi][yi] == 2:
            print(visit)
            break
