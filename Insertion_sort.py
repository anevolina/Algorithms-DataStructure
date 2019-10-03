from random import randint
import time

def insertion_sort(array):

    for i in range(1, len(array)):
        temp = array[i]

        j = i-1
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

    return array


"""
====================================
Test sort 
====================================
"""


array = [randint(1,100) for i in range(10)]
sorted_array = insertion_sort(array)

print('Sort is working correctly:', sorted_array == sorted(array))

is_time = 0
for i in range(20):
    array = [randint(0, 100) for j in range(1000)]

    start = time.time()
    insertion_sorted = insertion_sort(array)
    end = time.time()

    is_time += end-start

print('Mean execution time for quick sort: ', is_time/20)