# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    return sum([arrayProductSum(el, 2) if type(el) is list else el for el in array])

def arrayProductSum(array, factor):
    if type(array) is int:
        return array
    else:
        return factor * sum([arrayProductSum(el, factor+1) for el in array])
