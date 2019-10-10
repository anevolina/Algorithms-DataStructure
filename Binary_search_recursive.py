from random import randint

def binary_search(array, start, end, value):

    if start > end:
        return False

    middle = (start + end)//2

    if array[middle] == value:
        return True

    elif array[middle] < value:
        result = binary_search(array, middle+1, end, value)
    else:
        result = binary_search(array, start, middle-1, value)

    return result

array =  [randint(0, 100) for i in range(100)]

result = binary_search(sorted(array), 0, len(array), 30)
print(result, 30 in array, sep='\n')