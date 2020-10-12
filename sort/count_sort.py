# 리스트 선언
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 값이 등장한 횟수를 저장할 배열
count = [0] * (max(array) + 1)

# array에서 값을 하나씩 보며 count에 적립
for i in array:
    count[i] += 1

# 정렬된 것을 저장할 리스트 선언
sorted_array = []

# 0부터 리스트의 최대값까지 나온 횟수만큼 sorted_array에 순서대로 넣음
for i in range(len(count)):
    for j in range(count[i]):
        sorted_array.append(i)

print(sorted_array)
