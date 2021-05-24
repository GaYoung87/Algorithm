def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):  # str.startswith(): 원하는 문자열 찾기
            return False
    return True

# phone_book = ["119", "97674223", "1195524421"]  # false
# phone_book = ["123","456","789"]  # true
phone_book = ["12","123","1235","567","88"]  # false
