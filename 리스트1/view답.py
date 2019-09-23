import sys
sys.stdin = open("input.txt", 'r')  # file redirection -> 내가 지정한 input.txt에서 읽어오겠다고 방향 재설정
                                    # 이 두줄 적으면 input.txt라는 파일에서 읽어옴


def getMax(idx):
    tmax = heights[idx - 2]

    if tmax < heights[idx - 1]; tmax = heights[idx - 1]
    if tmax < heights[idx + 1]; tmax = heights[idx + 1]
    if tmax < heights[idx + 2]; tmax = heights[idx + 2]

    return tmax


for tc in range(1, 11):  # 디버그모드로 돌리려면 break point로 간다.
    N = int(input())
    heights = list(map(int, input().split()))
    view = 0

    for i in range(2, N - 2):
        side = getMax(i)
        if side < heights[i]:
            view += heights[i] - side

    print('#%d %d' % (tc, view))