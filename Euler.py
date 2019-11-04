# # Первая задача
#
# summ = 0
#
# for i in range(1, 1000):
#     if (i % 3 == 0) or (i % 5 == 0):
#         summ += i
#
# print(summ)


# # Вторая задача
#
# pr_number = 2
# number = 3
#
# sum = 2
#
# while number < 4000000:
#     if number % 2 == 0:
#         sum += number
#     number, pr_number = number + pr_number, number
#
# print(sum)

# # Третья задача
#
# import math
#
#
# def is_simple(number):
#     for i in range(2, int(math.sqrt(number))):
#         if number % i == 0:
#             return False
#
#     return True
#
#
# for div in range(1, int(600851475143//2)):
#     if 600851475143 % div == 0:
#         print(div)
#         if is_simple(600851475143/div):
#             answer = div
#             break
#
# print(answer)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [elem for elem in a if elem < 5]
#
# # for i in a:
# #     if i < 5:
# #         b.append(i)
#
# print(b)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# c = list(set(a) & set(b))
#
# print(c)
#
# c = [elem for elem in a if elem in b]
#
# print(c)


# def binary_search(list, item):
#     low_index = 0
#     high_index = len(list) - 1
#
#     while low_index <= high_index:
#         mid = (low_index + high_index) // 2
#         guess = list[mid]
#         if guess == item:
#             return mid + 1
#         elif guess > item:
#             high_index = mid - 1
#         else:
#             low_index = mid + 1
#     return "Элемент не найден"
#
#
# my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
#
# while True:
#     user_guess = input("Введите число, мы выведем его позицию в списке: ")
#     if user_guess == "Хватит":
#         break
#     print(binary_search(my_list, int(user_guess)))


# from random import *
# from tkinter import *
# import time
#
# size = 600
# root = Tk()
# canvas = Canvas(root, width=size, height=size)
# canvas.pack()
# diapason = 0
#
# while diapason < 1000:
#     colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
#                      'pink', 'purple', 'red', 'yellow', 'violet', 'indigo', 'chartreuse', 'lime', "#f55c4b"])
#     x0 = randint(0, size)
#     y0 = randint(0, size)
#     d = randint(0, size/5)
#     canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors)
#     root.update()
#     diapason += 1
#
# time.sleep(5)


from tkinter import *


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.set_ui()
        self.brush_size = 10
        self.brush_color = "black"

    def set_ui(self):
        self.parent.title("Pythonicway PyPaint")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>", self.draw)

        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)

        red_btn = Button(self, text="Red", width=10, command=lambda: self.set_color("red"))
        red_btn.grid(row=0, column=1)

        green_btn = Button(self, text="Green", width=10, command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        red_btn = Button(self, text="Blue", width=10, command=lambda: self.set_color("blue"))
        red_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=10, command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="White", width=10, command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)

        one_btn = Button(self, text="Two", width=10, command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10, command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="Seven", width=10, command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="Ten", width=10, command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="Twenty", width=10, command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="Fifty", width=10, command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)

        clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.brush_color, outline=self.brush_color)

    def set_color(self, new_color):
        self.brush_color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size


def main():
    root = Tk()
    root.geometry("1920x1080")
    app = Paint(root)
    root.mainloop()


if __name__ == "__main__":
    main()


