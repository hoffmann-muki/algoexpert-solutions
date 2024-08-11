# O(n) time | O(1) space
def threeNumberSort(array, order):
    last = 0
    for element in order:
        for i in range(len(array)):
            if array[i] == element:
                tmp = array[last]
                array[last] = element
                array[i] = tmp
                last += 1
    return array

# O(n) time | O(1) space
def threeNumberSort(array, order):
    countMap = dict()
    for element in array:
        if element in countMap:
            countMap[element] += 1
        else:
            countMap[element] = 1
    start, end = 0, 0
    for element in order:
        if element in countMap.keys():
            end += countMap[element]
            for j in range(start, end):
                array[j] = element
            start = end
    return array
