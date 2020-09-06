import heapq
import sys

# heap을 이용한 다익스트라 알고리즘

# graph를 이용해 구현한 다익스트라 알고리즘
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 개수 입력
n, m = map(int, input().split())

# 시작 위치 입력
s = int(input())

# 각 노드의 연결 정보를 저장할 리스트 만들기
graph = [[] for i in range(n+1)]

# 노드의 연결 정보 입력
for i in range(m):
    a, b, c = map(int, input().split())
    # a노드에서 b노드까지 비용은 c라는 의미로 저장
    graph[a].append((b, c))

# 방문 확인 리스트
visited = [False] * (n+1)

# 최단 거리를 저장할 리스트
distance = [INF] * (n+1)


def set_short(index):  # 시작할 때 초기 거리를 저장할 함수
    distance[index] = 0
    for node in graph[index]:
        distance[node[0]] = node[1]


def get_small_index():  # 방문하지 않은 노드 중 최단 거리 노드 선택. 선형 탐색
    min = INF
    index = 0
    for i in range(n):
        if distance[i] < min and not visited[i]:
            min = distance[i]
            index = i
    visited[index] = True
    return index


def update_short(index):  # 방문한 index를 거쳐가는 distance와 현재 저장된 distance를 비교 갱신
    for node in graph[index]:
        if distance[index] + node[1] < distance[node[0]]:
            distance[node[0]] = distance[index] + node[1]


def dijstra(start):  # 다익스트라 알고리즘 구현
    # 방문 표시
    visited[start] = True
    # start노드를 이용해 거리 입력
    set_short(start)
    # n-1번 반복
    for _ in range(n-1):
        # 방문하지 않은 노드 중 가장 가까운 노드를 선택
        small = get_small_index()
        # 그 노드에서 거리 정보 갱신
        update_short(small)


# 실행
dijstra(s)

# 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


# # 단순히 구현한 다익스트라 알고리즘
# number = 6
# INF = 10000

# # 전체 그래프 초기화
# a = [[0, 2, 5, 1, INF, INF],
#      [2, 0, 3, 2, INF, INF],
#      [5, 3, 0, 3, 1, 5],
#      [1, 2, 3, 0, 1, INF],
#      [INF, INF, 5, 1, 0, 2],
#      [INF, INF, 5, INF, 2, 0]]

# visited = [False] * 6  # 방문했는지
# distance = []  # 최단 거리

# # 방문하지 않은 노드 중 최단 거리 노드 선택


# def getSmallIndex():
#     min = INF
#     index = 0
#     for n in range(number):
#         if distance[n] < min and not visited[n]:
#             min = distance[n]
#             index = n
#     visited[index] = True
#     return index

# # 방문하지 않은 노드 중에서 최단 거리 노드를 거쳐서 특정 노드로 가는 경우 고려해서 최단 거리 갱신


# def updateShort(i):
#     for n in range(number):
#         if distance[i] + a[i][n] < distance[n]:  # 지금 최단 거리보다 거쳐온 최단 거리가 짧은 경우 갱신
#             distance[n] = distance[i] + a[i][n]

# # 출발 노드 설정


# def setShort(i):
#     visited[i] = True
#     for n in range(number):
#         distance.append(a[i][n])


# def dijstra(i):
#     setShort(i)
#     for n in range(number-1):
#         small = getSmallIndex()
#         updateShort(small)
#     print(distance)
#     print(visited)


# dijstra(0)
