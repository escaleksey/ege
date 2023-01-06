data = open('26.txt', 'r').readlines()
money = int(data[0].split()[0])
c = 0
data = list(map(int, data[1:]))
rare = sorted(list(filter(lambda x: x > 3000, data)))
rare_books = [rare[0], rare[1]]
enc_books = sorted([x for x in data if 2000 <= x <= 3000])
common_books = sorted([x for x in data if 2000 > x])
for elem in rare_books:
    money -= elem
c += 2
money -= sum(enc_books)
c += len(enc_books)
i = 0
prices = []
while money - common_books[i] >= common_books[i]:
    prices.append(common_books[i])
    money -= common_books[i]
    i += 1

common_books = common_books[::-1]

for elem in common_books:
    if money - elem >= 0:
        prices.append(elem)
        break

print(len(prices) + c, max(prices))


