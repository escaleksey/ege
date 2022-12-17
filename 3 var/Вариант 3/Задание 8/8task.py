b = 'ИДИЛЛИЯ'
x = []
for q in b:
    for w in b:
        for e in b:
            for r in b:
                for t in b:
                    for y in b:
                        for u in b:
                            z = q + w + e + r + t + y + u
                            f = True
                            for elem in z:
                                if z.count(elem) != b.count(elem):
                                    f = False
                            if f:
                                x.append(z)

print(len(set(x)))