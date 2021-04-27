'''
삽입정렬
1. 개념: 아직 정렬되어있지 않은 값을 이미 정렬된 배열 사이에 끼워 넣는 과정
2. 시간복잡도: 1) 정렬되어있는 경우: O(n)
             2) 정렬되어있지 않은 경우: O(n^2)
'''
unsorted_list = [4, 8, 0, 2, 4, 1, 9, 3]
def insertion_sort(unsorted_list):
    for j in range(1, len(unsorted_list)):
        key = unsorted_list[j]
        print(key)
        i = j - 1
        while i >= 0 and unsorted_list[i] > key:
            unsorted_list[i+1] = unsorted_list[i]
            i -= 1
        unsorted_list[i+1] = key

    return unsorted_list

print(insertion_sort(unsorted_list))