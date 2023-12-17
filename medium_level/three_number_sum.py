def threeNumberSum(array, targetSum):
    result = []
    for elem in array:
        elem_index = array.index(elem)
        array_without_elem = array[:elem_index] + array[elem_index+1:]
        two_number_sums = twoNumberSums(array_without_elem, targetSum-elem)
        if len(two_number_sums) != 0:
            result += [sorted([elem] + two_number_sum) for two_number_sum in two_number_sums]
    result = sorted(result)       
    return [result[i] for i in range(len(result)) if i == 0 or result[i] != result[i-1]]

def twoNumberSums(array, targetSum):
    result = []
    for i in range(len(array)):
        remainder = targetSum - array[i]
        if (remainder in array) and (remainder != array[i]):
            result += [[remainder, array[i]]]
    return result

def threeNumberSum(array, targetSum):
    result = []
    array = sorted(array)
    for elem in array:
        res = getTriplets(array, targetSum, elem)
        if len(res) != 0:
            result += res
    result = sorted(result)       
    return [result[i] for i in range(len(result)) if i == 0 or result[i] != result[i-1]]

def getTriplets(array, targetSum, elem):
    if len(array) < 3:
        return []
    elem_index = array.index(elem)
    array_without_elem = array[:elem_index] + array[elem_index+1:]
    left_ptr = 0
    right_ptr = len(array)-2
    revised_targetSum = targetSum - elem
    result = []
    while left_ptr < right_ptr:
        while (array_without_elem[left_ptr] + array_without_elem[right_ptr]) != revised_targetSum and left_ptr < right_ptr:
            if (array_without_elem[left_ptr] + array_without_elem[right_ptr]) > revised_targetSum:
                right_ptr -= 1 # backtrack the right ptr
            else:
                left_ptr += 1 # advance the left ptr
        if (array_without_elem[left_ptr] + array_without_elem[right_ptr]) == revised_targetSum and left_ptr != right_ptr:
            result += [sorted([array_without_elem[left_ptr], elem, array_without_elem[right_ptr]])]
            left_ptr += 1 # advance to find more pairs
    return result

