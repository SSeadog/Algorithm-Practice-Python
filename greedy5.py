# 곱하기 혹은 더하기

# s 입력
s = list(map(int, input()))

# 결과를 저장할 변수
result = 0

# 첫번째 값은 무조건 더해야 하므로 result에 더함
result = s[0]

# 첫번째 항은 계산했기에 2번째 항부터 반복
for i in s[1:]:
    # i가 0,1이거나 result가 0이면 i를 result에 더해줌
    if i <= 1 or result <= 1:
        result += i
    # 그 외는 곱해줌
    else:
        result *= i

print(result)
