# 위상 정렬

from collections import deque

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i_ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)


def topology_sort():  # 위상 정렬 함수, 출력
    q = deque()
    # 각 노드 진입차수 갱신
    for g in graph:
        for n in g:
            indegree[n] += 1
    # 방문 표시 리스트
    visited = [False] * (v + 1)
    # 진입차수 0인 노드 넣고 방문 표시
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            visited[i] = True
    result = []
    # 큐가 빌때까지 반복
    while q:
        n = q.popleft()
        result.append(n)
        for node in graph[n]:
            indegree[node] -= 1
        for i in range(1, v + 1):
            if indegree[i] == 0 and visited[i] == False:
                q.append(i)
                visited[i] = True
    print(result)


topology_sort()
