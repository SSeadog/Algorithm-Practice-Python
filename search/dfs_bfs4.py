# 연구소

# n,m 입력
n, m = map(int, input().split())

# 지도 모양 입력
graph = []
# 벽이 설치된 후의 지도. 특정 크기의 2차원 리스트는 리스트 컴프리헨션을 이용해야 함.
temp = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))


result = []

# 이동 방향에 대한 리스트 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_safe():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(cnt):
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 바이러스 퍼지고 안전 영역 구하기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        safe_score = get_safe()
        result.append(safe_score)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)
                graph[i][j] = 0
                cnt -= 1


dfs(0)
print(max(result))
