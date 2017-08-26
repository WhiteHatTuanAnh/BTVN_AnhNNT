from turtle import*
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)

index_no = 0
for j in range ( 3, 9 ):
    pencolor(colors[index_no])
    for i in range ( j ):
        fd(100)
        lt(360/j)
    index_no += 1
    if index_no == 5:
        break

#def start_at_other_place():
up()
fd(300)
down()

i = 1
j = 1

for j in range(5):
    print(j)
    fillcolor(colors[j])
    begin_fill()
    for i in range(2):
        fd(30)
        lt(90)
        fd(60)
        lt(90)

    fd(30)
    end_fill()

mainloop()