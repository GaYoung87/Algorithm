def solution(begin, target, words):
    answer = 0
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]  # 4

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log"]  # 0

cnt = 0
queue = [begin]

while queue:
    for q in queue:
        if q == target:
            print(cnt)
            break
        
        diff = 0
        for a, b in list(zip(q, target)):
            if a != b:
                diff += 1
        
        if diff == 1:
            queue.append(q)
            
