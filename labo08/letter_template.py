'''
Copy this template for each letter. Then change the functions.
The placeholders in this file just draw rectangles.
'''

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
    '''Draw uppercase letter'''
    draw() # change this