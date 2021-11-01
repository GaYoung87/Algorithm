from itertools import combinations

def solution(relation):

    total = []
    y = len(relation[0])
    for i in range(1, y + 1):
        total.extend(combinations(range(y), i))

    # 유일성
    unique = []
    for t in total:
        temp = []
        for rel in relation:
            temp.append(tuple([rel[i] for i in t]))
        
        if len(set(temp)) == len(relation):
            unique.append(t)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)-1):
        for j in range(i+1, len(unique)):
            if len(set(unique[i])) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)


relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]
