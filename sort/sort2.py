# 성적이 낮은 순서로 학생 출력하기

# 학생 수 입력
n = int(input())

# # 학생 정보 입력
# array = []
# for _ in range(n):
#     array.append(list(map(str, input().split())))

# 학생 정보 입력2
array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# lambda를 이용해 list의 2번째 인덱스를 기준으로 정렬
student_list = sorted(array, key=lambda array: array[1])

# 결과 출력
for student in student_list:
    print(student[0], end=" ")
