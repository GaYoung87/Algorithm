import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)

    cnt = 0
    while scoville[0] < K:
        if len(scoville) >= 2:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            cnt += 1
        else:
            return -1

    return cnt


scoville = [1, 2, 3, 9, 10, 12]
K = 7


