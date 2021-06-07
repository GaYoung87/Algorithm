# def solution(orders, course):
#     answer = []
#     return answer

from itertools import combinations

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]  # ["AC", "ACDE", "BCFG", "CDE"]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3]  # ["ACD", "AD", "ADE", "CD", "XYZ"]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]  # ["WX", "XY"]

check = {}
for number in course:
    for order in orders:
        if number <= len(order):
            menu_ls = list(combinations(sorted(order), number))
        
            for menu in menu_ls:
                print(menu)
                set_menu = ''.join(menu)
                if set_menu not in check:
                    check[set_menu] = 1
                else:
                    check[set_menu] += 1

temp = sorted(check.items(), key = lambda x: x[1], reverse=True)
print(temp)
[('AD', 3), ('CD', 3), ('AB', 2), ('AC', 2), 
('AE', 2), ('DE', 2), ('XY', 2), ('XZ', 2), 
('YZ', 2), ('ACD', 2), ('ADE', 2), ('XYZ', 2), 
('BC', 1), ('BD', 1), ('BE', 1), ('CE', 1), 
('ABC', 1), ('ABD', 1), ('ABE', 1), ('ACE', 1), 
('BCD', 1), ('BCE', 1), ('BDE', 1), ('CDE', 1)]
# ["ACD", "AD", "ADE", "CD", "XYZ"]
