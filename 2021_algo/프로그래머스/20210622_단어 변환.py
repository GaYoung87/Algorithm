def solution(begin, target, words):
    cnt = 0
    queue = [begin]

    while True:
        temp = []
        for q in queue:
            if q == target:
                return cnt
            
            for idx in range(len(words)-1, -1, -1):
                word2 = words[idx]
                # print('<word2>')
                # print(word2)

                diff = 0
                for a, b in list(zip(q, word2)):
                    if a != b:
                        diff += 1
            
                if diff == 1:
                    temp.append(words.pop(idx))
        #             print('<temp>')
        #             print(temp)
        # print('<temp_total>')
        # print(temp)
        
        if not temp:
            return 0
        
        queue = temp
        cnt += 1

    return cnt

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]  # 4

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log"]  # 0

