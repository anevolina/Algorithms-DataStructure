from random import randint
import time

def buble_sort(array):

    array = buble_sort_rec(array, len(array))

    return array

def buble_sort_rec(array, right_index):

    if right_index == 0:
        return

    for i in range(right_index - 1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]

    buble_sort_rec(array, right_index-1)

    return array


"""
====================================
Test sort 
It doesn't work for arrays more than 996 elements - 
maximum recursion depth exceeded error occurs
====================================
"""

array = [randint(0, 100) for j in range(10)]
buble_sorted = buble_sort(array)
print('Sort is working correctly:', buble_sorted == sorted(array))


bs_time = 0

for i in range(20):
    array = [randint(0, 100) for j in range(997)]

    start = time.time()
    buble_sorted = buble_sort(array)
    end = time.time()

    bs_time += end-start

print('Mean execution time for buble sort: ', bs_time/20)