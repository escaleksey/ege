with open('17.txt', 'r') as file:
    data = list(map(int, file.readlines()))


elements = list(filter(lambda x: str(x)[-1] == '3', data))
avg = sum(elements) // len(elements)
m_num = max(data)
l = []
for i in range(len(data) - 1):
    a = data[i]
    b = data[i + 1]
    if m_num % a == 0 or m_num % b == 0:
        if (a + b) > avg:
           l.append(a + b)
print(len(l), min(l))