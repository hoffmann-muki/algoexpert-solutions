# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    n = len(array)
    if n == 0:
        return 0
    if n == 1:
        return array[0]
    maxSubsetSums = []
    currentIndex = 0
    while currentIndex < n:
        if currentIndex == 0:
            maxSubsetSums.append(array[currentIndex])
        elif currentIndex == 1:
            maxSubsetSums.append(max(array[currentIndex], array[currentIndex-1]))
        else:
            currentMax = max(maxSubsetSums[currentIndex-2] + array[currentIndex], maxSubsetSums[currentIndex-1])
            maxSubsetSums.append(currentMax)
        currentIndex += 1
    return maxSubsetSums[len(maxSubsetSums)-1]
