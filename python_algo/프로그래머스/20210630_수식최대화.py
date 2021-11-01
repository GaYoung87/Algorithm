# expression = "100-200*300-500+20"  # 60420
expression = "50*6-3*2"  # 300

from itertools import permutations

def solution(expression):
    # 1.숫자랑 수식 분리
    expressions = expression.replace('-', ' - ').replace('*', ' * ').replace('+', ' + ')
    expressions_ls = expressions.split()

    # 2.수식의 우선순위
    oper = ['-', '*', '+']
    oper_ls = list(permutations(oper, 3))
    # print(expressions_ls)
    # print('------------------------')

    # 3.우선순위에 따른 결과계산
    mymax = 0
    for temp in oper_ls:
        # print('temp')
        # print(temp)
        copy_expressions_ls = expressions_ls[:]
        for t in temp:
            # print('t')
            # print(t)
            idx = 0
            while idx < len(copy_expressions_ls):
                if copy_expressions_ls[idx] == t:
                    # print('yes')
                    if t == '-':
                        val = int(copy_expressions_ls[idx-1]) - int(copy_expressions_ls[idx+1])
                        # print('minus')
                    elif t == '+':
                        val = int(copy_expressions_ls[idx-1]) + int(copy_expressions_ls[idx+1])
                        # print('plus')
                    else:
                        val = int(copy_expressions_ls[idx-1]) * int(copy_expressions_ls[idx+1])
                        # print('double')
                    copy_expressions_ls = copy_expressions_ls[:idx-1] + list(str(val).split()) + copy_expressions_ls[idx+2:]
                    # print(copy_expressions_ls)

                else:
                    # print('+1')
                    idx += 1
        # print('-------------------------------------')
        final_val = abs(int(copy_expressions_ls[0]))
        if mymax < final_val:
            mymax = final_val
    # print(mymax)

    return mymax


