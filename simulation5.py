# 럭키 스트레이트

# n 입력
n = list(map(int, input()))

# 반 자르고 각각 다른 배열에 저장
half = int(len(n)/2)
a = []
b = []
for i in range(half):
    a.append(n[i])
for i in range(half, len(n)):
    b.append(n[i])

# 각 부분의 합을 비교
if sum(a) == sum(b):
    print("LUCKY")
else:
    print("READY")
