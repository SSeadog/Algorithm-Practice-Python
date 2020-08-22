import math

n = 1000
# 모두 소수인 것으로 초기화
array = [True for _ in range(n+1)]

result = []

# n의 제곱근까지만 확인
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        # 소수이면 자기 빼고 다음 배수부터 n되기 전까지 F로 바꿔줌
        for m in range(i+i, n, i):
            array[m] = False

for a in range(2, n+1):
    if array[a]:
        print(a, end=' ')

# a = []

# num = 100000

# # 배열에 값 넣기
# for n in range(num + 1):
#     a.append(n)

# # 2부터 특정 수의 배수 지우기
# for n in range(2, num + 1):
#     for m in range(n + n, num + 1, n):
#         if a[m] == 0:
#             continue
#         a[m] = 0

# # 소수 출력
# for n in range(2, num+1):
#     if a[n] != 0:
#         print(a[n])
