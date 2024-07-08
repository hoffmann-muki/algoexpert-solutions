# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n^2) time | O(n) space
def reconstructBst(preOrderTraversalValues):
    return reconstructBstFromRange(preOrderTraversalValues, 0, len(preOrderTraversalValues))

def reconstructBstFromRange(preOrderTraversalValues, startIdx, endIdx):
    if startIdx >= endIdx:
        return None
    currentValue = preOrderTraversalValues[startIdx]
    currentBst = BST(currentValue)
    leftIdx = startIdx + 1
    rightIdx = endIdx
    if leftIdx < endIdx:
        currentIndex = leftIdx + 1
        while currentIndex < endIdx:
            if preOrderTraversalValues[currentIndex] >= currentValue:
                rightIdx = currentIndex
                break
            currentIndex += 1
        if preOrderTraversalValues[leftIdx] < currentValue:
            currentBst.left = reconstructBstFromRange(preOrderTraversalValues, leftIdx, rightIdx)
            currentBst.right = reconstructBstFromRange(preOrderTraversalValues, rightIdx, endIdx)
        else:
            currentBst.right = reconstructBstFromRange(preOrderTraversalValues, leftIdx, endIdx)
    return currentBst

# *************************** Alternate Solution *********************************

class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx
        
# O(n) time | O(h) space
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float('-inf'), float('inf'), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None

    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None

    currentSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree)
