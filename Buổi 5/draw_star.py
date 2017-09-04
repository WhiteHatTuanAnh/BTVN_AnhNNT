from turtle import *

def draw_star(x,y, length):
    penup()
    goto(x,y)
    lt(180-144)
    pendown()
    begin_fill()
    for i in range(6):
        fd(length)
        lt(144)
    end_fill()
    rt(180-144)

speed(0)
bgcolor('black')
color('yellow')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(20, 40)
    draw_star(x, y, length)

mainloop()
