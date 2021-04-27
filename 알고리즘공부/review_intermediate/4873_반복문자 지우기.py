for t in range(int(input())):
    word = list(input())

    stack = []
    for i in range(len(word)):
        if not stack or word[i] != stack[-1]:
            stack.append(word[i])
        elif word[i] == stack[-1]:
            stack.pop()
    print('#{} {}'.format(t + 1, len(stack)))
