def solution(cap, n, deliveries, pickups):

    deliver, pickup = 0, 0
    for i in range(n):
        deliver += deliveries[n-i-1]
        pickup += pickups[n-i-1]

    answer = -1
    return answer