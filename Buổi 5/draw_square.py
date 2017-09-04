from turtle import*

speed(0)

def draw_square(length, colors):
    color(colors)
    begin_fill()
    for i in range(4):
        fd(length)
        lt(90)
    end_fill()

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
