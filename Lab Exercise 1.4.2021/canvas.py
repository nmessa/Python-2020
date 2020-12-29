##Canvas class definition
##Author: nmessa
##Date: 1/4/2021

import turtle

class Canvas:
    def __init__(self,w,h):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.width = w
        self.height = h

        self.screen.setup(width=self.width,height=self.height)
        self.turtle.hideturtle()

    def draw(self,gObject):
        self.turtle.up()
        self.screen.tracer(0)
        gObject._draw(self.turtle)
        self.screen.tracer(1)
        
    def freeze(self):
        self.screen.exitonclick()
