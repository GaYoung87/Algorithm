def solution(phone_book):
    # 갯수가 작은거 부터 확인! -> 접두어 확인시 무조건 다음값이 크다
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                return False

    return True


def solution(phone_book):
    # 갯수가 작은거 부터 확인! -> 접두어 확인시 무조건 다음값이 크다
    phone_book.sort()
    
    answer = True
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break

    return answer




# phone_book = ["119", "97674223", "1195524421"]  # false
phone_book = ["123","456","789"]  # true
# phone_book = ["12","123","1235","567","88"]  # false

print(solution(phone_book))