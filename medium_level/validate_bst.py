import math

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree, min=None, max=None):
    rootValue = tree.value
    if tree.left is not None and tree.right is not None:
        return tree.left.value < tree.value and validateSubTree(tree.left, -math.inf, rootValue) and tree.right.value >= tree.value and validateSubTree(tree.right, rootValue, math.inf)
    elif tree.left is None and tree.right is not None:
        return validateSubTree(tree.right, rootValue, math.inf)
    elif tree.right is None and tree.left is not None:
        return validateSubTree(tree.left, -math.inf, rootValue)
    else:
        return True

def validateSubTree(tree, min, max):
    current = tree.value
    if tree.value >= min and tree.value < max:
        if tree.left is not None and tree.right is not None:
            return tree.left.value < tree.value and validateSubTree(tree.left, min, current) and tree.right.value >= tree.value and validateSubTree(tree.right, min, max)
        elif tree.left is None and tree.right is not None:
            return tree.right.value >= tree.value and validateSubTree(tree.right, min, max)
        elif tree.right is None and tree.left is not None:
            return tree.left.value < tree.value and validateSubTree(tree.left, min, current)
        else:
            return True
    else:
        return False
