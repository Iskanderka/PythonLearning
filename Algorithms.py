# insertion sort


def insert_sort(a):
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k-1] > a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            k -= 1


A = [2, 24, 876, 1, 9, 7]
insert_sort(A)

print(A)
