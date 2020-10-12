array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 right 와 pivot 교체. 피벗 값을 기준으로 왼쪽엔 작은 값만이, 오른쪽엔 큰 값만이 있으므로
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 값과 큰 값을 교체. 피벗을 기준으로 왼쪽엔 작은 값이, 오른쪽엔 큰 값이 있게 하기 위해
            array[right], array[left] = array[left], array[right]
    # 왼쪽 부분과 오른쪽 부분에서 각각 quick_sort 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array)-1)
print(array)
