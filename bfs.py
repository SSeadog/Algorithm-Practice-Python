# BFS

# 큐를 이용한 bfs

import queue

# bfs 함수 생성


def bfs(graph, start):
    # 시작 값을 큐에 넣고 방문 처리
    q.put(start)
    visited[start] = True
    # 큐가 빌때까지 반복
    while q.qsize() != 0:
        # 큐에서 값을 꺼냄, 출력해서 꺼낸 순서 확인
        v = q.get()
        print(v, end=" ")
        for near_node in graph[v]:
            # 방문하지 않은 인접노드들을 큐에 넣음, 방문 처리
            if visited[near_node] == False:
                q.put(near_node)
                visited[near_node] = True


# 그래프를 2차원 배열로 구현
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 방문 확인을 위한 변수 초기화
visited = [False for _ in range(9)]

# bfs 구현을 위한 queue 인스턴스 생성
q = queue.Queue()

# 실행, 결과 확인
bfs(graph, 1)
print(visited)
