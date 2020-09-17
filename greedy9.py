# import heapq

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

import heapq


def solution(food_times, k):

    q = []
    answer = -1

    food_length = len(food_times)

    for i, food in enumerate(food_times):
        heapq.heappush(q, (food, i))

    while k > 0:
        value = heapq.heappop(q)[0]
        if k >= value * food_length:
            k -= value * food_length
            for i in range(len(food_times)):
                if food_times[i] == value:
                    food_length -= 1
                food_times[i] -= value
        else:
            i = 0
            while k > 0:
                if i < len(food_times):
                    if food_times[i] != 0:
                        k -= 1
                        if k == 0:
                            answer = food_times[i]
                    i += 1
    return answer


print(solution([3, 1, 2], 5))
