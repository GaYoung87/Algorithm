def solution(s):
    answer = ""

    number = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
              "nine": 9}

    temp = ""
    for word in s:
        temp += word

        if temp in number:
            answer += str(number[temp])
            temp = ""
        if word.isdigit():
            answer += word
            temp = ""

    return int(answer)

s = "one4seveneight"  # 1478
# s = "23four5six7"  # 234567
# s = "2three45sixseven"  # 234567
# s = "123"  # 123