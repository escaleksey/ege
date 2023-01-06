def f(n, b):
    if n > b:
        return 0
    if n == b:
        return 1
    return f(n + 1, b) + f(n * 2, b) + f(n * 3, b)



c = 0
c += f(1, 7)
c *= f(7, 14)
c *= f(14, 30)
print(c)