# 특정 거리의 도시 찾기

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# n,m,k,x 입력
n, m, k, x = map(int, input().split())

# 노드 정보 입력
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

# 방문 확인 리스트
visited = [False] * (n+1)

# 최단 거리
distance = [INF] * (n+1)


def update_short(index):
    for node in graph[index]:
        if distance[index] + node[1] < distance[node[0]]:
            distance[node[0]] = distance[index] + node[1]


def dijstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        n = heapq.heappop(q)[1]
        if visited[n]:
            continue
        visited[n] = True
        update_short(n)
        for node in graph[n]:
            heapq.heappush(q, (node[1], node[0]))


dijstra(x)

isPrinted = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        isPrinted = True
if not isPrinted:
    print(-1)
