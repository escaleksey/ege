b = open('24.txt', 'r').read().replace('AD', ' X ').split()
x = [elem[-1] for elem in b]
z1 = {}
for i in range(len(x) - 1):
    if x[i + 1] == 'X':
        if x[i] == 'X':
            z1['D'] += 1
        elif x[i] in z1:
            z1[x[i]] += 1
        else:
            z1[x[i]] = 1

z = [(elem, z1[elem]) for elem in z1.keys()]

print(z)