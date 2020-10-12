# 게임 개발

# 1
# 맵의 세로 크기 가로 크기 입력 받음
n, m = map(int, input().split())

# 현재 캐릭터의 좌표와 방향 입력 받음
x, y, direction = map(int, input().split())

# 맵의 정보를 입력 받음
Map = []
for i in range(n):
    Map.append(list(map(int, input().split())))

# 캐릭터가 이동할 방향을 direction에 맞춰 저장
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 현재 방문 위치 포함해서 방문 횟수 초기화, 현재 위치에 방문했다는 의미로 2로 바꿈
cnt = 1
Map[x][y] = 2

# 회전 횟수
turn = 0

while True:
    # 캐릭터 방향 왼쪽으로 회전, 회전 횟수 증가
    direction -= 1
    turn += 1
    # 방향이 0~3 사이의 인덱스를 가지게 함
    if direction == -1:
        direction = 3
    # 방문하려는 위치가 0이면 방문, 회전 횟수 초기화, 방문 표시, 방문 횟수 증가
    if Map[x + d[direction][1]][y + d[direction][0]] == 0:
        x += d[direction][1]
        y += d[direction][0]
        turn = 0
        Map[x][y] = 2
        cnt += 1
        continue
    # 4방향 모두 방문할 수 없으면 뒤로 돌아가기, 회전 횟수 초기화
    if turn == 4:
        x -= d[direction][1]
        y -= d[direction][0]
        turn = 0
        # 뒤로 갔는데 바다인 경우 종료
        if Map[x][y] == 1:
            break
print(cnt)


# # 2
# # 맵의 세로 크기, 가로 크기를 입력 받음
# n, m = map(int, input().split())

# # 캐릭터의 좌표(a, b)와 방향 d를 입력 받음
# a, b, d = map(int, input().split())

# # 맵의 상태를 저장할 리스트 선언
# Map = []

# # 맵의 각 좌표마다 상태를 입력 받음
# for i in range(n):
#     Map.append(list(map(int, input().split())))

# # 캐릭터의 현재 좌표와 방향 저장
# character = [a, b, d]

# # 캐릭터가 방문한 칸의 수를 1로 초기화, 현재 위치를 방문했단 의미로 2로 변경
# cnt = 1
# Map[character[0]][character[1]] = 2

# # 캐릭터의 회전 수를 0으로 초기화
# turn_time = 0

# while True:
#     # 방향을 상 0 좌 3 하 2 우 1 로 의미하며 왼쪽으로 회전, 회전 수 1 증가
#     character[2] -= 1
#     turn_time += 1
#     if character[2] == -1:
#         character[2] = 3
#     # 캐릭터가 바라보는 방향을 확인하고 해당 방향의 칸에 방문할 수 있는지 확인
#     if character[2] == 0:
#         if Map[character[0]+1][character[1]] == 0:
#             # 방문 할 수 있다면 방문하고 방문 위치를 2로 변경, 회전 수 초기화, 방문한 칸의 수 증가, 반복문의 맨 처음으로 이동
#             character[0] += 1
#             Map[character[0]][character[1]] = 2
#             turn_time = 0
#             cnt += 1
#             continue
#     if character[2] == 3:
#         if Map[character[0]][character[1]-1] == 0:
#             character[1] -= 1
#             Map[character[0]][character[1]] = 2
#             turn_time = 0
#             cnt += 1
#             continue
#     if character[2] == 2:
#         if Map[character[0]-1][character[1]] == 0:
#             character[0] -= 1
#             Map[character[0]][character[1]] = 2
#             turn_time = 0
#             cnt += 1
#             continue
#     if character[2] == 1:
#         if Map[character[0]][character[1]+1] == 0:
#             character[1] += 1
#             Map[character[0]][character[1]] = 2
#             turn_time = 0
#             cnt += 1
#             continue

#     # 이동 없이 회전만 4번 한 경우
#     if turn_time == 4:
#         # 캐릭터의 방향을 확인하고 뒤로 이동
#         if character[2] == 0:
#             character[0] += 1
#             turn_time = 0
#             if Map[character[0]][character[1]] == 1:
#                 break
#         if character[2] == 3:
#             character[1] += 1
#             turn_time = 0
#             if Map[character[0]][character[1]] == 1:
#                 break
#         if character[2] == 2:
#             character[0] -= 1
#             turn_time = 0
#             if Map[character[0]][character[1]] == 1:
#                 break
#         if character[2] == 1:
#             character[1] -= 1
#             turn_time = 0
#             if Map[character[0]][character[1]] == 1:
#                 break

# print(cnt)
