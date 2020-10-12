# 위에서 아래로

# 데이터의 개수 입력 받기
n = int(input())

# 리스트에 값 넣기
list = []
for _ in range(n):
    list.append(int(input()))

# 정렬한 리스트를 한 요소씩 띄워서 출력
for i in sorted(list, reverse=True):
    print(i, end=" ")
