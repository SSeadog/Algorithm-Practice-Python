import math

# 이진 탐색
# 다음에 반복문으로도 구현해보기

# 이진 탐색 함수 선언


def binary_search(array, find, start, end):
    # start가 end가 크면 찾는 값이 없다고 판단
    if start > end:
        return None
    # mid 값 계산, math 라이브러리 이용할 필요 없이 python의 몫 연산자(//)를 이용해 더 편하게 구현 가능
    mid = math.floor((start + end)/2)
    # 같으면 인덱스 반환
    if array[mid] == find:
        return mid
    # 찾는 값보다 mid값이 크면 end를 mid-1로 바꿔서 재귀호출
    elif array[mid] > find:
        return binary_search(array, find, start, mid-1)
    # 찾는 값보다 mid값이 작으면 start를 mid+1로 바꿔서 재귀호출
    elif array[mid] < find:
        return binary_search(array, find, mid+1, end)


# 정렬된 배열 선언
array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 실행 및 결과 출력
print(binary_search(array, 8, 0, len(array)-1))
