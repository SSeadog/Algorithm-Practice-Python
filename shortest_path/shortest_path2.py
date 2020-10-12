# 전보

import heapq

# 1e9를 무한대를 의미하게 함
INF = int(1e9)

# 힙을 이용한 다익스트라

# n,m,c 입력
n, m, c = map(int, input().split())

# 연결 정보를 저장할 그래프 초기화
graph = [[] for _ in range(n+1)]

# 연결 정보 저장. x에서 y로 가는 비용은 z
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 방문 표시를 저장할 리스트
visited = [False for _ in range(n+1)]

# 거리 비용을 저장할 리스트. INF로 초기화
distance = [INF for _ in range(n+1)]


def dijstra(start):  # 다익스트라 구현
    heap = []
    # 자기 자신은 비용이 0
    distance[start] = 0
    # heap에 비용과 노드(start) 넣음
    heapq.heappush(heap, (distance[start], start))
    # heap이 빌때까지 반복
    while heap:
        # 힙에서 가장 거리가 짧은 노드 꺼내고 노드만 node에 저장
        node = heapq.heappop(heap)[1]
        # 방문하지 않은 노드라면
        if not visited[node]:
            # 연결된 노드 거리 비용 갱신
            for n in graph[node]:
                if distance[n[0]] > n[1] + distance[node]:
                    distance[n[0]] = n[1] + distance[node]
            # 방문 표시
            visited[node] = True
            # 연결된 노드 갱신된 비용과 함께 heaq에 넣음
            for n in graph[node]:
                heapq.heappush(heap, (distance[n[1]], n[0]))


dijstra(c)

# 메시지 받은 도시 개수 저장할 변수
cnt = 0
for i, d in enumerate(distance):
    if d != INF and d != 0:
        cnt += 1
    else:
        distance[i] = -1

# 총 시간
time = max(distance)

print(cnt, time)
