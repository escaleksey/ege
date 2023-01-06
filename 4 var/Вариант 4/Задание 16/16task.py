def f(n):
    if n == 1 or n == 2:
        return 1
    if n % 3 == 0:
        return n + f(n//3)
    return n * f(n-2)

print(f(35))