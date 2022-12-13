l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
for x in l:
    n1 = '26' + x + '34'
    n2 = '3' + x + '597'

    '''a = list(reversed(list(' '.join(n1).split())))
    b = list(reversed(list(' '.join(n2).split())))
    a = list(reversed(list(map(int, ' '.join(n1).split()))))
    b = list(reversed(list(map(int, ' '.join(n2).split()))))
    
    for i in range(5):
        a[i] = l.index(a[i]) * 17 ** i
        b[i] = l.index(b[i]) * 17 ** i'''

    n1 = int(n1, 17)
    n2 = int(n2, 17)
    if (n1 + n2) % 13 == 0:
        print(x, (n1 + n2) // 13)
    '''c = sum(b)
    z = sum(a)

    if (z + c) % 13 == 0:
        print(x, (z + c) / 13)'''