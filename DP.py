d = [0] * 100

def fibonacci(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibonacci(x-1) + fibonacci(x-2)
    return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(50))