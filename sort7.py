# 카드 정렬하기

# 최소 힙에 넣고 두개를 빼서 더한 뒤 다시 힙에 넣어서 합을 구하는 게 더 효율적일 듯

import heapq

# n 입력
n = int(input())

# 카드 묶음을 힙에 넣음
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))

# 결과 저장 변수
result = 0

while len(h) > 1:
    # 힙에서 최소 값 두개를 꺼낸 뒤 더해서 다시 힙에 넣음
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    heapq.heappush(h, a+b)
    result += a+b
print(result)


# 8%에서 런타임 에러가 뜸
# 너무 많이 재귀호출돼서 그런 거 같으니 스택으로 구현해야 할듯, 메모이제이션으로 구현
# 접근을 잘못함 작은 것부터 쭉 더해나가는 방법보다 더 좋은 방법이 있었음

# # n 입력
# n = int(input())

# # 카드 묶음 입력
# cards = []
# for _ in range(n):
#     cards.append(int(input()))

# # 카드 오름차순으로 정렬
# cards.sort()

# # n번째까지 합을 저장할 리스트 선언
# s = [0 for _ in range(100001)]

# # 1번째까지의 합은 1번째 혼자이므로 그대로 넣어줌
# s[0] = cards[0]

# # s[0] 을 초기화 해두고 i=1부터 n까지 s[i] = s[i-1] + cards[i]를 계속 대입시킴
# for i in range(1, n):
#     s[i] = s[i-1] + cards[i]

# if n == 1:
#     # 값이 하나인 경우 비교를 안함?
#     print(0)
# else:
#     print(sum(s[1:n]))
