from random import randint
import time

def merge_sort(array):

    if len(array) <= 1:
        return array
    else:
        left, right = split(array)
        return merge_lists(merge_sort(left), merge_sort(right))


def split(array):
    middle = len(array)//2

    left = array[:middle]
    right = array[middle:]

    return left, right

def merge_lists(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    index_left = 0
    index_right = 0
    sum_len = len(left) + len(right)
    merged_list = []

    while len(merged_list) < sum_len:
        if left[index_left] <= right[index_right]:
            merged_list.append(left[index_left])
            index_left += 1

        else:
            merged_list.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            merged_list += left[index_left:]
            break
        if index_left == len(left):
            merged_list += right[index_right:]

    return merged_list

"""
====================================
Test sort 
====================================
"""

array = [randint(0, 100) for j in range(100)]
merge_sorted = merge_sort(array)

print('Sort is working correctly:', merge_sorted == sorted(array))

ms_time = 0

for i in range(20):
    array = [randint(0, 100) for j in range(1000)]

    start = time.time()
    merge_sorted = merge_sort(array)
    end = time.time()

    ms_time += end-start

print('Mean execution time for merge sort: ', ms_time/20)