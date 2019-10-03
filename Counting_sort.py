from random import randint
import time

def counting_sort(array):
    aux_array = [0 for i in range(100)]

    for i in range(len(array)):
        aux_array[array[i]] += 1

    for i in range(len(aux_array) - 1):
        aux_array[i + 1] += aux_array[i]

    result = [0 for i in range(len(array))]

    for item in array:
        result[aux_array[item]-1] = item
        aux_array[item] -= 1

    return result


"""
====================================
Test sort 
====================================
"""


array = [randint(1, 99) for i in range(10)]
sorted_array = counting_sort(array)

print('Sort is working correctly:', sorted_array == sorted(array))

cs_time = 0
for i in range(20):
    array = [randint(1, 99) for j in range(100000)]

    start = time.time()
    counting_sorted = counting_sort(array)
    end = time.time()

    cs_time += end-start

print('Mean execution time for quick sort: ', cs_time/20)