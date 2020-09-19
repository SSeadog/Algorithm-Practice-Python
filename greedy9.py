# import heapq

# 나동빈씨의 알고리즘을 참고해서 만든 알고리즘. 보기도 편하지만 로직 또한 간결함. 더 연습해야할 듯

import heapq


def solution(food_times, k):
    # k가 전체를 다 먹는 시간보다 크거나 같으면 더 이상 먹을 게 없으므로 -1 리턴
    if k >= sum(food_times):
        return -1

    q = []
    # 최소 시간을 뽑기 위해 큐를 이용
    for i, time in enumerate(food_times):
        heapq.heappush(q, (time, i+1))

    # 총 소요 시간, 반복문에서 바로 전에 사용한 시간, 현재 남은 음식을 저장할 변수
    total = 0
    previous = 0
    length = len(food_times)

    while k >= (q[0][0] - previous) * length:
        now = heapq.heappop(q)[0]
        total = (now - previous) * length
        k -= total
        previous = now
        length -= 1

    result = sorted(q, key=lambda x: x[1])
    answer = result[k % length][1]

    return answer


print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))


# # q를 이용해서 하려 했으나 테스트 케이스만 통과함.. 다시 풀어봐야 할듯

# # 각 음식 먹는 시간
# food_times = [3, 1, 2]

# # 총 시간 5
# k = 5

# q = []

# answer = -1

# food_length = len(food_times)

# for i,food in enumerate(food_times):
#   heapq.heappush(q, (food, i))

# while k > 0:
#   # 힙에서 최솟값 꺼냄
#   value = heapq.heappop(q)[0]
#   # k가 최솟값 * length보다 길다면
#   if k >= value * food_length:
#     # k에서 최솟값 * length 뺌
#     k -= value * food_length
#     # food_times 순차 탐색하며 각 값에서 최솟값 뺌. 0이 되는 값이 있으면 length 에서 1 뺌
#     for i in range(len(food_times)):
#       if food_times[i] == value:
#         food_length -= 1
#       food_times[i] -= value
#   # k가 최솟값 * length 보다 작다면
#   else:
#     i = 0
#     # k가 0보다 클때
#     while k > 0:
#       # i가 food_times 인덱스로 될 수 있는지 확인
#       if i < len(food_times):
#         # food_times[i]가 0이 아니면 k에서 1 빼며 0이 되면 answer 갱신
#         if food_times[i] != 0:
#           k -= 1
#           if k == 0:
#             answer = food_times[i]
#         i += 1

# print(answer)
