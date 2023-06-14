# 연속된 부분수열의 합! -> 무조건 투포인트

def solution(sequence, k):
    n = len(sequence)
    end = 0
    total = 0
    mymin = 1e9
    answer = []
    for start in range(n):
        while end < n and total < k:
            total += sequence[end]
            end += 1

        if total == k:
            if mymin > end - start:
                answer = [start, end - 1]
            mymin = end - start

        total -= sequence[start]  # sequence[start] 값을 빼줘야 다음 start값부터 시작할 수 있음
        # Test
        # [1,1,1,2,3,4,5] -> answer=[1,1,1,2] -> [1,1,2,3,(4)] -> [1,2,3,(4)] -> answer=[2,3]

    return answer