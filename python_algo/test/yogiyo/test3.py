# N보다 큰 두 개의 연속 숫자를 포함하지 않는 가장 작은 정수
def solution(N):
    # write your code in Python 3.6
    pass

# N = 55
# N = 1765
N = 98
# N = 44432
# N = 3298
num = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9}
def check_same(N):
    N = str(N)
    for i in range(len(N)-1):
        if N[i] == N[i+1]:
            return True
    return False

def solution(N):
    while True:
        N += 1
        if not check_same(N):
            return N

print(solution(N))


