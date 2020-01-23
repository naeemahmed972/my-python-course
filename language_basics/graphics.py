# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:59:50 2020

@author: naeem
"""

import turtle
from random import randint

def get_input():
    message = 'Please provide an angle: '
    value_as_string = input(message)
    
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    
    return int(value_as_string)

def generate_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

print('Set up Screen')
turtle.title('Colorful Pattern')
turtle.setup(640, 600)
turtle.hideturtle()
turtle.bgcolor('black')
turtle.colormode(255)
turtle.tracer(10)
turtle.speed(2000)

angle = get_input()

print('Start the drawing')

for i in range(0, 2000):
    turtle.color(generate_random_color())
    turtle.forward(i)
    turtle.right(angle)
    
print('Done')
turtle.done()