orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3]  # ["ACD", "AD", "ADE", "CD", "XYZ"]

from itertools import combinations

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
    print(res)

