
b = sorted(list(map(int, open('27_A.txt').readlines()[1:])))
c = []
z = []
for i in range(len(b)):
    a = b[i] % 5
    if a not in z:
        z.append(a)
        c.append(b[i])
    if len(c) == 5: break
print(sum(c))