# 시간초과 -> 실패!(1~14)
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if j <= len(numbers)-1 and numbers[j] > numbers[i]:
                answer.append(j)
                break

            if j == len(numbers)-1:
                answer.append(-1)

    answer.append(-1)

    return answer

# 해결1 : 기존에 -1로 셋팅해놓고, 있는 값만 넣으면 됨(이중for문) -> 실패!(1~19)
def solution(numbers):
    answer = [-1] * len(numbers)
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[j] > numbers[i]:
                answer[i] = numbers[j]
                break

    return answer


# 해결2 : 기존에 -1로 셋팅해놓고, stack 사용

# numbers = [2, 3, 3, 5]
# stack = [0] -> numbers[0]=2 < 3 -> answer[0] = 3
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer