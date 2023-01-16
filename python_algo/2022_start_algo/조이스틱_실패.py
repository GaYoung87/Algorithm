# name = "JEROEN"  # 56
# name = "JAN"  # 23
name = "BBBAAAAAAAB"  # 8


"""
1. 글자마다 최소 이동횟수 찾기
2. 오른쪽 왼쪽 이동하면서 최소 횟수 찾기
"""


def solution(name):
    i = 0
    answer = 0
    name = list(name)

    while True:

        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        name[i] = 'A'
        print('name')
        print(name)

        if name.count("A") == len(name):
            return answer

        left, right = 1, 1

        for x in range(1, len(name)):
            if name[i - x] == 'A':
                left += 1
            else:
                break

        for y in range(1, len(name)):
            if name[i + y] == 'A':
                right += 1
            else:
                break
        print('left, right')
        print(left, right)

        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right
        print('i')
        print(i)
        print('answer')
        print(answer)
        print('-------------------------------')

print(solution(name))

