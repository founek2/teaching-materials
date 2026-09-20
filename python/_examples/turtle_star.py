import turtle

n = 15
angle = 180 - (180/n)
len = 100
for x in range(n):  # 0, 1, 2...
    turtle.forward(len)
    turtle.right(angle)

turtle.exitonclick()
