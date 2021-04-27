def calc(x, y, eq):
    if eq == '+':
        return x + y
    elif eq == '-':
        return x - y
    elif eq == '*':
        return x * y
    elif eq == '/':
        return x // y

# stack 안에서의 우선순위
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
# stack 밖에서의 우선순위
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

for t in range(10):
    N = int(input())
    data = input()
    number = []
    stack = []
    # print(data)
    for i in data:
        if '0' <= i <= '9':
            number.append(int(i))
        else:
            if i == '(':
                stack.append('(')
            elif i == ')':
                while True:
                    j = stack.pop()
                    if j == '(':
                        break
                    number.append(j)
            else:
                if stack:
                    if isp[stack[-1]] > icp[i]:
                        k = stack[-1]
                        while isp[k] > icp[i]:
                            number.append(stack.pop())
                            if not stack:
                                break
                            k = stack[-1]
                        stack.append(i)
                    else:
                        stack.append(i)        
                else:
                    stack.append(i)
    # print(stack)
    # print(number)

    for _ in range(len(stack)):
        number.append(stack.pop())

    result = 0
    stack2 = []
    for num in number:
        if type(num) == int:
            stack2.append(num)
        else:
            b = int(stack2.pop())
            a = int(stack2.pop())
            stack2.append(calc(a, b, num))

    print('#{} {}'.format(t+1, calc(a, b, num)))
