# Floyd-Warshall Algorithm 구현

# 무한을 의미하는 값으로 10억 설정
INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력
n = int(input())
m = int(input())

# 2차원 리스트 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(n+1):
    graph[i][i] = 0

# 각 간선에 대한 정보 입력, 그 값으로 초기화
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a][b] = d

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for node in range(1, n+1):
    for i in range(1, n+1):
        if i == node:
            continue
        for j in range(1, n+1):
            if j == node:
                continue
            graph[i][j] = min(graph[i][j], graph[i][node] + graph[node][j])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INF", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
