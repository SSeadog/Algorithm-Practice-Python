# # 미로 탈출

from collections import deque

# # 나동빈씨의 알고리즘으로 2차 구상
# # 만들며 최대한 조건문을 최대한 간단하게 해보려 했으나 에러가 났음. 모든 상황을 고려하기 위해 조건문을 추가해야 할듯

# # 미로 크기 입력
# n, m = map(int, input().split())

# # 미로 상태 입력
# miro = []
# for _ in range(n):
#     miro.append(list(map(int, input())))

# # 이동 방향 정의(상, 하, 좌, 우)
# dx = [-1, 1, 0, 0, ]
# dy = [0, 0, -1, 1]

# # BFS 구현


# def bfs(x, y):
#     # 큐 생성, 큐에 x,y입력
#     queue = deque()
#     queue.append((x, y))
#     # 큐가 빌때까지 반복
#     while queue:
#         # 큐에서 좌표 꺼냄
#         x, y = queue.popleft()
#         print(x, y)
#         # 4방향 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 1이면 거리 갱신, 큐에 nx, ny 넣음
#             if miro[nx][ny] == 1:
#                 miro[nx][ny] = miro[x][y] + 1
#                 queue.append((nx, ny))
#     return miro[n-1][m-1]


# bfs(0, 0)
# print(miro)


# 나동빈씨의 알고리즘을 그대로 따라 씀. 시작 위치를 제외하고 갈 수 있는 모든 노드에 최단 거리가 적힘

# 미로 크기 입력
n, m = map(int, input().split())

# 미로 상태 입력
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

# 이동 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 구현


def bfs(x, y):
    # 큐 생성
    queue = deque()
    queue.append((x, y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        print(x, y)
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if miro[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우 최단 거리 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
        # 가장 오른쪽 아래의 최단 거리 반환
    return miro[n-1][m-1]


# BFS 결과 출력
print(bfs(0, 0))


# # 혼자서 구상해본 것 에러 났음 (TypeError: 'int' object is not subscriptable)


# def bfs(graph, start):
#     queue = deque(start)
#     cur_node = start
#     while cur_node[0] != n-1 or cur_node[1] != m-1:
#         cur_node = queue.popleft()
#         if graph[cur_node[0]][cur_node[1]+1] == 1:
#             cur_node[1] += 1
#         if graph[cur_node[0]+1][cur_node[1]] == 1:
#             cur_node[0] += 1
#         print(cur_node)
#     print("last:", cur_node)


# n, m = map(int, input().split())

# miro = []
# for _ in range(n):
#     miro.append(list(map(int, input())))

# bfs(miro, [0, 0])
