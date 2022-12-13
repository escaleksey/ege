l = 'ЕКОР'
c = 0
for q in l:
    for w in l:
        for e in l:
            for r in l:
                for t in l:
                    for y in l:
                        word = q + w + e + r + t + y
                        c += 1
                        #print(word, c)
                        if y == 'К' and 'РР' not in word:

                            print(c)