data = list(map(lambda x: sorted([int(_) for _ in x.split()]), open('9.txt', 'r').readlines()))

print(len([x for x in data if (x[0] * x[-1]) > (x[1] * x[2])]))
