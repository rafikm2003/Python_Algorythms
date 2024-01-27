import psutil
import time
import copy
import pandas as pd


def bubble(tab):
    if tab:
        for i in range(0, len(tab)):
            for j in range(i, len(tab)):
                if tab[i] > tab[j]:
                    a = tab[i]
                    tab[i] = tab[j]
                    tab[j] = a


def insertion(tab):
    if tab:
        for i in range(1, len(tab)):
            j = i
            while j > 0:
                if tab[j] < tab[j - 1]:
                    a = tab[j - 1]
                    tab[j - 1] = tab[j]
                    tab[j] = a
                    j -= 1
                else:
                    break


def selection(tab):
    if tab:
        for i in range(0, len(tab)):
            min_index = i
            for j in range(i, len(tab)):
                if tab[min_index] > tab[j]:
                    min_index = j

            a = tab[i]
            tab[i] = tab[min_index]
            tab[min_index] = a


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


def load_into_array(file):
    data = []
    with open(file, 'r') as file:
        data_raw = file.read()
        data_lines = data_raw.split('\n')
        data = [int(line) for line in data_lines if line]
    return data


def run_test(sort_type, file):
    tab = load_into_array(file)
    process = psutil.Process()
    mem_before = process.memory_info().rss / 1024
    start_time = time.time()
    sort_type(tab)
    mem_after = process.memory_info().rss / 1024
    end_time = time.time()

    mem_consumed = mem_after - mem_before
    elapsed_time = end_time - start_time

    results = [sort_type.__name__, len(tab), mem_consumed, elapsed_time]
    return results


def run_quick(sort_type, file):
    tab = load_into_array(file)
    low = 0
    high = len(tab) - 1
    process = psutil.Process()
    mem_before = process.memory_info().rss / 1024
    start_time = time.time()
    sort_type(tab, low, high)
    mem_after = process.memory_info().rss / 1024
    end_time = time.time()

    mem_consumed = mem_after - mem_before
    elapsed_time = end_time - start_time

    results = [sort_type.__name__, len(tab), mem_consumed, elapsed_time]
    return results


def write_array_into_file(file, array):
    with open(file, 'w') as txt_file:
        for row in array:
            txt_file.write(' '.join([str(a) for a in row]) + '\n')


# bubble, insertion, selection, merge, quick, heap
results = []
names = ['Sort type', 'lenght of file', 'memory consumed', 'time to sort']
results.append(names)

results.append(run_test(bubble, 'lab-6-student-bida-agh-master/data_1.txt'))
results.append(run_test(insertion, 'lab-6-student-bida-agh-master/data_1.txt'))
results.append(run_test(selection, 'lab-6-student-bida-agh-master/data_1.txt'))
results.append(run_test(merge, 'lab-6-student-bida-agh-master/data_1.txt'))
results.append(run_quick(quick, 'lab-6-student-bida-agh-master/data_1.txt'))
results.append(run_test(heap, 'lab-6-student-bida-agh-master/data_1.txt'))

print('finished data 1')

# results.append(run_test(bubble, 'lab-6-student-bida-agh-master/data_2.txt'))
# results.append(run_test(insertion, 'lab-6-student-bida-agh-master/data_2.txt'))
# results.append(run_test(selection, 'lab-6-student-bida-agh-master/data_2.txt'))
results.append(run_test(merge, 'lab-6-student-bida-agh-master/data_2.txt'))
results.append(run_quick(quick, 'lab-6-student-bida-agh-master/data_2.txt'))
results.append(run_test(heap, 'lab-6-student-bida-agh-master/data_2.txt'))

print('finished data 2')

# results.append(run_test(bubble, 'lab-6-student-bida-agh-master/data_6.txt'))
# results.append(run_test(insertion, 'lab-6-student-bida-agh-master/data_6.txt'))
# results.append(run_test(selection, 'lab-6-student-bida-agh-master/data_6.txt'))
results.append(run_test(merge, 'lab-6-student-bida-agh-master/data_6.txt'))
# results.append(run_quick(quick, 'lab-6-student-bida-agh-master/data_6.txt'))
results.append(run_test(heap, 'lab-6-student-bida-agh-master/data_6.txt'))

print('finished data 6')
write_array_into_file('results.txt', results)
