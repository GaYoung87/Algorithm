def game(a, b):
    if a == '1' and b == '2':
        return b
    elif a == '1' and b == '3':
        return a
    elif a == '2' and b == '1':
        return a
    elif a == '2' and b == '3':
        return b
    elif a == '3' and b == '1':
        return b
    elif a == '3' and b == '2':
        return a
    elif a == b:
        return a

for t in range(int(input())):
    N = int(input())
    data = input().split()
    
