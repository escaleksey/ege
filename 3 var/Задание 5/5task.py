c = 0
z = [x for x in range(130, 351)]
for n in range(1400):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += '00'
    else:
        b += '10'

    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'

    r = int(b, 2)
    if r in z:
        c += 1

print(c)