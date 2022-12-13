s = '>' + '2' * 12 + '3' * 21 + '5' * 15 + '3'
while '>2' in s or '>3' in s or '>5' in s:
    if '>2' in s:
        s = s.replace('>2', '55>')
    if '>3' in s:
        s = s.replace('>3', '523>')

    if '>5' in s:
        s = s.replace('>5', '52>')

b = sum(list(map(int, ' '.join(s[:-1].split()))))
print(b)