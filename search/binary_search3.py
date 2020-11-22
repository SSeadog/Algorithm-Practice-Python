# 정렬된 배열에서 특정 수의 개수 구하기

def get_first(li, t, start, end):
    mid = (end + start) // 2
    # 이 발상이 전혀 가능해 보이지 않는데..
    if li[mid] == t and (mid == 0 or t > li[mid - 1]):
        return mid
    elif li[mid] >= t:
        return get_first(li, t, start, mid - 1)
    else:
        return get_first(li, t, mid + 1, end)


n, x = map(int, input().split())

l = list(map(int, input().split()))

if x <= l[n - 1]:
    first = get_first(l, x, 0, n - 1)
else:
    first = n - 1
if x + 1 <= l[n - 1]:
    last = get_first(l, x + 1, 0, n - 1)
else:
    last = n - 1

if first == last:
    print(-1)
else:
    print(last - first)
