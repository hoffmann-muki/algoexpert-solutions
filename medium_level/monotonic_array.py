def isMonotonic(array):
    n = len(array)
    if n == 0 or n == 1:
        return True
    curr_index = 0
    while curr_index < n-1:
        current, next = array[curr_index], array[curr_index+1]
        if current < next:
            return is_monotonously_increasing(array, curr_index, n)
        elif current > next:
            return is_monotonously_decreasing(array, curr_index, n)
        curr_index += 1
    return True

def is_monotonously_increasing(array, curr_index, n):
    i = curr_index+1
    while i < n-1: 
        if array[i] > array[i+1]:
            return False
        i += 1
    return True
    
def is_monotonously_decreasing(array, curr_index, n):
    i = curr_index+1
    while i < n-1: 
        if array[i] < array[i+1]:
            return False
        i += 1
    return True
