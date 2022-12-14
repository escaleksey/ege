for x in range(1, 12800):
    a = 243 ** 5 + 3 ** 7 - 2 - x
    d = 3
    y = []
    while a > 0:
        y.append(a % d)
        a //= d

    if y.count(2) == 20:
        print(x)