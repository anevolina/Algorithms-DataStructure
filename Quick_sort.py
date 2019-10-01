from random import randint
import time

def quick_sort(array, start, end):

    if start < end:

        index = compare_and_switch(array, start, end)

        quick_sort(array, start, index-1)
        quick_sort(array, index+1, end)

    return array


def compare_and_switch(array, start, end):
    min_index = start
    pivot = array[end]

    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[min_index] = array[min_index], array[i]
            min_index += 1

    array[min_index], array[end] = array[end], array[min_index]

    return min_index


"""
====================================
Test sort 
====================================
"""

array = [randint(0, 100) for j in range(10)]
quick_sorted = quick_sort(array, 0, len(array)-1)

print('Sort is working correctly:', quick_sorted == sorted(array))

qs_time = 0

for i in range(20):
    array = [randint(0, 100) for j in range(1000)]

    start = time.time()
    quick_sorted = quick_sort(array, 0, 999)
    end = time.time()

    qs_time += end-start

print('Mean execution time for quick sort: ', qs_time/20)