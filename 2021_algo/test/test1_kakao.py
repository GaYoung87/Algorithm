# s = "one4seveneight"   # 1478
s = "23four5six7"   # 234567
# s = "2three45sixseven"   # 234567
# s = "123"   # 123

def solution(s):
    words = ["zer","one","two","thr","fou","fiv","six","sev","eig","nin"]
    words_dic = {"zer":(4,"0"),"one":(3,"1"),"two":(3,"2"),"thr":(5,"3"),"fou":(4,"4"),"fiv":(4,"5"),"six":(3,"6"),"sev":(5,"7"),"eig":(5,"8"),"nin":(4,"9")}
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    answer = ""
    idx = 0
    while idx < len(s):
        if s[idx] in numbers:
            answer += s[idx]
            idx += 1
        else:
            letter = s[idx:idx+3]
            if letter in words:
                move_idx, numb = words_dic[letter][0], words_dic[letter][1]
                answer += numb
                idx += move_idx

    return answer