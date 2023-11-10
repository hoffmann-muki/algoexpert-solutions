def bubbleSort(array):
    n = len(array)
    k = 0
    for i in range(n):
        for j in range(n-k-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
        k += 1
    return array
