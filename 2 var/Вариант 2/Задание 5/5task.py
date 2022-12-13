for i in range(1, 5000):
    b = bin(i)[2:]
    if i % 2 == 0:
        b += '01'
    else:
        b = '1' + b + '10'

    r = int(b, 2)
    if r <= 105:
        print(i)