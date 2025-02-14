import turtle
import time
wn = turtle.Screen()
wn.title("Stoplight")
wn.bgcolor("grey")

pen=turtle.Turtle()
pen.color("black")
pen.width(5)
pen.up()
pen.goto(-600,0)
pen.down()
pen.lt(90)
pen.fd(300)
pen.rt(90)
pen.fd(250)
pen.rt(90)
pen.fd(600)
pen.rt(90)
pen.fd(250)
pen.rt(90)
pen.fd(300)


red_light=turtle.Turtle()
red_light.shape("circle")
red_light.shapesize(9,9)
red_light.color("red")
red_light.penup()
red_light.goto(-475,200)

yellow_light=turtle.Turtle()
yellow_light.shape("circle")
yellow_light.shapesize(9,9)
yellow_light.color("yellow")
yellow_light.penup()
yellow_light.goto(-475,0)

green_light=turtle.Turtle()
green_light.shape("circle")
green_light.shapesize(9,9)
green_light.color("green")
green_light.penup()
green_light.goto(-475,-200)
while True:
    green_light.color("grey")
    yellow_light.color("grey")
    red_light.color("red")
    time.sleep(5)

    green_light.color("green")
    yellow_light.color("grey")
    red_light.color("grey")
    time.sleep(5)

    green_light.color("grey")
    yellow_light.color("yellow")
    red_light.color("grey")
    time.sleep(5)

wn.mainloop()