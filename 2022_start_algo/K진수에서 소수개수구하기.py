def isPrime(x):
    for i in range(2,
                   int(x ** 0.5) + 1):  # TypeError: 'float' object cannot be interpreted as an integer에러는 range에서 정수부터 정수까지 진행되어야하는데 x**0.5는 소수가 나올 수 있다. 이를 정수로 바꿔줘야함.
        if x % i == 0:
            return False
    return True


def solution(n, k):
    k_word = ''

    while n:
        n, mod = divmod(n, k)
        k_word += str(mod)
    k_word = k_word[::-1]

    temp = k_word.split('0')
    print(temp)
    answer = 0
    for t in temp:
        if t:  # temp='110011'이면 temp=['11', '', '11']이므로 공백이 아닌경우만 소수인지 판별해야함
            if int(t) >= 2 and isPrime(int(t)):
                answer += 1

    return answer

n = 437674
k = 3  # result = 3
# n = 110011
# k = 10  # result = 2
