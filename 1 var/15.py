def f(n, m):
    return (n % m) == 0


for A in range(300, 1000):
    if all((((f(x, A) or not f(x, 27) or not f(x, 89)) and (A > 300))) == 1 for x in range(1, 100000)):
        print(A)
        break