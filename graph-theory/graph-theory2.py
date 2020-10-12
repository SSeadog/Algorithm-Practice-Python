# 도시 분할 계획


def find(parent, x):  # 특정 원소가 속한 집합 찾기
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):  # 두 원소가 속한 집합을 합치기
    a = find(parent, x)
    b = find(parent, y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


# 노드의 개수와 union 연산 개수 입력
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (n+1)
for i in range(1, n + 1):
    parent[i] = i

# 모든 간선을 담을 리스트와 비용을 담을 리스트
e = []
m_cost = []

# 모든 간선(union 연산) 정보 입력
for _ in range(m):
    x, y, cost = map(int, input().split())
    e.append((cost, x, y))

# 간선을 비용순으로 정렬
e.sort()

# 간선을 하나씩 확인하며, 사이클이 발생하지 않는 경우 포함시키고 m_cost에 cost 추가
for edge in e:
    cost, x, y = edge
    a = find(parent, x)
    b = find(parent, y)
    if a != b:
        union(parent, a, b)
        m_cost.append(cost)


# 모든 비용의 합에서 최대 비용을 뺀 값을 출력
print(sum(m_cost)-max(m_cost))
