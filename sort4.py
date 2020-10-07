# 국영수

# n 입력
n = int(input())

# 이름, 국어, 영어, 수학 리스트 입력
score = []
for _ in range(n):
    a, b, c, d = input().split()
    score.append([a, int(b), int(c), int(d)])
# 주어진 조건이 여러 개일시 람다식을 이용해 간편하게 할 수 있었음
score = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in score:
    print(s[0])
