orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3, 5]  # ["ACD", "AD", "ADE", "CD", "XYZ"]

from itertools import combinations

answer = []
for num in course:
    total = {}
    for order in orders:
        if (num > len(orders)):
            continue
        li = list(map(''.join, combinations(sorted(order), num)))

        for key in li:
            if key not in total:
                total[key] = 1
            else:
                total[key] += 1

    res = sorted(total.items(), key = lambda x:x[1], reverse=True)
    # [('AD', 3), ('CD', 3), ('AB', 2), ('AC', 2), ('AE', 2), ('DE', 2), 
    # ('XY', 2), ('XZ', 2), ('YZ', 2), ('BC', 1), ('BD', 1), ('BE', 1), ('CE', 1)]
    
    # [('ACD', 2), ('ADE', 2), ('XYZ', 2), ('ABC', 1), ('ABD', 1), ('ABE', 1), 
    # ('ACE', 1), ('BCD', 1), ('BCE', 1), ('BDE', 1), ('CDE', 1)]
    # print(res)

    if res:
        temp = res[0][1]
        for a, b in res:
            if b == temp and b >= 2:
                answer.append(a)
print(sorted(answer))
