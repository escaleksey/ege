with open('26.txt', 'r') as file:
    data = file.readlines()
money = int(data[0].split()[0])
data = list(map(int, data[1:]))
rare = sorted(list(filter(lambda x: x > 3000, data)))
common = sorted(list(filter(lambda x: x <= 3000, data)))
rare_books = [rare[0], rare[1], rare[2]]
for elem in rare_books:
    money -= elem

i = 0
common_books = []
while money - common[i] >= common[i]:
    common_books.append(common[i])
    money -= common[i]
    i += 1

common = common[::-1]
for elem in common:
    if money - elem >= 0:
        common_books.append(elem)
        break
print(len(common_books) + 3, max(common_books))