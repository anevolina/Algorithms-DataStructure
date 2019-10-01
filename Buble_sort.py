from random import randint
import time

def buble_sort(array):

    # array = list(array)

    edge = len(array) - 1

    for j in range(len(array)-1):
        for i in range(edge):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        edge -= 1


    return array



"""
====================================
Test sort 
====================================
"""

array = [randint(0, 100) for j in range(100)]
buble_sorted = buble_sort(array)
print('Sort is working correctly:', buble_sorted == sorted(array))


bs_time = 0

for i in range(20):
    array = [randint(0, 100) for j in range(1000)]

    start = time.time()
    buble_sorted = buble_sort(array)
    end = time.time()

    bs_time += end-start

print('Mean execution time for buble sort: ', bs_time/20)