def solution(cap, n, deliveries, pickups):

    deliver, pickup = 0, 0
    answer = 0
    for i in range(n):
        deliver += deliveries[n-i-1]
        pickup += pickups[n-i-1]

        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            answer += 2*(n-i)
    return answer
"""
1 0 3 1 2
0 3 0 4 0
        2 -> 배달
      1/4 -> 2를 배달가면서 1을 배달, 4 수거해가고 
    3     -> 배달하면서 앞에 1도 배달
  3       -> 수거해가고 
"""