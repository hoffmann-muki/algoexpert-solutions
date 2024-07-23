# O(nm) space | O(nm) time
def numberOfWaysToTraverseGraph(width, height):
    ways = [[0 for _ in range(width)] for _ in range(height)]
    ways[0] = [1 for j in range(width)]
    for i in range(height):
        ways[i][0] = 1
    for i in range(1, height):
        for j in range(1, width):
            left = getLeft(i, j, ways)
            top = getTop(i, j, ways)
            ways[i][j] = left + top
    return ways[height-1][width-1]

def getLeft(i, j, ways):
    if j-1 >= 0:
        return ways[i][j-1]
    return 0

def getTop(i, j, ways):
    if i-1 >= 0:
        return ways[i-1][j]
    return 0

# O(width + height) space | worst case O(2^(width + height)) time
def numberOfWaysToTraverseGraph(width, height):
    return ways(height-1, width-1)
    
def ways(height, width):
    if width == 0 and height == 0:
        return 0
    elif width == 0 or height == 0:
        return 1
    else:
        return ways(height-1, width) + ways(height, width-1)

import math

# O(n+m) time | O(1) space
def numberOfWaysToTraverseGraph(width, height):
    return math.factorial(width-1 + height-1)//(math.factorial(width-1) * math.factorial(height-1))
