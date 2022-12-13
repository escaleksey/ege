l1 = ['E', 'I']
l2 = ['F', 'G', 'H']
b = open('24-var2.txt', 'r').read()
for elem in l1:
    for elem2 in l2:
        b = b.replace(elem + elem2, ' ')
lengths = list(map(lambda x: len(x), b.split()))
print(max(lengths))