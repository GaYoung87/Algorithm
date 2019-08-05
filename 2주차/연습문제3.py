# arr = 9 20 2 18 11 19 1 25 3 21 8 24 10 17 7 15 4 16 5 6 12 13 22 23 14

# arr 정렬

data = list(map(int, input().split()))

for k in range(len(data)-1):
    for i in range(len(data)-k-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]

board = [[0 for j in range(5)] for l in range(5)]
print(board)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

row = 1
while board == []:
    if row == 1:
        for x in range(5):
        for i in range(4):
            testX = x + d[i]

