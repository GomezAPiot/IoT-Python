import turtle
from letters import letter_g

scrn = turtle.Screen()
ttl = turtle.Turtle()

# Go to the left lower corner.
ttl.penup()
ttl.setpos(scrn.window_width(+25) / -2 + 25, scrn.window_height(+25) / -2 + 25)

letter_g.draw_capital(ttl, 300)


def draw(turtle, size=400):
    '''Draw lowercase letter.'''
    turtle.pensize(1)
    turtle.setheading(0)
    turtle.pencolor('grey')
    turtle.pendown()
    for s in (1, 2):
        for side in (size / 2, size):
            turtle.forward(side)
            turtle.left(90)
    turtle.penup()
    turtle.setx(turtle.pos()[0] + size / 2 + size / 40)


def draw_capital(turtle, size=400):
    '''G'''
    draw(G)  # change this


turtle.done()
