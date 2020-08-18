class Edge:
    def __init__(self, a, b, distance):
        self.a = a
        self.b = b
        self.distance = distance

    def __str__(self):
        return f"{self.a} {self.b} {self.distance}"

def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return 1
    else:
        return 0

# 각 간선을 배열에 넣음
E = []
E.append(Edge(1,7,12))
E.append(Edge(1,4,28))
E.append(Edge(1,2,67))
E.append(Edge(1,5,17))
E.append(Edge(2,4,24))
E.append(Edge(2,5,62))
E.append(Edge(3,5,20))
E.append(Edge(3,6,37))
E.append(Edge(4,7,13))
E.append(Edge(5,6,45))
E.append(Edge(5,7,73))

# 배열을 정렬
E_sorted = sorted(E, key=lambda E: E.distance)

# 그래프 연결 확인용 배열
set = []
for i in range(8):
    set.append(i)

# 거리의 합 초기화
sum = 0

for edge in E_sorted:
    # 두 정점이 연결되어 있지 않으면 연결하고 sum에 추가
    if not findParent(set, edge.a, edge.b):
        unionParent(set, edge.a, edge.b)
        sum += edge.distance

print(sum)

