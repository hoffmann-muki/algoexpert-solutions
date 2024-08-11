# O(nm) time | O(1) space
def searchInSortedMatrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return [i, j]
            elif matrix[i][j] > target:
                break
            else:
                continue
    return [-1, -1]

# O(n+m) time | O(1) space
def searchInSortedMatrix(matrix, target):
    i = 0
    j = len(matrix[0])-1
    while i <= len(matrix)-1 and j >= 0:
        print(i, j)
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    return [-1, -1]
