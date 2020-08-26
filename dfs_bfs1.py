# 음료수 얼려 먹기


# 혼자서 구상하고 만든 것(실패)

# 현재 위치에서 연결된 얼음을 재귀하며 모두 찾기
def find_near_ice(ice_plate, ice, position):
    cur_pos = position
    if cur_pos[0] - 1 >= 0 and ice_plate[cur_pos[0]-1][cur_pos[1]] == 0 and ice[cur_pos[0]-1][cur_pos[1]] == False:
        cur_pos[0] -= 1
        ice[cur_pos[0]][cur_pos[1]] = True
        find_near_ice(ice_plate, ice, cur_pos)
    if cur_pos[1] - 1 >= 0 and ice_plate[cur_pos[0]][cur_pos[1]-1] == 0 and ice[cur_pos[0]][cur_pos[1]-1] == False:
        cur_pos[1] -= 1
        ice[cur_pos[0]][cur_pos[1]] = True
        find_near_ice(ice_plate, ice, cur_pos)
    if cur_pos[0] + 1 <= n-1 and ice_plate[cur_pos[0]+1][cur_pos[1]] == 0 and ice[cur_pos[0]+1][cur_pos[1]] == False:
        cur_pos[0] += 1
        ice[cur_pos[0]][cur_pos[1]] = True
        find_near_ice(ice_plate, ice, cur_pos)
    if cur_pos[1] + 1 <= m-1 and ice_plate[cur_pos[0]][cur_pos[1]+1] == 0 and ice[cur_pos[0]][cur_pos[1]+1] == False:
        cur_pos[1] += 1
        ice[cur_pos[0]][cur_pos[1]] = True
        find_near_ice(ice_plate, ice, cur_pos)


# 얼음틀의 크기 입력 받기
n, m = map(int, input().split())

# 얼음틀의 상태 입력받을 리스트 초기화
ice_plate = []

# 얼음틀의 상태 입력 받기
for _ in range(n):
    ice_plate.append(list(map(int, input())))

# 방문한 얼음인지 확인 배열 생성
ice = [[False for _ in range(m)]] * n

# 현재 위치
current = [0, 0]

# 얼음의 개수
cnt = 0

# 현재 위치가 마지막이 될때까지 반복
while current[0] < n and current[1] < m:
    # 현재 위치가 얼음이고 방문하지 않은 얼음이라면
    if ice_plate[current[0]][current[1]] == 0 and ice[current[0]][current[1]] == False:
        # 얼음 개수 증가, 얼음 방문 표시, 인접한 얼음 모두 찾아 방문 표시
        cnt += 1
        ice[current[0]][current[1]] = True
        find_near_ice(ice_plate, ice, current)

    # 현재 위치 증가, 열 크기가 최대 열 크기보다 커지면 열 -> 0, 행 증가
    current[1] += 1
    if current[1] == m:
        current[1] = 0
        current[0] += 1

print(cnt)
