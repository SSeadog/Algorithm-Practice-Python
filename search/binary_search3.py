# 정렬된 배열에서 특정 수의 개수 구하기

def get_start(li, t, start, end):
    mid = (end - start) // 2
    print(li[mid - 1], li[mid])
    if li[mid] == t and (mid == n - 1 or li[mid] != li[mid + 1]):
        return mid
    elif li[mid] >= t:
        return get_start(li, t, start, mid - 1)
    else:
        return get_start(li, t, mid + 1, end)


def get_last(li, t, start, end):
    mid = (end - start) // 2
    print(li[mid], li[mid + 1])
    if li[mid] == t and (mid == 0 or li[mid] != li[mid - 1]):
        return mid
    elif li[mid] > t:
        return get_last(li, t, start, mid - 1)
    else:
        return get_last(li, t, mid + 1, end)


n, x = map(int, input().split())

l = list(map(int, input().split()))

start = get_start(l, x + 1, 0, n)
end = get_last(l, x - 1, 0, n)

print(start-end)
