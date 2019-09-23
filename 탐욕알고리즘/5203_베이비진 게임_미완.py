for t in range(int(input())):
    data = list(map(int, input().split()))
    check1 = [0] * 10
    check2 = [0] * 10

    player1 = []
    player2 = []
    for i in range(0, 12, 2):
        player1.append(data[i])  # [9, 5, 5, 1, 4, 2]
        player2.append(data[i + 1])  # [9, 6, 6, 1, 2, 1]

    for i in range(6):
        check1[player1[i]] += 1
        check2[player2[i]] += 1
