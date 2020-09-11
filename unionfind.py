# union-find ver2

# 특정 원소가 속한 집합을 찾기, 경로 압축 기법
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기


def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


# 노드의 개수와 union연산개수(간선의 개수) 입력 받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for _ in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v + 1):
    print(find(parent, i), end=" ")

print()

# 부모 테이블 내용 출력
for i in range(1, v + 1):
    print(parent[i], end=" ")

# union-find ver1

# def getParent(parent, x):
#     if parent[x] == x:
#         return x
#     return getParent(parent, parent[x])

# def unionParent(parent, a, b):
#     a = getParent(parent, a)
#     b = getParent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def findParent(parent, a, b):
#     a = getParent(parent, a)
#     b = getParent(parent, b)
#     if a == b:
#         return 1
#     else:
#         return 0

# parent = [0,1,2,3,4,5,6,7,8,9,10]

# unionParent(parent, 1, 2)
# unionParent(parent, 7, 8)
# unionParent(parent, 8, 9)
# unionParent(parent, 7, 1)
# print(parent)

# print(findParent(parent, 1, 2))
# print(findParent(parent, 7, 9))
