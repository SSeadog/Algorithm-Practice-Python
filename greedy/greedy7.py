# 만들 수 없는 금액

# 나동빈씨의 해결 방법을 이용

# 동전 개수 n 입력
n = int(input())

# 동전 종류 coin 입력
coin = list(map(int, input().split()))

# coin 오름차순으로 정렬
coin.sort()

# target-1까지 만들 수 있다는 의미를 위해 target 선언
target = 1

# target을 갱신하며 target보다 작은 동전이 없다면 target을 만들 수 없으므로 종료
for c in coin:
    if c > target:
        break
    else:  # c가 target보다 작으면 target-1+c까지 금액을 만들 수 있으므로 target에 더해줌
        target += c

print(target)


# # 마땅한 방안이 안 떠오름

# # 동전 개수 n 입력
# n = int(input())

# # 동전 종류 coin 입력
# coin = list(map(int, input().split()))

# # coin 내림차순으로 정렬
# coin.sort(reverse=True)

# # coin에 마지막항에 0을 넣음
# coin.append(0)

# # 결과 저장 변수
# result = 0

# print(coin)

# n = 1

# while not result:
#     current = n
#     for i in coin:
#         if i == 0:
#             result = n
#         if i > n:
#             continue
#         else:
#             current -= i
#             if current == 0:
#                 break
#     n += 1
#     print(n)

# print(result)
