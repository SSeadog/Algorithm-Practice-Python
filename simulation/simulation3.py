# 왕실의 나이트

# 1
# 좌표 입력 받기
data = input()

# 좌표를 row, column에 저장
row = int(data[1])
column = ord(data[0]) - ord("a") + 1

# 8가지 이동을 routes에 저장
routes = ((2, -1), (2, 1), (-2, -1), (-2, 1),
          (-1, 2), (1, 2), (-1, -2), (1, -2))

# 결과 저장 변수 초기화
result = 0

# 8가지의 이동을 하나씩 적용한 뒤 if문으로 이동 후 좌표가 유효 좌표 안에 있는지 확인
for r in routes:
    movex = column + r[1]
    movey = row + r[0]
    if movex >= 1 and movex <= 8 and movey >= 1 and movey <= 8:
        result += 1

print(result)

# 2
# # 좌표 입력 받기
# p = input()

# # 가로 좌표는 알파벳으로 와서 딕셔너리로 알파벳: 숫자로 선언하고 딕셔너리의 키값으로 입력받은 좌표 알파벳을 줘서 숫자로 변환
# # ex) input a1, x좌표 => a, p[0] => a, trans_a_to_1[p[0]] => 1
# trans_a_t0_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

# # 좌표 x,y를 변수에 저장
# x = trans_a_t0_1[p[0]]
# y = int(p[1])

# # 결과 저장 변수 초기화
# result = 0

# # 8가지의 움직임을 if문으로 검사 후 각 좌표값이 1~8사이를 넘어가지 않으면 결과에 추가
# if x + 2 <= 8 and y - 1 >= 1:
#     result += 1
# if x + 2 <= 8 and y + 1 <= 8:
#     result += 1
# if x - 2 >= 1 and y - 1 >= 1:
#     result += 1
# if x - 2 >= 1 and y + 1 <= 8:
#     result += 1
# if y - 2 >= 1 and x - 1 >= 1:
#     result += 1
# if y - 2 >= 1 and x + 1 <= 8:
#     result += 1
# if y + 2 <= 8 and x - 1 >= 1:
#     result += 1
# if y + 2 <= 8 and x + 1 <= 8:
#     result += 1

# print(result)
