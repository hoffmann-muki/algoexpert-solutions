def arrayOfProducts(array):
    n = len(array)
    result = []
    for i in range(n):
        left_product, right_product = 1, 1
        for j in range(i):
            left_product *= array[j]
        for j in range(i+1, n):
            right_product *= array[j]
        result += [left_product * right_product]
    return result

# TODO: implement optimal solution from algoexpert