# 경쟁적 전염

# heap을 이용한 bfs로 구현

import heapq

# 이동 방향 구현 상,우,하,좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, virus):  # bfs 구현
    graph[x][y] = virus
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus


# n,k 입력
n, k = map(int, input().split())

# 시험관 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# s,x,y 입력
s, x, y = map(int, input().split())

# 힙 선언
heap = []

time = 0
while time < s:
    time += 1
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                heapq.heappush(heap, (graph[i][j], i, j))
    while heap:
        v, c_x, c_y = heapq.heappop(heap)
        bfs(c_x, c_y, v)

print(graph[x-1][y-1])
