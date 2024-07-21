def levenshteinDistance(str1, str2):
    if len(str1) < len(str2):
        return computeLevenshteinDistance(str1, str2)
    else:
        return computeLevenshteinDistance(str2, str1)

# O(nm) space | O(nm) time -- can be optimized to O(min(n, m)) space
def computeLevenshteinDistance(str1, str2):
    n = len(str1)
    m = len(str2)
    edits = [[0 for j in range(n+1)] for i in range(m+1)]
    edits[0] = [j for j in range(n+1)]
    for i in range(m+1):
        edits[i][0] = i
    for r in range(1, m+1):
        for c in range(1, n+1):
            top = getTop(r, c, edits)
            diag = getDiag(r, c, edits)
            left = getLeft(r, c, edits)
            if str2[r-1] == str1[c-1]:
                edits[r][c] = diag
            else:
                edits[r][c] = 1 + min(top, diag, left)
    return edits[m][n]

def getTop(i, j, edits):
    if i-1 >= 0:
        return edits[i-1][j]
    return 0

def getDiag(i, j, edits):
    if i-1 >= 0 and j-1 >= 0:
        return edits[i-1][j-1]
    return 0

def getLeft(i, j, edits):
    if j-1 >= 0:
        return edits[i][j-1]
    return 0
