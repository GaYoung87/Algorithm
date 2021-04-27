def calc(x, y, eq):
    if eq == '+':
        return x + y
    if eq == '-':
        return x - y
    if eq == '*':
        return x * y
    if eq == '/':
        return x // y

for t in range(int(input())):
    data = list(input().split())
    word = ['+', '-', '*', '/']
    stack = []
    for i in range(len(data)):
        if data[i] not in word and data[i] != '.':
            stack.append(data[i])
        elif data[i] in word:
            if len(stack) >= 2:
                a = int(stack.pop(-2))
                b = int(stack.pop(-1))
                stack.append(calc(a, b, data[i]))
            else:
                result = 'error'
                break
        elif data[i] == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'

    print('#{} {}'.format(t + 1, result))