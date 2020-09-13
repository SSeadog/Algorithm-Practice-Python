# 커리큘럼

from collections import deque

# 간선 개수 입력
n = int(input())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range((n+1))]

# 강의 듣는 시간
time = [0] * (n+1)

# 방향 그래프의 모든 간선 정보 입력
for i in range(1, n+1):
    node = []
    input_list = list(map(int, input().split()))
    for index, li in enumerate(input_list):
        if index == 0:
            time[i] = li
            continue
        if li == -1:
            break
        node.append(li)
    graph[i] = node


# 위상 정렬 함수
def topology_sort():
    q = deque()
    # 각 노드 진입차수 갱신
    for i in range(1, n+1):
        for g in graph[i]:
            indegree[i] += 1

    # 방문 표시 리스트 선언
    visited = [False] * (n+1)

    # 진입차수 0인 노드 넣고 방문 표시
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            visited[i] = True

    # 큐가 빌때까지 반복
    while q:
        node = q.popleft()
        for i in range(1, n+1):
            if node in graph[i]:
                indegree[i] -= 1
                if indegree[i] == 0 and visited[i] == False:
                    q.append(i)
                    visited[i] = True
                    pre_time = []
                    for pre_node in graph[i]:
                        pre_time.append(time[pre_node])
                    time[i] += max(pre_time)
    print(visited)


topology_sort()
print(time)
