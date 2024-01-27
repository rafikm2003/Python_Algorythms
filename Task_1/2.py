from random import randint


def merge(tab):
    if len(tab) > 1:
        mid = len(tab)//2
        left = tab[:mid]
        right = tab[mid:]

        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            tab[k] = right[j]
            j += 1
            k += 1


def partition(tab, low, high):
    pivot = tab[high]
    i = low - 1
    for j in range(low, high):
        if tab[j] <= pivot:
            i = i+1
            (tab[i], tab[j]) = (tab[j], tab[i])
    (tab[i+1], tab[high]) = (tab[high], tab[i+1])
    return i+1


def quick(tab, low, high):
    if low < high:
        pi = partition(tab, low, high)
        quick(tab, low, pi - 1)
        quick(tab, pi+1, high)


def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap(tab):
    n = len(tab)

    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, n, i)

    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, i, 0)


tab = []
tab2 = []
tab3 = []
for i in range(0, 20):
    tab.append(randint(0, 100))
    tab2.append(randint(0, 100))
    tab3.append(randint(0, 100))


print('tab before sort')
print(tab)
print('tab after sort')
merge(tab)
print(tab)
print('tab 2 before sort')
print(tab2)
quick(tab2, 0, len(tab2) - 1)
print('tab 2 after sort')
print(tab2)
print('tab 3 before sort')
print(tab3)
heap(tab3)
print('tab 3 after sort')
print(tab3)
