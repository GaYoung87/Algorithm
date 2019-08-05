# 열 우선 순회
for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j]

# 행의 지그재그 순회
for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j + (m-1-2*j) * (i%2)]  # m은 Array 갯수

# 어떤 수 i 에서 j번째 bit는?
if i & (1 << j)

# 비트 연산자 -> 간결하게 부분집합을 생성하는 방법
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1<<n)  # 1<<n: 부분 집합의 갯수
    for j in range(n):
        if i & (1 << j):  # 원소의 수만큼 비
            print(arr[j], end=', ')
    print()
print()


# 검색 - 정렬안됨
def sequentialSearch2(a, n, key):
	i = 0
    while i < n and a[i] != key: #i가 n보다 작고, a[i]가 검색할 key와 != 라면,
    	i = i + 1 # 검색될 i의 수를 늘려줘서 a[i] 즉, 비교대상을 바꿔준다.
        
    if i < n:
    	return i
    else:
    	return -1

# 검색 - 정렬
def sequentialSearch2(a, n, key):
	i = 0
    while i < n and a[i] < key:
    	i = i + 1


# 이진 검색 (범위 재조정)
def BinarySearch(a, key):
    start = 0 # 시작점
    end = len(a) - 1  # 종료점
​
    while start <= end:
        middle = start + (end - start) // 2 # 임시로 middle 지정, -> middle은 계속 달라진다.
        
        if key == a[middle]: # key와 임시 가운데 인덱스를 통한 리스트 원소가 == 일시,
            return True # 검색 성공
        
        elif key < a[middle]: # 그렇지 않고 더 크면
            end = middle - 1 # 종료점은 가운데에서 -1을 한 값이 된다.
        else:
            start = middle + 1 # 더 작으면, 가운데에서 +1을 한 값이된다.
​
    return False # 검색 실패


# 선택 검색
def select(list, k):
    for i in range(0, k):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list[k-1]


# 정렬
# 버블정렬 : 두개 비교
# 선택 알고리즘 : 하나의 값과 뒤에 있는 모든 값과 비교
