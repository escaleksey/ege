counter = 0
m_d = 0
for i in range(50 * 10 ** 6, 60 * 10 ** 6 + 1):
    if (i % int(i ** 0.5)) == 0:
        c = 0
        m_d1 = 0
        for x in range(2, int(i ** 0.5)):
            if i % x == 0:
                c += 1
                if m_d1 < i // x:
                    m_d1 = i // x
            if c > 3:
                break
        if c == 3:
            counter += 1
            if m_d < m_d1:
                m_d = m_d1


print(counter, m_d)
