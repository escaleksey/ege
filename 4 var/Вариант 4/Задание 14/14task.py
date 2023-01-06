for x in range(1, 11100):
    a = 81 ** 8 + 3 ** 7 - 9 - x
    y = []
    d = 3
    while a > 0:
        y.append(a % d)
        a //= d

    if y.count(2) == 30:
        print(x)
        exit()

