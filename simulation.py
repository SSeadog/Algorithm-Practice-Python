# 상하좌우

n = input()

direction = list(map(str, input().strip()))

p = [1, 1]

for d in direction:
    if d == "L" and p[1] != 1:
        p[1] -= 1
    elif d == "R" and p[1] != n:
        p[1] += 1
    elif d == "U" and p[0] != 1:
        p[0] -= 1
    elif d == "D" and p[0] != n:
        p[0] += 1

print(p[0], p[1])
