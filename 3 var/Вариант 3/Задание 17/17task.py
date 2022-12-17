
data = list(map(int, open('17.txt', 'r').readlines()))
x = [data[i] + data[i + 1] for i in range(len(data) - 1) if abs(data[i]) % 5 == 0 and abs(data[i + 1]) % 5 == 0]
print(len(x), max(x))