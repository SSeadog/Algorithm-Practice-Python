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

parent = [0,1,2,3,4,5,6,7,8,9,10]

unionParent(parent, 1, 2)
unionParent(parent, 7, 8)
unionParent(parent, 8, 9)
unionParent(parent, 7, 1)
print(parent)

print(findParent(parent, 1, 2))
print(findParent(parent, 7, 9))
