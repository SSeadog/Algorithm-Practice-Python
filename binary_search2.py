# 떡볶이 떡 만들기

# 이진 탐색으로 구현

# 이진 탐색 함수 선언
def binary_search(find, start, end):
    mid = (start + end) // 2
    # 잘린 길이 저장 변수 초기화
    split_length = 0
    for l in length:
        # 절단기보다 긴 떡만 계산해서 추가
        if l > mid:
            split_length += l - mid
    # 총 자른 길이가 M과 같으면 반환
    if split_length == find:
        return mid
    # 총 자른 길이가 M보다 작으면 절단기 높이를 줄여서 떡을 더 자름
    elif split_length < find:
        return binary_search(find, start, mid-1)
    # 총 길이가 M보다 크면 절단기 높이를 높여서 떡을 덜 자름
    else:
        return binary_search(find, mid+1, end)


# n, m 입력
n, m = map(int, input().split())

# 떡의 개별 높이 입력
length = list(map(int, input().split()))

# 실행, 출력
print(binary_search(m, 0, max(length)))
