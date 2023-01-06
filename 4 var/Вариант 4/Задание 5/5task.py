c = 0
for i in range(4000):
    b = bin(i)[2:]
    if i % 2 == 0:
        b += '00'
    else:
        b += '10'

    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'

    r = int(b, 2)
    if 160 <= r <= 630:
        c += 1

print(c)