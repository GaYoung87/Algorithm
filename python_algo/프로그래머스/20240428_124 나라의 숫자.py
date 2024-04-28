"""
1  -> 1   4  -> 11   7  -> 21   10 -> 41   13 -> 111
2  -> 2   5  -> 12   8  -> 22   11 -> 42   14 -> 112
3  -> 4   6  -> 14   9  -> 24   12 -> 44   15 -> 114
"""

def solution(n):
    answer = ''
    while n:
        if n % 3 == 0:
            answer += "4"
            n = n // 3 - 1
        else:
            answer += str(n % 3)
            n = n // 3
    # print(answer)

    return answer[::-1]