# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class TreeInfo:
    def __init__(self, nextValue=None, takeNext=False, arrivedAtLeaf=False, elemCount=0):
        self.nextValue = nextValue
        self.takeNext = takeNext
        self.arrivedAtLeaf = arrivedAtLeaf
        self.elemCount = elemCount

# O(n) time | O(logn) space
def findSuccessor(tree, node):
    treeInfo = TreeInfo()
    inOrderTraversal(tree, node, treeInfo)
    return treeInfo.nextValue

def inOrderTraversal(tree, node, treeInfo):
    if tree is None:
        treeInfo.arrivedAtLeaf = True
        return
    else:
        inOrderTraversal(tree.left, node, treeInfo)
        if treeInfo.arrivedAtLeaf:
            if treeInfo.takeNext and treeInfo.elemCount == 1:
                treeInfo.nextValue = tree
                treeInfo.takeNext = False
            if tree.value == node.value:
                treeInfo.takeNext = True
                treeInfo.elemCount += 1
        inOrderTraversal(tree.right, node, treeInfo)

# ********************* Alternate Solution ************************

# O(h) time | O(1) space
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftmostChild(node.right)
    return getRightmostParent(node)

def getLeftmostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode

def getRightmostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent
