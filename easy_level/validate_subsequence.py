def isValidSubsequence(array, sequence):
    for elem in sequence:
        if elem in array:
            array_index = array.index(elem)
            array = array[(array_index+1):]
        else:
            return False
    return True
