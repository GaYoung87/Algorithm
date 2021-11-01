def solution(citations):
    citations.sort()
    # print(citations)  # [0, 1, 3, 5, 6]
    temp = len(citations)
    for i in range(temp):
        if citations[i] >= temp - i:
            return temp - i

    return 0

citations = [22, 24]
citations = [3, 0, 6, 1, 5]	
