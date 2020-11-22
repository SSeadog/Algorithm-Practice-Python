# 떡볶이 떡 만들기


# 반복문으로 구현. 반복문이 재귀적으로 표현한 것보다 성능이 좋으므로

# n, m 입력
n, m = map(int, input().split())

# 떡의 개별 높이 입력
length = list(map(int, input().split()))

# start, end 초기화
start = 0
end = max(length)

# 최대 높이를 저장할 변수 초기화
h = 0

# start가 end보다 커지면 반복 종료
while start <= end:
    # mid 계산
    mid = (start + end) // 2
    # 잘린 떡 길이 총합 초기화
    s = 0
    # 절단기 높이보다 높은 경우만 계산
    for len in length:
        if len > mid:
            s += len - mid
    # 총합이 m보다 낮으면 더 자르기 위해 왼쪽 부분 탐색
    if s < m:
        end = mid - 1
    # 총합이 m보다 높으면 덜 자르기 위해 오른쪽 부분 탐색
    else:
        start = mid + 1
        # h 갱신 방법이 왜 여기서 이뤄져야 할지 잘 모르겠음
        # h의 최댓값을 구하기 때문에
        h = mid

print(h)

# # 이진 탐색으로 구현

# # 이진 탐색 함수 선언
# def binary_search(find, start, end):
#     mid = (start + end) // 2
#     # 잘린 길이 저장 변수 초기화
#     split_length = 0
#     for l in length:
#         # 절단기보다 긴 떡만 계산해서 추가
#         if l > mid:
#             split_length += l - mid
#     # 총 자른 길이가 M과 같으면 반환
#     if split_length == find:
#         return mid
#     # 총 자른 길이가 M보다 작으면 절단기 높이를 줄여서 떡을 더 자름
#     elif split_length < find:
#         return binary_search(find, start, mid-1)
#     # 총 길이가 M보다 크면 절단기 높이를 높여서 떡을 덜 자름
#     else:
#         return binary_search(find, mid+1, end)


# # n, m 입력
# n, m = map(int, input().split())

# # 떡의 개별 높이 입력
# length = list(map(int, input().split()))

# # 실행, 출력
# print(binary_search(m, 0, max(length)))
