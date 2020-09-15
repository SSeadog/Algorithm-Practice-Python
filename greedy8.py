# 볼링공 고르기

# n, m 입력
n, m = map(int, input().split())

# 공의 각 무게 입력
ball = list(map(int, input().split()))

# 경우의 수를 저장할 result 선언
result = 0

# 첫번째부터 n번째까지 반복
for i in range(n):
    # i+1부터 n까지 반복
    for j in range(i+1, n):
        # 두 공의 무게가 같으면 추가 안함
        if ball[i] == ball[j]:
            continue
        # 공의 무게가 다르면 경우의 수 1 추가
        result += 1

print(result)
