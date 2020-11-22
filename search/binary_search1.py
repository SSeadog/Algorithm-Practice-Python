import math

# 부품 찾기

# 계수 정렬로 구현

# n 입력
n = int(input())
# 매장의 부품 종류 입력
materials = list(map(int, input().split()))

# m 입력
m = int(input())
# 요청 부품 종류 입력
requests = list(map(int, input().split()))

# material이 있는지 저장할 배열
material_list = [0 for _ in range(1000001)]

# 제품이 있다고 표시하기 위해 1로 갱신
for material in materials:
    material_list[material] = 1

# 요청 부품이 있는지 확인
for request in requests:
    if material_list[request] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")

# # 이진 탐색 함수 구현(반복문)
# def binary_search(array, find, start, end):
#     if start > end:
#         return "no"
#     # mid = (start + end) // 2
#     mid = math.floor((start + end)/2)
#     if array[mid] == find:
#         return "yes"
#     elif array[mid] > find:
#         return binary_search(array, find, start, mid-1)
#     elif array[mid] < find:
#         return binary_search(array, find, mid+1, end)


# # n 입력
# n = int(input())
# # 매장의 부품 종류 입력
# materials = list(map(int, input().split()))

# # m 입력
# m = int(input())
# # 요청 부품 종류 입력
# requests = list(map(int, input().split()))

# # 매장 부품 정렬 오름차순으로
# materials.sort()

# for request in requests:
#     print(binary_search(materials, request, 0, len(materials)-1), end=" ")
