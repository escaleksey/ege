from turtle import *
from time import sleep
m = 100
color('black', 'red')
begin_fill()
left(90)
right(30)
for i in range(2):
    forward(6 * m)
    right(120)
    forward(6 * m)
    right(60)

end_fill()
canvas = getcanvas()
c = 0
for x in range(-20 * m, m * 20, m):
    for y in range(-20 * m, m * 20, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            c += 1

print(c)
sleep(5)