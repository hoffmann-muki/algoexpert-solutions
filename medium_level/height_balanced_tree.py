# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, arrivedAtLeaf=False, isHeightBalanced=True):
        self.arrivedAtLeaf = arrivedAtLeaf
        self.isHeightBalanced = isHeightBalanced

class TreeData:
    def __init__(self, value, leftSubtreeHeight, rightSubtreeHeight):
        self.value = value
        self.leftSubtreeHeight = leftSubtreeHeight
        self.rightSubtreeHeight = rightSubtreeHeight

# O(n) time | O(h) space
def heightBalancedBinaryTree(tree):
    treeInfo = TreeInfo()
    computeSubtreeHeights(tree, treeInfo)
    return treeInfo.isHeightBalanced

def computeSubtreeHeights(tree, treeInfo):
    if tree is None:
        treeInfo.arrivedAtLeaf = True
        return
    computeSubtreeHeights(tree.left, treeInfo)
    computeSubtreeHeights(tree.right, treeInfo)
    if treeInfo.arrivedAtLeaf:
        if tree.left is None and tree.right is None:
            tree.value = TreeData(tree.value, 0, 0)
        elif tree.left is None and tree.right is not None:
            rightSubtreeHeight = max(tree.right.value.leftSubtreeHeight, tree.right.value.rightSubtreeHeight) + 1
            tree.value = TreeData(tree.value, 0, rightSubtreeHeight)
            if rightSubtreeHeight > 1:
                treeInfo.isHeightBalanced = False
        elif tree.left is not None and tree.right is None:
            leftSubtreeHeight = max(tree.left.value.leftSubtreeHeight, tree.left.value.rightSubtreeHeight) + 1
            tree.value = TreeData(tree.value, leftSubtreeHeight, 0)
            if leftSubtreeHeight > 1:
                treeInfo.isHeightBalanced = False
        else:
            leftSubtreeHeight = max(tree.left.value.leftSubtreeHeight, tree.left.value.rightSubtreeHeight) + 1
            rightSubtreeHeight = max(tree.right.value.leftSubtreeHeight, tree.right.value.rightSubtreeHeight) + 1
            tree.value = TreeData(tree.value, leftSubtreeHeight, rightSubtreeHeight)
            if abs(leftSubtreeHeight - rightSubtreeHeight) > 1:
                treeInfo.isHeightBalanced = False
