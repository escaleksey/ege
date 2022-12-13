b = '123456789abc'
for e in b:
    c = int('186' + e + '4', 13) + int('5' + e + '716', 13)
    if c % 11 == 0:
        print(c//11)