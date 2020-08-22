# 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 큰 수가 몇번 더해졌는지 data의 인덱스, 더해진 횟수 저장
big = [0, 0]

r = 0

for _ in range(m):
    max = 0
    d = 0
    # 큰 값을 구하고 big에 큰값의 인덱스 저장
    while d < len(data):
        if data[d] > max:
            if big[1] == k:
                print("k full")
            else:
                max = data[d]
                big[0] = d
        d += 1
    r += max
    big[1] += 1
    print(k, big[1])

print(r)
