from turtle import *

color('black', 'red')
m = 100
begin_fill()
left(90)
for i in range(3):
    forward(8*m)
    left(120)
end_fill()
canvas = getcanvas()
c = 0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x,y,x,y)
        print(item)
        if len(item) == 1 and item[0] == 5:
            c += 1

print(c)