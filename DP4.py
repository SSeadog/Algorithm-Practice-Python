# 효율적인 화폐 구성

# n,m 입력
n, m = map(int, input().split())

# 화폐 종류 입력
currency = []
for _ in range(n):
    currency.append(int(input()))

# 결과를 저장할 리스트
r = [10001] * 10001

# 입력받은 화폐는 1번만에 가므로 입력
for c in currency:
    r[c] = 1

# 10000까지 계산, 화폐의 가장 큰값 다음부터
for i in range(max(currency)+1, 10001):
    # 최솟값을 구하기 위해 값들을 저장할 리스트
    s = []
    # i에서 화폐 종류들을 뺀 값을 s에 저장. i-c <= 이면 그 값은 저장하지 않음
    for c in currency:
        if i-c > 0:
            s.append(r[i-c])
    # i 전 값에서 최소 방법에 1을 더하여 i인덱스에 해당하는 값을 구함
    r[i] = min(s) + 1

# 값이 10001이라면 m값을 만드는 방법이 없다고 판단
if r[m] == 10001:
    print(-1)
else:
    print(r[m])
