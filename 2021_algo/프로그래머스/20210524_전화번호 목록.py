def solution(phone_book):
    # 갯수가 작은거 부터 확인! -> 접두어 확인시 무조건 다음값이 크다
    phone_book.sort()
    
    # 효율성 시간초과 해결하기 위해서는 for문을 하나로 줄여야한다.
    # 앞에서 정렬을 했기때문에 앞뒤로만 확인해도 충분하다...?
    for i in range(len(phone_book) - 1):
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
            return False

    return True


# phone_book = ["119", "97674223", "1195524421"]  # false
phone_book = ["123","456","789"]  # true
# phone_book = ["12","123","1235","567","88"]  # false

print(solution(phone_book))