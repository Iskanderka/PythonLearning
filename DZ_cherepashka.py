import turtle
turtle.shape('turtle')

# # тестовый запуск
#
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)

# # квадрат
#
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# # окружность
#
# for i in range(60):
#     turtle.forward(10)
#     turtle.left(6)

# # вложенные квадраты
#
# length = 20
#
# for i in range(10):
#     for j in range(4):
#         turtle.forward(length)
#         turtle.left(90)
#     turtle.penup()
#     turtle.goto(turtle.xcor() - 10, turtle.ycor() - 10)
#     length += 20
#     turtle.pendown()

# спираль

degree = 10

for i in range(500):
    turtle.forward(5)
    turtle.left(degree)
    degree = degree * 0.99


turtle.done()
