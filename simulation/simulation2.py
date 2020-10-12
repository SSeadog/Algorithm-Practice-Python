# 시각

n = input()

# 시계 구현 0번째 인덱스는 시간 1번째 인덱스는 분 2번째 인덱스는 초
clock = [0, 0, 0]

# 결과 저장
result = 0

# 시간이 n보다 작을 때까지만 반복
while clock[0] <= int(n):
    # 시분초에 3이 있다면 결과 1증가
    if clock[0] % 10 == 3 or int(clock[1] / 10) == 3 or clock[1] % 10 == 3 or int(clock[2] / 10) == 3 or clock[2] % 10 == 3:
        result += 1
    # 매 반복마다 초를 의미하는 2번째 인덱스에 1추가
    clock[2] += 1

    # 초가 60초가 되면 초를 0으로 바꾸고 분을 의미하는 1번째 인덱스에 1추가
    if clock[2] == 60:
        clock[2] = 0
        clock[1] += 1

    # 분이 60분이 되면 분을 0으로 바꾸고 시를 의미하는 0번째 인덱스에 1추가
        if clock[1] == 60:
            clock[1] = 0
            clock[0] += 1

print(result)
