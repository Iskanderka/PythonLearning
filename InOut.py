# def cleaning(text):
#     textlist = list(text)
#     for sign in [" ", ".", ",", "!", "?", ":", ";", "(", ")", "...", "-", "'", "\""]:
#         if sign in textlist:
#             for number in range(0, textlist.count(sign)):
#                 textlist.remove(sign)
#
#     cleantext = "".join(textlist).lower()  # lower опускает всё в нижний регистр
#     return cleantext
#
#
# def reverse(text):
#     text = cleaning(text)
#     return text[::-1]
#
#
# def is_palindrome(text):
#     return cleaning(text) == reverse(text)
#
#
# something = input('Введите текст: ')
# if is_palindrome(something):
#     print("Да, это палиндром")
# else:
#     print("Нет, это не палиндром")


# работа с файлами

# poem = '''
# Программировать весело.
# Если работа скучна,
# Чтобы придать ей весёлый тон
#         используй Python!
# '''
# f = open('poem.txt', 'w')  # открываем для записи ('w'riting). Есть ещё a (append) и r. Если файла нет, он создаётся
# f.write(poem)  # записываем текст в файл
# f.close()  # закрываем файл
#
# f = open('poem.txt')  # если не указан режим, по умолчанию подразумевается # режим чтения ('r'eading)
#
# while True:
#     line = f.readline()  # построчное считывание
#     if len(line) == 0:  # Нулевая длина обозначает конец файла (EOF)
#         break
#     print(line, end='')  # из файла считываются строки с переводом строки в конце
#
# f.close()  # закрываем файл

# # сохранение объектов в файл
#
# import pickle
#
# # имя файла, в котором мы сохраним объект
# shoplistfile = 'shoplis.data'
# # список покупок
# shoplist = ['яблоки', 'манго', 'морковь']
#
# # Запись в файл
# f = open(shoplistfile, 'wb')  # b - открытие и запись в бинарном виде (write binary)
# pickle.dump(shoplist, f)  # помещаем объект в файл
# f.close()
#
# del shoplist  # уничтожаем переменную shoplist
#
# # Считываем из хранилища
# f = open(shoplistfile, 'rb')  # read binary
# storedlist = pickle.load(f)  # загружаем объект из файла
# print(storedlist)

