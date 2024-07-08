# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class SubtreeValue:
    def __init__(self, leftValue, rightValue):
        self.leftValue = leftValue
        self.rightValue = rightValue
        self.total = self.leftValue + self.rightValue

class TreeInfo:
    def __init__(self, arrivedAtLeafNode):
        self.arrivedAtLeafNode = arrivedAtLeafNode

maxDiameter = 0

# O(n) time | O(logn) space
def binaryTreeDiameter(tree):
    global maxDiameter
    computeSubTreeDiameter(tree, None, TreeInfo(False))
    return maxDiameter

def computeSubTreeDiameter(tree, parent, treeInfo):
    global maxDiameter
    if tree is None:
        treeInfo.arrivedAtLeafNode = True
        return
    computeSubTreeDiameter(tree.left, tree, treeInfo)
    computeSubTreeDiameter(tree.right, tree, treeInfo)
    if treeInfo.arrivedAtLeafNode == True:
        if tree.left is None and tree.right is None:
            tree.value = SubtreeValue(0, 0)
        elif tree.left is not None and tree.right is None:
            leftValue = max(tree.left.value.leftValue, tree.left.value.rightValue) + 1
            tree.value = SubtreeValue(leftValue, 0)
            if leftValue > maxDiameter:
                maxDiameter = leftValue
        elif tree.left is None and tree.right is not None:
            rightValue = max(tree.right.value.leftValue, tree.right.value.rightValue) + 1
            tree.value = SubtreeValue(0, rightValue)
            if rightValue > maxDiameter:
                maxDiameter = rightValue
        else:
            leftValue = max(tree.left.value.leftValue, tree.left.value.rightValue) + 1
            rightValue = max(tree.right.value.leftValue, tree.right.value.rightValue) + 1
            tree.value = SubtreeValue(leftValue, rightValue)
            if tree.value.total > maxDiameter:
                maxDiameter = tree.value.total
