# solution with O(n) time and O(n) space

def firstDuplicateValue(array):
    s = set()
    n = len(array)
    for i in range(n):
        el = array[i]
        if el in s:
            return el
        else:
            s.add(el)
    return -1

# TODO: implement optimal solution from algoexpert
