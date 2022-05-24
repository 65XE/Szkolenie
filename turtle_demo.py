import math
import turtle

turt = turtle.Pen()
turtle.speed(0)


def trochoida(R, r, h):
    t = 0
    x0 = 0
    y0 = 0
    for i in range(int(2*math.pi*150)):
        x = ((R - r) * math.cos(t)) + (h * math.cos(t * (R - r)/r))
        y = ((R - r) * math.sin(t)) - (h * math.sin(t * (R - r)/r))
        t += (2*math.pi)/50
        turt.setpos(x, y)
        if i == 0:
            x0 = x
            y0 = y
            turt.down()
        else:
            if int(x) == int(x0) and int(y) == int(y0):
                break
turt.up()
trochoida(400, 220, 110)
turt.up()
turt.setpos(0, 0)
trochoida(800, 400, 50)
turt.up()
turt.setpos(0, 0)
trochoida(70, 30, 30)


turtle.Screen().exitonclick()