
    answer = [[]]


# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# # result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

def check(answer):
    for x, y, a in answer:
        # 기둥이 가능한 경우
        # 1) 바닥 위에 있기
        # 2) 보의 한쪽 끝 부분 위에 있기
        # 3) 다른 기둥 위에 있기
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:  # 설치 성공, 삭제 실패
                # print("기둥one")
                pass  # 기둥 설치 - 가능
                      # 기둥 제거 - 불가능
            else:
                # print("기둥two")
                return False  # 설치실패, 삭제 성공

        # 보가 가능한 경우
        # 1) 한쪽 끝 부분이 기둥 위에 있기
        # 2) 양쪽 끝 부분이 다른 보와 동시에 연결되어 있기
        if a == 1:
            # print(x, y, a)
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                # print("보one")
                pass  # 보 설치 - 가능
                      # 보 삭제 - 불가능
            else:
                # print("보two")
                return False  # 보 설치 - 불가능

    return True  # 기둥이나 보 설치 - 온전하게 가능

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            answer.append([x, y, a])  # 일단 넣고, 설치 가능하면 유지, 설치 못하는 케이스면 빼기
            if not check(answer):
                answer.remove([x, y, a])
            # print(answer)

        else:  # 삭제
            answer.remove([x, y, a])
            if check(answer) is False:  # 만약, 빼도 무관하다면 remove된 상태로 유지
                                        # 만약, 빼면 절대로 안된다면 remove다시 append해주기
                answer.append([x, y, a])

    return sorted(answer)