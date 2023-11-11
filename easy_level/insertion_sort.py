def insertionSort(array):
    n = len(array)
    cursor = 1
    for i in range(1, n):
        if array[i-1] > array[i]:
            temp = array[i]
            array[i] = array[i-1]
            array[i-1] = temp
            array = sortArray(array[:(i+1)]) + array[(i+1):]
    return array

def sortArray(array):
    n = len(array)
    for j in range(n-1, 0, -1):
        if array[j] < array[j-1]:
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
    return array

