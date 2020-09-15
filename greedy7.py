# 만들 수 없는 금액

# 마땅한 방안이 안 떠오름

# 동전 개수 n 입력
n = int(input())

# 동전 종류 coin 입력
coin = list(map(int, input().split()))

# coin 내림차순으로 정렬
coin.sort(reverse=True)

# coin에 마지막항에 0을 넣음
coin.append(0)

# 결과 저장 변수
result = 0

print(coin)

n = 1

while not result:
    current = n
    for i in coin:
        if i == 0:
            result = n
        if i > n:
            continue
        else:
            current -= i
            if current == 0:
                break
    n += 1
    print(n)

print(result)
