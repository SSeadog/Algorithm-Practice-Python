# 숫자 카드 게임

# O(n)
# n, m = map(int, input().split())

# min_data = []

# for i in range(n):
#     data = list(map(int, input().split()))
#     min_data.append(min(data))

# max_in_min_data = max(min_data)

# print(max_in_min_data)

# O(n)
n, m = map(int, input().split())

# 작은 수 중에서 가장 큰 수를 0으로 초기화
max_in_min_data = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 작은 수 저장
    min_data = min(data)
    # 작은 수가 작은 수 중 큰 수보다 크면 갱신
    if min_data > max_in_min_data:
        max_in_min_data = min_data

print(max_in_min_data)
