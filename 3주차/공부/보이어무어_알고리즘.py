# <개념>
# 1. part 끝 문자와 text의 현재 위치의 문자가 일치하는지 검사
# 2. 끝이 일치하면 part과 text를 다 검사.
#    마지막까지 일치하지 않으면 len(part)만큼 skip
# 3. 끝이 일치하지않으면 text의 현재위치 문자가 skip배열에 있는지 확인.
#    있으면 인덱스만큼 skip, 없으면 패턴길이만큼 skip

# <아이디어>
# rithm 문자열의 skip 배열 : m h t i r 다른문자
#                           0 1 2 3 4 5
# 전체 string : a pattern matching algorithm
# 부분 string : rithm  -> 비교1 : t m이라 일치X -> t -> 2skip

# 전체 string : a pattern matching algorithm
# 부분 string :   rithm  -> 비교2 : e m이라 일치X -> e -> 5skip

# 전체 string : a pattern matching algorithm
# 부분 string :        rithm  -> 비교3 : a m이라 일치X -> a -> 5skip

# 전체 string : a pattern matching algorithm
# 부분 string :             rithm  -> 비교4 : n m이라 일치X -> n -> 5skip

# 전체 string : a pattern matching algorithm
# 부분 string :                  rithm  -> 비교5 : g m이라 일치X -> g -> 5skip

# 전체 string : a pattern matching algorithm
# 부분 string :                       rithm  -> 비교6 : h m이라 일치X -> h -> 1skip

# 전체 string : a pattern matching algorithm
# 부분 string :                        rithm  -> 비교7 : m m이라 일치 -> htir순으로 확인


# <시간복잡도>
# 보통: O(N), 최악: O(N + M)


# 알고리즘
text = 'an algorithm pattern matching algorithm'
part =        'rithm'

def bm_algo(text, pattern):
    i = len(text)
    j = len(pattern)

    text_index = j - 1
    pattern_index = j - 1  # rithm을   m h t i r 로 바꾸어 인덱스 지정
    count = 0   # pattern이 나오는 횟수

    while text_index < i:
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                count += 1
                text_index = text_index + j
                pattern_index = j - 1
            else:
                text_index -= 1
                pattern_index -= 1
        else:
            while pattern_index >= 0:
                if text[text_index] == pattern[pattern_index]:
                    text_index = text_index + j - (pattern_index + 1)
                    pattern_index = j - 1
                    break
                else:
                    pattern_index -= 1
            if pattern_index == -1:
                text_index = text_index + j
                pattern_index = j - 1

    return count

print(bm_algo(text, part))
 