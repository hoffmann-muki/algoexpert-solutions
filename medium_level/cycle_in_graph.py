# O(v+e) time | O(v) space
def cycleInGraph(edges):
    vertexMap = {}
    for index in range(len(edges)):
        vertexMap[index] = set(edges[index])
    for currentVertex in vertexMap:
        if vertexPathContainsCycle(currentVertex, currentVertex, vertexMap, set([currentVertex])):
            return True
    return False

def vertexPathContainsCycle(startVertex, currentVertex, vertexMap, path):
    outgoingVertices = vertexMap[currentVertex]
    if not outgoingVertices:
        return False
    if startVertex in outgoingVertices:
        return True
    for outgoingVertex in outgoingVertices:
        if outgoingVertex in path:
            return False
        if startVertex in vertexMap[outgoingVertex]:
            return True
    return any([vertexPathContainsCycle(startVertex, outgoingVertex, vertexMap, path.union(set([outgoingVertex]))) for outgoingVertex in outgoingVertices])
