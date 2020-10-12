# 1로 만들기

# 점화식을 이용해 구현하기
# x 입력
x = int(input())

# 값 저장할 리스트 선언
a = [0] * 30001

# 2부터 반복할 시 a[1]에 대한 정보가 없으므로 수동으로 입력
a[1] = 1

# 다이나믹 바텀업. 2부터 x+1까지(range는 최대값 -1까지이기에) 반복. 1부터하면 수동으로 a[1] = 1 해줄 필요 없음
for n in range(1, x+1):
    # 계산된 값들을 저장할 리스트 선언
    b = []
    # 5로 나눠지면 나누고 횟수 +1 해서 b에 저장
    if n % 5 == 0:
        b.append(a[int(n/5)]+1)
    # 3으로 나눠지면 나누고 횟수 +1 해서 b에 저장
    if n % 3 == 0:
        b.append(a[int(n/3)]+1)
    #  2로 나눠지면 나누고 횟수 +1 해서 b에 저장
    if n % 2 == 0:
        b.append(a[int(n/2)]+1)
    # 1은 항상 계산 되니까 빼고 횟수 +1 해서 b에 저장
    b.append(a[n-1]+1)
    # 이중 최솟값을 구해서 a[n]에 저장. 그러므로 a[n]에는 항상 최솟값만 들어감
    a[n] = min(b)

# 출력
print(a[x])


# # 범위가 3만이니까 3만까지 최소 연산 구해서 배열에 저장해서 계산. 실패!
# # x 입력
# x = int(input())

# # 크기가 30001인 리스트 선언
# list = [10000] * 30001
# list[1] = 0
# list[2] = 1
# list[3] = 1
# list[5] = 1
# yeonsan = [1, 2, 3, 5]


# def func(a, index):
#     if index == 0:
#         if a + yeonsan[index] <= 30000 and list[a + yeonsan[index]] >= list[a] + 1:
#             n = a + yeonsan[index]
#             list[n] = list[a] + 1
#             for i in range(4):
#                 func(n, i)
#     else:
#         if a * yeonsan[index] <= 30000 and list[a * yeonsan[index]] >= list[a] + 1:
#             n = a * yeonsan[index]
#             list[n] = list[a] + 1
#             for i in range(4):
#                 func(n, i)


# func(1, 0)
# print(list[x])


# 혼자서 구상했으나 동적프로그래밍을 적용할 줄을 몰라서 헤맴. 엄청 이상한 방향으로 함
# # x 입력
# x = int(input())

# x1 = x
# x2 = x

# # 연산 횟수 초기화
# cnt1 = 0
# cnt2 = 0

# # x가 1이 될때까지 반복 5->3->2->1 순으로 가능한지 확인하며
# while x1 != 1:
#     if x1 % 5 == 0:
#         x1 /= 5
#     elif x1 % 3 == 0:
#         x1 /= 3
#     elif x1 % 2 == 0:
#         x1 /= 2
#     else:
#         x1 -= 1
#     cnt1 += 1
#     print("x1", x1)

# print(cnt1)

# # x가 뭔가의 제곱이 될때까지 빼기
# while x2 != 1:
#     for i in range(1, 7):
#         if x2 == 5 ** i:
#             x2 /= 5 ** i
#             cnt2 += i
#     if x2 % 3 == 0:
#         x2 /= 3
#         cnt2 += 1
#     if x2 % 2 == 0:
#         x2 /= 2
#         cnt2 += 1
#     if x2 > 1:
#         x2 -= 1
#         cnt2 += 1
#     print("x2", x2)

# print(cnt2)
