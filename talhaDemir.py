import turtle

def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    if height < 0:
        t.penup()
        t.forward(-20)
        t.right(90)
        t.forward(6)
        t.write(height,font=("Arial", 12, "italic", "bold"))
        t.forward(-6)
        t.left(90)
        t.forward(20)
        t.pendown()
    else:
        t.penup()
        t.right(90)
        t.forward(6)
        t.write(height, font=("Arial", 12, "italic", "bold"))
        t.forward(-6)
        t.left(90)
        t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.end_fill()
    t.left(90)
    t.penup()
    t.forward(10)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("white")

tess = turtle.Turtle()
tess.pensize(3)
tess.penup()
tess.setposition(-170, 0)
tess.pendown()


xs = [-48,117,200,-240,160,260,220]

for a in xs:
    if a >= 200:
        tess.color("black", "red")
    elif a > 100:
        tess.color("black", "yellow")
    else:
        tess.color("black", "green")
    draw_bar(tess, a)



wn.mainloop()