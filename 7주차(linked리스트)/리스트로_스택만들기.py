class Node(object):
    def __init__(self, data, link):
        self.data = data
        self.link = link

    def __str__(self):  # 객체의 내부정보를 문자열로 반환
        return "data=%s, link=%s" % (self.data, self.link)

    def __repr__(self):  # JSON 문자열로 반환. 추후 JSON.parse()로 복구 위한 문자열
        return ""  # 리스트(파이썬) = 길이가 자동으로 변환  # {"data": 100, "link": None, "arr": [3, 7, "9"]}


n1 = Node(100, None)
