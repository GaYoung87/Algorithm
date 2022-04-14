
# begin = "hit"
# target = "cog"
# words = ["hot", "git", "got", "dot", "dog", "lot", "log", "cog"]  # 4
# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log"]  # 0

# begin = "aab"
# target = "aba"
# words = ["abb", "aba"]

# begin = "hit"
# target = "hhh"
# words = ["hhh","hht"]

begin = "hot"
target = "lot"
words = ["hot", "dot", "dog", "lot", "log"]

from collections import deque

def solution(begin, target, words):

    answer = 0
    visit = [0 for _ in range(len(words))]
    q = deque()
    q.append([begin, 0])

    while q:
        print(q)
        check_word, cnt = q.popleft()

        if check_word == target:
            answer = cnt
            break

        for i in range(len(words)):
            same_cnt = 0
            if not visit[i]:
                for j in range(len(check_word)):
                    if check_word[j] != words[i][j]:
                        same_cnt += 1

                if same_cnt == 1:
                    q.append([words[i], cnt+1])
                    visit[i] = 1

    return answer


"""
Q. 뭐가 다른거지,,?
1. 실패
for j in range(len(check_word)):
    if check_word[j] == words[i][j]:
        same_cnt += 1

if same_cnt == 2:
    q.append([words[i], cnt + 1])
    visit[i] = 1
    
2. 성공
for j in range(len(check_word)):
    if check_word[j] != words[i][j]:
        same_cnt += 1

if same_cnt == 1:
    q.append([words[i], cnt + 1])
    visit[i] = 1
"""
print(solution(begin, target, words))