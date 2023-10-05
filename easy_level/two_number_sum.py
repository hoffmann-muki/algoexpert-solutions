def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        remainder = targetSum - array[i]
        if (remainder in array) and (remainder != array[i]):
            return [remainder, array[i]]
    return []
