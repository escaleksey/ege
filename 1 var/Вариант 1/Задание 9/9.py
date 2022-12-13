print(sum([1 for elem in list(map(lambda x: sorted(list(map(int, x.split()))), open('9.txt', 'r').readlines())) if (elem[0] + elem[-1]) < (2 * (elem[1] + elem[2]))]))
