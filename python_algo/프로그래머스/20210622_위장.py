clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]  # 5
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]  # 3

def solution(clothes):
    check = {}
    for a, b in clothes:
        if b not in check:
            check[b] = 1
        else:
            check[b] += 1

    cnt = 1
    for num in check.values():
        cnt *= (num + 1)

    return cnt - 1
