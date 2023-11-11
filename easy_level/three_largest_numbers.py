def findThreeLargestNumbers(array):
    n = len(array)
    for k in range(3):
        for j in range(n-1-k):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array[(n-3):]
