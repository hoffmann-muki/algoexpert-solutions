# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space
def mergeBinaryTrees(tree1, tree2):
    mergedTree = BinaryTree(tree1.value)
    return sumTreeNodes(tree1, tree2)

def sumTreeNodes(tree1, tree2):
    if tree1 is None and tree2 is None:
        return None
    elif tree1 is not None and tree2 is None:
        return tree1
    elif tree1 is None and tree2 is not None:
        return tree2
    else:
        mergedTree = BinaryTree(tree1.value + tree2.value, sumTreeNodes(tree1.left, tree2.left), sumTreeNodes(tree1.right, tree2.right))
        return mergedTree

# ********************** Alternate Solution **********************

# O(n) time | O(h) space
def mergeBinaryTrees(tree1, tree2):
    sumTreeNodes(tree1, tree2)
    return tree1

def sumTreeNodes(tree1, tree2):
    if tree1 is None and tree2 is None:
        return None
    elif tree1 is not None and tree2 is None:
        return tree1
    elif tree1 is None and tree2 is not None:
        return tree2
    else:
        tree1.value = tree1.value + tree2.value
        tree1.left = sumTreeNodes(tree1.left, tree2.left)
        tree1.right = sumTreeNodes(tree1.right, tree2.right)
        return tree1
