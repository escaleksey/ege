b = open('24.txt').read()
b = b.replace('ABC', '1')
b = b.split('1')
dictionary = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

for elem in b:
    if elem:
        dictionary[elem[0]] += 1
    else:
        dictionary['A'] += 1

z = list(dictionary.items())
z.sort(key=lambda x: x[-1])
print(*z[0], sep='')
