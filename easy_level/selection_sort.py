def selectionSort(array):
    n = len(array)
    for i in range(n):
        smallest = array[i]
        for j in range(i, n-1):
            if array[j+1] < smallest:
                smallest = array[j+1]
                pos = j+1
        if smallest != array[i]:
                temp = array[pos]
                array[pos] = array[i]
                array[i] = temp
    return array
