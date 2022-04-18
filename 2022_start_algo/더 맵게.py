
# scoville = [1, 2, 3, 9, 10, 12]
K = 15  # 2

scoville = [1, 13, 3, 5, 4, 8, 7]

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        print(scoville)
        temp = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        print(scoville)
        heapq.heappush(scoville, temp)
        print(scoville)
        print('---------------------------')
        answer += 1

        if len(scoville) == 1:
            return -1
    return answer

print(solution(scoville, K))