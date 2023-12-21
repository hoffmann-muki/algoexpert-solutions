import math

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    ptrOne, ptrTwo = 0, 0
    n, m = len(arrayOne), len(arrayTwo)
    smallest_diff = math.inf
    result_pair = [arrayOne[0], arrayTwo[0]]
    while ptrOne < n and ptrTwo < m:
        arrayOne_elt, arrayTwo_elt = arrayOne[ptrOne], arrayTwo[ptrTwo]
        diff = abs(arrayOne_elt - arrayTwo_elt)
        if diff == 0:
            return [arrayOne_elt, arrayTwo_elt]
        if diff < smallest_diff:
            smallest_diff = diff
            result_pair = [arrayOne_elt, arrayTwo_elt]
        # increment ptr to the smaller element
        if arrayOne_elt < arrayTwo_elt:
            ptrOne += 1
        else:
            ptrTwo += 1
    return result_pair
