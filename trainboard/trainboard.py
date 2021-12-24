import http.client
import json
from datetime import datetime
from turtle import Screen, Turtle


con = http.client.HTTPSConnection("api.irail.be")
con.request(
    "GET", "/liveboard/?id=BE.NMBS.008892007&arrdep=departure&format=json")
test1 = con.getresponse()
print(test1.status)
test1 = test1.read()
# print(test1)

dataTest1 = json.loads(test1)
# print(dataTest1)
departureList = dataTest1["departures"]["departure"]
for x in departureList:
    print(x["station"], datetime.fromtimestamp(int(x["time"])),
          x["platform"], x["vehicleinfo"]["shortname"])
    # dest, time, platform, train name

    # print(departureList)


def drawboxes():
    turtle.setheading(270)

    for _ in range(2):
        for fill_color in ('blue', 'darkblue'):
            turtle.fillcolor(fill_color)
            turtle.begin_fill()

            for _ in range(2):
                turtle.forward(100)
                turtle.left(90)
                turtle.forward(400)
                turtle.left(90)

            turtle.end_fill()

            turtle.penup()
            turtle.forward(100)
            turtle.pendown()


screen = Screen()

turtle = Turtle()
turtle.pencolor('white')

drawboxes()

screen.exitonclick()
