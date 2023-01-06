b = open('17.txt', 'r').readlines()
b = list(map(int, b))
sums = []
for i in range(len(b) - 1):
    if (b[i] % 2) == 0:
        sums.append(b[i] + b[i + 1])
    elif b[i + 1] % 2 == 0:
        sums.append(b[i] + b[i + 1])

print(len(sums), min(sums), '\nВ учебнике другой ответ')