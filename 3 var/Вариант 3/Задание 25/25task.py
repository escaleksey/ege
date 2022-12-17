x = []
for i in range(50 * 10 ** 6, 60 * 10 ** 6 + 1):
    if i % 911 == 0:
        c = 0
        for j in range(2, round(i ** 0.5) + 1):
            if i % j == 0:
                c += 1
            if c > 3:
                break
        if c == 3:
            x.append(i)

print(len(x), min(x))