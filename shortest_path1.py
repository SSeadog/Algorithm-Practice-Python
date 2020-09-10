# 미래 도시

# 다익스트라로 구현하려 했으나, 플로이드 워셜로 구현하는 게 더 편할 듯

# 1e9를 무한대로 의미
INF = int(1e9)

# n, m 입력
n, m = map(int, input().split())

# 연결 정보를 저장할 리스트, INF로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 갱신
for i in range(1, n+1):
    graph[i][i] = 0

# 연결 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x, k 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for node in range(1, n+1):
    for i in range(1, n+1):
        if i == node:
            continue
        for j in range(1, n+1):
            if j == node:
                continue
            graph[i][j] = min(graph[i][j], graph[i][node] + graph[node][j])

# 출력
if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
