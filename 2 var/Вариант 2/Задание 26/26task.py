with open('26.txt', 'r') as file:
    data = list(map(lambda x: [int(_) for _ in x.split()], file.readlines()[1:]))

data.sort(key=lambda x: (x[1], x[0]))

d_cols = {}
for elem in data:
    if elem[1] in d_cols:
        d_cols[elem[1]] += [elem[0]]
    else:
        d_cols[elem[1]] = [elem[0]]
print(d_cols)
numbers_cols = []
for key in d_cols.keys():
    v = d_cols[key]
    delta = []
    for i in range(len(v) - 1):
        delta.append(abs(v[i] - v[i + 1]) - 1)
    if 10 in delta:
        numbers_cols.append(key)

print(max(numbers_cols), max(d_cols[max(numbers_cols)]) - 1)
