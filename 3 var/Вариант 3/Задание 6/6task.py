from turtle import *
color('black', 'red')
m = 100
begin_fill()
left(90)
for i in range(2):
    left(60)
    forward(4 * m)
    left(120)
    forward(4 * m)
end_fill()
canvas = getcanvas()
c = 0
for x in range(-20 * m, 20 * m, m):
    for y in range(-20 * m, 20 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            c += 1

print(c)