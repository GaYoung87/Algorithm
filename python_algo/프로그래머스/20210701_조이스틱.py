def solution(name):
    answer = 0
    return answer

name = "JEROEN"  # 56
# name = "JAN"  # 23
# name = "BAZAAAAB"

make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
