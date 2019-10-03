from random import randint
import time

def selection_sort(array):
    start = 0

    for i in range(len(array)):
        min_index = start

        for j in range(start, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[min_index], array[i] = array[i], array[min_index]
        start += 1

    return array


"""
====================================
Test sort 
====================================
"""


array = [randint(1,100) for i in range(10)]
sorted_array = selection_sort(array)

print('Sort is working correctly:', sorted_array == sorted(array))

ss_time = 0
for i in range(20):
    array = [randint(0, 100) for j in range(1000)]

    start = time.time()
    selection_sorted = selection_sort(array)
    end = time.time()

    ss_time += end-start

print('Mean execution time for quick sort: ', ss_time/20)