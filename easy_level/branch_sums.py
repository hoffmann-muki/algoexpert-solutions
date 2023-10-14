# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(tree):
    initValue = tree.value
    if tree.left is not None and tree.right is not None:
        leftSums = branchSums(tree.left)
        rightSums = branchSums(tree.right)
        return mergeBranchSums(initValue, leftSums, rightSums)
    elif tree.left is not None and tree.right is None:
        leftSums = branchSums(tree.left)
        return mergeBranchSums(initValue, leftSums, [])
    elif tree.left is None and tree.right is not None:
        rightSums = branchSums(tree.right)
        return mergeBranchSums(initValue, [], rightSums)
    else:
        return mergeBranchSums(initValue, [], [])

def mergeBranchSums(initValue, leftSums, rightSums):
    if leftSums and rightSums:
        left = [(initValue + l) for l in leftSums]
        right = [(initValue + r) for r in rightSums]
        return left + right
    elif leftSums and not rightSums:
        return [(initValue + l) for l in leftSums]
    elif rightSums and not leftSums:
        return [(initValue + r) for r in rightSums]
    else:
        return [initValue]
