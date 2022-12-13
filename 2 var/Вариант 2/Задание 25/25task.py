for i in range(18400960, 10 ** 9 + 1):
    b = str(i)
    if b[0:4] == '1840' and b[5] == '9' and b[-2] == '6':
        if i % 149 == 0:
            print(i, i // 149)