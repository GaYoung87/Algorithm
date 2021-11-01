def solution(prices):
    len_price = len(prices)
    answer = [0] * len_price
    
    for i in range(len_price):
        for j in range(i+1, len_price):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer