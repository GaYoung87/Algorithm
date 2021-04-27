# 역순으로 진행이 되는 것이면 스택을 사용할 수 있는 문제인지 의심

stack = [0] * 10
top = -1

# push
for i in range(3):
    stack[top + 1] = i
    top += 1

# pop
for i in range(3):
    t = stack[top]
    top -= 1
    print(t)