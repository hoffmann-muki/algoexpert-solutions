# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# right -> middle -> left
def backwardsOrderTraverse(tree):
    if tree.left is not None and tree.right is not None:
        return backwardsOrderTraverse(tree.right) + [tree.value] + backwardsOrderTraverse(tree.left)
    elif tree.left is not None and tree.right is None:
        return [tree.value] + backwardsOrderTraverse(tree.left)
    elif tree.left is None and tree.right is not None:
        return backwardsOrderTraverse(tree.right) + [tree.value]
    else:
        return [tree.value]

# O(n) space | O(n) time
def findKthLargestValueInBst(tree, k):
    return backwardsOrderTraverse(tree)[k-1]

# **************************** Optimal Solution ******************************

class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue

# O(h+k) time | O(h) space
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
    if node == None or treeInfo.numberOfNodesVisited >= k:
        return
        
    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)
