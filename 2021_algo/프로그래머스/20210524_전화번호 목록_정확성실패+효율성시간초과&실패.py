def solution(phone_book):
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                return False

    return True



# phone_book = ["119", "97674223", "1195524421"]  # false
phone_book = ["123","456","789"]  # true
# phone_book = ["12","123","1235","567","88"]  # false

print(solution(phone_book))

