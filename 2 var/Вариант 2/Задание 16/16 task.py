from functools import lru_cache
import sys

@lru_cache()
def f(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n % 4 == 0:
        return n - f(n // 4) - f(n - 3)
    if n % 4 != 0:
        return 2 + f(n - 1) + f(n // 5)


c = 0
for n in range(40, 120):
    b = f(n)
    if (b > 60) and (b <= 240):
        print(b)
        c += 1


print(c)