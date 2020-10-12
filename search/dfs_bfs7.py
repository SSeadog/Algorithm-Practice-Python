# 연산자 끼워 넣기


# 재귀 함수 호출할 때 변수들이 공유되는 거 같음. 다른 방식으로 해야 할듯
# dfs 호출 방식을 바꿔서 해결
# 나중에 또 봐야 할듯

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
        value += a[sum(op_cnt)]
    elif operation == 1:  # 빼기
        value -= a[sum(op_cnt)]
    elif operation == 2:  # 곱하기
        value *= a[sum(op_cnt)]
    elif operation == 3:  # 나누기, c++ 방식으로 나눗셈이 제대로 안댐
        cur = a[sum(op_cnt)]
        if value < 0:
            value = abs(value)//cur
            value *= -1
        else:
            value = value//cur

    # 연산을 다 했다면 그 결과 result에 저장
    if sum(op) == sum(op_cnt):
        return result.append(value)
    # 다 하지 않았다면 op_cnt 각항 최대를 넘지 않는 선에서 재귀 호출
    else:
        if op_cnt[0] < op[0]:
            # 재귀호출하기 전, 더하기 횟수 증가를 위해
            op_cnt[0] += 1
            dfs(op_cnt, value, 0)
            # 더하기 횟수가 더해진 채로 다음 함수가 호출되었고, 아래 조건문에서 적용되면 안되기 때문에 다시 빼줌
            op_cnt[0] -= 1
        if op_cnt[1] < op[1]:
            op_cnt[1] += 1
            dfs(op_cnt, value, 1)
            op_cnt[1] -= 1
        if op_cnt[2] < op[2]:
            op_cnt[2] += 1
            dfs(op_cnt, value, 2)
            op_cnt[2] -= 1
        if op_cnt[3] < op[3]:
            op_cnt[3] += 1
            dfs(op_cnt, value, 3)
            op_cnt[3] -= 1


for i in range(4):
    if op[i] > 0:
        op_cnt = [0, 0, 0, 0]
        op_cnt[i] += 1
        dfs(op_cnt, a[0], i)

print(max(result))
print(min(result))
