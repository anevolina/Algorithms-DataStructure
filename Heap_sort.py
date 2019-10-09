from random import randint
import time

def heap_sort(array):

    for i in range(len(array)//2, -1, -1):
        heapify(array, len(array)-1 , i)


    for i in range(len(array)-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i-1, 0)


    return array

def heapify(array, max_index, current_index):

    left_child_index = current_index * 2 + 1
    right_child_index = current_index*2 + 2

    largest_val_index = current_index

    if left_child_index <= max_index and array[left_child_index] > array[largest_val_index]:
        largest_val_index = left_child_index

    if right_child_index <= max_index and array[right_child_index] > array[largest_val_index]:
        largest_val_index = right_child_index

    if largest_val_index != current_index:
        array[largest_val_index], array[current_index] = array[current_index], array[largest_val_index]
        heapify(array, max_index, largest_val_index)



"""
====================================
Test sort 
====================================
"""


array = [randint(1, 100) for i in range(10)]
sorted_array = heap_sort(array)

print('Sort is working correctly:', sorted_array == sorted(array))

hs_time = 0
for i in range(20):
    array = [randint(0, 100) for j in range(1000)]

    start = time.time()
    selection_sorted = heap_sort(array)
    end = time.time()

    hs_time += end-start

print('Mean execution time for heap sort: ', hs_time/20)