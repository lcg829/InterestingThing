#coding = utf-8

import turtle
import time

turtle.speed(30)
# 吹风机
# 1. nose
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.setheading(-30)

# pencolor, fillcolor
turtle.color("black", "pink")
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        turtle.left(3)
        turtle.forward(a)
    else:
        a = a - 0.08
        turtle.left(3)
        turtle.forward(a)
turtle.end_fill()

# 2.鼻孔
turtle.penup()
turtle.setheading(90)# 设置鼻子朝向
turtle.forward(25)
turtle.setheading(0)
turtle.forward(10)
turtle.pendown()
turtle.setheading(10)
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.setheading(0)
turtle.forward(20)
turtle.pendown()
turtle.setheading(10)
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# head
turtle.penup()
turtle.goto(-69, 167)
turtle.setheading(0)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(180)
turtle.circle(300, -30)
turtle.circle(100, -60)
turtle.circle(80, -100)
turtle.circle(150, -20)
turtle.circle(60, -95)
turtle.setheading(161)
turtle.circle(-300, 15)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.setheading(-30)
a = 0.4
for i in range(60):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        turtle.left(3) #向左转3度
        turtle.forward(a) #向前走a的步长
    else:
        a = a - 0.08
        turtle.left(3)  # 向左转3度
        turtle.forward(a)  # 向前走a的步长
turtle.end_fill()

# ears
turtle.penup()
turtle.goto(0, 160)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(100)
turtle.circle(-50, 50)
turtle.circle(-10, 120)
turtle.circle(-50, 54)
turtle.end_fill()

turtle.penup()
turtle.setheading(90)
turtle.forward(-12)
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(100)
turtle.circle(-50, 50)
turtle.circle(-10, 120)
turtle.circle(-50, 56)
turtle.end_fill()

# eyes
turtle.fillcolor("white")
turtle.penup()
turtle.setheading(90)
turtle.forward(-20)
turtle.setheading(0)
turtle.forward(-95)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.setheading(90)
turtle.forward(12)
turtle.setheading(0)
turtle.forward(-3)
turtle.pendown()
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()

turtle.penup()
turtle.seth(90)
turtle.forward(-25)
turtle.seth(0)
turtle.forward(40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.setheading(90)
turtle.forward(12)
turtle.setheading(0)
turtle.forward(-3)
turtle.pendown()
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()

# 腮
turtle.color("violet")
turtle.penup()
turtle.goto(80, 10)
turtle.pendown()
turtle.setheading(0)
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# mouth
turtle.color("red")
turtle.penup()
turtle.goto(-20, 30)
turtle.pendown()
turtle.setheading(-80)
turtle.circle(30, 40)
turtle.circle(40, 80)

# body
turtle.fillcolor("red")
turtle.penup()
turtle.goto(-32, -8)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(-130)
turtle.circle(100, 10)
turtle.circle(300, 30)
turtle.setheading(0)
turtle.forward(230)
turtle.setheading(90)
turtle.circle(300, 30)
turtle.circle(100, 3)
turtle.setheading(-135)
turtle.circle(-80, 63)
turtle.circle(-150, 24)
turtle.end_fill()

# hand
turtle.color("pink")
turtle.pensize(15)
turtle.penup()
turtle.goto(-56, -45)
turtle.pendown()
turtle.setheading(-160)
turtle.circle(300,15)
turtle.penup()
turtle.setheading(90)
turtle.forward(15)
turtle.setheading(0)
turtle.forward(0)
turtle.pendown()
turtle.setheading(-10)
turtle.circle(-20, 90)

turtle.penup()
turtle.setheading(90)
turtle.forward(30)
turtle.setheading(0)
turtle.forward(237)
turtle.pendown()
turtle.setheading(-20)
turtle.circle(-300, 15)
turtle.penup()
turtle.setheading(90)
turtle.forward(20)
turtle.setheading(0)
turtle.forward(0)
turtle.pendown()
turtle.setheading(-170)
turtle.circle(20, 90)

# tail
turtle.pensize(4)
turtle.penup()
turtle.goto(148, -155)
turtle.pendown()
turtle.seth(0)
turtle.circle(70, 20)
turtle.circle(10, 330)
turtle.circle(70, 30)

# foot
turtle.pensize(10)
turtle.penup()
turtle.goto(2, -177)
turtle.pendown()
turtle.setheading(-90)
turtle. forward(40)
turtle.setheading(-180)
turtle.color("blue")
turtle.pensize(15)
turtle.forward(20)

turtle.color("pink")
turtle.pensize(10)
turtle.penup()
turtle.setheading(90)
turtle.forward(40)
turtle.setheading(0)
turtle.forward(90)
turtle.pendown()
turtle.setheading(-90)
turtle.forward(40)
turtle.setheading(-180)
turtle.color("blue")
turtle.pensize(15)
turtle.forward(20)

time.sleep(2)

turtle.penup()
turtle.goto(200, -140)
turtle.color("violet")
turtle.write("Done", font=('Arial', 15, 'normal'))
turtle.goto(200, -180)
turtle.write("2019-1-20", font=('Arial', 15, 'normal'))
turtle.goto(200, -220)
turtle.write("LCG", font=('Arial', 15, 'normal'))
turtle.mainloop()
