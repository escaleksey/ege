for i in range(50):
    for j in range(20):
        for z in range(50):
            a = '0' + '2' * i + '4' * j + '6' * z
            while '02' in a or '04' in a or '06' in a:
                if '02' in a:
                    a = a.replace('02', '620', 1)
                if  '04' in a:
                    a = a.replace('04', '4206', 1)
                if '06' in a:
                    a = a.replace('06', '402', 1)

            if a.count('2') == 38 and a.count('4') == 32 and a.count('6') == 28:
                print(j)