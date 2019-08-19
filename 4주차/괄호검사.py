# data1 = '()()((()))'
# data2 = '((()((((()()((()())((())))))'

# def check(text):
#     stack = [0] * len(text)
#     top = -1
#     for i in range(len(text)):   
#         if text[i] == '(': 
#             stack[i] = '('
#         elif text[i] == ')':
#             try:

#             except IndexError:
#                 return False
        
#     # elif i == ')':
#     #     try:
#     #         t = stack[top]
#     #         top -= 1
#     return stack

# # print(check(data1))


# 선생님 코드
stack = [0] * 100
top = -1
str_ = '(()()))'

correct = True
for i in range(len(str_)):
    if str[i] == '(':  # push
        top += 1
        stack[top] = str[i]
        print(stack)
#     elif str[i] == '(':  # pop
#         if top == -1:
#             correct = False
#             break
#         top -= 1

# if top == -1 and correct:
#     print('Correct!')
# else:
#     print('Wrong..')