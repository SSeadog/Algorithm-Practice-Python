# 문자열 뒤집기

# 0인 지역과 1인 지역의 개수를 구해서 적은 쪽의 개수가 최소 뒤집기 횟수

# s 입력
s = list(map(int, input()))

# 현재 무슨 지역인지 나타낼 변수 초기화
current = 2

# 지역의 개수를 저장할 변수 초기화
part = [0, 0]

# 0지역인지 1지역인지 순차 탐색
for p in s:
    # current와 p가 다르면 current에 p를 넣고 해당 지역 개수 1 증가
    if current != p:
        current = p
        part[p] += 1

print(min(part))
