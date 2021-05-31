from itertools import combinations

def solution(orders, course):
    answer = []
    check = {}

    for order in orders:
        for i in course:
            menu = list(combinations(order, i))
            print(menu)

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]  # ["AC", "ACDE", "BCFG", "CDE"]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]  # ["ACD", "AD", "ADE", "CD", "XYZ"]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]  # ["WX", "XY"]

answer = []
check = {}

for order in orders:
    for i in course:
        menu_ls = list(combinations(order, i))
        
        for menu in menu_ls:
            set_menu = ''.join(menu)
            if set_menu not in check:
                check[set_menu] = 1
            else:
                check[set_menu] += 1

print(check)

for menu, cnt in check.items():  # key, value 한번에 다뽑고싶으면 .itmes()
    if cnt >= 2:
        answer.append(menu)
print(answer)


# 문제점: BC:2, BCF:2, BCFG: 2 -> BCFG만 최종적으로 선택되어야함