# import sys
# import os  # нужно будет писать название модуля через точку, что хорошо, потому что явно
#
# print('Аргументы командной строки:')
# for i in sys.argv:  # работает только если запскать из cmd с параметрами
#     print(i)
#
# print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')  # выводит директории, из которых можно брать модули
#
# print(os.getcwd())  # выводит текущую директорию

# from math import *  # импортирует всё публичное из модуля, но не импортирует, например, __version__
# print("Квадратный корень от 16 -", sqrt(16))  # можно использовать без названия модуля через точку

# if __name__ == "__main__":  # испульзуется атрибут модуля
#     print("Это программа сама ппо себе")  # если просто запустить
# else:
#     print("Меня импортировали в другой модуль")  # если импортнуть из другой проги

# import mymodule  # модуль был засунут в одну из папок, выдаваемых sys.path. Также можно запихивать в директорию
# # с файлом, из которого происходит вызов
# mymodule.say_hi()
# print("Версия", mymodule.__version__)

# from mymodule import say_hi, __version__  # можно и так, но тогда возможно смешение методов и объектов
# say_hi()
# print("Версия", __version__)

# import this  # просто запусти это

# import mymodule
# print(dir(mymodule))  # dir выводит все функции, классы и переменные этого модуля
# print(dir())  # список отрибутов текущего модуля
#
# a = 5
# print(dir())
#
# del a
# print(dir())  # все изменения фиксируются