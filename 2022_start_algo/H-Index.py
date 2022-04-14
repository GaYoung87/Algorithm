# citations = [3, 0, 6, 1, 5]  # 3
# citations = [10, 10, 10, 10, 10]  # 5
citations = [0, 0, 0, 0, 0]  # 0

def solution(citations):
    citations.sort()  # [0, 1, 3, 5, 6]
                      # [0, 1, 2, 3, 4]
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0   # 예외 조심!!

print(solution(citations))