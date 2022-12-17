def f(n, x):
    if n > x:
        return 0
    if n == x:
        return 1
    return f(n + 1, x) + f(n * 2, x) + f(n * 5, x)


print(f(1, 10) * f(10, 20) * f(20, 38))