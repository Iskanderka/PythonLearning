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

# # спираль
#
# fi_rad = 0.2
# fi_degr = fi_rad*(180/3.14)
# ro = fi_rad
#
# for i in range(0, 1000):
#     turtle.forward(ro)
#     turtle.left(fi_degr)
#     ro += 0.2

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

# # павук
#
# number_of_legs = int(turtle.textinput("Окошечко", "Введите число ног паучка"))
# angle = 360 / number_of_legs
#
# for i in range(number_of_legs):
#     turtle.left(angle)
#     turtle.forward(70)
#     turtle.stamp()
#     turtle.left(180)
#     turtle.forward(70)
#     turtle.right(180)

# # вложенные квадраты
#
# length = 5
#
# for i in range(40):
#     turtle.forward(length)
#     turtle.left(90)
#     length += 5

# вложенные многоугольники


def n_apex_figure(n: int):
    angle = 180 - 360/n
    turtle.left(angle/2)
    for i in range(n):
        turtle.left(180 - angle)
        turtle.forward(100)


turtle.done()
