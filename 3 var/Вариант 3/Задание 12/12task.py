for i in range(20):
    for j in range(30):
        for k in range(20):
            a = '0' + '2' * i + '4' * j + '6' * k
            while '02' in a or '04' in a or '06' in a:
                if '02' in a:
                    a = a.replace('02', '6404', 1)
                if '04' in a:
                    a = a.replace('04', '2206', 1)
                if '06' in a:
                    a = a.replace('06', '440', 1)

            if a.count('2') == 30 and a.count('4') == 54 and a.count('6') == 10:
                print(f' 2 - {i} \n 4 = {j} \n 6 = {k} - ОТВЕТ')
