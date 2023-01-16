from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        candidates = []
        new_menu = {}
        for menu in orders:
            menu_li = list(''.join(menu))
            for li in combinations(menu_li, c):
                res = ''.join(sorted(li))  # 여기서 정렬안해주면, XW, WX를 다른것으로 인식함
                if res not in new_menu:
                    new_menu[res] = 1
                else:
                    new_menu[res] += 1
        sort_menu = sorted(new_menu.items(), reverse=True, key=lambda x: x[1])

        if len(sort_menu):  # sort_menu = []일 수 있음
            mymax = sort_menu[0][1]

            if mymax > 1:
                for i in sort_menu:
                    if i[1] == mymax:
                        answer.append(i[0])

    answer = sorted(answer)

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]  # ["AC", "ACDE", "BCFG", "CDE"]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]  # ["ACD", "AD", "ADE", "CD", "XYZ"]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]  # ["WX", "XY"]


