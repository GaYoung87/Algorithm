'''
십진수를 이진수로 바꾼다는 것
    ex) x=10 -> 10//2=5...0, 5//2=2...1, 2//2=1...0, 1//2=0...1
        => x = 1010(2)
'''

'''
진수표현시 0~9까지는 0~9, 10부터는 A, B, ,,,
'''

Conversion = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9,
        'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}

def binary(number):
    global result

    mok, nam = 0, 0
    for i in range(4):  # 2진수 4자리로 표현되므로 1도 0001로 표현
        mok = number // 2
        nam = number % 2
        result = str(nam) + result
        number = mok

    return result


for t in range(int(input())):
    length, ls = map(str, input().split())  # 4 47FE

    result_final = ''
    for l in ls:
        result = ''
        binary(Conversion[l])
        result_final += result

    print('#{} {}'.format(t+1, result_final))
