# insertion sort


def insert_sort(a):
    """Сортировка списка A вставками"""
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


def choise_sort(a):
    """Сортировка списка A выбором"""
    n = len(a)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def bubble_sort(a):
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]


A = [2, 24, 876, 1, 9, 7]
insert_sort(A)

B = [2, 24, 876, 1, 9, 7]
choise_sort(B)

C = [2, 24, 876, 1, 9, 7]
bubble_sort(C)

print(A)
print(B)
print(C)

