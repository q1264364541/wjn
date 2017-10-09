import turtle 

turtle.color('red')
turtle.begin_fill()
for i in range(2):
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.up()
turtle.color('red')
turtle.end_fill()
#画矩形，有星星的那个小矩形

turtle.goto(20,60)
turtle.down()
turtle.color('yellow','yellow')
turtle.begin_fill()
for i in range(5):
    turtle.forward(60)
    turtle.right(144)
turtle.end_fill()
#大的星星

turtle.up()
turtle.goto(100,80)
turtle.down()
turtle.color('yellow','yellow')
turtle.left(217)
turtle.forward(10)
turtle.right(162)
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
#右上角的星星

turtle.up()
turtle.goto(120,60)
turtle.color('yellow','yellow')
turtle.right(172)
turtle.forward(10)
turtle.down()
turtle.right(170)
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
#右上角第二个小星星

turtle.up()
turtle.goto(120,30)
turtle.down()
turtle.color('yellow','yellow')
turtle.left(164)
turtle.forward(10)
turtle.right(164)
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
#右上角第三个小星星

turtle.up()
turtle.goto(100,10)
turtle.down()
turtle.color('yellow','yellow')
turtle.left(141)
turtle.forward(10)
turtle.right(162)
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
#右上角第四个小星星

turtle.up()
turtle.home()
turtle.down()
turtle.color('red','red')
turtle.begin_fill()
for i in range(2):
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.up()
turtle.end_fill()

turtle.home()
turtle.forward(150)
turtle.down()
turtle.begin_fill()
for i in range(2):
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.up()
turtle.color('red','red')
turtle.end_fill()

turtle.home()
turtle.forward(150)
turtle.down()
turtle.begin_fill()
for i in range(2):
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.up()
turtle.color('red','red')
turtle.end_fill()

turtle.write('Done')
turtle.done()
import turtle 

def rectangle(sides,color):
    turtle.color(color,color)
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)    
    turtle.end_fill()

def stapelia(pos_x,pos_y,color,angle1,forward_distance,angle2,side_length):
    turtle.up()
    turtle.goto(pos_x,pos_y)
    turtle.color(color,color)
    turtle.down()
    turtle.right(angle1)
    turtle.forward(forward_distance)
    turtle.right(angle2)
    turtle.begin_fill()    
    for i in range(5):
        turtle.forward(side_length)
        turtle.right(144)
    turtle.end_fill()

turtle.hideturtle()
rectangle(2,'red')
stapelia(20,160,'yellow',0,0,0,60)
#大的星星
stapelia(100,180,'yellow',143,10,162,20)
#右上角第一个星星
stapelia(120,160,'yellow',172,10,170,20)
#右上角第二个星星
stapelia(120,130,'yellow',196,10,164,20)
#右上角第三个星星
stapelia(100,110,'yellow',219,10,162,20)
#右上角第四个星星
turtle.done()
