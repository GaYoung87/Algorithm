import sys
sys.stdin = open("4866input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    data = input()
    mystack = []
    for i in range(len(data)):  # 짝이 맞는지만 검사
        if data[i] == "(" or data[i] == "{":
            mystack.append(data[i])
        elif data[i] == ")" or data[i] == "}":
            if len(mystack) == 0:
                mystack.append((data[i]))  # 잘못된 문장
                break   # 잘못된 경우 발견시 종료
            elif (data[i] == ")" and mystack[-1] != "(") or (data[i] == "}" and mystack[-1] != "{"):
                mystack.append(data[i])   # 잘못된 문장
                break
            else:
                mystack.pop()
    if len(mystack) == 0:
        print('#{} {}'.format(tc, 1))  # 바른 문장
    else:
        print('#{} {}'.format(tc, 0))  # 올바르지 않은 문장
