# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeMetaData:
    def __init__(self, nodeValue, subTreeSum):
        self.nodeValue = nodeValue
        self.subTreeSum = subTreeSum

class TreeInfo:
    def __init__(self, arrivedAtLeafNode=False, splitTreeSum=0):
        self.arrivedAtLeafNode = arrivedAtLeafNode
        self.splitTreeSum = splitTreeSum

def annotateTree(tree, treeInfo):
    if tree is None:
        treeInfo.arrivedAtLeafNode = True
        return
    annotateTree(tree.left, treeInfo)
    annotateTree(tree.right, treeInfo)
    if treeInfo.arrivedAtLeafNode:
        if tree.left is None and tree.right is None:
            tree.value = TreeMetaData(tree.value, tree.value)
        elif tree.left is None and tree.right is not None:
            tree.value = TreeMetaData(tree.value, tree.value + tree.right.value.subTreeSum)
        elif tree.left is not None and tree.right is None:
            tree.value = TreeMetaData(tree.value, tree.value + tree.left.value.subTreeSum)
        else:
            tree.value = TreeMetaData(tree.value, tree.value + tree.left.value.subTreeSum + tree.right.value.subTreeSum)

def splitBinaryTreeEvenly(tree, splitInfo, halfTreeSum):
    if tree is None:
        return
    if tree.value.subTreeSum == halfTreeSum:
        splitInfo.splitTreeSum = halfTreeSum
        return
    splitBinaryTreeEvenly(tree.left, splitInfo, halfTreeSum)
    splitBinaryTreeEvenly(tree.right, splitInfo, halfTreeSum)

# O(n) time | O(h) space
def splitBinaryTree(tree):
    if tree.left is None and tree.right is None:
       return 0
    leafInfo = TreeInfo()
    annotateTree(tree, leafInfo)
    treeSum = tree.value.subTreeSum
    if treeSum % 2 == 1:
        return 0
    splitInfo = TreeInfo()
    halfTreeSum = treeSum // 2
    if tree.left is None:
        splitBinaryTreeEvenly(tree.right, splitInfo, halfTreeSum)
    elif tree.right is None:
        splitBinaryTreeEvenly(tree.left, splitInfo, halfTreeSum)
    else:    
        splitBinaryTreeEvenly(tree.left, splitInfo, halfTreeSum)
        splitBinaryTreeEvenly(tree.right, splitInfo, halfTreeSum)
    return splitInfo.splitTreeSum
