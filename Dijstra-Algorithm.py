import heapq

number = 6
INF = 10000

a = [[0, 2, 5, 1, INF, INF],
     [2, 0, 3, 2, INF, INF],
     [5, 3, 0, 3, 1, 5],
     [1, 2, 3, 0, 1, INF],
     [INF, INF, 5, 1, 0, 2],
     [INF, INF, 5, INF, 2, 0]]

visited = [False] * 6
distance = []

# 여기서 최소 노드 구하는 로직이 문제가 있는 듯


def getShortIndex():
    heap = []
    for n in range(number):
        if visited[n] == False:
            heapq.heappush(heap, distance[n])
    short_distance = heapq.heappop(heap)
    for n in range(number):
        if distance[n] == short_distance and visited[n] == False:
            return n


def updateShort(short_index):
    visited[short_index] = True
    for n in range(number):
        if distance[short_index] + a[short_index][n] < distance[n]:
            distance[n] = distance[short_index] + a[short_index][n]


def dijstra(start):
    visited[start] = True
    for n in range(number):
        distance.append(a[start][n])
    for n in range(3):
        short_index = getShortIndex()
        updateShort(short_index)


dijstra(0)
print(distance)


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
