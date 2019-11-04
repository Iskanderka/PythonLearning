# try:
#     text = input('Введите что-нибудь --> ')
# except EOFError:
#     print('Ну зачем вы сделали мне EOF?')  # нужно ввсести ctrl+d
# except KeyboardInterrupt:
#     print('Вы отменили операцию.')  # а вот ето хз как
# else:
#     print('Вы ввели {0}'.format(text))


# class ShortInputException(Exception):
#     """Пользовательский класс исключения."""
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
#
# try:
#     text = input('Введите что-нибудь --> ')
#     if len(text) < 3:
#         raise ShortInputException(len(text), 3)
#         # Здесь может происходить обычная работа
# except EOFError:
#     print('Ну зачем вы сделали мне EOF?')
# except ShortInputException as ex:
#     print('ShortInputException: Длина введённой строки -- {0}; \
#      ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
#
# else:
#     print('Не было исключений.')

# import time
#
# try:
#     f = open('poem.txt')
#     while True:  # наш обычный способ читать файлы
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line, end='')
#         time.sleep(2)  # Пусть подождёт некоторое время. Приостановка на 2 секунды
#
# except KeyboardInterrupt:
#     print('!! Вы отменили чтение файла.')
# finally:  # выполняется по-любому
#     f.close()
#     print('(Очистка: Закрытие файла)')

# with open("poem.txt") as f:
#     for line in f:  # оказывается так можно было лул
#         print(line, end='')
