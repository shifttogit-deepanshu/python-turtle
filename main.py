# # import colorgram
# #
# # colors = []
# #
# # for color in colorgram.extract('image.jpg',10):
# #     colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
#
# import turtle
# import random
#
# dh = turtle.Turtle()
#
# screen = turtle.Screen()
#
# screen.colormode(255)
#
# color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]
#
# def random_color():
#     color = random.choice(color_list)
#     return color
#
#
# def generate_dot():
#     dh.penup()
#     dh.dot(20,random_color())
#     dh.forward(20)
#
#
# for x in range(10):
#     generate_dot()
#
# while dh.xcor()==200 and dh.ycor()==200:
#     for y in range(0,10):
#         for x in range(0,10):
#             generate_dot()
#         dh.setpos(0,y)
#
# screen.exitonclick()
import turtle

dh = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    dh.forward(10)

def move_backward():
    dh.backward(10)

def move_left():
    dh.left(10)

def move_right():
    dh.right(10)


screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

screen.listen()
screen.exitonclick()