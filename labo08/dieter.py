import turtle
from letters import letter_d, letter_i

scrn = turtle.Screen()
ttl = turtle.Turtle()

# Go to the left lower corner.
ttl.penup()
ttl.setpos(scrn.window_width() / -2 + 25, scrn.window_height() / -2 + 25)

letter_d.draw_capital(ttl, 300)
letter_i.draw(ttl, 300)
#letter_e.draw(ttl, 300)
#letter_t.draw(ttl, 300)
#letter_e.draw(ttl, 300)
#letter_r.draw(ttl, 300)

turtle.done()