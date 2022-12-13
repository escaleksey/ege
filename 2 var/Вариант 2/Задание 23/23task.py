
def f(n, y):
    if n == y:
        return 1
    if n > y:
        return 0
    return f(n+1, y) + f(n * 3, y)


print(f(1, 24) * f(24, 60))