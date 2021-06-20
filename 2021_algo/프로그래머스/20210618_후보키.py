def solution(relation):
    answer = 0
    return answer


relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

from itertools import combinations

total = []
y = len(relation[0])
for i in range(1, y + 1):
    total.extend(combinations(range(y), i))
print(total)


