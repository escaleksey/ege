l = 'ЕКОР'
c = 0
for i in l:
    for j in l:
        for k in l:
            for h in l:
                for u in l:
                    for p in l:
                        b = i + j + k + h + u + p
                        c += 1
                        if b[0] == "О" and "ЕЕ" not in b:
                            print(c)