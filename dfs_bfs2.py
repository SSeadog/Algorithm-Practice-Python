# # 혼자서 구상해본 것 에러 났음 (TypeError: 'int' object is not subscriptable)
# # 미로 탈출

# from collections import deque


# def bfs(graph, start):
#     queue = deque(start)
#     cur_node = start
#     while cur_node[0] != n-1 or cur_node[1] != m-1:
#         cur_node = queue.popleft()
#         if graph[cur_node[0]][cur_node[1]+1] == 1:
#             cur_node[1] += 1
#         if graph[cur_node[0]+1][cur_node[1]] == 1:
#             cur_node[0] += 1
#         print(cur_node)
#     print("last:", cur_node)


# n, m = map(int, input().split())

# miro = []
# for _ in range(n):
#     miro.append(list(map(int, input())))

# bfs(miro, [0, 0])
