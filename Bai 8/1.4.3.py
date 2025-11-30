import turtle

colors = ["red","green","blue","orange","purple","pink","yellow"]
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)

for i in range(12):
    painter.pencolor(colors[i % len(colors)])  # đổi màu lần lượt
    painter.circle(100)
    painter.right(30)  # xoay đều 360/12 = 30 độ

turtle.done()
