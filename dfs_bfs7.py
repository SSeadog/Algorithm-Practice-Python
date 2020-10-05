# 연산자 끼워 넣기

# n 입력
n = int(input())

# An 입력
a = list(map(int, input().split()))

# 연산자 개수
op = list(map(int, input().split()))

# 결과 저장 리스트
result = []


def dfs(op_cnt, value, operation):
    if operation == 0:  # 더하기
        op_cnt[0] += 1
        value += a[sum(op_cnt)]
    elif operation == 1:  # 빼기
        op_cnt[1] += 1
        value -= a[sum(op_cnt)]
    elif operation == 2:  # 곱하기
        op_cnt[2] += 1
        value *= a[sum(op_cnt)]
    else:  # 나누기, c++ 방식으로 나눗셈이 제대로 안댐
        op_cnt[3] += 1
        cur = a[sum(op_cnt)]
        value = int(value/cur)
        print(value)

    # 연산을 다 했다면 그 결과 result에 저장
    if sum(op) == sum(op_cnt):
        return result.append(value)
    # 다 하지 않았다면 op_cnt 각항 최대를 넘지 않는 선에서 재귀 호출
    else:
        if op_cnt[0] < op[0]:
            dfs(op_cnt, value, 0)
        if op_cnt[1] < op[1]:
            dfs(op_cnt, value, 1)
        if op_cnt[2] < op[2]:
            dfs(op_cnt, value, 2)
        if op_cnt[3] < op[3]:
            dfs(op_cnt, value, 3)


for i in range(4):
    if op[i] > 0:
        dfs([0, 0, 0, 0], a[0], i)

print(max(result))
print(min(result))
# print((((((1-2)//3)+4)+5)*6))
# print(-(1//3))
# aa = -1
# bb = 3
# print(abs(aa)//bb)
