a = []

num = 100000

# 배열에 값 넣기
for n in range(num + 1):
    a.append(n)

# 2부터 특정 수의 배수 지우기
for n in range(2, num + 1):
    for m in range(n + n, num + 1, n):
        if a[m] == 0:
            continue
        a[m] = 0

# 소수 출력
for n in range(2, num+1):
    if a[n] != 0:
        print(a[n])
