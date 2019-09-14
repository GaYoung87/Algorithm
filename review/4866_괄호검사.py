for t in range(int(input())):
    word = list(input())

    result = 1
    stack = []
    for i in range(len(word)):
        if word[i] == '(' or word[i] == '{':
            stack.append(word[i])
        elif word[i] == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
        elif word[i] == '}' and stack:
            if stack[-1] == '{':
                stack.pop()
        elif word[i] == ')' and not stack:
            result = 0
        elif word[i] == '}' and not stack:
            result = 0

    if stack:
        result = 0

    print('#{} {}'.format(t + 1, result))