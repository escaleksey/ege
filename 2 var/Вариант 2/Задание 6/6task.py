from turtle import *
from time import sleep
color("black", "red")
m = 100
begin_fill()
left(90)
for i in range(3):
    forward(6 * m)
    right(120)

end_fill()
canvas = getcanvas()
c = 0
for x in range(-20 * m, 20 * m, m):
    for y in range(-20 * m, 20 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            c += 1
print(c)
sleep(2)