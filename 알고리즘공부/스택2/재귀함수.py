# ctrl + d : 줄 삭제
# ctrl + Alt + 아래쪽 화살표 : 줄 복사
# Alt + 위아래 : 줄 이동

print(__name__)
# n = 3 + 2 + 1

def my_sum(num):
    # 멈춤조건
    if num == 1:
        return 1
    return num + my_sum(num - 1)


n = my_sum(3)
print(n)