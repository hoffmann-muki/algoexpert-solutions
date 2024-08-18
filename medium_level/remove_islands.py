class VisitedNodes:
    def __init__(self):
        self.coordinates = []

# O(w*h) time | O(w*h) space
def removeIslands(matrix):
    if len(matrix) == 0:
        return []
    height = len(matrix)
    width = len(matrix[0])
    visited = [[0 for _ in range(width)] for _ in range(height)]
    for h in range(1, height-1):
        for w in range(1, width-1):
            if matrix[h][w] == 0 or visited[h][w]:
                continue
            else:
                visitedNodes = VisitedNodes()
                if visit(h, w, matrix, visited, visitedNodes):
                    clearIslands(matrix, visitedNodes.coordinates)    
    return matrix

def visit(i, j, matrix, visited, visitedNodes):
    if not matrix[i][j]:
        return True
    else:
        if i >= 1 and i < len(matrix)-1 and j >= 1 and j < len(matrix[0])-1:
            if visited[i][j]:
                return True
            else:
                visited[i][j] = 1
                validIsland = visit(i-1, j, matrix, visited, visitedNodes) and visit(i, j-1, matrix, visited, visitedNodes) and visit(i+1, j, matrix, visited, visitedNodes) and visit(i, j+1, matrix, visited, visitedNodes)
                if validIsland:
                    visitedNodes.coordinates.append((i, j))
                return validIsland
        else:
            return False

def clearIslands(matrix, coordinates):
    for (i, j) in coordinates:
        matrix[i][j] = 0
