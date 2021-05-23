n = 15
def solution(n):
    answer = ''
    if n <= 3:
        return '124'[n - 1]
    else:
        mok, na = divmod(n-1, 3)
        return solution(mok) + '124'[na]

print(solution(n))