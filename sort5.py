# 안테나

# n 입력
n = int(input())

# 위치 입력
place = list(map(int, input().split()))

place.sort()
print(place[(n - 1)//2])


# # 왜 안되는지 모르겠음
# # n 입력
# n = int(input())

# # 위치 입력
# place = list(map(int, input().split()))

# # 평균 구하기
# avr = sum(place)/len(place)

# # 위치에서 평균 뺌
# for i in range(n):
#     place[i] -= avr

# # 절대값 기준으로 오름차순 정렬 값이 같은 경우 오름차순으로 음수 먼저
# place = sorted(place, key=lambda x: (abs(x), x))

# # 0번째가 거리가 젤 가까우면서 값도 젤 작은 것, avr을 뺐었으니 다시 더해서 int형으로 출력
# print(int(place[0] + avr))
