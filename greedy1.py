# 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# O(1)
# data를 정렬하고
data.sort()

# 정렬된 data에서 가장 큰 값과 그 다음 큰 값을 추출
B = data[-1]
b = data[-2]

# 두 번째 큰값이 더해지는 횟수는 m / k+1 의 몫
b_plus = int(m / (k + 1))
# 첫 번째 큰 값이 더해지는 횟수는 m에서 두 번째 큰 값이 더해지는 횟수를 뺀 것
B_plus = m - b_plus

# 수 * 횟수
result = B * B_plus + b * b_plus

print(result)


# O(n)
# data.sort()

# B = data[-1]
# b = data[-2]

# cnt = 0

# result = 0

# for i in range(m):
#     if cnt == k:
#         result += b
#         cnt = 0
#     else:
#         result += B
#         cnt += 1

# print(result)
