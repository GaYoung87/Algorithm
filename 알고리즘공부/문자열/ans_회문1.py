def calpal():
    cnt = 0
    for i in range(8):
        for j in range(8 - N + 1):
            cnt += is_pal(i, j)

    for i in range(8 - N + 1):
        for j in range(8):
            cnt += is_palH(i, j)

    return cnt