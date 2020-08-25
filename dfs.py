# DFS

# 재귀 함수로 만든 dfs
def dfs(graph, node):
    # 호출될 때 그 노드를 입력 -> 노드가 스택에 들어가는 순서 출력
    print(node, end=" ")
    # 받은 node는 방문 표시
    visited[node] = True
    # 인접 노드들을 하나씩 방문한 노드인지 확인
    for near_node in graph[node]:
        if visited[near_node] == False:
            # 방문하지 않은 노드라면 dfs호출
            dfs(graph, near_node)


# 방문 표시 저장 배열
visited = [False for _ in range(9)]

# 그래프를 2차원 리스트(배열로) 구현
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 실행, 결과 확인
dfs(graph, 1)
print(visited)

# # 스택을 이용해 개인적으로 만든 dfs
# def dfs(graph, start):
#     # 노드의 방문 처리 배열을 0으로 초기화
#     visited = [0 for _ in range(9)]
#     # dfs 구현을 위한 스택을 초기화
#     stack = []
#     # 스택에 시작 값을 넣음
#     stack.append(start)
#     # start 값을 방문했다고 표시
#     visited[start] = 1
#     # 스택이 빌때까지 반복
#     while stack:
#         # 현재 노드를 의미하는 current 선언하고 스택의 마지막 값 넣음
#         current = stack[-1]
#         # 현재 노드의 인접노드를 전부 방문했는지 확인하는 변수, 0으로 초기화
#         leng = 0
#         # 현재 노드의 인접노드들을 하나씩 확인
#         for near_node in graph[current]:
#             # 해당 인접 노드를 방문하지 않았다면 스택에 추가, 방문 표시, leng을 초기화, while문의 처음으로 이동
#             if visited[near_node] == 0:
#                 stack.append(near_node)
#                 visited[near_node] = 1
#                 leng = 0
#                 break
#             # 방문한 노드라면 leng 1 증가
#             else:
#                 leng += 1
#             # 인접 노드들을 전부 방문했으면 스택에서 마지막 노드를 꺼냄
#             if leng == len(graph[current]):
#                 stack.pop()
#     # 전부 탐색했는지 확인
#     print(visited)


# # 그래프를 2차원 리스트(배열로) 구현
# graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
#          [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# # 노드의 방문 처리 배열
# visited = [0 for _ in range(9)]

# # stack
# stack = []

# # dfs 실행
# dfs(graph, 1)
