def binarySearch(array, target):
    n = len(array)
    if n == 1:
        if target == array[0]:
            return 0
        else:
            return -1
    else:
        mid_index = n // 2
        left_half = array[:mid_index]
        right_half = array[mid_index:]
        if target <= array[mid_index-1]:
            return findElement(left_half, target, mid_index)
        else:
            return findElement(right_half, target, n)

def findElement(array, target, pos):
    n = len(array)
    if n == 1:
        if target == array[0]:
            return pos-1
        else:
            return -1
    else:
        mid_index = n // 2
        left_half = array[:mid_index]
        right_half = array[mid_index:]
        if target <= array[mid_index-1]:
            return findElement(left_half, target, pos-mid_index if n % 2==0 else pos-mid_index-1)
        else:
            return findElement(right_half, target, pos)
