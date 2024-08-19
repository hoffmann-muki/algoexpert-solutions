# O(n^2) time | O(n) space
def nextGreaterElement(array):
    if not array:
        return []
    if len(array) == 1:
        return [-1]
    outputArray = []
    n = len(array)
    for index in range(n):
        currentIndex = (index + 1) % n
        foundGreaterElement = False
        while currentIndex != index:
            if array[currentIndex] > array[index]:
                outputArray.append(array[currentIndex])
                foundGreaterElement = True
                break
            else:
                currentIndex = (currentIndex + 1) % n
        if not foundGreaterElement:
            outputArray.append(-1)
    return outputArray
