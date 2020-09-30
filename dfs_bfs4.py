# 연구소

# n,m 입력
n, m = map(int, input().split())

# 지도 모양 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


result = []

test_graph = graph

# 아무 위치에 벽 세우기
for a_i in range(n):
    for a_j in range(m):
        if test_graph[a_i][a_j] != 0:
            continue
        test_graph[a_i][a_j] = 1
        for b_i in range(n):
            for b_j in range(m):
                if test_graph[b_i][b_j] != 0:
                    continue
                test_graph[b_i][b_j] = 1
                for c_i in range(n):
                    for c_j in range(m):
                        if test_graph[c_i][c_j] != 0:
                            continue
                        test_graph[c_i][c_j] = 1
                        # 바이러스 퍼뜨리기 0 개수 구하기
                        cnt = 0
                        # for g in test_graph:
                        #     for x in g:
                        #         if x == 0:
                        #             cnt += 1
                        # result.append(cnt)
                        print(test_graph)
                test_graph = graph


# print(result)
