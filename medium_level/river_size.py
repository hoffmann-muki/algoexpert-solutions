# O(h*w) time | O(h*w) space
def riverSizes(matrix):
    if len(matrix) == 0:
        return []
    height = len(matrix)
    width = len(matrix[0])
    visited = [[0 for _ in range(width)] for _ in range(height)]
    river_lengths = []
    for h in range(height):
        for w in range(width):
            if matrix[h][w] == 0 or visited[h][w]:
                continue
            else:
                river_lengths.append(exploreNode(h, w, matrix, visited))
    return river_lengths

def exploreNode(i, j, matrix, visited):
    if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and matrix[i][j] and not visited[i][j]:
        visited[i][j] = 1
        return 1 + exploreNode(i-1, j, matrix, visited) + exploreNode(i, j-1, matrix, visited) + exploreNode(i+1, j, matrix, visited) + exploreNode(i, j+1, matrix, visited)
    else:
        return 0
