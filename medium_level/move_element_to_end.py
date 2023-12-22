def moveElementToEnd(array, toMove):
    n = len(array)
    for i in range(n):
        if array[i] != toMove:
            sendToFront(array, i, toMove)
    return array

def sendToFront(array, pos, toMove):
    for i in range(pos):
        if array[i] == toMove:
            array[i] = array[pos]
            array[pos] = toMove

def moveElementToEnd(array, toMove):
    n = len(array)
    left_ptr = 0
    right_ptr = n-1
    while left_ptr < right_ptr:
        if array[right_ptr] == toMove:
            if array[left_ptr] == toMove:
                swap(array, left_ptr, right_ptr-1)
                right_ptr -= 1
            else:
                left_ptr += 1
        else: # right_ptr != toMove
            if array[left_ptr] == toMove:
                swap(array, left_ptr, right_ptr)
                left_ptr += 1
            else:
                left_ptr += 1
    return array

def swap(array, left_ptr, right_ptr):
    temp = array[left_ptr]
    array[left_ptr] = array[right_ptr]
    array[right_ptr] = temp

