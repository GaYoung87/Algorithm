import sys
sys.stdin = open("4873input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    data = list(input())
    n = len(data)
    stack = []
    for i in range(n):
        if not stack or stack[-1] != data[i]:
            stack.append(data[i])
        elif stack and stack[-1] == data[i]:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))