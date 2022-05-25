import turtle
import math
import sys


class BadValueException(ValueError):
    pass


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def trochoida(big_radius, small_radius, h):

    try:
        if big_radius <= 0 or small_radius <= 0 or h < 0:
            raise BadValueException()
        turtle.up()
        t = 0
        theta = 2 * math.pi * lcm(big_radius, small_radius) / big_radius
        while t <= theta:
            x = ((big_radius - small_radius) * math.cos(t)) + (h * math.cos(t * (big_radius - small_radius) / small_radius))
            y = ((big_radius - small_radius) * math.sin(t)) - (h * math.sin(t * (big_radius - small_radius) / small_radius))
            turtle.setpos(x, y)
            if t == 0:
                turtle.down()
            t += theta / 1000
    except BadValueException:
        print('Dupa')
        # sys.exit()
turtle.tracer(0, 0)

trochoida(-400, 220, 110)
trochoida(800, -400, 50)
trochoida(70, 30, -30)

turtle.update()
turtle.Screen().exitonclick()