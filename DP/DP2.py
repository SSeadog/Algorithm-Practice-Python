# 개미 전사

# dp 바텀업 구현
# n 입력
n = int(input())

# 각 방의 식량 개수 입력
array = list(map(int, input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
d[2] = max(d[1], d[0] + array[2])
for i in range(3, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d)


# # dp 구현. dp의 의미를 잘 이해하지 못하고 제대로 구현 x. 결과는 제대로 나오는 듯
# # n 입력
# n = int(input())

# # 각 방의 식량 개수 입력
# k = list(map(int, input().split()))

# # 현재 인덱스 저장 변수, 결과 저장 변수 초기화
# i = 0
# result = 0

# # i가 k의 길이보다 작을 때만 반복
# while i < len(k):
#     # i + 1 이 k의 길이보다 짧으면 i번째와 i+1번째를 비교하며 계산
#     if i + 1 < len(k):
#         if k[i] >= k[i+1]:
#             result += k[i]
#             i += 2
#         else:
#             result += k[i+1]
#             i += 3
#     # i + 1 이 k의 길이보다 길거나 같으면 i번째 더하고 i += 1
#     else:
#         result += k[i]
#         i += 1

# print(result)
