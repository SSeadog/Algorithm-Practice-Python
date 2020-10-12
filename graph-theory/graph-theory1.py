# 팀 결성

def find(parent, x):  # find 연산 선언
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):  # union 연산 선언
    a = find(parent, x)
    b = find(parent, y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def check(parent, x, y):  # check 연산 선언
    a = find(parent, x)
    b = find(parent, y)
    if a == b:
        print("YES")
    else:
        print("NO")


# n,m 입력
n, m = map(int, input().split())

# 연산 입력
operation = []
for _ in range(m):
    operation.append(list(map(int, input().split())))

# parent 선언
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# 각 연산 적용
for op in operation:
    code, a, b = op
    if code == 0:
        union(parent, a, b)
    else:
        check(parent, a, b)
