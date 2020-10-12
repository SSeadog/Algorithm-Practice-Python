# 모험가 길드

# 공포도를 레벨에 따라 저장한 후 그 개수를 각 레벨만큼 나눠서 나온 몫을 결과에 저장하는 방식으로 품

# n 입력
n = int(input())

# 공포도 입력
fear = list(map(int, input().split()))

# 공포도 리스트 정렬 내림차순으로
fear.sort(reverse=True)

# 공포도를 레벨에 따라 저장할 리스트
level = [0] * (n+1)

# 공포도를 레벨에 따라 저장
for f in fear:
    level[f] += 1

# 총 그룹 개수를 저장할 변수
result = 0

# 각 레벨을 i로 나눠서 나온 몫을 결과에 저장
for i in range(1, n+1):
    mok = level[i] // i
    result += mok

# 출력
print(result)
