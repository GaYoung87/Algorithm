import sys
sys.stdin = open("1267input.txt", "r")

TC = 10
for tc in range(1, TC + 1):
    mynode, mykube = map(int, input().split())
    mymap = [[0] * (mynode + 1) for i in range(mynode + 1)]  # 2차원 맵 생성
    # 간선 정보 입력
    data = list(map(int, input().split()))
    n = int(len(data) / 2)  # 나누기 결과 실수 -> 정수로 변환 필요
    for i in range(n):
        start = data[i * 2]
        end = data[i * 2 + 1]
        mymap[end][start] = 1

    result = []  # 작업 경로 저장
    while True:
        if len(result) == mynode:  # 전체 노드가 경로에 저장되면 검색 중단
            break
        start_col = []
        for col in range(1, len(mymap)):  # 모든 칼럼을 검색
            if 1 not in mymap[col] and col not in result:  # 작업 경로에 등록 안된
                start_col.append(col)  # 출발 가능한 노드 등록

        for col in start_col:
            result.append(col)   # 출발 가능한 노드를 작업 경로에 등록
            for row in range(len(mymap)):
                mymap[row][col] = 0   # 출발하는 노드로 연결되는 정보 삭제

    print('#{}'.format(tc), end=' ')
    for i in result:
        print('{}'.format(i), end=' ')
    print()