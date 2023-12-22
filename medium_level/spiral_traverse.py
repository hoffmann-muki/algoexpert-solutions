def spiralTraverse(array):
    n, m = len(array), len(array[0])
    if n==0:
        return []
    result = []
    total_num_elts = n*m
    count, i, j = 0, 0, 0
    depth = 0
    while count < total_num_elts:
        while j < m-depth and count < total_num_elts:
            result += [array[i][j]]
            count, j = count+1, j+1
        j -= 1
        while i < n-depth-1 and count < total_num_elts:
            result += [array[i+1][j]]
            count, i = count+1, i+1
        while j > depth and count < total_num_elts:
            result += [array[i][j-1]]
            count, j = count+1, j-1
        i -= 1
        while i > depth and count < total_num_elts:
            result += [array[i][j]]
            count, i = count+1, i-1
        i, j, depth = i+1, j+1, depth+1
    return result
