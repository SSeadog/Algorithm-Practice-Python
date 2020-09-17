# 무지의 먹방 라이브

food_times = list(map(int, input().split()))

k = int(input())

food_times_dict = {i: food_times[i] for i in range(len(food_times))}

print(food_times_dict)

print(sorted(food_times_dict.items(), key=lambda x: x[1]))
