def findClosestValueInBst(tree, target):
    if tree.value == target:
        return target
    if tree.left is not None and tree.right is not None:
        leftCloserValue = closerValue(tree.value, findClosestValueInBst(tree.left, target), target)
        rightCloserValue = closerValue(tree.value, findClosestValueInBst(tree.right, target), target)
        return closerValue(leftCloserValue, rightCloserValue, target)
    elif tree.left is None and tree.right is not None:
        return closerValue(tree.value, findClosestValueInBst(tree.right, target), target)
    elif tree.left is not None and tree.right is None:
        return closerValue(tree.value, findClosestValueInBst(tree.left, target), target)
    else:
        return tree.value

def closerValue(current, next, target):
    if abs(current - target) < abs(next - target):
        return current
    else:
        return next

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
