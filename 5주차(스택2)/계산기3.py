def calc(x, y, eq):
    if eq == '+':
        return x + y
    elif eq == '-':
        return x - y
    elif eq == '*':
        return x * y
    elif eq == '/':
        return x // y

def priority(word):
    if word == "*" or word == "/":
        return 2
    elif word == "+" or word == "-":
        return 1
    elif word == "(" or word == ")":
        return 0
    return -1

for t in range(1):
    N = int(input())
    data = input()
    number = ''
    stack = []
    # print(data)
    for num in data:
        if '0' <= num <= '9':
            number.append(int(num))
        else:
            if num == '(':
                stack.append('(')
            elif num == ')':
                while True:
                    ch = stack.pop()
                    if ch == '(':
                        break
                    number.append(ch)
            
            