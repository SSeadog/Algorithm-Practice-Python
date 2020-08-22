import heapq

# 다음에 꼭 heap을 이용해 다익스트라 구현하기 해야함

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
