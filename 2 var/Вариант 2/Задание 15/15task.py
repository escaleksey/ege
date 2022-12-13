def DEL(n, m):
    return n % m == 0


def f(x, A):
    return ((not (DEL(x, A))) or not(not(DEL(x, 24)) or (not(DEL(x, 74))))) and (A > 500)


for A in range(500, 2000):
    if all(f(x, A) for x in range(10000)):
        print(A)
        break
