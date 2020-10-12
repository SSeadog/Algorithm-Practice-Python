# 실패율

from collections import deque

# n 입력
n = int(input())

# stages 입력
stages = list(map(int, input().split()))

# 사람 수 저장
total = len(stages)

# stages 오름차순으로 정렬
stages.sort()

cnt = 1

q = deque()

# 스테이지 별로 (스테이지, 개수) 형식으로 저장
for i in range(1, len(stages)):
    if stages[i] == stages[i-1]:
        cnt += 1
    else:
        q.append((stages[i-1], cnt))
        cnt = 1
# 마지막항 계산
q.append((stages[-1], cnt))

rates = []

for i in range(1, n + 1):
    if q:
        # i 스테이지에서 멈춘 사람이 있다면
        if i == q[0][0]:
            stage, person = q.popleft()
            rate = person / total
            rates.append((rate, stage))
            total -= person
        # i 스테이지에서 멈춘 사람이 없다면
        else:
            rate = 0
            rates.append((rate, i))
    # 큐가 비었다면 남은 스테이지는 사람들이 도달하지 못한 것이므로 실패율을 0으로 지정
    else:
        rate = 0
        rates.append((rate, i))

rates = sorted(rates, key=lambda x: (-x[0], x[1]))

answer = []
for rate in rates:
    answer.append(rate[1])
print(answer)
