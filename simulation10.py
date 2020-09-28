# 기둥과 보 설치


# 현재 wall 내의 모든 구조물이 가능한 것인지 확인하는 함수
def possible(wall, n, result):
    for r in result:
        # 기둥이면
        if r[2] == 0:
            # 벽면을 벗어나는지
            if r[1] >= 0 and r[1] < n and r[0] >= 0 and r[0] <= n:
                # 바닥이면
                if r[1] == 0:
                    continue
                # 보의 한쪽 위거나
                elif 1 in wall[r[1]][r[0]] or r[0] > 0 and 1 in wall[r[1]][r[0]-1]:
                    continue
                # 기둥 위거나
                elif 0 in wall[r[1]-1][r[0]]:
                    continue
                # 위 조건문에서 걸리지 않았다면 false 리턴
                return False
        # 보면
        elif r[2] == 1:
            # 벽면을 벗어나는지 확인
            if r[1] >= 0 and r[1] <= n and r[0] >= 0 and r[0] < n:
                # 한쪽이 기둥 위인지
                if r[1] > 0 and 0 in wall[r[1]-1][r[0]] or r[1] > 0 and r[0] < n and 0 in wall[r[1]-1][r[0]+1]:
                    continue
                # 양쪽이 다른 보와 연결되는지
                elif r[0] > 0 and 1 in wall[r[1]][r[0]-1] and r[0] < n and 1 in wall[r[1]][r[0]+1]:
                    continue
                return False
    return True


def solution(n, build_frame):
    # 구조물들을 저장할 wall
    wall = [[[] for _ in range(n+1)] for _ in range(n+1)]
    # 구조물 리스트
    result = []
    for build in build_frame:
        # 설치
        if build[3] == 1:
            # 기둥이면
            if build[2] == 0:
                # 벽면을 벗어나는지 확인, 좌표는 0부터 n까지
                if build[1] >= 0 and build[1] < n and build[0] >= 0 and build[0] <= n:
                    # 바닥이면
                    if build[1] == 0:
                        # wall에 추가(설치)
                        wall[build[1]][build[0]].append(build[2])
                        result.append([build[0], build[1], build[2]])
                    # 보의 한쪽 위거나
                    elif 1 in wall[build[1]][build[0]] or build[0] > 0 and 1 in wall[build[1]][build[0]-1]:
                        # wall에 추가(설치)
                        wall[build[1]][build[0]].append(build[2])
                        result.append([build[0], build[1], build[2]])
                    # 기둥 위거나
                    elif 0 in wall[build[1]-1][build[0]]:
                        # wall에 추가(설치)
                        wall[build[1]][build[0]].append(build[2])
                        result.append([build[0], build[1], build[2]])
            # 보면
            elif build[2] == 1:
                # 벽면을 벗어나는지 확인
                if build[1] >= 0 and build[1] <= n and build[0] >= 0 and build[0] < n:
                    # 한쪽이 기둥 위인지
                    if build[1] > 0 and 0 in wall[build[1]-1][build[0]] or build[1] > 0 and build[0] < n and 0 in wall[build[1]-1][build[0]+1]:
                        # wall에 추가(설치)
                        wall[build[1]][build[0]].append(build[2])
                        result.append([build[0], build[1], build[2]])
                    # 양쪽이 다른 보와 연결되는지
                    elif build[0] > 0 and 1 in wall[build[1]][build[0]-1] and build[0] < n and 1 in wall[build[1]][build[0]+1]:
                        # wall에 추가(설치)
                        wall[build[1]][build[0]].append(build[2])
                        result.append([build[0], build[1], build[2]])
        # 삭제
        elif build[3] == 0:
            # 빼고
            result.remove([build[0], build[1], build[2]])
            wall[build[1]][build[0]].remove(build[2])
            # 확인, 불가능하면 다시 넣음
            if not possible(wall, n, result):
                result.append([build[0], build[1], build[2]])
                wall[build[1]][build[0]].append(build[2])
    return sorted(result)


# n 입력
n = int(input())
# build_frame 입력
build_frame = []
for _ in range(10):
    build_frame.append(list(map(int, input().split())))


print(solution(n, build_frame))
