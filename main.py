# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     col=(r,g,b)
#     rgb_colors.append(col)

# print(rgb_colors)

'''our color list from above code is [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), 
                                   (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), 
                                   (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), 
                                   (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), 
                                   (174, 200, 188), (65, 66, 56)]'''

color_list=[(140, 184, 162),(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

import turtle as t
import random

t.colormode(255)

tim= t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for j in range(10):

    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen= t.Screen()
screen.exitonclick()