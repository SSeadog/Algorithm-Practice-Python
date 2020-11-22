# 고정점 찾기

# 이진 탐색으로 구현
# 이진 탐색에 대한 이해가 부족함 아직

n = int(input())

array = list(map(int, input().split()))


def binary_search(array, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    elif array[mid] < mid:
        return binary_search(array, mid+1, end)


result = binary_search(array, 0, len(array)-1)

print(result)
