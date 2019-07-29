p = "is"  # 찾을패턴  # 틀리면 다시 앞으로 돌아감! -> i로 돌아가서 시작
t = "This is a book~!"  # 전체텍스트  
M = len(p)  # 2
N = len(t)  # 16
# 최악의 경우 맨 끝에서 같다는 것이 처음 나오면 시간 N*M

def BruteForce(p, t): # 처음부터 끝까지
    i = 0  # t의 인덱스  0 1 2
    j = 0  # p의 인덱스  0 1 2 ,,, 15 16
    while j < M and i < N: #p는 0 1, t는 0 ~ 15
        if t[i] != p[j]:  # i=0, j=0이면 T랑 i -> 맞지않아서 i = 0, j = -1
            i = i - j
            j = -1  # -1로 해야 뒤에 if 문이랑 줄 맞는 j += 1에서 0이 된다. -> 처음으로 돌아가기!
        i += 1
        j += 1
        print(i, j)  # 1 0 / 2 0 / 3 1 / 4 2 나옴

    if j == M:
        return i - M  # 위치반환
    else:
        return -1

print(BruteForce(p, t))
