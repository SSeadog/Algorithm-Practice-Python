# 카드 정렬하기

# 8%에서 런타임 에러가 뜸

# n 입력
n = int(input())

# 카드 묶음 입력
cards = []
for _ in range(n):
    cards.append(int(input()))


# n번째까지 합을 저장할 리스트 선언
s = [0 for _ in range(100001)]

# 1번째까지의 합은 1번째 혼자이므로 그대로 넣어줌
s[0] = cards[0]

# 카드 오름차순으로 정렬
cards.sort()

# s[i]에 값이 있다면 그대로 리턴 값이 없다면 s[i]에 s[i-1] + cards[i]를 넣고 s[i] 리턴


def sum_card(i):
    if s[i] == 0:
        s[i] = sum_card(i-1) + cards[i]
    return s[i]


sum_card(n-1)
if n == 1:
    print(s[0])
else:
    print(sum(s[1:n]))
