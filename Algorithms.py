# # sort
#
#
# def insert_sort(a):
#     """Сортировка списка A вставками"""
#     n = len(a)
#     for top in range(1, n):
#         k = top
#         while k > 0 and a[k - 1] > a[k]:
#             a[k], a[k - 1] = a[k - 1], a[k]
#             k -= 1
#
#
# def choise_sort(a):
#     """Сортировка списка A выбором"""
#     n = len(a)
#     for pos in range(0, n-1):
#         for k in range(pos+1, n):
#             if a[k] < a[pos]:
#                 a[k], a[pos] = a[pos], a[k]
#
#
# def bubble_sort(a):
#     n = len(a)
#     for bypass in range(1, n):
#         for k in range(0, n-bypass):
#             if a[k] > a[k + 1]:
#                 a[k], a[k + 1] = a[k + 1], a[k]
#
#
# A = [2, 24, 876, 1, 9, 7]
# insert_sort(A)
#
# B = [2, 24, 876, 1, 9, 7]
# choise_sort(B)
#
# C = [2, 24, 876, 1, 9, 7]
# bubble_sort(C)
#
# print(A)
# print(B)
# print(C)

# # factor
#
#
# def f(n: int):
#     assert n >= 0, "Факториал от отрицательного не определён"
#     if n == 0:
#         return 1
#     return f(n-1)*n
#
#
# print(f(12))

# # Быстрое возведение в степень
#
#
# def power(a: float, n: int):
#     if n == 0:
#         return 1
#     elif n % 2 == 1:  # нечёт
#         return power(a, n-1)*a
#     else:  # чёт, можно поделить её на 2, вместе с тем возвести само число в квадрат
#         return power(a**2, n//2)
#
#
# print(power(5, 3))


# #  генерация всех перестановок
#
# # # но сначала генерация всех чисел заданной длины в n-ричной СС
# #
# #
# # def generate_numbers(n: int, m: int, prefix=None):
# #     if m == 0:
# #         print(prefix)
# #         return
# #     prefix = prefix or []
# #     for digit in range(n):
# #         prefix.append(digit)
# #         generate_numbers(n, m-1, prefix)
# #         prefix.pop()
# #
# #
# # generate_numbers(3, 3)
#
#
# def gen_permutations(n: int, m: int = -1, prefix=None):
#     if m == -1:
#         m = n
#     prefix = prefix or []
#     if m == 0:
#         print(*prefix, sep="")
#         return
#     for number in range(1, n + 1):
#         if number in prefix:
#             continue
#         prefix.append(number)
#         gen_permutations(n, m - 1, prefix)
#         prefix.pop()
#
#
# gen_permutations(3)
